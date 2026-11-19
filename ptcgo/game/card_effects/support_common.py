"""Reusable search / draw / heal / switch / energy effect factories.

Every factory returns an `async def effect(ctx)` usable on attacks, abilities
AND trainers (TrainerCardDef(effect=...)); attack usages resolve the printed
damage first (text order). The matching playability `condition=` factories at
the bottom accept both the trainer (board, player_id) and the ability
(board, player_id, pokemon) call shapes.
"""

from typing import Callable, List, Optional

from ptcgo.game.card_effects.pokemon import energy_provides_type

from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import def_for
from ptcgo.game.models.board import CardEntity, PokemonEntity
from ptcgo.game.session.constants import BENCH_CAPACITY
from ptcgo.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_trainer_card,
)
from ptcgo.game.session.passives import effective_max_hp
from ptcgo.game.card_effects.trainers import is_energy_card

# Spec-friendly aliases used as factory defaults.
is_basic = is_basic_pokemon
is_energy = is_energy_card


# --- Internal helpers --------------------------------------------------------

async def _deal_printed(ctx):
    """Printed attack damage first (text order); no-op for abilities/trainers."""
    if ctx.is_attack_effect() and getattr(ctx.ability, "damage", 0) > 0:
        await ctx.deal_damage()


def entity_name(entity) -> str:
    """A board entity's printed name.

    A CardEntity carries no `display_name`; the name lives on the definition
    (`card.card_obj` is the same card model). Resolve through `def_for`, the
    way the rest of the effect library does, so a predicate that names a card
    cannot silently read nothing."""
    definition = def_for(getattr(entity, "archetype_id", None) or "")
    return getattr(definition, "display_name", "") or ""


def _card_label(card: CardEntity) -> str:
    return entity_name(card) or "the card"


def _is_damaged(board, pokemon: PokemonEntity) -> bool:
    return pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


def _has_conditions(pokemon: PokemonEntity) -> bool:
    return bool(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS))


def _opponent_of(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


async def _attach_all(ctx, cards, target: PokemonEntity) -> list:
    """Attach each card and RETURN the ones that actually attached.

    `ctx.attach_energy` answers False when the target is not a card entity or the
    card is not in the board's index, and the result used to be dropped -- so a
    caller reported "attached" pairs for cards that never moved. A silent False
    here is indistinguishable from a broken board read."""
    import logging
    if target.entity_id not in ctx.visual_targets:
        ctx.visual_targets.append(target.entity_id)
    attached = []
    for card in cards:
        if await ctx.attach_energy(card, target):
            attached.append(card)
        else:
            logging.warning(
                f"[Effects] attach_energy refused {getattr(card, 'entity_id', card)}"
                f" onto {getattr(target, 'entity_id', target)}")
    return attached


# --- Deck searches -----------------------------------------------------------

def search_to_hand(predicate=None, count=1, minimum=0, reveal=True, prompt=""):
    """Search the deck for up to `count` matches into hand, then shuffle.

    reveal follows the card text ("reveal it" -> True; Adaman-style -> False).
    """
    async def effect(ctx):
        await _deal_printed(ctx)
        picks = await ctx.search_deck(
            predicate, count=count, minimum=minimum,
            prompt=prompt or "Choose a card to put into your hand.",
        )
        await ctx.put_in_hand(picks, reveal=reveal)
        await ctx.shuffle_deck()
    return effect


def search_to_bench(predicate=is_basic, count=1, then=None, prompt=""):
    """Search the deck for Pokémon onto the Bench (capped by free bench
    space, regi_gate shape), shuffle after; `then(ctx, benched)` runs last."""
    async def effect(ctx):
        await _deal_printed(ctx)
        space = BENCH_CAPACITY - len(ctx.my_bench())
        benched: List[CardEntity] = []
        take = min(count, space)
        if take > 0:
            picks = await ctx.search_deck(
                predicate, count=take, minimum=0,
                prompt=prompt or "Choose a Pokémon to put onto your Bench.",
            )
            for card in picks:
                if await ctx.bench_pokemon(card):
                    benched.append(card)
        await ctx.shuffle_deck()
        if then is not None and benched:
            await then(ctx, benched)
    return effect


# --- Energy search & attachment ----------------------------------------------

def on_bench(pokemon) -> bool:
    """Target predicate: `pokemon` sits on its owner's Bench ("attach them to
    your Benched Pokémon", "1 of your opponent's Benched Pokémon")."""
    parent = getattr(pokemon, "parent", None)
    return parent is not None and parent.get_attribute(AttrID.NAME) == "bench"


async def distribute_energy(ctx, cards, candidates):
    """Attach each card to a chosen Pokémon ("in any way you like"); each card
    may pick a different target. Returns the (card, target) pairs."""
    attached = []
    for card in cards:
        target = await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon to attach {_card_label(card)} to"
        )
        if target is None:
            target = candidates[0]
        await _attach_all(ctx, [card], target)
        attached.append((card, target))
    return attached


def search_attach_energy(predicate=is_energy, count=1, to_self=False,
                         target_pred=None, distribute=True, shuffle=True,
                         prompt=""):
    """Search the deck for up to `count` Energy and attach: to this Pokémon
    (to_self), per-card free distribution, or all onto one chosen target."""
    async def effect(ctx):
        await _deal_printed(ctx)
        picks = await ctx.search_deck(
            predicate, count=count, minimum=0,
            prompt=prompt or f"Choose up to {count} Energy card(s) to attach.",
        )
        if picks:
            if to_self:
                await _attach_all(ctx, picks, ctx.source)
            else:
                candidates = [p for p in ctx.my_pokemon_in_play()
                              if target_pred is None or target_pred(p)]
                if candidates and distribute:
                    await distribute_energy(ctx, picks, candidates)
                elif candidates:
                    target = await ctx.choose_pokemon(
                        candidates, "Choose a Pokémon to attach the Energy to"
                    )
                    if target is not None:
                        await _attach_all(ctx, picks, target)
        if shuffle:
            await ctx.shuffle_deck()
    return effect


def swap_with_named(name: Optional[str] = None, predicate=None,
                    destination: str = "deck", then=None):
    """"Search your deck for another <name> and switch it with <name>" (Ditto's
    Sudden Transformation): the deck copy takes the exact board spot with
    everything attached, and the outgoing card goes to `destination` -- "deck"
    is the bottom of the deck, the printed wording's pile.

    `name` defaults to the source Pokemon's own display name; `then(ctx, new)`
    gets the Pokémon now in play."""
    async def effect(ctx):
        source = ctx.attacker if ctx.attacker is not None else ctx.source
        if source is None or not isinstance(source, PokemonEntity):
            return None
        wanted = (name or "").strip().lower()

        def matches(card) -> bool:
            if predicate is not None:
                return predicate(card)
            definition = def_for(getattr(card, "archetype_id", "") or "")
            return bool(wanted) and (getattr(definition, "display_name", "") or "").strip().lower() == wanted

        found = await ctx.search_deck(matches, count=1, minimum=0,
                                      prompt=f"Search your deck for another {name or 'copy'}")
        if not found:
            return None
        incoming = found[0]
        swapped = await ctx.identity_swap(source, incoming, destination=destination)
        if swapped and then is not None:
            await then(ctx, incoming)
        return incoming if swapped else None
    return effect


def trigger_counters(counters: int = 1, pred=None):
    """"Whenever any player puts a Basic Pokemon onto their Bench / plays a
    Pokemon to evolve / attaches an Energy, put N damage counters on that
    Pokemon" -- a Stadium trigger body. Reads whichever entity the trigger is
    about (benched_pokemon, evolved_pokemon or energy_receiver) and takes
    `pred(pokemon, ctx)` for the type/stage gates."""
    async def effect(ctx):
        pokemon = (getattr(ctx, "benched_pokemon", None)
                   or getattr(ctx, "evolved_pokemon", None)
                   or getattr(ctx, "energy_receiver", None))
        if pokemon is None or pred is not None and not pred(pokemon, ctx):
            return
        await ctx.deal_damage(counters * 10, target=pokemon, as_counters=True)
    return effect


def counters_each_in_play(counters: int = 1, pred=None):
    """"Between turns, put N damage counters on each <matching> Pokemon in
    play (both sides)" -- Shrine of Punishment, Faded Town."""
    async def effect(ctx):
        targets = [p for pid in (ctx.player_id, ctx.opponent_id)
                   for p in ctx.session.board_state.pokemon_in_play(pid)]
        for pokemon in targets:
            if pred is not None and not pred(pokemon):
                continue
            await ctx.deal_damage(counters * 10, target=pokemon, as_counters=True)
    return effect


def bare_mill(count: int = 3, opponent: bool = True, then=None, predicate=None):
    """"Discard the top N cards of your opponent's deck" with no damage step,
    for the ability and Trainer printings of the same wording (mill_attack is
    the attack-side twin, which deals the printed damage first).

    `then` runs after the discard and receives the milled cards; `predicate`
    narrows what `then` sees (Energy among them) without changing what is
    discarded."""
    async def effect(ctx):
        pid = ctx.opponent_id if opponent else ctx.player_id
        milled = ctx.deck_top(count, player_id=pid)
        if not milled:
            return []
        await ctx.discard_cards(milled)
        if then is not None:
            matches = [c for c in milled if predicate is None or predicate(c)]
            await then(ctx, matches)
        return milled
    return effect


def look_top_attach_energy(n, predicate=is_energy, rest="shuffle",
                           target_pred=None, distribute=True, minimum=0):
    """Look at the top `n` deck cards and attach the Energy you find there;
    rest: 'shuffle' the deck after, 'back' leaves the others on top in order."""
    async def effect(ctx):
        await _deal_printed(ctx)
        top = ctx.deck_top(n)
        matches = [c for c in top if predicate(c)]
        if top:
            # No matches still shows the looked-at cards (nothing selectable).
            picks = await ctx.choose_cards(
                matches, max(len(matches), 1), minimum=minimum,
                prompt="Choose Energy cards to attach to your Pokémon.",
                display_cards=top,
            )
            candidates = [p for p in ctx.my_pokemon_in_play()
                          if target_pred is None or target_pred(p)]
            if picks and candidates:
                if distribute:
                    await distribute_energy(ctx, picks, candidates)
                else:
                    target = await ctx.choose_pokemon(
                        candidates, "Choose a Pokémon to attach the Energy to"
                    )
                    if target is not None:
                        await _attach_all(ctx, picks, target)
        if rest == "shuffle":
            await ctx.shuffle_deck()
    return effect


# --- Discard-pile recursion ----------------------------------------------------

def attach_from_discard(predicate=is_energy, count=1, target="self",
                        minimum=1, then=None, prompt="", distribute=False):
    """Attach up to `count` matching discard-pile cards to one Pokémon:
    'self' = the acting Pokémon (abilities only), 'choice' = pick any of
    yours, or a predicate narrowing the pickable targets. minimum=1 keeps the
    activated public-zone pick mandatory; gate activation with a condition=.

    distribute=True is the "attach them ... in any way you like" wording: each
    card picks its own holder, so two Energy can land on two different Pokémon."""
    async def effect(ctx):
        await _deal_printed(ctx)
        cards = [c for c in ctx.discard_pile() if predicate(c)]
        if not cards:
            return []
        picks = await ctx.choose_cards(
            cards, count, minimum=minimum,
            prompt=prompt or "Choose card(s) from your discard pile to attach",
        )
        if not picks:
            return []
        if target == "self":
            holder: Optional[PokemonEntity] = ctx.source
        else:
            pred = None if target == "choice" else target
            candidates = [p for p in ctx.my_pokemon_in_play()
                          if pred is None or pred(p)]
            if not candidates:
                return []
            if distribute:
                await distribute_energy(ctx, picks, candidates)
                if then is not None:
                    await then(ctx, picks)
                return picks
            holder = await ctx.choose_pokemon(
                candidates, "Choose a Pokémon to attach the Energy to"
            ) or candidates[0]
        attached = await _attach_all(ctx, picks, holder)
        if then is not None:
            await then(ctx, picks)
        # Same contract as attach_from_hand: the attached pairs are the signal,
        # and only the cards that really attached are in it.
        return [(card, holder) for card in attached]
    return effect


def recover_from_discard(predicate=None, count=1, minimum=1, reveal=False,
                         to="hand", prompt=""):
    """Move up to `count` matching discard-pile cards to 'hand',
    'deck_shuffle', or 'deck_top' (ordered pick; the last pick ends on top).
    minimum=1 discipline for activated public-zone picks."""
    async def effect(ctx):
        await _deal_printed(ctx)
        cards = [c for c in ctx.discard_pile()
                 if predicate is None or predicate(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, count, minimum=minimum, ordered=(to == "deck_top"),
            prompt=prompt or "Choose card(s) from your discard pile",
        )
        if not picks:
            return
        if to == "hand":
            await ctx.put_in_hand(picks, reveal=reveal)
        elif to == "deck_shuffle":
            await ctx.shuffle_into_deck(picks)
        elif to == "deck_top":
            for card in picks:
                await ctx.put_on_top_of_deck(card)
    return effect


# --- Draw family ---------------------------------------------------------------

def draw_attack(n):
    """Printed damage (if an attack), then draw `n`; also fine as an ability."""
    async def effect(ctx):
        await _deal_printed(ctx)
        await ctx.draw_cards(n)
    return effect


def conditional_draw(base, bonus, predicate):
    """Draw `base`, or `base + bonus` when `predicate(ctx)` holds (Kabu shape)."""
    async def effect(ctx):
        await _deal_printed(ctx)
        count = base + (bonus if predicate(ctx) else 0)
        if count > 0:
            await ctx.draw_cards(count)
    return effect


def discard_then_draw(discard_count, draw_count, whole_hand=False,
                      optional=True, predicate=None, prompt=""):
    """Discard from hand, then draw. optional=True gates the draw on any
    discard ("If you do..."); whole_hand discards everything and always draws.
    draw_count may be `int` or `(ctx, discarded) -> int` (Milo's 2-per)."""
    async def effect(ctx):
        await _deal_printed(ctx)
        if whole_hand:
            discarded = [c for c in ctx.hand()
                         if predicate is None or predicate(c)]
            await ctx.discard_cards(discarded)
        else:
            discarded = await ctx.discard_from_hand(
                discard_count, minimum=0 if optional else None,
                predicate=predicate,
                prompt=prompt or ("Choose up to %d card(s) to discard" % discard_count
                                  if optional else
                                  "Choose %d card(s) to discard" % discard_count),
            )
            if not discarded:
                return
        n = draw_count(ctx, discarded) if callable(draw_count) else draw_count
        if n > 0:
            await ctx.draw_cards(n)
    return effect


def draw_until_effect(n, optional=False):
    """Draw until the hand holds `n` cards (Dragon's Hoard shape).

    `optional=True` is the "you may draw until you have N cards in your hand"
    wording: the ability is announced and the player may stop where they are."""
    async def effect(ctx):
        await _deal_printed(ctx)
        if optional:
            asked = await ctx.ask_yes_no(
                f"Draw until you have {n} cards in your hand?", player_id=ctx.player_id)
            if not asked:
                return 0
        return await ctx.draw_until(n)
    return effect


def shuffle_hand_into_deck_draw(n, opponent_n=None):
    """Shuffle your hand into your deck and draw `n` (Cynthia); with
    opponent_n the opponent then does the same drawing that many (Judge)."""
    async def effect(ctx):
        await _deal_printed(ctx)
        await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
        await ctx.draw_cards(n)
        if opponent_n is not None:
            await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
            await ctx.draw_cards(opponent_n, ctx.opponent_id)
    return effect


def look_at_top(n, take=1, predicate=None, rest="shuffle", minimum=None,
                prompt=""):
    """Look at the top `n` deck cards, put up to `take` matches into hand;
    rest: 'shuffle' the deck, 'bottom' the others under it, 'back' leaves
    them on top in order. minimum=None picks exactly `take` (or all if fewer)."""
    async def effect(ctx):
        await _deal_printed(ctx)
        top = ctx.deck_top(n)
        if not top:
            return []
        candidates = [c for c in top if predicate is None or predicate(c)]
        picks: List[CardEntity] = []
        if take > 0:
            # No matches still shows the looked-at cards (nothing selectable).
            picks = await ctx.choose_cards(
                candidates, take, minimum=minimum,
                prompt=prompt or "Choose a card to put into your hand.",
                display_cards=top if len(candidates) < len(top) else None,
            )
            if picks:
                await ctx.put_in_hand(picks, reveal=False)
        if rest == "shuffle":
            await ctx.shuffle_deck()
        elif rest == "bottom":
            for card in top:
                if card not in picks:
                    await ctx.put_on_bottom_of_deck(card)
        elif rest == "discard":
            for card in top:
                if card not in picks:
                    await ctx.discard_cards([card])
        # The signal for a follow-up rider: the cards taken into hand, or --
        # with take=0, where the body is only "look at them" -- the cards looked
        # at, which is what a reorder/attach rider consumes.
        return picks if take > 0 else list(top)
    return effect


# --- Heal family -----------------------------------------------------------------

async def _heal_scope_targets(ctx, scope, condition_cure=False):
    """Targets for a heal scope; 'choice'/'bench_choice' pick one eligible."""
    if scope == "active":
        active = ctx.my_active()
        return [active] if active is not None else []
    if scope in ("each_own", "all_own"):
        return ctx.my_pokemon_in_play()
    pool = ctx.my_bench() if scope == "bench_choice" else ctx.my_pokemon_in_play()
    eligible = [p for p in pool
                if _is_damaged(ctx.board, p)
                or (condition_cure and _has_conditions(p))]
    if not eligible:
        return []
    target = await ctx.choose_pokemon(eligible, "Choose a Pokémon to heal")
    return [target] if target is not None else []


def heal_attack(amount=None, all_damage=False, discard_energy=0, target="self"):
    """Printed damage, optional self energy-discard cost, then heal this
    Pokémon (`target='self'`) or your Active; all_damage heals everything."""
    async def effect(ctx):
        await _deal_printed(ctx)
        pokemon = ctx.attacker if target == "self" else ctx.my_active()
        if pokemon is None:
            return 0
        if discard_energy > 0:
            await ctx.discard_energy_from(
                pokemon, discard_energy,
                prompt=f"Discard {discard_energy} Energy",
            )
        heal_amount = (ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)) \
            if all_damage else (amount or 0)
        if heal_amount <= 0:
            return 0
        # HP actually healed, so "if you healed" riders are testable.
        return await ctx.heal(heal_amount, pokemon)
    return effect


def heal_targets(amount, scope="each_own", pred=None):
    """Heal `amount` from the scope: 'each_own'/'all_own' (every one of
    yours), 'active', 'bench_choice', or 'choice' (pick one damaged).

    `pred(pokemon)` narrows the scope, for "heal 30 from each of your Pokemon
    that has any damage counters on it"."""
    async def effect(ctx):
        await _deal_printed(ctx)
        healed = 0
        for pokemon in await _heal_scope_targets(ctx, scope):
            if pred is not None and not pred(pokemon):
                continue
            healed += await ctx.heal(amount, pokemon)
        return healed
    return effect


def heal_item(amount, scope="choice", condition_cure=False):
    """Trainer heal over a scope (see heal_targets); condition_cure also
    removes Special Conditions (Pokémon Center Lady). Gate playability with
    requires_damaged_pokemon()."""
    async def effect(ctx):
        for pokemon in await _heal_scope_targets(ctx, scope, condition_cure):
            if amount > 0:
                await ctx.heal(amount, pokemon)
            if condition_cure:
                await ctx.cure_all_conditions(pokemon)
    return effect


def cure_conditions_effect(scope="active"):
    """Remove all Special Conditions from the scope ('active', 'choice',
    'each_own'); conditions only, never attack locks."""
    async def effect(ctx):
        await _deal_printed(ctx)
        if scope == "choice":
            afflicted = [p for p in ctx.my_pokemon_in_play() if _has_conditions(p)]
            if not afflicted:
                return
            target = await ctx.choose_pokemon(afflicted, "Choose a Pokémon to recover")
            targets = [target] if target is not None else []
        elif scope in ("each_own", "all_own"):
            targets = [p for p in ctx.my_pokemon_in_play() if _has_conditions(p)]
        else:
            active = ctx.my_active()
            targets = [active] if active is not None else []
        for pokemon in targets:
            await ctx.cure_all_conditions(pokemon)
    return effect


# --- Switching / gusting -----------------------------------------------------------

async def opponent_switches(ctx):
    """The opponent switches their Active with a Benched Pokémon of THEIR
    choice (escape_rope precedent); returns the new Active, or None."""
    bench = ctx.opponent_bench()
    if not bench:
        return None
    target = await ctx.choose_pokemon(
        bench, "Choose your new Active Pokémon", player_id=ctx.opponent_id
    ) or bench[0]
    await ctx.switch_active(ctx.opponent_id, target)
    return target


def flip_opponent_switches(title=""):
    """Flip a coin. If heads, the opponent switches their Active with a
    Benched Pokémon of their choice (Pokémon Reversal)."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, title or "Pokémon Reversal")
        if results and results[0]:
            await opponent_switches(ctx)
    return effect


def switch_self_attack(damage=None, optional=False, bench_predicate=None,
                       then=None):
    """Damage first (text order), then switch this Pokémon with a Benched one
    of your choice; optional adds the "you may" dialog. `then(ctx, new_active)`
    runs only when the switch actually happened, for the "if you do, ..."
    riders (move Energy onto it, put counters on it)."""
    async def effect(ctx):
        if damage is not None:
            if damage > 0:
                await ctx.deal_damage(damage)
        else:
            await _deal_printed(ctx)
        bench = [p for p in ctx.my_bench()
                 if bench_predicate is None or bench_predicate(p)]
        if not bench:
            return None
        if optional and not await ctx.ask_yes_no(
                "Switch this Pokémon with 1 of your Benched Pokémon?"):
            return None
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is not None and await ctx.switch_active(ctx.player_id, target):
            if then is not None:
                await then(ctx, target)
            # The new Active (or None) is the signal for "then the opponent switches".
            return target
        return None
    return effect


def switch_then_opponent_switches(damage=None, optional=False):
    """Damage, then "switch this Pokemon with 1 of your Benched Pokemon. If you
    do, your opponent switches [the Defending Pokemon] with 1 of their Benched
    Pokemon" (Sonic Blade, Gyro Ball). The opponent picks their new Active, so
    the rider is `opponent_switches`; it runs only when our switch happened."""
    async def then(ctx, new_active):
        await opponent_switches(ctx)
    return switch_self_attack(damage, optional=optional, then=then)


async def _gust(ctx, opponent_chooses=False):
    """Switch one of the opponent's Benched Pokémon with their Active;
    returns the new Active or None (no bench / effect-shielded Active)."""
    old_active = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if old_active is None or not bench:
        return None
    if ctx.effects_blocked(old_active):
        return None
    if opponent_chooses:
        return await opponent_switches(ctx)
    target = await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon"
    ) or bench[0]
    await ctx.switch_active(ctx.opponent_id, target)
    return target


def gust_attack(damage_to_new_active=0, damage_before=None, opponent_chooses=False):
    """Gust: switch an opposing Benched Pokémon with their Active (YOU choose
    unless the text says the opponent switches); optional damage before the
    switch (printed by default) and onto the new Active after."""
    async def effect(ctx):
        if damage_before is not None:
            if damage_before > 0:
                await ctx.deal_damage(damage_before)
        else:
            await _deal_printed(ctx)
        new_active = await _gust(ctx, opponent_chooses)
        if new_active is not None and damage_to_new_active > 0:
            await ctx.deal_damage(damage_to_new_active, target=new_active)
    return effect


def gust_then_damage(amount: int, opponent_chooses: bool = False):
    """"Switch in 1 of your opponent's Benched Pokemon to the Active Spot. This
    attack does N damage to the new Active Pokemon." A thin name for
    `gust_attack(damage_to_new_active=amount, damage_before=0)`, which already
    chains the switched-in Active as the target; both attack and ability bodies
    can use it."""
    return gust_attack(damage_to_new_active=amount, damage_before=0,
                       opponent_chooses=opponent_chooses)


def gust_then(then, opponent_chooses=False):
    """Gust composite: switch, then `then(ctx, new_active)` (conditions etc.)."""
    async def effect(ctx):
        await _deal_printed(ctx)
        new_active = await _gust(ctx, opponent_chooses)
        if new_active is not None:
            await then(ctx, new_active)
    return effect


# --- Self-removal from play -----------------------------------------------------

_REMOVAL_PROMPTS = {
    "hand": "Put this Pokémon and all attached cards into your hand?",
    "deck": "Shuffle this Pokémon and all attached cards into your deck?",
    "lost_zone": "Put this Pokémon in the Lost Zone?",
}


def remove_self_from_play(destination="hand", with_attachments="same",
                          optional=False, prompt=""):
    """Remove the acting Pokémon from play to 'hand', 'deck' (shuffled) or
    'lost_zone'; with_attachments 'same' takes the whole stack along ("this
    Pokémon and all attached cards"), 'discard' discards the attachments
    (Scoop Up Net). Vacating the Active defers promotion (psychic_leap)."""
    async def effect(ctx):
        pokemon = ctx.source
        await _deal_printed(ctx)
        if optional and not await ctx.ask_yes_no(
                prompt or _REMOVAL_PROMPTS.get(destination, "Remove this Pokémon from play?")):
            return
        was_active = pokemon is ctx.my_active()
        if with_attachments == "discard":
            await ctx.discard_cards([c for c in full_stack(pokemon) if c is not pokemon])
            stack = [pokemon]
        else:
            stack = full_stack(pokemon)
        if destination == "hand":
            await ctx.put_in_hand(stack, reveal=False)
        elif destination == "deck":
            await ctx.shuffle_into_deck(stack, ctx.player_id)
        elif destination == "lost_zone":
            await ctx.move_to_lost_zone(stack)
        if was_active:
            # Promotion must wait for the attack bracket to flush, or the client
            # sees the new Active land while the old one still stands there.
            async def _promote():
                if not await ctx.session._promote_new_active(ctx.player_id):
                    screen_name = ctx.session.players[ctx.player_id].screen_name
                    await ctx.session.end_game(
                        ctx.opponent_id, f"{screen_name} has no Pokémon left"
                    )

            ctx.deferred_actions.append(_promote)
    return effect


# --- Playability condition factories ---------------------------------------------
# Each returns a check accepting BOTH call shapes: trainers/energies call
# (board, player_id), abilities call (board, player_id, pokemon).

def requires_discard(predicate=None, n=1):
    """At least `n` matching cards sit in the player's discard pile."""
    def check(board, player_id, pokemon=None):
        area = board.find_player_area(player_id, "discard")
        cards = list(area.children) if area else []
        return sum(1 for c in cards if predicate is None or predicate(c)) >= n
    return check


def requires_bench_space(n=1):
    """At least `n` free bench slots."""
    def check(board, player_id, pokemon=None):
        bench = board.find_player_area(player_id, "bench")
        return bench is not None and BENCH_CAPACITY - len(bench.children) >= n
    return check


def _side_player_ids(board, player_id, side) -> List[str]:
    pids = [player_id] if side in ("mine", "any") else []
    if side in ("opponent", "any"):
        opponent = _opponent_of(board, player_id)
        if opponent:
            pids.append(opponent)
    return pids


def requires_in_play(predicate, side="mine"):
    """A Pokémon matching `predicate` is in play on 'mine'/'opponent'/'any' side."""
    def check(board, player_id, pokemon=None):
        return any(predicate(p) for pid in _side_player_ids(board, player_id, side)
                   for p in board.pokemon_in_play(pid))
    return check


def requires_hand(predicate=None, n=1, exclude_self=True):
    """At least `n` matching cards in hand. exclude_self discounts the card
    being played when it may be among the matches (predicate None always
    matches it; otherwise only Trainer-card matches are suspect) -- pass
    exclude_self=False when the card itself can never match `predicate`."""
    def check(board, player_id, pokemon=None):
        hand = board.find_player_area(player_id, "hand")
        matches = [c for c in (hand.children if hand else [])
                   if predicate is None or predicate(c)]
        discount = 0
        if exclude_self and pokemon is None:
            if predicate is None or any(is_trainer_card(c) for c in matches):
                discount = 1
        return len(matches) - discount >= n
    return check


def requires_damaged_pokemon(side="mine"):
    """A damaged Pokémon is in play on 'mine'/'opponent'/'any' side."""
    def check(board, player_id, pokemon=None):
        return any(_is_damaged(board, p)
                   for pid in _side_player_ids(board, player_id, side)
                   for p in board.pokemon_in_play(pid))
    return check


def heal_all_from_one():
    """Heal all damage from 1 of your Pokemon (pick the damaged one)."""
    async def effect(ctx):
        await _deal_printed(ctx)
        damaged = [p for p in ctx.my_pokemon_in_play() if _is_damaged(ctx.board, p)]
        if not damaged:
            return
        target = await ctx.choose_pokemon(damaged, "Choose a Pokémon to heal")
        if target is None:
            return
        amount = ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)
        if amount > 0:
            await ctx.heal(amount, target)
    return effect


# --- Ultimate Zone ---------------------------------------------------------

def _bench_energy_holders(ctx):
    return [p for p in ctx.my_bench() if ctx.board.attached_energies(p)]


def move_bench_energy_to_named_active(name):
    """"The player may move an Energy card attached to 1 of his or her
    Benched Pokemon to his or her Active <name> as often as he or she likes"
    (Ultimate Zone) -- an UNLIMITED Stadium ability, so it is repeatable."""

    def _active_is_named(board, player_id):
        active = board.active_pokemon(player_id)
        if active is None:
            return False
        printed = (getattr(def_for(active.archetype_id), "display_name", "") or "").lower()
        return printed == name.lower() or printed.startswith(name.lower() + " ")

    def condition(board, player_id, stadium):
        if not _active_is_named(board, player_id):
            return False
        bench = board.find_player_area(player_id, "bench")
        return any(bool(board.attached_energies(p)) for p in (bench.children if bench else []))

    async def effect(ctx):
        active = ctx.board.active_pokemon(ctx.player_id)
        if active is None:
            return
        energies = [energy for pokemon in _bench_energy_holders(ctx)
                    for energy in ctx.board.attached_energies(pokemon)]
        if not energies:
            return
        for energy in await ctx.choose_cards(
                energies, 1, minimum=1,
                prompt=f"Choose an Energy to move to your Active {name}"):
            await ctx.move_energy(energy, active)

    return effect, condition


def search_attach_energy_then_lock_attacks(count=2, prompt=""):
    """"Search your deck for up to N Basic Energy cards and attach them to 1
    of your Pokemon. Then, shuffle your deck. During this turn, your Pokemon
    can't attack. (This includes Pokemon that come into play this turn.)"
    (Geeta)."""
    async def effect(ctx):
        cards = await ctx.search_deck(
            lambda card: is_energy_card(card) and not bool(card.get_attribute(AttrID.IS_SPECIAL_ENERGY)),
            count=count, minimum=0,
            prompt=prompt or f"Choose up to {count} Basic Energy cards",
        )
        if cards:
            target = None
            in_play = ctx.my_pokemon_in_play()
            if len(in_play) == 1:
                target = in_play[0]
            else:
                picks = await ctx.choose_cards(
                    in_play, 1, minimum=1,
                    prompt="Choose a Pokémon to attach the Energy to",
                )
                target = picks[0] if picks else None
            if target is not None:
                for card in cards:
                    await ctx.attach_energy(card, target)
        await ctx.shuffle_deck()
        ctx.lock_player_attacks()

    return effect


async def sabrinas_psychic_control(ctx):
    """"Flip a coin. If heads, choose a Trainer card in your opponent's discard
    pile that isn't put in play ... You may use that card as if it were in your
    hand" (Sabrina's Psychic Control)."""
    if not await ctx.flip_coins(1):
        return
    await ctx.use_trainer_from_opponent_discard(
        "Choose a Trainer card in your opponent's discard pile to use"
    )


def baby_evolution(*names):
    """"Once during your turn, you may put <name> from your hand onto this
    Pokemon (this counts as evolving it) and remove all damage counters from
    it" (Baby Evolution).

    Returns (effect, condition): the offer must disappear when no copy of the
    named card is in hand. perform_evolution nests the pre-evolution under a
    NEW entity and carries the damage across, so the counters are cleared on
    the evolution card that was just played, not on ctx.source."""
    wanted = {" ".join((name or "").lower().split()) for name in names}

    def _in_hand(board, player_id, pokemon) -> bool:
        area = board.find_player_area(player_id, "hand")
        return any(
            " ".join(entity_name(card).lower().split()) in wanted
            for card in (area.children if area else [])
        )

    async def effect(ctx):
        cards = [card for card in ctx.hand()
                 if " ".join(entity_name(card).lower().split()) in wanted]
        if not cards:
            return
        picks = cards if len(cards) == 1 else await ctx.choose_cards(
            cards, 1, minimum=1,
            prompt="Choose the Evolution card to put onto this Pokémon",
        )
        if not picks:
            return
        evolution = picks[0]
        if not await ctx.evolve_pokemon(ctx.source, evolution):
            return
        remaining = evolution.get_attribute(AttrID.HP, 0)
        await ctx.heal(max(0, ctx.max_hp(evolution) - remaining), evolution)

    return effect, _in_hand


def attach_from_hand(predicate=None, count=1, target="choice", target_pred=None,
                     distribute=False, minimum=1, then=None, prompt=""):
    """"Attach up to N Energy from your hand to <target>": offers the matching
    hand cards, then attaches them to this Pokemon ("self"), to one chosen
    Pokemon of `ctx.my_pokemon_in_play()` filtered by `target_pred` ("choice"),
    or one per card through distribute_energy ("in any way you like").

    `then(ctx, attached)` runs afterwards with the (card, target) pairs, for the
    "if you attached Energy to a Pokemon in this way, ..." riders. `minimum=0`
    for "you may ... up to N" and repeatable abilities; `minimum=1` when
    choosing the ability is the commitment."""
    predicate = predicate or is_energy_card

    def _targets(ctx):
        return [pokemon for pokemon in ctx.my_pokemon_in_play()
                if target_pred is None or target_pred(pokemon)]

    async def effect(ctx):
        hand = [card for card in ctx.hand() if predicate(card)]
        if not hand:
            return []
        picks = await ctx.choose_cards(
            hand, count, minimum=minimum,
            prompt=prompt or f"Choose up to {count} card(s) to attach")
        if not picks:
            return []
        attached = []
        if target == "self":
            for card in picks:
                await _attach_all(ctx, [card], ctx.source)
                attached.append((card, ctx.source))
        else:
            candidates = _targets(ctx)
            if not candidates:
                return []
            if distribute:
                attached = await distribute_energy(ctx, picks, candidates)
            else:
                pokemon = await ctx.choose_pokemon(
                    candidates, "Choose a Pokémon to attach the Energy to")
                if pokemon is None:
                    pokemon = candidates[0]
                await _attach_all(ctx, picks, pokemon)
                attached = [(card, pokemon) for card in picks]
        if then is not None and attached:
            # Sync or async: a rider that only reads the pairs is written
            # plainly, and one that moves cards awaits.
            outcome = then(ctx, attached)
            if outcome is not None and hasattr(outcome, "__await__"):
                await outcome
        # The (card, target) pairs are the "did an Energy actually land" signal
        # for composed()/do_a_then_b riders.
        return attached

    return effect


def hand_attach_condition(predicate=None, target="choice", target_pred=None) -> Callable:
    """Gate for a hand-attach ability: offering it would do nothing unless a
    matching hand card and a legal target are both there. An UNLIMITED
    activation MUST carry a condition or its offer never disappears."""
    predicate = predicate or is_energy_card

    def condition(board, player_id, pokemon) -> bool:
        hand = board.find_player_area(player_id, "hand")
        if not any(predicate(card) for card in (hand.children if hand else [])):
            return False
        if target == "self":
            return True
        return any(target_pred is None or target_pred(p)
                   for p in board.pokemon_in_play(player_id))

    return condition


def _energy_pool(ctx, name, predicate=None):
    if name == "bench":
        pool = ctx.my_bench()
    elif name == "active":
        active = ctx.my_active()
        pool = [active] if active is not None else []
    else:
        pool = ctx.my_pokemon_in_play()
    return [pokemon for pokemon in pool if predicate is None or predicate(pokemon)]


def move_energy_between(predicate=None, count=1, from_pool="any", to_pool="any",
                        source_pred=None, then=None,
                        prompt="Choose an Energy to move", to_pred=None):
    """"Move [up to N] Energy card(s) attached to <one of your Pokemon> to
    another of your Pokemon" (Sceptile, Simisear, Team Rocket's Energy).

    Pools are "any" (every Pokemon in play), "bench" or "active"; the holder is
    never offered as its own destination. `count=None` allows any number, and
    `to_pred(pokemon, ctx)` narrows which Pokemon may receive it (Misty's Water
    Command: "to your Active Pokemon")."""
    predicate = predicate or is_energy_card

    async def effect(ctx):
        sources = _energy_pool(ctx, from_pool, source_pred)
        energies = [energy for pokemon in sources
                    for energy in ctx.attached_energies(pokemon)
                    if predicate(energy)]
        if not energies:
            return
        destinations = [p for p in _energy_pool(ctx, to_pool)
                        if to_pred is None or to_pred(p, ctx)]
        if not destinations or (len(destinations) == 1 and destinations[0] is sources[0]
                                and len(sources) == 1):
            return
        moved = await ctx.move_energy_freely(
            sources, destinations, predicate=predicate,
            max_count=count, prompt=prompt,
        )
        if then is not None and moved:
            await then(ctx, moved)

    return effect


def can_move_energy(predicate=None, from_pool="any", to_pool="any",
                    source_pred=None) -> Callable:
    """Condition for a repeatable move-Energy ability: an eligible Energy sits
    on a source and another Pokemon can receive it."""
    predicate = predicate or is_energy_card

    def condition(board, player_id, pokemon) -> bool:
        def pool(name):
            if name == "bench":
                area = board.find_player_area(player_id, "bench")
                return list(area.children) if area else []
            if name == "active":
                active = board.active_pokemon(player_id)
                return [active] if active is not None else []
            return board.pokemon_in_play(player_id)

        sources = [p for p in pool(from_pool) if source_pred is None or source_pred(p)]
        carriers = [p for p in sources
                    if any(predicate(energy) for energy in board.attached_energies(p))]
        return bool(carriers) and len(pool(to_pool)) >= 2

    return condition


def return_attached_energy(count=1, energy_type=None, all=False, to="hand",
                           target="self", then=None, prompt=""):
    """"Return [an] Energy card[s] attached to <target> to your hand|deck."

    `target` is "self" (the source Pokemon), "choice" (any of yours) or a
    callable(pokemon) predicate. `then(ctx, returned)` runs only when something
    was actually returned, for the "If you do, ..." riders."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        if callable(target):
            pool = [pokemon for pokemon in ctx.my_pokemon_in_play() if target(pokemon)]
        elif target == "choice":
            pool = ctx.my_pokemon_in_play()
        else:
            pool = [ctx.source] if isinstance(ctx.source, PokemonEntity) else []
        candidates = []
        for pokemon in pool:
            for energy in ctx.attached_energies(pokemon):
                if type_value is None or energy_provides_type(energy, type_value):
                    candidates.append(energy)
        if not candidates:
            return
        if all:
            picks = candidates
        elif len(candidates) == 1:
            picks = candidates
        else:
            picks = await ctx.choose_cards(
                candidates, count, minimum=0,
                prompt=prompt or f"Choose up to {count} Energy card(s) to return")
        if not picks:
            return
        if to == "deck":
            await ctx.shuffle_into_deck(picks)
        else:
            await ctx.put_in_hand(picks)
        if then is not None:
            await then(ctx, picks)

    return effect
