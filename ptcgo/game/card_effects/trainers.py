"""Behaviors for the Trainer cards of the Lugia VSTAR and Mew VMAX decks."""

import re

from ptcgo.game.attributes import (
    AttrID, CardType, CLIENT_POKEMON_TYPE_NAMES, PokemonStage, PokemonTypes,
    SpecialConditions, TrainerType,
)
from ptcgo.game.models.board import PokemonEntity
from ptcgo.game.data_utils import (
    Ability, Activations, Attack, def_for, evolves_from, has_rule_box,
    is_pokemon_v, subtypes_for, VisualizationArrow, VisualizationType,
)
from ptcgo.game.session.constants import BENCH_CAPACITY
from ptcgo.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_evolution_pokemon,
    is_item_card,
    is_pokemon_card,
    is_special_energy,
    is_supporter_card,
    is_trainer_card,
    is_water_pokemon,
)
from ptcgo.game.session.passives import (
    Passive,
    TurnDamageModifier,
    carrier_pokemon,
    effective_bench_capacity,
    effective_max_hp,
    trainer_play_blocked,
)
from ptcgo.game.card_effects.passives_common import (
    attack_discount_passive,
    condition_immunity_passive,
    is_in_active_spot,
    TempShieldPassive,
    hp_bonus_tool,
    no_resistance_passive,
    retreat_free_when,
    no_weakness_passive,
    retreat_discount,
    takes_less_passive,
    typed_damage_boost_tool,
)


# --- Shared playability predicates -----------------------------------------

def hand_size_at_least(count: int):
    """Condition: the hand holds `count` cards INCLUDING the trainer itself."""
    def check(board, player_id):
        hand = board.find_player_area(player_id, "hand")
        return hand is not None and len(hand.children) >= count
    return check


def _bench_pokemon(board, player_id):
    bench = board.find_player_area(player_id, "bench")
    return [c for c in (bench.children if bench else [])
            if isinstance(c, PokemonEntity)]


def _other_player(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


def opponent_has_bench(board, player_id):
    opponent = _other_player(board, player_id)
    return bool(opponent) and bool(_bench_pokemon(board, opponent))

################### --- make_target_selector ---
# The make_target_selector function is a factory that returns a targeting selector for Trainer cards to highlight valid targets on the UI.
# It allows the card to be dragged directly into a Pokémon for cards that require selecting a Pokémon.
# It dynamically evaluates configurations based on two boolean flags:
# 1) opponent: If True, the only Pokémon you can drag the trainer to will be the ones in the opponent's side; if False, the ones on the player's own side.
# 2) bench_only: If True, the only Pokémon you can drag the trainer to are the ones inside that player's "bench" area; if False, the Active is also included.

def make_target_selector(opponent=False, bench_only=False):

    def selector(board, player_id, card):
        if card is None:
            return []
            
        # Determine the target player ID based on the opponent flag
        target_id = (
            next((p for p in board.player_ids if p != player_id), None)
            if opponent 
            else player_id
        )
        if not target_id:
            return []

        # Configuration 1: Returns ONLY Benched Pokémon entities (e.g., Boss's Orders, Switch)
        if bench_only:
            bench = board.find_player_area(target_id, "bench")
            return [c for c in (bench.children if bench else []) if c is not None]

        # Configuration 2: Returns all Pokémon in play (Active + Bench) (e.g., Crushing Hammer, Potion)
        return [p for p in board.pokemon_in_play(target_id) if p is not None]
        
    return selector

# --- TEMPORARY BACKWARD COMPATIBILITY LAYER ---
# These functions route old card registrations directly into the new engine. Please update your coding as it will be removed in the future. 
def play_targets(opponent=False, bench_only=False):
    """Deprecated: Use make_target_selector(opponent=..., bench_only=...) instead."""
    return make_target_selector(opponent=opponent, bench_only=bench_only)

def opponent_play_targets(bench_only=False):
    """Deprecated: Use make_target_selector(opponent=True, bench_only=...) instead."""
    return make_target_selector(opponent=True, bench_only=bench_only)
    
def player_play_targets(bench_only=False):
    """Deprecated: Use make_target_selector(opponent=False, bench_only=...) instead."""
    return make_target_selector(opponent=False, bench_only=bench_only)
#####################

def player_has_bench(board, player_id):
    return bool(_bench_pokemon(board, player_id))


def someone_has_bench(board, player_id):
    return bool(_bench_pokemon(board, player_id)) or opponent_has_bench(board, player_id)


def has_supporter_in_discard(board, player_id):
    return any(is_supporter_card(c) for c in _discard(board, player_id))


def has_discard_card(board, player_id):
    return bool(_discard(board, player_id))


def opponent_prizes_low(board, player_id):
    """Roxanne's gate: the opponent has 3 or fewer Prize cards remaining."""
    opponent = _other_player(board, player_id)
    if not opponent:
        return False
    area = board.find_player_area(opponent, "prizePile")
    return bool(area) and len(area.children) <= 3


def battle_vip_pass_playable(board, player_id):
    turn_state = getattr(board, "turn_state", None)
    if turn_state is None or turn_state.turn_number > 2:
        return False
    bench = board.find_player_area(player_id, "bench")
    return bool(bench) and len(bench.children) < BENCH_CAPACITY


def has_other_item_in_hand(board, player_id):
    """Cram-o-matic's gate: another Item card besides itself sits in hand."""
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and sum(1 for c in hand.children if is_item_card(c)) >= 2


def deck_nonempty(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck) and bool(deck.children)


def _opponent_special_energies(board, player_id):
    opponent = _other_player(board, player_id)
    if not opponent:
        return []
    out = []
    for pokemon in board.pokemon_in_play(opponent):
        out.extend(c for c in pokemon.children if is_special_energy(c))
    return out


def opponent_has_special_energy(board, player_id):
    return bool(_opponent_special_energies(board, player_id))


def _discard(board, player_id):
    area = board.find_player_area(player_id, "discard")
    return list(area.children) if area else []


def is_energy_card(card) -> bool:
    return card.get_attribute(AttrID.CARD_TYPE) == CardType.ENERGY.value


def is_basic_energy_card(card) -> bool:
    return is_energy_card(card) and not is_special_energy(card)


def is_metal_energy_card(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.METAL.value in types


def is_grass_energy_card(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.GRASS.value in types


def is_psychic_energy_card(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.PSYCHIC.value in types


def is_darkness_pokemon(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.DARKNESS.value in types


def is_pokemon_vmax(archetype_id) -> bool:
    return "VMAX" in subtypes_for(archetype_id)


def has_basic_energy_in_hand(board, player_id) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_basic_energy_card(c) for c in hand.children)


def bede_playable(board, player_id) -> bool:
    return player_has_bench(board, player_id) and has_basic_energy_in_hand(board, player_id)


def _opponent_energies(board, player_id):
    opponent = _other_player(board, player_id)
    if not opponent:
        return []
    out = []
    for pokemon in board.pokemon_in_play(opponent):
        out.extend(c for c in pokemon.children if is_energy_card(c))
    return out


def opponent_has_energy_attached(board, player_id) -> bool:
    return bool(_opponent_energies(board, player_id))


def _my_vmax_pokemon(board, player_id):
    return [p for p in board.pokemon_in_play(player_id) if is_pokemon_vmax(p.archetype_id)]


def has_vmax_in_play(board, player_id) -> bool:
    return bool(_my_vmax_pokemon(board, player_id))


def has_two_metal_energy_in_hand(board, player_id) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and sum(1 for c in hand.children if is_metal_energy_card(c)) >= 2


def _tools_and_stadium(board):
    """Every attached Pokemon Tool plus the Stadium in play."""
    targets = []
    for pid in board.player_ids:
        for pokemon in board.pokemon_in_play(pid):
            for child in pokemon.children:
                if child.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value:
                    targets.append(child)
    stadium_area = board.find_global_area("activeStadium")
    targets.extend(stadium_area.children if stadium_area else [])
    return targets


def lost_vacuum_playable(board, player_id):
    return hand_size_at_least(2)(board, player_id) and bool(_tools_and_stadium(board))


def serena_playable(board, player_id):
    if hand_size_at_least(2)(board, player_id):
        return True
    opponent = _other_player(board, player_id)
    return bool(opponent) and any(
        is_pokemon_v(p.archetype_id) for p in _bench_pokemon(board, opponent)
    )


# --- Supporters -------------------------------------------------------------

async def professors_research(ctx):
    """Discard your hand and draw 7 cards."""
    await ctx.discard_cards(ctx.hand())
    await ctx.draw_cards(7)


async def marnie(ctx):
    """Both players shuffle their hands under their decks; you draw 5, the
    opponent draws 4. Per player in sequence: shuffle-to-bottom, then draw."""
    await ctx.hand_to_bottom_of_deck(ctx.player_id)
    await ctx.draw_cards(5)
    await ctx.hand_to_bottom_of_deck(ctx.opponent_id)
    await ctx.draw_cards(4, ctx.opponent_id)


async def bosss_orders(ctx):
    """Switch 1 of the opponent's Benched Pokemon with their Active."""
    target = await ctx.choose_play_target(
        ctx.opponent_bench(), "Choose the opponent's new Active Pokémon"
    )
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


async def serena(ctx):
    """Choose 1: discard up to 3 then draw to 5, OR gust a Benched Pokemon V."""
    v_bench = [p for p in ctx.opponent_bench() if is_pokemon_v(p.archetype_id)]
    can_discard = bool(ctx.hand())
    if can_discard and v_bench:
        gust = await ctx.choose(
            "Choose 1:", ["Discard up to 3 cards from your hand. If you do, draw cards until you have 5 cards in your hand.", 
                          "Switch 1 of your opponent's Benched Pokemon V with their Active Pokemon."]
        ) == 1
    else:
        gust = bool(v_bench)
    if gust:
        target = await ctx.choose_pokemon(
            v_bench, "Choose the opponent's new Active Pokémon"
        )
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
        return
    discarded = await ctx.discard_from_hand(
        3, minimum=1, prompt="Choose up to 3 cards to discard"
    )
    if discarded:
        await ctx.draw_until(5)


async def irida(ctx):
    """Search the deck for up to 1 Water Pokemon and up to 1 Item card."""
    water, items = await ctx.search_deck_groups(
        [
            # loc keys render the {W} energy icon in the slot labels
            (is_water_pokemon, 1, "playmat.prompt.selectapokemonwater"),
            (is_item_card, 1, "playmat.prompt.select1item"),
        ],
        prompt="Choose up to 1 Water Pokémon and up to 1 Item card",
    )
    await ctx.put_in_hand(water + items, reveal=True)
    await ctx.shuffle_deck()


async def pal_pad(ctx):
    """Shuffle up to 2 Supporter cards from your discard pile into your deck."""
    picks = await ctx.choose_cards(
        [c for c in ctx.discard_pile() if is_supporter_card(c)], 2, minimum=1,
        prompt="Choose up to 2 Supporter cards to shuffle into your deck",
    )
    await ctx.shuffle_into_deck(picks)


async def judge(ctx):
    """Each player shuffles their hand into their deck and draws 4 cards."""
    for pid in (ctx.player_id, ctx.opponent_id):
        await ctx.shuffle_into_deck(ctx.hand(pid), pid)
        await ctx.draw_cards(4, pid)


async def roxanne(ctx):
    """Opponent has 3 or fewer Prize cards remaining: each player shuffles
    their hand into their deck, then you draw 6 and the opponent draws 2."""
    for pid, count in ((ctx.player_id, 6), (ctx.opponent_id, 2)):
        await ctx.shuffle_into_deck(ctx.hand(pid), pid)
        await ctx.draw_cards(count, pid)


async def cyllene(ctx):
    """Flip 2 coins; put up to that many cards from your discard pile on
    top of your deck, in an order you choose."""
    heads = await ctx.flip_coins(2, "Cyllene")
    count = heads.count(True)
    if count <= 0:
        return
    picks = await ctx.choose_cards(
        ctx.discard_pile(), count, minimum=1, ordered=True,
        prompt="Choose cards to put on top of your deck, in order",
    )
    # Ordered picks stack in selection order -- the last one picked ends up
    # on top of the deck.
    for card in picks:
        await ctx.put_on_top_of_deck(card)


async def piers(ctx):
    """Search your deck for an Energy card and a Darkness Pokemon, reveal
    them, and put them into your hand. Then, shuffle your deck."""
    energy, darkness = await ctx.search_deck_groups(
        [
            (is_energy_card, 1, "Energy card"),
            (is_darkness_pokemon, 1, "Darkness Pokémon"),
        ],
        prompt="Choose an Energy card and a Darkness Pokémon",
    )
    await ctx.put_in_hand(energy + darkness, reveal=True)
    await ctx.shuffle_deck()


async def bede(ctx):
    """Attach a basic Energy card from your hand to 1 of your Benched Pokemon."""
    energies = [c for c in ctx.hand() if is_basic_energy_card(c)]
    picked = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a basic Energy card to attach"
    )
    if not picked:
        return
    target = await ctx.choose_pokemon(
        ctx.my_bench(), "Choose the Benched Pokémon to attach it to"
    )
    if target is not None:
        await ctx.attach_energy(picked[0], target)


async def team_yell_grunt(ctx):
    """Put an Energy attached to 1 of the opponent's Pokemon into their hand."""
    targets = _opponent_energies(ctx.board, ctx.player_id)
    picked = await ctx.choose_cards(
        targets, 1, minimum=1,
        prompt="Choose an Energy card to return to its owner's hand",
    )
    # Already visible in play (attached), so no reveal-on-move is needed.
    await ctx.put_in_hand(picked, reveal=False)


async def milo(ctx):
    """Discard up to 2 cards from your hand, and draw 2 cards for each card
    you discarded in this way."""
    discarded = await ctx.discard_from_hand(
        2, minimum=0, prompt="Choose up to 2 cards to discard"
    )
    if discarded:
        await ctx.draw_cards(2 * len(discarded))


async def sonia(ctx):
    """Search your deck for up to 2 Basic Pokemon or up to 2 basic Energy
    cards, reveal them, and put them into your hand. Then, shuffle your deck."""
    want_energy = await ctx.choose(
        "Choose 1:", ["Up to 2 Basic Pokémon", "Up to 2 basic Energy cards"]
    ) == 1
    predicate = is_basic_energy_card if want_energy else is_basic_pokemon
    picks = await ctx.search_deck(
        predicate, count=2, minimum=0,
        prompt="Choose up to 2 Basic Pokémon or up to 2 basic Energy cards.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def kabu(ctx):
    """Shuffle your hand into your deck. Then, draw 4 cards; draw 8 instead
    if your Active Pokemon is your only Pokemon in play."""
    await ctx.shuffle_into_deck(ctx.hand())
    only_active = len(ctx.my_pokemon_in_play()) <= 1
    await ctx.draw_cards(8 if only_active else 4)


async def rose(ctx):
    """Attach up to 2 basic Energy cards from your discard pile to 1 of your
    Pokemon VMAX. If you attached any this way, discard your hand."""
    target = await ctx.choose_pokemon(
        _my_vmax_pokemon(ctx.board, ctx.player_id), "Choose your Pokémon VMAX"
    )
    if target is None:
        return
    energies = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    picks = await ctx.choose_cards(
        energies, 2, minimum=0, prompt="Choose up to 2 basic Energy cards to attach",
    )
    for energy in picks:
        await ctx.attach_energy(energy, target)
    if picks:
        await ctx.discard_cards(ctx.hand())


async def hop(ctx):
    """Draw 3 cards."""
    await ctx.draw_cards(3)


async def adaman(ctx):
    """Discard 2 Metal Energy cards from your hand, then search your deck
    for up to 2 cards and put them into your hand. Then, shuffle your deck."""
    discarded = await ctx.discard_from_hand(
        2, predicate=is_metal_energy_card,
        prompt="Discard 2 Metal Energy cards for Adaman",
    )
    if len(discarded) < 2:
        return
    picks = await ctx.search_deck(
        None, count=2, minimum=0, prompt="Choose up to 2 cards to put into your hand.",
    )
    # No "reveal it" clause on this card's text.
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


async def gardenias_vigor(ctx):
    """Draw 2 cards. If you drew any this way, attach up to 2 Grass Energy
    cards from your hand to 1 of your Benched Pokemon."""
    drawn = await ctx.draw_cards(2)
    if not drawn:
        return
    energies = [c for c in ctx.hand() if is_grass_energy_card(c)]
    if not energies:
        return
    target = await ctx.choose_pokemon(
        ctx.my_bench(), "Choose the Benched Pokémon to attach Grass Energy to",
        optional=True,
    )
    if target is None:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=0, prompt="Choose up to 2 Grass Energy cards to attach",
    )
    for energy in picks:
        await ctx.attach_energy(energy, target)


async def kamado(ctx):
    """Choose a card in your hand, and discard the other cards. If you do,
    draw 4 cards."""
    hand = ctx.hand()
    if not hand:
        return
    keep = await ctx.choose_cards(
        hand, 1, minimum=1, prompt="Choose a card to keep in your hand"
    )
    if not keep:
        return
    await ctx.discard_cards([c for c in hand if c is not keep[0]])
    await ctx.draw_cards(4)


async def zisu(ctx):
    """Draw cards until you have 1 more card in your hand than your opponent."""
    await ctx.draw_until(ctx.hand_size(ctx.opponent_id) + 1)


def _center_lady_targets(board, player_id):
    return [
        p for p in board.pokemon_in_play(player_id)
        if p.get_attribute(AttrID.SPECIAL_CONDITIONS)
        or p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
    ]


def center_lady_playable(board, player_id) -> bool:
    return bool(_center_lady_targets(board, player_id))


async def pokemon_center_lady(ctx):
    """Heal 60 damage from 1 of your Pokemon, and it recovers from all
    Special Conditions."""
    target = await ctx.choose_pokemon(
        _center_lady_targets(ctx.board, ctx.player_id), "Choose a Pokémon to heal"
    )
    if target is None:
        return
    await ctx.heal(60, target)
    await ctx.cure_all_conditions(target)


# --- Items -------------------------------------------------------------------

async def switch(ctx):
    """Switch your Active Pokemon with 1 of your Benched Pokemon."""
    target = await ctx.choose_play_target(ctx.my_bench(), "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


async def quick_ball(ctx):
    """Discard 1 other card, then search the deck for a Basic Pokemon."""
    if not await ctx.discard_from_hand(1, prompt="Discard a card for Quick Ball"):
        return
    picks = await ctx.search_deck(
        is_basic_pokemon, count=1, minimum=0,
        prompt="Choose a Basic Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def ultra_ball(ctx):
    """Discard 2 other cards, then search the deck for any Pokemon."""
    if len(await ctx.discard_from_hand(2, prompt="Discard 2 cards for Ultra Ball")) < 2:
        return
    picks = await ctx.search_deck(
        is_pokemon_card, count=1, minimum=0,
        prompt="Choose a Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def evolution_incense(ctx):
    """Search the deck for an Evolution Pokemon."""
    picks = await ctx.search_deck(
        is_evolution_pokemon, count=1, minimum=0,
        prompt="Choose an Evolution Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def escape_rope(ctx):
    """Each player switches their Active with a Benched Pokemon; the opponent
    chooses first and their swap is shown to both clients before the Escape
    Rope player decides (no Bench, no switch)."""
    opp_bench = ctx.opponent_bench()
    if opp_bench:
        target = await ctx.choose_pokemon(
            opp_bench, "Choose your new Active Pokémon", player_id=ctx.opponent_id
        )
        await ctx.switch_active(ctx.opponent_id, target or opp_bench[0])
        # Flush the opponent's swap so both clients see it land before the
        # Escape Rope player is prompted for their own switch.
        await ctx.flush_choreography()
    my_bench = ctx.my_bench()
    if my_bench:
        target = await ctx.choose_pokemon(
            my_bench, "Choose your new Active Pokémon", player_id=ctx.player_id
        )
        await ctx.switch_active(ctx.player_id, target or my_bench[0])


async def lost_vacuum(ctx):
    """Lost-Zone a card from hand, then Lost-Zone a Tool in play or the Stadium."""
    cost = await ctx.choose_cards(
        ctx.hand(), 1, prompt="Choose a card to put in the Lost Zone"
    )
    if not cost:
        return
    await ctx.move_to_lost_zone(cost)
    targets = _tools_and_stadium(ctx.board)
    picks = await ctx.choose_cards(
        targets, 1, prompt="Choose a Pokémon Tool or Stadium to put in the Lost Zone",
    )
    await ctx.move_to_lost_zone(picks)


async def battle_vip_pass(ctx):
    """First turn only: search the deck for up to 2 Basic Pokemon and put
    them onto your Bench."""
    bench = ctx.board.find_player_area(ctx.player_id, "bench")
    space = BENCH_CAPACITY - len(bench.children) if bench else 0
    count = min(2, space)
    if count <= 0:
        return
    picks = await ctx.search_deck(
        is_basic_pokemon, count=count, minimum=0,
        prompt="Choose up to 2 Basic Pokémon to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


def dream_ball_playable(board, player_id):
    """Dream Ball never plays from hand: its window is the prize-take prompt."""
    return False


async def dream_ball(ctx):
    """Search your deck for a Pokemon and put it onto your Bench."""
    picks = await ctx.search_deck(
        is_pokemon_card, count=1, minimum=0,
        prompt="Choose a Pokémon to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


async def dream_ball_prize_window(ctx):
    """Taken as a face-down Prize: you may play it before it settles in hand."""
    ctx.suppress_announce = True
    board, pid = ctx.board, ctx.player_id
    bench = board.find_player_area(pid, "bench")
    if not bench or len(bench.children) >= effective_bench_capacity(board, pid):
        return
    if not ctx.deck(pid):
        return
    if trainer_play_blocked(board, pid, ctx.source):
        return
    if not await ctx.ask_yes_no("Play Dream Ball? Search your deck for a "
                                "Pokémon and put it onto your Bench."):
        return
    await ctx.session._execute_play_trainer(pid, ctx.source)


async def power_tablet(ctx):
    """This turn, your Fusion Strike Pokemon's attacks do 30 more damage to
    the opponent's Active Pokemon (before Weakness and Resistance)."""
    ctx.add_turn_damage_modifier(
        TurnDamageModifier(30, ctx.player_id, requires_subtype="Fusion Strike")
    )
    # Green up-arrow PiP on each buffed Fusion Strike Pokemon in play.
    for pokemon in ctx.my_pokemon_in_play():
        if "Fusion Strike" in subtypes_for(pokemon.archetype_id):
            await ctx.add_stat_visualization(
                pokemon, VisualizationArrow.POSITIVE,
                VisualizationType.DAMAGE_DEALT_INCREASED, card_text="+30 damage"
            )


async def cramomatic(ctx):
    """Discard another Item card, then flip a coin; heads searches the deck
    for any card and puts it into your hand."""
    if not await ctx.discard_from_hand(
        1, predicate=is_item_card, prompt="Discard an Item card for Cram-o-matic"
    ):
        return
    heads, = await ctx.flip_coins(1, "Cram-o-matic")
    if not heads:
        return
    picks = await ctx.search_deck(
        None, count=1, minimum=0, prompt="Choose a card to put into your hand.",
    )
    # No "reveal it" clause on this card's text (unlike Ultra/Quick Ball).
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


async def rotom_phone(ctx):
    """Look at the top 5 cards of your deck, choose 1, shuffle the rest back
    into your deck, then put the chosen card on top."""
    top = ctx.deck_top(5)
    if not top:
        return
    picks = await ctx.choose_cards(
        top, 1, minimum=1, prompt="Choose a card to put on top of your deck",
    )
    if not picks:
        return
    await ctx.shuffle_deck_below(picks[0])


async def fan_of_waves(ctx):
    """Put a Special Energy attached to 1 of the opponent's Pokemon on the
    bottom of their deck."""
    targets = _opponent_special_energies(ctx.board, ctx.player_id)
    picks = await ctx.choose_cards(
        targets, 1, minimum=1,
        prompt="Choose a Special Energy to put on the bottom of their deck",
    )
    for card in picks:
        await ctx.put_on_bottom_of_deck(card)


async def star_alchemy(ctx):
    """Search your deck for a card and put it into your hand (VSTAR Power)."""
    picks = await ctx.search_deck(
        None, count=1, minimum=0, prompt="Choose a card to put into your hand.",
    )
    # No "reveal it" clause on this card's text (unlike Ultra/Quick Ball).
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


# --- Stadiums & Pokemon Tools -------------------------------------------------

class BigParasolPassive(Passive):
    """While the holder is in the Active Spot, shields the owner's whole
    side from the opponent's attack EFFECTS (not damage)."""

    def blocks_attack_effects(self, target, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or target.owning_player_id != holder.owning_player_id:
            return False
        parent = holder.parent
        return bool(parent) and parent.get_attribute(AttrID.NAME) == "activePokemonArea"


class PathToThePeakPassive(Passive):
    """Rule Box Pokemon (both sides) have no Abilities."""

    def blocks_abilities(self, pokemon, carrier):
        return has_rule_box(pokemon.archetype_id)


class LostCityPassive(Passive):
    """Knocked Out Pokemon go to the Lost Zone instead of the discard pile."""

    def knockout_destination(self, pokemon, carrier):
        return "lostZone"


class CollapsedStadiumPassive(Passive):
    """Each player can't have more than 4 Benched Pokemon (excess is discarded
    by enforce_bench_capacity when this comes into play)."""

    def bench_capacity(self, player_id, carrier):
        return 4


async def gapejaw_bog_watch(ctx):
    """Gapejaw Bog: 2 damage counters on any Basic just benched from hand."""
    pokemon = ctx.benched_pokemon
    if pokemon is None:
        return
    await ctx.deal_damage(20, target=pokemon, apply_modifiers=False,
                          as_counters=True)


class SkatersParkPassive(Passive):
    """Basic Energy paid for either player's retreat goes to hand instead."""

    def retreat_cost_destination(self, pokemon, energy, carrier):
        return "hand" if is_basic_energy_card(energy) else None


# ======================================================================
# Lost Zone Box + Regigigas decks
# ======================================================================

def is_v_or_gx(archetype_id) -> bool:
    return is_pokemon_v(archetype_id) or "GX" in subtypes_for(archetype_id)


def has_basic_energy_in_discard(board, player_id) -> bool:
    return any(is_basic_energy_card(c) for c in _discard(board, player_id))


def has_pokemon_or_basic_energy_in_discard(board, player_id) -> bool:
    return any(is_pokemon_card(c) or is_basic_energy_card(c)
               for c in _discard(board, player_id))


# --- Colress's Experiment (LOR, Supporter) -------------------------------

async def colresss_experiment(ctx):
    """Look at the top 5 cards of your deck, put 3 into your hand, and put the
    other cards in the Lost Zone."""
    top = ctx.deck_top(5)
    if not top:
        return
    take = min(3, len(top))
    picks = await ctx.choose_cards(
        top, take, minimum=take, prompt="Choose 3 cards to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.move_to_lost_zone([c for c in top if c not in picks])


# --- Klara (CRE, Supporter) ----------------------------------------------

async def klara(ctx):
    """Choose 1 or both: up to 2 Pokemon and/or up to 2 basic Energy from your
    discard pile into your hand."""
    pokemon = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    picks_p = await ctx.choose_cards(
        pokemon, 2, minimum=0,
        prompt="Choose up to 2 Pokémon from your discard pile.",
    ) if pokemon else []
    picks_e = await ctx.choose_cards(
        energy, 2, minimum=0,
        prompt="Choose up to 2 basic Energy from your discard pile.",
    ) if energy else []
    await ctx.put_in_hand(picks_p + picks_e, reveal=False)


# --- Mirage Gate (LOR, Item) ---------------------------------------------

def mirage_gate_condition(board, player_id):
    """Usable only with 7 or more cards in the Lost Zone."""
    lost = board.find_player_area(player_id, "lostZone")
    return bool(lost) and len(lost.children) >= 7


async def mirage_gate(ctx):
    """Search your deck for up to 2 basic Energy of different types and attach
    them to your Pokemon in any way you like. Then, shuffle your deck."""
    deck_cards = list(ctx.deck(ctx.player_id))
    reps = []
    labels = {}
    seen_types = []
    for card in deck_cards:
        if not is_basic_energy_card(card):
            continue
        types = card.get_attribute(AttrID.POKEMON_TYPES) or []
        if not types or types[0] in seen_types:
            continue
        seen_types.append(types[0])
        reps.append(card)
        labels[card.entity_id] = f"{CLIENT_POKEMON_TYPE_NAMES[PokemonTypes(types[0])]} Energy"

    if not reps:
        await ctx.search_deck(
            is_basic_energy_card, count=2, minimum=0,
            prompt="Choose up to 2 basic Energy cards of different types.",
        )
        await ctx.shuffle_deck()
        return

    picks = await ctx.choose_cards(
        reps, 2, minimum=0,
        prompt="Choose up to 2 basic Energy cards of different types.",
        display_cards=deck_cards,
    )
    for energy in picks:
        label = labels[energy.entity_id]
        target = await ctx.choose_pokemon(
            ctx.my_pokemon_in_play(), f"Choose a Pokémon to attach {label} to"
        )
        if target is not None:
            await ctx.attach_energy(energy, target)
    await ctx.shuffle_deck()


# --- Scoop Up Net (RCL, Item) --------------------------------------------

async def scoop_up_net(ctx):
    """Put 1 of your Pokemon that isn't a Pokemon V or GX into your hand.
    Discard all attached cards."""
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if not is_v_or_gx(p.archetype_id)]
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your Pokémon to put into your hand"
    )
    if target is None:
        return
    was_active = target is ctx.my_active()
    await ctx.discard_cards([c for c in full_stack(target) if c is not target])
    await ctx.put_in_hand([target], reveal=False)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left"
                )
        ctx.deferred_actions.append(_promote)


# --- Switch Cart (ASR, Item) ---------------------------------------------

def switch_cart_condition(board, player_id):
    active = board.active_pokemon(player_id)
    return (
        active is not None
        and active.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
        and bool(_bench_pokemon(board, player_id))
    )


async def switch_cart(ctx):
    """Switch your Active Basic Pokemon with a Benched Pokemon; heal 30 from
    the Pokemon you moved to the Bench."""
    active = ctx.my_active()
    bench = ctx.my_bench()
    if active is None or not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is None:
        return
    await ctx.switch_active(ctx.player_id, target)
    await ctx.heal(30, active)


# --- Ordinary Rod (SSH, Item) --------------------------------------------

async def ordinary_rod(ctx):
    """Choose 1 or both: shuffle up to 2 Pokemon and/or up to 2 basic Energy
    from your discard pile into your deck."""
    pokemon = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    picks_p = await ctx.choose_cards(
        pokemon, 2, minimum=0,
        prompt="Choose up to 2 Pokémon to shuffle into your deck.",
    ) if pokemon else []
    picks_e = await ctx.choose_cards(
        energy, 2, minimum=0,
        prompt="Choose up to 2 basic Energy to shuffle into your deck.",
    ) if energy else []
    picks = picks_p + picks_e
    if picks:
        await ctx.shuffle_into_deck(picks)


# --- Energy Recycler (BST, Item) -----------------------------------------

async def energy_recycler(ctx):
    """Shuffle up to 5 basic Energy cards from your discard pile into your deck."""
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not energy:
        return
    picks = await ctx.choose_cards(
        energy, 5, minimum=1,
        prompt="Choose up to 5 basic Energy to shuffle into your deck.",
    )
    if picks:
        await ctx.shuffle_into_deck(picks)


# --- Trekking Shoes (ASR, Item) ------------------------------------------

async def trekking_shoes(ctx):
    """Look at the top card of your deck; you may put it into your hand,
    otherwise discard it and draw a card."""
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    idx = await ctx.present_card_choice(
        card, "Put this card into your hand?",
        ["Put into hand", "Discard and draw a card"],
    )
    if idx == 0:
        await ctx.put_in_hand([card], reveal=False)
    else:
        await ctx.discard_cards([card])
        await ctx.draw_cards(1)


# --- Hisuian Heavy Ball (ASR, Item) --------------------------------------

async def hisuian_heavy_ball(ctx):
    """Look at your Prize cards; you may reveal a Basic Pokemon there, put it
    into your hand, and put this card in its place as a face-down Prize. Then
    shuffle your face-down Prize cards. (No Basic revealed -> discard normally.)

    The prize-fan node keeps the client's peek-your-prizes click handler
    suppressed; the reveal browser did not, which crashed on prize clicks."""
    await ctx.look_at_prizes_take_basic()


# --- Peonia (CRE, Supporter) ----------------------------------------------

def peonia_playable(board, player_id) -> bool:
    prizes = board.find_player_area(player_id, "prizePile")
    return bool(prizes and prizes.children)


async def peonia(ctx):
    """Put up to 3 Prize cards into your hand. Then, for each Prize card put
    into your hand this way, put a card from your hand face down as a Prize."""
    taken = await ctx.take_prizes(3, minimum=1, check_win=False)
    if not taken:
        return
    picks = await ctx.choose_cards(
        list(ctx.hand()), len(taken), minimum=len(taken),
        prompt=f"Choose {len(taken)} card(s) to put face down as Prize cards",
    )
    await ctx.put_in_prizes(picks)


# --- Air Balloon (SSH, Pokemon Tool) -------------------------------------

class AirBalloonPassive(Passive):
    """The Retreat Cost of the holder is [C][C] less."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is pokemon:
            return cost - 2
        return cost


# --- Memory Capsule (SWSH4) ------------------------------------------------

class MemoryCapsulePassive(Passive):
    """The holder can use any attack from its tucked previous Evolutions
    (energy costs still apply)."""

    def granted_attacks(self, board, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return []
        attacks = []
        for child in pokemon.children:
            if not isinstance(child, PokemonEntity):
                continue
            for ability in getattr(def_for(child.archetype_id), "abilities", None) or []:
                if isinstance(ability, Attack):
                    attacks.append(ability)
        return attacks


# --- Training Court (RCL, Stadium) ---------------------------------------

def training_court_condition(board, player_id, stadium):
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(is_basic_energy_card(c) for c in discard.children)


async def training_court(ctx):
    """Put a basic Energy card from your discard pile into your hand."""
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not energy:
        return
    picks = await ctx.choose_cards(
        energy, 1, minimum=1,
        prompt="Choose a basic Energy card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)


# --- Thorton (SWSH11) -------------------------------------------------------

def _basic_pokemon_in_play(board, player_id):
    """In-play Basics; fossils count (Basic Pokemon in play, Trainer CARD_TYPE)."""
    return [
        p for p in board.pokemon_in_play(player_id)
        if isinstance(p, PokemonEntity)
        and p.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
    ]


def thorton_condition(board, player_id):
    if not any(is_basic_pokemon(c) for c in _discard(board, player_id)):
        return False
    return bool(_basic_pokemon_in_play(board, player_id))


async def thorton(ctx):
    """Choose a Basic Pokemon in your discard pile and switch it with 1 of
    your Basic Pokemon in play; everything remains on the new Pokemon."""
    candidates = [c for c in ctx.discard_pile() if is_basic_pokemon(c)]
    in_play = _basic_pokemon_in_play(ctx.board, ctx.player_id)
    if not candidates or not in_play:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Choose a Basic Pokémon from your discard pile",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(
        in_play, "Choose 1 of your Basic Pokémon in play to switch it with")
    if target is not None:
        await ctx.identity_swap(target, picks[0], destination="discard")


TRAINING_COURT_ABILITY = Ability(
    title="Training Court",
    game_text="Once during each player's turn, that player may put a basic Energy card from their discard pile into their hand.",
    activation=Activations.ONCE_PER_TURN,
    effect=training_court,
    condition=training_court_condition,
)


# --- Fossils (Unidentified Fossil / Rare Fossil) ---------------------------

class FossilBodyPassive(Passive):
    """Fossil rules text: this card can't retreat; Rare Fossil additionally
    can't be affected by Special Conditions."""

    def __init__(self, blocks_conditions: bool = False):
        self.condition_immune = blocks_conditions

    def blocks_retreat(self, pokemon, carrier):
        return pokemon is carrier

    def blocks_special_conditions(self, target, condition, carrier):
        return self.condition_immune and target is carrier


async def fossil_discard(ctx):
    """Discard this fossil from play; attached cards go to the discard too."""
    fossil = ctx.source
    was_active = fossil is ctx.my_active()
    discard = ctx.board.find_player_area(ctx.player_id, "discard")
    if discard is not None and discard.entity_id not in ctx.visual_targets:
        ctx.visual_targets.append(discard.entity_id)
    await ctx.discard_cards([c for c in full_stack(fossil) if c is not fossil])
    await ctx.discard_cards([fossil])
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left"
                )
        ctx.deferred_actions.append(_promote)


def fossil_discard_ability() -> Ability:
    """"At any time during your turn, you may discard this card from play."
    Fresh instance per print: ability_id derives from the owning card GUID."""
    return Ability(
        "Discard",
        "At any time during your turn, you may discard this card from play.",
        activation=Activations.ONCE_PER_TURN,
        effect=fossil_discard,
    )


def is_rare_fossil(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == "Rare Fossil"


def bench_has_room(board, player_id):
    bench = board.find_player_area(player_id, "bench")
    return bench is not None \
        and len(bench.children) < effective_bench_capacity(board, player_id)


# --- Brandon (SWSH12) -------------------------------------------------------

def brandon_playable(board, player_id) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and len(hand.children) == 1


async def brandon(ctx):
    """Draw a card for each Benched Pokemon (both yours and your opponent's)."""
    count = len(_bench_pokemon(ctx.board, ctx.player_id)) \
        + len(_bench_pokemon(ctx.board, ctx.opponent_id))
    if count > 0:
        await ctx.draw_cards(count)


# --- Candice (SWSH12) --------------------------------------------------------

def is_water_energy_card(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.WATER.value in types


def candice_predicate(card) -> bool:
    return is_water_pokemon(card) or is_water_energy_card(card)


# --- Capturing Aroma (SWSH12) ------------------------------------------------

async def capturing_aroma(ctx):
    """Flip a coin: heads searches for an Evolution Pokemon, tails a Basic
    Pokemon; reveal it and put it into your hand. Then, shuffle your deck."""
    heads, = await ctx.flip_coins(1, "Capturing Aroma")
    predicate = is_evolution_pokemon if heads else is_basic_pokemon
    prompt = "Choose an Evolution Pokémon to put into your hand." if heads \
        else "Choose a Basic Pokémon to put into your hand."
    picks = await ctx.search_deck(predicate, count=1, minimum=0, prompt=prompt)
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


# --- Earthen Seal Stone (SWSH12) ---------------------------------------------

async def star_gravity(ctx):
    """Put damage counters on each of the opponent's Pokemon V until its
    remaining HP is 100 (VSTAR Power)."""
    for pokemon in ctx.opponent_pokemon_in_play():
        if not is_pokemon_v(pokemon.archetype_id):
            continue
        current = pokemon.get_attribute(AttrID.HP, ctx.max_hp(pokemon))
        if current > 100:
            await ctx.deal_damage(current - 100, target=pokemon,
                                  apply_modifiers=False, as_counters=True)


# --- Emergency Jelly (SWSH12) -------------------------------------------------

async def emergency_jelly(ctx):
    """End of each turn: if the holder has 30 HP or less remaining and any
    damage counters on it, heal 120 damage from it and discard this card."""
    pokemon = ctx.source
    hp = pokemon.get_attribute(AttrID.HP, 0)
    max_hp = ctx.max_hp(pokemon)
    if hp <= 30 and hp < max_hp:
        await ctx.heal(120, target=pokemon)
        tool = next((t for t, p in ctx.tools_in_play() if p is pokemon), None)
        if tool is not None:
            await ctx.discard_cards([tool])


# --- Furisode Girl (SWSH12) ---------------------------------------------------

async def furisode_girl(ctx):
    """Search the deck for a Basic Pokemon and put it onto the Bench; then
    shuffle. You may switch that Pokemon with your Active Pokemon."""
    picks = await ctx.search_deck(
        is_basic_pokemon, count=1, minimum=0,
        prompt="Choose a Basic Pokémon to put onto your Bench.",
    )
    if not picks:
        await ctx.shuffle_deck()
        return
    target = picks[0]
    await ctx.bench_pokemon(target)
    await ctx.shuffle_deck()
    if await ctx.ask_yes_no("Switch that Pokémon with your Active Pokémon?"):
        await ctx.switch_active(ctx.player_id, target)


# --- Lance (SWSH12) -----------------------------------------------------------

def is_dragon_pokemon(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.DRAGON.value in types


async def lance(ctx):
    """Search the deck for up to 3 Dragon Pokemon, reveal them, and put them
    into your hand. Then, shuffle your deck."""
    picks = await ctx.search_deck(
        is_dragon_pokemon, count=3, minimum=0,
        prompt="Choose up to 3 Dragon Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


# --- Leafy Camo Poncho (SWSH12) -----------------------------------------------

def leafy_camo_poncho_protects(affected_entity, carrier):
    holder = carrier_pokemon(carrier)
    return holder is not None and affected_entity is holder


def leafy_camo_poncho_condition(board, carrier):
    holder = carrier_pokemon(carrier)
    if holder is None:
        return False
    subs = subtypes_for(holder.archetype_id)
    return "VSTAR" in subs or "VMAX" in subs


# --- Primordial Altar (SWSH12) ------------------------------------------------

def primordial_altar_condition(board, player_id, stadium):
    return deck_nonempty(board, player_id)


async def primordial_altar(ctx):
    """Once during each player's turn: look at the top card of the deck and
    may discard it."""
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    idx = await ctx.present_card_choice(
        card, "Discard the top card of your deck?",
        ["Discard", "Keep it on top"],
    )
    if idx == 0:
        await ctx.discard_cards([card])


PRIMORDIAL_ALTAR_ABILITY = Ability(
    title="Primordial Altar",
    game_text="Once during each player's turn, that player may look at the top card of their deck. They may discard that card.",
    activation=Activations.ONCE_PER_TURN,
    effect=primordial_altar,
    condition=primordial_altar_condition,
)


# --- Professor Laventon (SWSH12) ----------------------------------------------

def _is_hisuian_pokemon(card) -> bool:
    if not is_pokemon_card(card):
        return False
    name = getattr(def_for(card.archetype_id), "display_name", "") or ""
    return "Hisuian" in name


def professor_laventon_playable(board, player_id) -> bool:
    return any(_is_hisuian_pokemon(c) for c in _discard(board, player_id))


async def professor_laventon(ctx):
    """Put up to 3 Pokemon that have "Hisuian" in their names from the
    discard pile into your hand."""
    candidates = [c for c in ctx.discard_pile() if _is_hisuian_pokemon(c)]
    picks = await ctx.choose_cards(
        candidates, 3, minimum=0,
        prompt="Choose up to 3 Hisuian Pokémon from your discard pile.",
    )
    await ctx.put_in_hand(picks, reveal=False)


# --- Quad Stone (SWSH12) -------------------------------------------------------

async def quad_stone(ctx):
    """Use 1: heal 10 from your Active. Use 4 at once (this + 3 more from
    hand): heal all damage from each of your Pokemon."""
    others = [c for c in ctx.hand()
              if c is not ctx.source and c.archetype_id == ctx.source.archetype_id]
    use_four = False
    if len(others) >= 3 and await ctx.ask_yes_no(
        "Use 3 more Quad Stone cards from your hand to heal all damage from "
        "each of your Pokémon instead of healing 10 from your Active Pokémon?"
    ):
        picks = await ctx.choose_cards(
            others, 3, minimum=3, prompt="Choose 3 more Quad Stone cards to use",
        )
        if len(picks) >= 3:
            await ctx.discard_cards(picks)
            for pokemon in ctx.my_pokemon_in_play():
                await ctx.heal(9999, pokemon)
            use_four = True
    if not use_four:
        active = ctx.my_active()
        if active is not None:
            await ctx.heal(10, active)


# --- Wallace (SWSH12) ----------------------------------------------------------

async def wallace(ctx):
    """Draw 3 cards. Your opponent may draw a card; if they do, draw 1 more."""
    await ctx.draw_cards(3)
    if await ctx.ask_yes_no("Draw a card?", player_id=ctx.opponent_id):
        await ctx.draw_cards(1, ctx.opponent_id)
        await ctx.draw_cards(1)


def fossil_search(fossil_predicate, count: int = 2,
                  label: str = "Rare Fossil"):
    """Search your deck for up to `count` matching fossil cards and put them
    onto your Bench; then shuffle (Relicanth's Fossil Search, Cara Liss)."""
    async def effect(ctx):
        bench = ctx.board.find_player_area(ctx.player_id, "bench")
        space = effective_bench_capacity(ctx.board, ctx.player_id) \
            - len(bench.children) if bench else 0
        if space <= 0:
            return
        picks = await ctx.search_deck(
            fossil_predicate, count=min(count, space), minimum=0,
            prompt=f"Choose up to {min(count, space)} {label} cards to put "
                   f"onto your Bench.",
        )
        for card in picks:
            await ctx.bench_pokemon(card)
        await ctx.shuffle_deck()
    return effect


# ======================================================================
# Parametric effects
# ----------------------------------------------------------------------
# One factory per recurring printed-text shape. A card script keeps its own
# data and wires `effect=<factory>(...)` instead of carrying a copy of the
# logic, so a wording that appears in twenty sets is implemented once.
# tools/trainer_coverage.py is the audit that decides what belongs here.
# ======================================================================

def is_stadium_card(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value


def is_tool_card(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def is_stage_one(card) -> bool:
    return is_evolution_pokemon(card) \
        and card.get_attribute(AttrID.STAGE) == PokemonStage.STAGE1.value


def is_stage_two(card) -> bool:
    return is_evolution_pokemon(card) \
        and card.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value


def is_pokemon_ex(card) -> bool:
    return is_pokemon_card(card) and "ex" in " ".join(subtypes_for(card.archetype_id))


def is_rule_box_pokemon(card) -> bool:
    return is_pokemon_card(card) and has_rule_box(card.archetype_id)


POKEMON_TYPE_NAMES = {
    name.lower(): member.value for name, member in PokemonTypes.__members__.items()
    if name not in ("NO_COLOR", "STRONG", "HERBAL", "UNSET")
}


def pokemon_of(type_name: str):
    """Predicate: a Pokemon of the named type ("water", "psychic", ...)."""
    value = POKEMON_TYPE_NAMES[type_name.lower()]

    def predicate(card):
        return is_pokemon_card(card) \
            and value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])
    return predicate


def basic_energy_of(type_name: str):
    """Predicate: a Basic Energy card of the named type."""
    value = POKEMON_TYPE_NAMES[type_name.lower()]

    def predicate(card):
        return is_basic_energy_card(card) \
            and value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])
    return predicate


def is_rule_box_free_pokemon(card) -> bool:
    return (is_pokemon_card(card) and not has_rule_box(card.archetype_id)
            and "ex" not in subtypes_for(card.archetype_id))


def is_basic_pokemon_with_hp_at_most(limit: int):
    """Deck-search filter: Basic Pokemon with printed HP <= limit."""
    def predicate(card):
        return is_basic_pokemon(card) and card.get_attribute(AttrID.HP, 0) <= limit
    return predicate


# --- Draw ------------------------------------------------------------------

def draw_n(n: int):
    """Draw `n` cards."""
    async def effect(ctx):
        await ctx.draw_cards(n)
    return effect


def discard_hand_draw(n: int):
    """Discard your whole hand, then draw `n` (Professor's Research shape)."""
    async def effect(ctx):
        await ctx.discard_cards(ctx.hand())
        await ctx.draw_cards(n)
    return effect


def shuffle_hand_draw(n: int, opponent_prizes_low=None):
    """Shuffle your hand into your deck, then draw `n`. With
    opponent_prizes_low=(threshold, n_low) the draw becomes `n_low` once the
    opponent has that many Prize cards or fewer remaining."""
    async def effect(ctx):
        await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
        count = n
        if opponent_prizes_low is not None:
            opponent = next((p for p in ctx.board.player_ids
                             if p != ctx.player_id), None)
            area = ctx.board.find_player_area(opponent, "prizePile") if opponent else None
            if area is not None and len(area.children) <= opponent_prizes_low[0]:
                count = opponent_prizes_low[1]
        await ctx.draw_cards(count)
    return effect


def each_player_shuffle_draw(n: int):
    """Both players shuffle their hand into their deck and draw `n` (Judge)."""
    async def effect(ctx):
        await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
        await ctx.draw_cards(n)
        await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
        await ctx.draw_cards(n, ctx.opponent_id)
    return effect


# --- Discard from the opponent's side ---------------------------------------

def discard_energy_opponent(count: int = 1, flip: bool = False,
                            scope: str = "any", energy_pred=None):
    """Discard up to `count` Energy from the opponent's Pokemon; `scope` is
    'any' (choose the holder) or 'active'. flip=True pays a coin first
    ("Flip a coin. If heads, discard an Energy...")."""
    async def effect(ctx):
        if flip and not (await ctx.flip_coins(1, title="Discard an Energy"))[0]:
            return
        if scope == "active":
            pool = [ctx.opponent_active()]
        else:
            pool = ctx.opponent_pokemon_in_play()
        eligible = [p for p in pool if p is not None
                    and ctx.attached_energies(p)
                    and any(energy_pred is None or energy_pred(e)
                            for e in ctx.attached_energies(p))]
        if not eligible:
            return
        if len(eligible) == 1:
            holder = eligible[0]
        else:
            holder = await ctx.choose_pokemon(
                eligible, "Choose a Pokémon to discard an Energy from") or eligible[0]
        if holder is not None:
            await ctx.discard_energy_from(
                holder, count, predicate=energy_pred,
                prompt="Choose an Energy to discard")
    return effect


def discard_energy_each_opponent(predicate=None):
    """Discard one matching Energy from every one of the opponent's Pokemon
    that has one (Crushing Hammer's "each of your opponent's Pokemon"
    shape; Maiden's... 'Discard a Special Energy from each')."""
    async def effect(ctx):
        for pokemon in ctx.opponent_pokemon_in_play():
            energies = [e for e in ctx.attached_energies(pokemon)
                        if predicate is None or predicate(e)]
            if energies:
                await ctx.discard_energy_from(pokemon, 1, predicate=predicate)
    return effect


# --- Gusting ---------------------------------------------------------------

def opponent_bench_to_active(flip: bool = False, opponent_chooses: bool = False):
    """Switch one of the opponent's Benched Pokemon into the Active Spot
    ('Switch in 1 of your opponent's Benched Pokemon'). flip pays a coin
    first (Pokemon Catcher); opponent_chooses lets them pick (Escape Rope
    wording)."""
    async def effect(ctx):
        if flip and not (await ctx.flip_coins(1, title="Switch in a Benched Pokémon"))[0]:
            return
        active = ctx.opponent_active()
        bench = ctx.opponent_bench()
        if active is None or not bench or ctx.effects_blocked(active):
            return
        if opponent_chooses:
            target = await ctx.choose_pokemon(
                bench, "Choose your new Active Pokémon", player_id=ctx.opponent_id
            ) or bench[0]
        else:
            target = await ctx.choose_pokemon(
                bench, "Choose the opponent's new Active Pokémon") or bench[0]
        await ctx.switch_active(ctx.opponent_id, target)
    return effect


# --- Crooked deck searches -------------------------------------------------

def search_two_kinds(first, first_count: int, second, second_count: int):
    """Search the deck for up to `first_count` matches of `first` and
    `second_count` of `second`, reveal them, put them into hand, shuffle
    (Arven: an Item card and a Pokemon Tool card)."""
    async def effect(ctx):
        picks = []
        for predicate, count in ((first, first_count), (second, second_count)):
            found = [c for c in ctx.deck() if predicate(c)]
            if not found:
                continue
            picks.extend(await ctx.search_deck(
                predicate, count=count, minimum=0,
                prompt="Choose a card to put into your hand.",
            ))
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


# --- Energy movement -------------------------------------------------------

def move_basic_energy(predicate=None, count: int = 1):
    """Move `count` Energy from one of your Pokemon to another (Energy
    Switch). The player picks the source, then the Energy, then the target."""
    async def effect(ctx):
        fitted = [p for p in ctx.my_pokemon_in_play() if ctx.attached_energies(p)]
        if not fitted:
            return
        source = await ctx.choose_pokemon(
            fitted, "Choose a Pokémon to move an Energy from") if len(fitted) > 1 \
            else fitted[0]
        if source is None:
            return
        energies = [e for e in ctx.attached_energies(source)
                    if predicate is None or predicate(e)]
        if not energies:
            return
        take = min(count, len(energies))
        picked = await ctx.choose_cards(
            energies, take, minimum=1,
            prompt="Choose Energy to move") if len(energies) > 1 else energies[:take]
        if not picked:
            return
        targets = [p for p in ctx.my_pokemon_in_play() if p is not source]
        if not targets:
            return
        target = await ctx.choose_pokemon(
            targets, "Choose a Pokémon to move the Energy to") or targets[0]
        if target is None:
            return
        for card in picked:
            await ctx.move_energy(card, target)
    return effect


# --- Evolution shortcuts ---------------------------------------------------

def rare_candy():
    """Evolve a Basic in play straight into a Stage 2 from hand, skipping
    Stage 1 (not on your first turn; the script's `condition` covers that
    half of the printed restriction)."""
    async def effect(ctx):
        basics = [p for p in ctx.my_pokemon_in_play()
                  if p.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value]
        stages = [c for c in ctx.hand() if is_stage_two(c)]
        if not basics or not stages:
            return
        pairs = []
        for basic in basics:
            logic_name = basic.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
            if not logic_name:
                continue
            for card in stages:
                if evolves_from(card.archetype_id, logic_name):
                    pairs.append((basic, card))
        if not pairs:
            return
        picked = await ctx.choose(
            "Choose the Pokémon to evolve",
            [f"{def_for(card.archetype_id).display_name} on "
             f"{def_for(basic.archetype_id).display_name}"
             for basic, card in pairs],
        )
        if picked is None or not 0 <= picked < len(pairs):
            return
        basic, card = pairs[picked]
        await ctx.evolve_pokemon(basic, card)
    return effect


def opponent_shuffle_hand_draw(n: int):
    """The opponent shuffles their hand into their deck and draws `n`
    (Marnie's opponent half, Team Rocket's Admin shape)."""
    async def effect(ctx):
        await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
        await ctx.draw_cards(n, ctx.opponent_id)
    return effect


def discard_hand_n(n: int, minimum=None):
    """Discard `n` cards from your hand ("Discard 2 cards from your hand").
    minimum defaults to the full `n`: the printed text is a cost, so the pick
    is not optional."""
    async def effect(ctx):
        await ctx.discard_from_hand(
            n, minimum=n if minimum is None else minimum,
            prompt=f"Discard {n} card(s) from your hand",
        )
    return effect


def recover_then_draw(predicate=None, count: int = 1, draw: int = 3):
    """Shuffle up to `count` matching discard-pile cards back into the deck,
    then draw `draw` if any went in (Miriam)."""
    async def effect(ctx):
        cards = [c for c in ctx.discard_pile()
                 if predicate is None or predicate(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, count, minimum=0,
            prompt="Choose cards from your discard pile to shuffle into your deck",
        )
        if not picks:
            return
        await ctx.shuffle_into_deck(picks)
        await ctx.draw_cards(draw)
    return effect


def switch_then_draw_until(hand_size: int):
    """Switch your Active with a Benched Pokemon, then draw until the hand
    holds `hand_size` cards."""
    async def effect(ctx):
        bench = ctx.my_bench()
        if bench:
            target = await ctx.choose_play_target(bench, "Choose your new Active Pokémon")
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)
        await ctx.draw_until(hand_size)
    return effect


def discard_stadium_card():
    """Discard the Stadium in play (if any)."""
    async def effect(ctx):
        await ctx.discard_stadium()
    return effect


# --- Effect combinators ----------------------------------------------------
# A printing may put a requirement or a coin flip in front of an effect that
# is otherwise a shape the library already knows; these wrap the inner one.

def if_heads(inner):
    """Run `inner` only when a coin flip comes up heads."""
    async def effect(ctx):
        if (await ctx.flip_coins(1, title="Flip a coin"))[0]:
            await inner(ctx)
    return effect


def with_discard_cost(n: int, inner):
    """Discard `n` other cards from your hand as the card's cost, then run
    `inner` (declines when the hand cannot pay)."""
    async def effect(ctx):
        discarded = await ctx.discard_from_hand(
            n, minimum=n, prompt=f"Discard {n} card(s) from your hand",
        )
        if len(discarded) < n:
            return
        await inner(ctx)
    return effect


def return_pokemon_to_hand(predicate=None, with_attachments="same", flip: bool = False):
    """Put 1 of your Pokemon in play into your hand. with_attachments "same"
    takes the whole stack ("and all cards attached to it"), "discard" leaves
    the attachments behind in the discard pile. flip pays a coin first
    (Super Scoop Up)."""
    async def effect(ctx):
        if flip and not (await ctx.flip_coins(1, title="Return a Pokémon to your hand"))[0]:
            return
        candidates = [p for p in ctx.my_pokemon_in_play()
                      if predicate is None or predicate(p)]
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon to put into your hand") \
            if len(candidates) > 1 else candidates[0]
        if target is None:
            return
        if with_attachments == "discard":
            await ctx.discard_cards([c for c in full_stack(target) if c is not target])
            await ctx.put_in_hand([target], reveal=False)
        else:
            await ctx.put_in_hand(full_stack(target), reveal=False)
    return effect


def each_player_shuffle_draw_per_prize(bottom: bool = False):
    """Each player shuffles their hand into (or under) their deck, then draws
    1 card for each of their remaining Prize cards."""
    async def effect(ctx):
        for player_id in ctx.board.player_ids:
            if bottom:
                await ctx.hand_to_bottom_of_deck(player_id)
            else:
                await ctx.shuffle_into_deck(ctx.hand(player_id), player_id)
        for player_id in ctx.board.player_ids:
            area = ctx.board.find_player_area(player_id, "prizePile")
            count = len(area.children) if area else 0
            if count:
                await ctx.draw_cards(count, player_id)
    return effect


def first_turn_draw_until(hand_size: int, first_turn_size: int):
    """Draw until the hand holds `hand_size` cards, or `first_turn_size` when
    this is your first turn (Lillie)."""
    async def effect(ctx):
        turn_state = getattr(ctx.board, "turn_state", None)
        first_turn = turn_state is not None and turn_state.turn_number <= 2
        await ctx.draw_until(first_turn_size if first_turn else hand_size)
    return effect


def any_of(*predicates):
    """Predicate matching a card that satisfies any of `predicates`
    ("a Pokémon or a Basic Energy card")."""
    def predicate(card):
        return any(p(card) for p in predicates)
    return predicate


def all_of(*predicates):
    """Predicate matching a card that satisfies every one of `predicates`."""
    def predicate(card):
        return all(p(card) for p in predicates)
    return predicate


def search_to_top(n: int, predicate=None):
    """Search the deck for up to `n` cards and put them back on top in any
    order, then shuffle (the search half resolves like any other search)."""
    async def effect(ctx):
        picks = await ctx.search_deck(
            predicate, count=n, minimum=0,
            prompt="Choose cards to put back on top of your deck.",
        )
        await ctx.shuffle_deck()
        for card in reversed(picks):
            await ctx.put_on_top_of_deck(card)
    return effect


async def _evolve_in_play(ctx, evolution_cards):
    """Offer every (Basic in play, matching evolution in hand) pair and evolve
    the one the player picks. Shared by the Rare Candy / Evosoda shapes."""
    pairs = []
    for basic in ctx.my_pokemon_in_play():
        if basic.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value:
            continue
        logic_name = basic.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        if not logic_name:
            continue
        for card in evolution_cards:
            if evolves_from(card.archetype_id, logic_name):
                pairs.append((basic, card))
    if not pairs:
        return False
    if len(pairs) == 1:
        basic, card = pairs[0]
    else:
        picked = await ctx.choose(
            "Choose the Pokémon to evolve",
            [f"{def_for(card.archetype_id).display_name} on "
             f"{def_for(basic.archetype_id).display_name}"
             for basic, card in pairs],
        )
        if picked is None or not 0 <= picked < len(pairs):
            return False
        basic, card = pairs[picked]
    return await ctx.evolve_pokemon(basic, card)


def evolve_from_hand():
    """Choose 1 of your Basic Pokemon in play and put a card from your hand
    that evolves from it onto it (Evosoda shape); counts as evolving."""
    async def effect(ctx):
        await _evolve_in_play(ctx, [c for c in ctx.hand() if is_evolution_pokemon(c)])
    return effect


def turn_damage_boost(amount: int, pokemon_type=None, exclude_rule_box: bool = False):
    """During this turn, attacks used by your Pokemon do `amount` more damage
    to the opponent's Active Pokemon (before Weakness and Resistance).
    pokemon_type narrows the boost to one type; exclude_rule_box skips
    Rule Box Pokemon."""
    async def effect(ctx):
        def qualifies(entity):
            if exclude_rule_box and has_rule_box(entity.archetype_id):
                return False
            if pokemon_type is not None:
                types = entity.get_attribute(AttrID.POKEMON_TYPES) or []
                if POKEMON_TYPE_NAMES[pokemon_type] not in types:
                    return False
            return True

        ctx.add_turn_damage_modifier(TurnDamageModifier(
            amount, ctx.player_id, source_predicate=qualifies))
        for pokemon in ctx.my_pokemon_in_play():
            if qualifies(pokemon):
                await ctx.add_stat_visualization(
                    pokemon, VisualizationArrow.POSITIVE,
                    VisualizationType.DAMAGE_DEALT_INCREASED,
                    card_text=f"+{amount} damage",
                )
    return effect


# ======================================================================
# Tool and Stadium stat passives
# ----------------------------------------------------------------------
# Thin wrappers over the factories in passives_common so a tool or stadium
# script can be wired from its printed text (`passive=...`) the same way a
# trainer is wired from its effect text.
# ======================================================================

def holder_damage_boost(amount: int, target_pred=None, to_active_only: bool = True):
    """The attacks of the Pokemon this card is attached to do `amount` more
    damage to the opponent's Active (or to targets matching `target_pred`)."""
    return typed_damage_boost_tool(target_pred or (lambda target: True),
                                   amount, to_active_only)


def holder_hp_bonus(amount: int):
    """The Pokemon this card is attached to gets +`amount` max HP."""
    return hp_bonus_tool(amount)


def holder_retreat_discount(count: int):
    """The Retreat Cost of the Pokemon this card is attached to is `count`
    Colorless less."""
    return retreat_discount(count)


def holder_no_weakness(protect_type=None):
    """The Pokemon this card is attached to has no Weakness; protect_type
    restricts it to one typed holder."""
    if protect_type is None:
        return no_weakness_passive()
    holder_pred = pokemon_of(protect_type)
    return no_weakness_passive(
        protects=lambda target, carrier: carrier_pokemon(carrier) is target
        and holder_pred(target))


def holder_takes_less(amount: int, protect_type=None):
    """The Pokemon this card is attached to takes `amount` less damage from
    the opponent's attacks. protect_type restricts it to one typed holder."""
    if protect_type is None:
        return takes_less_passive(amount)
    holder_pred = pokemon_of(protect_type)
    return takes_less_passive(
        amount, protects=lambda target, carrier: carrier_pokemon(carrier) is target
        and holder_pred(target))


def stadium_retreat_discount(count: int, basic_only: bool = False):
    """Every (Basic) Pokemon in play has a Retreat Cost `count` Colorless less."""
    if basic_only:
        return retreat_discount(
            count, target_pred=lambda target, carrier: is_basic_pokemon(target))
    return retreat_discount(count, target_pred=lambda target, carrier: True)


def stadium_takes_less(amount: int, protect_type=None):
    """Pokemon (both sides) take `amount` less damage from opposing attacks,
    optionally only Pokemon of one type."""
    if protect_type is None:
        return takes_less_passive(
            amount, protects=lambda target, carrier: True)
    type_pred = pokemon_of(protect_type)
    return takes_less_passive(
        amount, protects=lambda target, carrier: type_pred(target))


class ToolsSuppressedStadiumPassive(Passive):
    """Pokemon Tools attached to each Pokemon (both sides) have no effect."""

    def suppresses_tool(self, tool, carrier):
        return True


class AllAbilitiesOffPassive(Passive):
    """Each Pokemon in play (both sides) has no Abilities."""

    def blocks_abilities(self, pokemon, carrier):
        return True


class CombinedPassive(Passive):
    """Two continuous effects printed on one card ("... takes 30 less damage
    and has no Weakness"), each hook forwarded to every part."""

    def __init__(self, *parts):
        self.parts = parts

    def modify_damage_dealt(self, calc, carrier):
        for part in self.parts:
            part.modify_damage_dealt(calc, carrier)

    def modify_weakness(self, calc, carrier):
        for part in self.parts:
            part.modify_weakness(calc, carrier)

    def modify_resistance(self, calc, carrier):
        for part in self.parts:
            part.modify_resistance(calc, carrier)

    def modify_damage_taken(self, calc, carrier):
        for part in self.parts:
            part.modify_damage_taken(calc, carrier)

    def max_hp_bonus(self, pokemon, carrier):
        return sum(part.max_hp_bonus(pokemon, carrier) for part in self.parts)

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        for part in self.parts:
            cost = part.modify_retreat_cost(cost, pokemon, carrier, board)
        return cost

    def suppresses_tool(self, tool, carrier):
        return any(part.suppresses_tool(tool, carrier) for part in self.parts)

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        for part in self.parts:
            count = part.modify_prizes_for_knockout(pokemon, ctx, count, carrier)
        return count


def combined(*parts):
    """One passive from several (a tool that both reduces damage and removes
    Weakness)."""
    return CombinedPassive(*parts)


# --- Composed shapes -------------------------------------------------------

def draw_n_prize_bonus(base: int, bonus: int, threshold: int):
    """Draw `base` cards; draw `bonus` more once the opponent holds
    `threshold` Prize cards or fewer."""
    async def effect(ctx):
        await ctx.draw_cards(base)
        area = ctx.board.find_player_area(ctx.opponent_id, "prizePile")
        if area is not None and len(area.children) <= threshold:
            await ctx.draw_cards(bonus)
    return effect


def shuffle_one_hand_draw(n: int):
    """Shuffle 1 card from your hand into your deck, then draw `n`; declines
    an empty hand ("If you have any cards in your hand...")."""
    async def effect(ctx):
        hand = ctx.hand()
        if not hand:
            return
        picks = await ctx.choose_cards(
            hand, 1, minimum=1,
            prompt="Choose a card from your hand to shuffle into your deck")
        if not picks:
            return
        await ctx.shuffle_into_deck(picks)
        await ctx.draw_cards(n)
    return effect


def flip_recover_basic_energy(maximum: int):
    """Flip a coin per card and put a Basic Energy from the discard pile into
    your hand for each heads (up to `maximum`)."""
    async def effect(ctx):
        heads = sum(1 for result in
                    await ctx.flip_coins(maximum, title="Recover Energy")
                    if result)
        cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        take = min(heads, len(cards))
        if take <= 0:
            return
        picks = await ctx.choose_cards(
            cards, take, minimum=take,
            prompt="Choose Basic Energy cards to put into your hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    return effect


def recover_basic_to_bench(count: int = 1):
    """Put Basic Pokemon from your discard pile onto your Bench."""
    async def effect(ctx):
        cards = [c for c in ctx.discard_pile() if is_basic_pokemon(c)]
        space = BENCH_CAPACITY - len(ctx.my_bench())
        take = min(count, len(cards), max(0, space))
        if take <= 0:
            return
        picks = await ctx.choose_cards(
            cards, take, minimum=0,
            prompt="Choose a Basic Pokémon to put onto your Bench")
        for card in picks:
            await ctx.bench_pokemon(card)
    return effect


def reveal_until_supporter():
    """Reveal cards from the top of your deck until a Supporter appears, put
    it into your hand, and shuffle the rest back in."""
    async def effect(ctx):
        revealed = []
        found = None
        for card in ctx.deck_top(len(ctx.deck())):
            revealed.append(card)
            if is_supporter_card(card):
                found = card
                break
        if revealed:
            await ctx.reveal_cards(revealed)
        if found is not None:
            await ctx.put_in_hand([found], reveal=False)
        await ctx.shuffle_deck()
    return effect


def devolve_one(count: int = 1):
    """Devolve `count` of your evolved Pokemon once each, putting the removed
    evolution card into your hand."""
    async def effect(ctx):
        evolved = [p for p in ctx.my_pokemon_in_play()
                   if is_evolution_pokemon(p)]
        if not evolved:
            return
        target = await ctx.choose_pokemon(
            evolved, "Choose an evolved Pokémon to devolve") \
            if len(evolved) > 1 else evolved[0]
        if target is None:
            return
        await ctx.devolve_pokemon(target, steps=count, destination="hand")
    return effect


def named(*words):
    """Predicate: a card whose printed name contains every one of `words`
    ("Team Rocket's Pokemon", "Ethan's Adventure")."""
    wanted = [word.lower() for word in words]

    def predicate(card):
        definition = def_for(card.archetype_id)
        name = (getattr(definition, "display_name", "") or "").lower()
        return all(word in name for word in wanted)
    return predicate


def excluding(predicate):
    """Predicate: matches what `predicate` rejects ("Basic Pokemon excluding
    Pokemon ex")."""
    def check(card):
        return not predicate(card)
    return check


def draw_then_discard(draw: int, discard: int):
    """Draw `draw` cards, then discard `discard` cards from your hand."""
    async def effect(ctx):
        await ctx.draw_cards(draw)
        await ctx.discard_from_hand(
            discard, minimum=discard,
            prompt=f"Discard {discard} card(s) from your hand")
    return effect


def draw_until_unless(hand_size: int, other_size: int, predicate):
    """Draw until the hand holds `hand_size`, or `other_size` instead while
    every one of your Pokemon in play matches `predicate` (Team Rocket's
    Ariana)."""
    async def effect(ctx):
        in_play = ctx.my_pokemon_in_play()
        matches = bool(in_play) and all(predicate(p) for p in in_play)
        await ctx.draw_until(other_size if matches else hand_size)
    return effect


def heal_all_own_discard_energy():
    """Remove all damage from each of your damaged Pokemon, then discard the
    Energy attached to each one healed that way."""
    async def effect(ctx):
        for pokemon in list(ctx.my_pokemon_in_play()):
            damage = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
            if damage <= 0:
                continue
            await ctx.heal(damage, pokemon)
            await ctx.discard_energy_from(
                pokemon, len(ctx.attached_energies(pokemon)),
                prompt="Discard the Energy attached to that Pokémon")
    return effect


def discard_tools(count: int = 1, sides: str = "any"):
    """Discard up to `count` Pokemon Tools attached to Pokemon in play."""
    async def effect(ctx):
        tools = [card for card, holder in ctx.tools_in_play()
                 if sides == "any"
                 or (sides == "mine" and card.owning_player_id == ctx.player_id)
                 or (sides == "theirs" and card.owning_player_id != ctx.player_id)]
        if not tools:
            return
        picks = await ctx.choose_cards(
            tools, count, minimum=0,
            prompt="Choose Pokémon Tools to discard")
        if picks:
            await ctx.discard_cards(picks)
    return effect


def trade_to_hand(predicate=None, count: int = 1):
    """Put a card from your hand on the bottom of your deck to take up to
    `count` matching cards from your discard pile into your hand."""
    async def effect(ctx):
        hand = ctx.hand()
        if not hand:
            return
        picks = await ctx.choose_cards(
            hand, 1, minimum=1, prompt="Choose a card from your hand to shuffle in")
        if not picks:
            return
        await ctx.shuffle_into_deck(picks)
        cards = [c for c in ctx.discard_pile()
                 if predicate is None or predicate(c)]
        if not cards:
            return
        taken = await ctx.choose_cards(
            cards, count, minimum=0,
            prompt="Choose cards from your discard pile")
        if taken:
            await ctx.put_in_hand(taken, reveal=True)
    return effect


def devolve_to_basic():
    """Return the highest evolution card on one of your Pokemon to your hand,
    discarding everything attached to it (Devolution Spray's older printing)."""
    async def effect(ctx):
        evolved = [p for p in ctx.my_pokemon_in_play() if is_evolution_pokemon(p)]
        if not evolved:
            return
        target = await ctx.choose_pokemon(
            evolved, "Choose a Pokémon to devolve") if len(evolved) > 1 else evolved[0]
        if target is None:
            return
        await ctx.discard_cards(
            [c for c in full_stack(target) if c is not target])
        await ctx.devolve_pokemon(target, steps=1, destination="hand")
    return effect


def holder_attack_discount(count: int, prize_behind: bool = False):
    """The holder's attacks cost `count` Colorless less; prize_behind gates it
    on having more Prize cards remaining than the opponent."""
    if not prize_behind:
        return attack_discount_passive(count)
    return AttackDiscountPassiveWithGate(count)


class AttackDiscountPassiveWithGate(Passive):
    """Attack cost discount that only applies while behind on Prizes."""

    def __init__(self, count):
        self.count = count

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier)
        if holder is not pokemon:
            return cost
        mine = board.find_player_area(pokemon.owning_player_id, "prizePile")
        theirs = board.find_player_area(
            next((p for p in board.player_ids
                  if p != pokemon.owning_player_id), None), "prizePile")
        if mine is None or theirs is None or len(mine.children) <= len(theirs.children):
            return cost
        return max(0, cost - self.count)


def heal_chosen(amount: int, count: int = 1, hp_at_most=None):
    """Heal `amount` from up to `count` of your Pokemon, chosen; a negative
    amount means "heal all damage", and hp_at_most filters the eligible
    Pokemon by remaining HP."""
    async def effect(ctx):
        pool = [p for p in ctx.my_pokemon_in_play()
                if hp_at_most is None or p.get_attribute(AttrID.HP, 0) <= hp_at_most]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, count, minimum=0, prompt="Choose a Pokémon to heal")
        for pokemon in picks:
            missing = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
            if missing <= 0:
                continue
            heal = missing if amount < 0 else min(amount, missing)
            await ctx.heal(heal, pokemon)
    return effect


async def _attach_discard_to_each(ctx, predicate, per_target, targets, target_pred):
    available = [c for c in ctx.discard_pile()
                 if predicate is None or predicate(c)]
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if target_pred is None or target_pred(p)]
    if not available or not candidates:
        return 0
    picks = await ctx.choose_cards(
        candidates, targets, minimum=0,
        prompt=f"Choose up to {targets} Pokémon to attach Energy to")
    attached = 0
    for pokemon in picks:
        if not available:
            break
        take = await ctx.choose_cards(
            available, per_target, minimum=min(per_target, len(available)),
            prompt="Choose Energy from your discard pile to attach")
        for card in take:
            available.remove(card)
            await ctx.attach_energy(card, pokemon)
            attached += 1
    return attached


def attach_discard_energy_to_each(predicate, per_target: int = 1, targets: int = 1,
                                  target_pred=None):
    """Attach `per_target` matching Energy from the discard pile to each of up
    to `targets` of your (matching) Pokemon."""
    async def effect(ctx):
        await _attach_discard_to_each(ctx, predicate, per_target, targets, target_pred)
    return effect


def switch_then_move_energy():
    """Switch your Active with a Benched Pokemon, then move an Energy from the
    Pokemon that went to the Bench onto the new Active."""
    async def effect(ctx):
        bench = ctx.my_bench()
        old_active = ctx.my_active()
        if not bench or old_active is None:
            return
        target = await ctx.choose_play_target(bench, "Choose your new Active Pokémon")
        if target is None or not await ctx.switch_active(ctx.player_id, target):
            return
        energies = ctx.attached_energies(old_active)
        if not energies or target is None:
            return
        picked = await ctx.choose_cards(
            energies, 1, minimum=1,
            prompt="Choose an Energy to move to the new Active") \
            if len(energies) > 1 else energies[:1]
        if picked:
            await ctx.move_energy(picked[0], target)
    return effect


def hand_to_bottom_draw_until(hand_size: int):
    """Put 1 card from your hand on the bottom of your deck, then draw until
    the hand holds `hand_size` cards."""
    async def effect(ctx):
        hand = ctx.hand()
        if not hand:
            return
        picks = await ctx.choose_cards(
            hand, 1, minimum=1,
            prompt="Choose a card to put on the bottom of your deck")
        if picks:
            await ctx.put_on_bottom_of_deck(picks[0])
        await ctx.draw_until(hand_size)
    return effect


def draw_until_unless_energy(hand_size: int, other_size: int):
    """Draw until the hand holds `hand_size`, or `other_size` when none of
    your Pokemon has any Energy attached."""
    async def effect(ctx):
        fitted = any(ctx.attached_energies(p) for p in ctx.my_pokemon_in_play())
        await ctx.draw_until(other_size if not fitted else hand_size)
    return effect


def discard_hand_no_rule_box_draw_per_card(draw_per_card: int, count: int = 2):
    """Discard up to `count` Rule-Box-free Pokemon from your hand and draw
    `draw_per_card` cards for each one discarded."""
    async def effect(ctx):
        pool = [c for c in ctx.hand()
                if is_rule_box_free_pokemon(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, count, minimum=0,
            prompt=f"Discard up to {count} Pokémon to draw cards")
        if not picks:
            return
        await ctx.discard_cards(picks)
        await ctx.draw_cards(draw_per_card * len(picks))
    return effect


def opponent_energy_to_deck_top(scope: str = "active"):
    """Put an Energy attached to the opponent's Active Pokemon on top of their
    deck (Team Star Grunt)."""
    async def effect(ctx):
        holder = ctx.opponent_active()
        if holder is None or not ctx.attached_energies(holder):
            return
        energies = ctx.attached_energies(holder)
        picked = await ctx.choose_cards(
            energies, 1, minimum=1,
            prompt="Choose an Energy to put on top of their deck") \
            if len(energies) > 1 else energies[:1]
        if picked:
            await ctx.put_on_top_of_deck(picked[0])
    return effect


def discard_from_opponent_hand(predicate=None, count: int = 1):
    """Your opponent reveals their hand; you discard up to `count` matching
    cards from it."""
    async def effect(ctx):
        hand = ctx.hand(ctx.opponent_id)
        if not hand:
            return
        cards = [c for c in hand if predicate is None or predicate(c)]
        await ctx.reveal_hand(ctx.opponent_id)
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, count, minimum=0,
            prompt=f"Choose up to {count} card(s) to discard from their hand")
        if picks:
            await ctx.discard_cards(picks)
    return effect


def is_pokemon_gx(card) -> bool:
    return is_pokemon_card(card) and "GX" in subtypes_for(card.archetype_id)


def is_pokemon_vstar(card) -> bool:
    return is_pokemon_card(card) and "VSTAR" in subtypes_for(card.archetype_id)


def retreat_cost_is(cost: int):
    """Predicate: a Pokemon whose printed Retreat Cost is exactly `cost`."""
    def predicate(card):
        return is_pokemon_card(card) \
            and card.get_attribute(AttrID.RETREAT_COST) == cost
    return predicate


def condition_opponent_active(*conditions):
    """Put Special Conditions on the opponent's Active Pokemon
    ("Your opponent's Active Pokemon is now Confused and Poisoned")."""
    async def effect(ctx):
        target = ctx.opponent_active()
        if target is None:
            return
        for condition in conditions:
            await ctx.apply_special_condition(target, condition)
    return effect


def heal_all_then_discard_energy():
    """Heal all damage from 1 of your Pokemon, then discard all Energy from
    it (Max Potion)."""
    async def effect(ctx):
        damaged = [p for p in ctx.my_pokemon_in_play()
                   if ctx.max_hp(p) > p.get_attribute(AttrID.HP, 0)]
        if not damaged:
            return
        target = await ctx.choose_pokemon(
            damaged, "Choose a Pokémon to heal") if len(damaged) > 1 else damaged[0]
        if target is None:
            return
        missing = ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)
        if missing > 0:
            await ctx.heal(missing, target)
        attachments = ctx.attached_energies(target)
        if attachments:
            await ctx.discard_energy_from(
                target, len(attachments),
                prompt="Discard all Energy from that Pokémon")
    return effect


def discard_benched_undamaged(count: int = 2):
    """Discard up to `count` of your Benched Pokemon that have no damage
    counters on them, with everything attached."""
    async def effect(ctx):
        pool = [p for p in ctx.my_bench()
                if p.get_attribute(AttrID.HP, 0) == ctx.max_hp(p)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, count, minimum=0,
            prompt=f"Discard up to {count} Benched Pokémon")
        for pokemon in picks:
            await ctx.discard_cards(full_stack(pokemon))
    return effect


def discard_in_play(predicates, count: int = 2):
    """Discard up to `count` matching cards from play (tools/stadiums on
    either side)."""
    async def effect(ctx):
        pool = []
        for card, _holder in ctx.tools_in_play():
            if any(check(card) for check in predicates):
                pool.append(card)
        stadium = ctx.stadium_in_play()
        if stadium is not None and any(check(stadium) for check in predicates):
            pool.append(stadium)
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, count, minimum=0,
            prompt=f"Choose up to {count} card(s) to discard")
        if picks:
            await ctx.discard_cards(picks)
    return effect


def opponent_shuffle_draw_per_prize():
    """The opponent shuffles their hand into their deck and draws 1 card for
    each of their remaining Prize cards."""
    async def effect(ctx):
        await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
        area = ctx.board.find_player_area(ctx.opponent_id, "prizePile")
        count = len(area.children) if area else 0
        if count:
            await ctx.draw_cards(count, ctx.opponent_id)
    return effect


def draw_n_if_active(subtype: str, base: int, bonus: int):
    """Draw `base` cards, or `base + bonus` while your Active Pokemon has the
    given subtype ("if your Active Pokemon is a TAG TEAM")."""
    async def effect(ctx):
        active = ctx.my_active()
        matches = active is not None and subtype in subtypes_for(active.archetype_id)
        await ctx.draw_cards(base + (bonus if matches else 0))
    return effect


def attach_hand_then_draw(predicate, count: int = 1, draw: int = 3):
    """Attach up to `count` matching Energy cards from your hand to 1 of your
    Pokemon, then draw `draw` cards if any were attached."""
    async def effect(ctx):
        cards = [c for c in ctx.hand() if predicate(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, count, minimum=0,
            prompt=f"Choose up to {count} Energy cards to attach")
        if not picks:
            return
        targets = ctx.my_pokemon_in_play()
        if not targets:
            return
        target = await ctx.choose_pokemon(
            targets, "Choose a Pokémon to attach the Energy to") \
            if len(targets) > 1 else targets[0]
        if target is None:
            return
        for card in picks:
            await ctx.attach_energy(card, target)
        if draw:
            await ctx.draw_cards(draw)
    return effect


def move_counters_between_opponents(max_count: int = 2, source_side: str = "opponent"):
    """Move up to `max_count` damage counters from one of the opponent's
    Pokemon to another of their Pokemon."""
    async def effect(ctx):
        pool = ctx.opponent_pokemon_in_play()
        damaged = [p for p in pool if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
        if not damaged:
            return
        source = await ctx.choose_pokemon(
            damaged, "Choose a Pokémon to move damage from") \
            if len(damaged) > 1 else damaged[0]
        if source is None:
            return
        targets = [p for p in pool if p is not source]
        if not targets:
            return
        dest = await ctx.choose_pokemon(
            targets, "Choose a Pokémon to move the damage to") or targets[0]
        if dest is not None:
            await ctx.move_damage_counters(source, [dest], max_count=max_count)
    return effect


def opponent_switch_then_self_switch():
    """The opponent switches their Active for a Benched Pokemon, then you
    switch yours (Escape Rope)."""
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if bench:
            target = await ctx.choose_pokemon(
                bench, "Choose your new Active Pokémon", player_id=ctx.opponent_id
            ) or bench[0]
            await ctx.switch_active(ctx.opponent_id, target)
        mine = ctx.my_bench()
        if mine:
            target = await ctx.choose_play_target(
                mine, "Choose your new Active Pokémon")
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)
    return effect


def pokemon_of_subtype(subtype: str):
    """Predicate: a Pokemon with the named printed subtype ("Ancient",
    "Future", "MEGA")."""
    wanted = subtype.lower()

    def predicate(card):
        if not is_pokemon_card(card):
            return False
        return any(wanted in name.lower()
                   for name in subtypes_for(card.archetype_id))
    return predicate


def shuffle_hand_n_draw(count: int, draw: int = 1):
    """Shuffle `count` cards from your hand into your deck, then draw `draw`."""
    async def effect(ctx):
        hand = ctx.hand()
        if not hand:
            return
        picks = await ctx.choose_cards(
            hand, count, minimum=min(count, len(hand)),
            prompt=f"Choose {count} card(s) to shuffle into your deck")
        if len(picks) < count:
            return
        await ctx.shuffle_into_deck(picks)
        await ctx.draw_cards(draw)
    return effect


def reveal_pokemon_then_search():
    """Reveal a Pokemon from your hand and put it into your deck; then search
    the deck for a Pokemon and put it into your hand."""
    async def effect(ctx):
        pokemon = [c for c in ctx.hand() if is_pokemon_card(c)]
        if not pokemon:
            return
        picks = await ctx.choose_cards(
            pokemon, 1, minimum=1,
            prompt="Choose a Pokémon from your hand to put into your deck")
        if not picks:
            return
        await ctx.shuffle_into_deck(picks)
        found = await ctx.search_deck(
            is_pokemon_card, count=1, minimum=0,
            prompt="Choose a Pokémon to put into your hand")
        if found:
            await ctx.put_in_hand(found, reveal=True)
        await ctx.shuffle_deck()
    return effect


def hand_to_top_then_search():
    """Put a card from your hand on top of your deck, then search the deck for
    a Pokemon and put it into your hand."""
    async def effect(ctx):
        hand = ctx.hand()
        if len(hand) <= 1:
            return
        picks = await ctx.choose_cards(
            hand, 1, minimum=1,
            prompt="Choose a card from your hand to put on top of your deck")
        if not picks:
            return
        await ctx.put_on_top_of_deck(picks[0])
        found = await ctx.search_deck(
            is_pokemon_card, count=1, minimum=0,
            prompt="Choose a Pokémon to put into your hand")
        if found:
            await ctx.put_in_hand(found, reveal=True)
        await ctx.shuffle_deck()
    return effect


def flip_search_basic():
    """Flip a coin per card; each heads searches the deck for a Basic Pokemon
    into your hand."""
    async def effect(ctx):
        heads = sum(1 for result in
                    await ctx.flip_coins(2, title="Flip 2 coins") if result)
        if heads <= 0:
            return
        found = await ctx.search_deck(
            is_basic_pokemon, count=heads, minimum=0,
            prompt="Choose a Basic Pokémon to put into your hand")
        if found:
            await ctx.put_in_hand(found, reveal=True)
        await ctx.shuffle_deck()
    return effect


def heal_all_then_energy_to_hand(predicate=None):
    """Heal all damage from 1 of your (matching) Pokemon, then put all Energy
    attached to it into your hand."""
    async def effect(ctx):
        damaged = [p for p in ctx.my_pokemon_in_play()
                   if ctx.max_hp(p) > p.get_attribute(AttrID.HP, 0)
                   and (predicate is None or predicate(p))]
        if not damaged:
            return
        target = await ctx.choose_pokemon(
            damaged, "Choose a Pokémon to heal") if len(damaged) > 1 else damaged[0]
        if target is None:
            return
        missing = ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)
        if missing > 0:
            await ctx.heal(missing, target)
        energies = ctx.attached_energies(target)
        if energies:
            await ctx.put_in_hand(energies, reveal=False)
    return effect


def trade_pokemon():
    """Trade a Basic Pokemon or Evolution card from your hand for one from
    your deck."""
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_pokemon_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=1,
            prompt="Choose a Pokémon from your hand to trade")
        if not picks:
            return
        await ctx.shuffle_into_deck(picks)
        found = await ctx.search_deck(
            is_pokemon_card, count=1, minimum=0,
            prompt="Choose a Pokémon from your deck")
        if found:
            await ctx.put_in_hand(found, reveal=True)
        await ctx.shuffle_deck()
    return effect


# --- Playability conditions ------------------------------------------------
# Each takes (board, player_id) and answers "may this card be played at all",
# matching the contract TrainerCardDef.condition documents.

def opponent_prizes_at_most(n: int):
    def check(board, player_id):
        opponent = _other_player(board, player_id)
        area = board.find_player_area(opponent, "prizePile") if opponent else None
        return bool(area) and len(area.children) <= n
    return check


def opponent_prizes_exactly(n: int):
    def check(board, player_id):
        opponent = _other_player(board, player_id)
        area = board.find_player_area(opponent, "prizePile") if opponent else None
        return bool(area) and len(area.children) == n
    return check


def hand_at_most(n: int):
    """The hand holds at most `n` cards besides this one."""
    def check(board, player_id):
        hand = board.find_player_area(player_id, "hand")
        return bool(hand) and len(hand.children) - 1 <= n
    return check


def hand_is_last():
    """This is the only card in hand."""
    def check(board, player_id):
        hand = board.find_player_area(player_id, "hand")
        return bool(hand) and len(hand.children) <= 1
    return check


def behind_on_prizes():
    """You have more Prize cards remaining than the opponent."""
    def check(board, player_id):
        opponent = _other_player(board, player_id)
        mine = board.find_player_area(player_id, "prizePile")
        theirs = board.find_player_area(opponent, "prizePile") if opponent else None
        if not mine or not theirs:
            return False
        return len(mine.children) > len(theirs.children)
    return check


def has_subtype_in_play(subtype: str):
    """A Pokemon of the named subtype is in play on your side."""
    wanted = subtype.lower()

    def check(board, player_id):
        return any(wanted in name.lower()
                   for pokemon in board.pokemon_in_play(player_id)
                   for name in subtypes_for(pokemon.archetype_id))
    return check


def ends_turn_after(inner):
    """Run `inner`, then end the turn ("Your turn ends")."""
    async def effect(ctx):
        await inner(ctx)
        ctx.ends_turn = True
    return effect


def is_damaged_pokemon(card) -> bool:
    """Predicate: a Pokemon with damage on it (deck/discard/idea filtering)."""
    return is_pokemon_card(card)


def draw_per_typed(type_name: str, per: int = 2):
    """Draw `per` cards for each of your Pokemon of the named type in play."""
    async def effect(ctx):
        wanted = POKEMON_TYPE_NAMES[type_name.lower()]
        count = sum(1 for p in ctx.my_pokemon_in_play()
                    if wanted in (p.get_attribute(AttrID.POKEMON_TYPES) or []))
        if count:
            await ctx.draw_cards(per * count)
    return effect


def draw_per_opponent_pokemon(per: int = 1):
    """Draw `per` card for each of the opponent's Pokemon in play."""
    async def effect(ctx):
        count = len(ctx.opponent_pokemon_in_play())
        if count:
            await ctx.draw_cards(per * count)
    return effect


def search_three_stages():
    """Search the deck for a Basic, a Stage 1 and a Stage 2 Pokemon."""
    async def effect(ctx):
        picks = []
        for predicate in (is_basic_pokemon, is_stage_one, is_stage_two):
            found = await ctx.search_deck(
                predicate, count=1, minimum=0,
                prompt="Choose a Pokémon to put into your hand")
            picks.extend(found)
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def attach_discard_energy_each_then_draw(predicate, per_target: int = 1,
                                         targets: int = 1, draw: int = 3,
                                         target_pred=None):
    """Attach Energy from the discard pile to each of up to `targets` of your
    (matching) Pokemon, then draw `draw` if any was attached."""
    async def effect(ctx):
        attached = await _attach_discard_to_each(ctx, predicate, per_target, targets,
                                                 target_pred)
        if attached and draw:
            await ctx.draw_cards(draw)
    return effect


def shuffle_hand_draw_exact_prizes(n: int, prizes: int, bigger: int):
    """Shuffle your hand into your deck, then draw `n` — or `bigger` when you
    have exactly `prizes` Prize cards remaining."""
    async def effect(ctx):
        await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
        area = ctx.board.find_player_area(ctx.player_id, "prizePile")
        count = n
        if area is not None and len(area.children) == prizes:
            count = bigger
        await ctx.draw_cards(count)
    return effect


def evolve_early_passive(type_name=None):
    """Pokemon of a type (or any) may evolve the turn they come into play,
    except on their owner's first turn."""
    wanted = POKEMON_TYPE_NAMES[type_name.lower()] if type_name else None
    return EvolveEarlyPassive(wanted)


class EvolveEarlyPassive(Passive):
    """Stadium: matching Pokemon can evolve on the turn they are played."""

    def __init__(self, wanted_type):
        self.wanted_type = wanted_type

    def may_evolve_early(self, pokemon, carrier):
        if self.wanted_type is None:
            return True
        return self.wanted_type in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def switch_then_heal_ex(amount: int = 80):
    """Switch your Active with a Benched Pokemon; heal `amount` from it if the
    Pokemon that went to the Bench was a Pokemon ex."""
    async def effect(ctx):
        bench = ctx.my_bench()
        old_active = ctx.my_active()
        if not bench or old_active is None:
            return
        target = await ctx.choose_play_target(bench, "Choose your new Active Pokémon")
        if target is None or not await ctx.switch_active(ctx.player_id, target):
            return
        if is_pokemon_ex(old_active):
            await ctx.heal(amount, old_active)
    return effect


def search_split_energy_to_hand_and_attach():
    """Search the deck for up to 2 Basic Energy of different types: one into
    your hand, the other attached to one of your Pokemon."""
    async def effect(ctx):
        found = await ctx.search_deck(
            is_basic_energy_card, count=2, minimum=0,
            prompt="Choose up to 2 Basic Energy cards")
        if not found:
            await ctx.shuffle_deck()
            return
        picks = await ctx.choose_cards(
            found, 1, minimum=1,
            prompt="Choose the Energy card to put into your hand") if found else []
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        rest = [card for card in found if card not in picks]
        if rest:
            targets = ctx.my_pokemon_in_play()
            if targets:
                target = await ctx.choose_pokemon(
                    targets, "Choose a Pokémon to attach the other Energy to") \
                    if len(targets) > 1 else targets[0]
                if target is not None:
                    await ctx.attach_energy(rest[0], target)
        await ctx.shuffle_deck()
    return effect


def attach_darkness_to_each_poison():
    """For each of up to N of your Darkness Pokemon, search the deck for a
    Basic Darkness Energy and attach it; if the Active got one, it is Poisoned."""
    async def effect(ctx):
        pool = [p for p in ctx.my_pokemon_in_play()
                if pokemon_of("darkness")(p)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 2, minimum=0,
            prompt="Choose up to 2 Darkness Pokémon to attach Energy to")
        active = ctx.my_active()
        attached_to_active = False
        for pokemon in picks:
            found = await ctx.search_deck(
                basic_energy_of("darkness"), count=1, minimum=0,
                prompt="Choose a Basic Darkness Energy")
            for card in found:
                await ctx.attach_energy(card, pokemon)
                if pokemon is active:
                    attached_to_active = True
        await ctx.shuffle_deck()
        if attached_to_active and active is not None:
            await ctx.apply_special_condition(active, SpecialConditions.POISONED)
    return effect


def shuffle_hand_draw_going_second(n: int, bigger: int):
    """Shuffle your hand into your deck, then draw `n` — or `bigger` when you
    went second and this is your first turn."""
    async def effect(ctx):
        await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
        turn_state = getattr(ctx.board, "turn_state", None)
        first_turn = turn_state is not None and turn_state.turn_number <= 2
        await ctx.draw_cards(bigger if first_turn else n)
    return effect


def draw_per_opponent_hand_card(predicate, per: int = 2):
    """Your opponent reveals their hand; draw `per` card for each matching
    card found there."""
    async def effect(ctx):
        hand = ctx.hand(ctx.opponent_id)
        await ctx.reveal_hand(ctx.opponent_id)
        matches = sum(1 for card in hand if predicate(card))
        if matches:
            await ctx.draw_cards(per * matches)
    return effect


def draw_per_opponent_bench(per: int = 1):
    """Draw `per` card for each of the opponent's Benched Pokemon."""
    async def effect(ctx):
        count = len(ctx.opponent_bench())
        if count:
            await ctx.draw_cards(per * count)
    return effect


def opponent_hand_to_bottom(predicate=None):
    """Your opponent reveals their hand; put 1 matching card from it on the
    bottom of their deck (they may then draw a card)."""
    async def effect(ctx):
        hand = ctx.hand(ctx.opponent_id)
        await ctx.reveal_hand(ctx.opponent_id)
        cards = [c for c in hand if predicate is None or predicate(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, 1, minimum=1,
            prompt="Choose a card to put on the bottom of their deck")
        if picks:
            await ctx.put_on_bottom_of_deck(picks[0])
            if await ctx.ask_yes_no("Draw a card?", player_id=ctx.opponent_id):
                await ctx.draw_cards(1, ctx.opponent_id)
    return effect


def opponent_energy_to_hand_then_attach():
    """Put an Energy attached to the opponent's Active into their hand, then
    attach an Energy card from your hand to your Active."""
    async def effect(ctx):
        holder = ctx.opponent_active()
        energies = ctx.attached_energies(holder) if holder is not None else []
        if not energies:
            return
        picked = await ctx.choose_cards(
            energies, 1, minimum=1,
            prompt="Choose an Energy to return to their hand") \
            if len(energies) > 1 else energies[:1]
        if not picked:
            return
        await ctx.put_in_hand(picked, reveal=True)
        mine = [c for c in ctx.hand() if is_energy_card(c)]
        target = ctx.my_active()
        if not mine or target is None:
            return
        chose = await ctx.choose_cards(
            mine, 1, minimum=1,
            prompt="Choose an Energy to attach to your Active") \
            if len(mine) > 1 else mine[:1]
        if chose:
            await ctx.attach_energy(chose[0], target)
    return effect


def reveal_then_search_same():
    """Reveal up to 2 Pokemon from your hand and put them into your deck; then
    search the deck for that many Pokemon."""
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_pokemon_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 2, minimum=0,
            prompt="Choose up to 2 Pokémon from your hand to put into your deck")
        if not picks:
            return
        await ctx.shuffle_into_deck(picks)
        found = await ctx.search_deck(
            is_pokemon_card, count=len(picks), minimum=0,
            prompt="Choose a Pokémon to put into your hand")
        if found:
            await ctx.put_in_hand(found, reveal=True)
        await ctx.shuffle_deck()
    return effect


def opponent_active_has(condition_code: str):
    """The opponent's Active Pokemon has the named Special Condition."""
    code = condition_code.upper()

    def check(board, player_id):
        opponent = _other_player(board, player_id)
        if not opponent:
            return False
        area = board.find_player_area(opponent, "activePokemonArea")
        pokemon = next((c for c in (area.children if area else [])
                        if isinstance(c, PokemonEntity)), None)
        if pokemon is None:
            return False
        wanted = SpecialConditions[code].value
        conditions = pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        return wanted in conditions
    return check


def heal_each_typed(amount: int, type_name: str):
    """Heal `amount` from each of your Pokemon of one type."""
    async def effect(ctx):
        wanted = POKEMON_TYPE_NAMES[type_name.lower()]
        for pokemon in ctx.my_pokemon_in_play():
            if wanted in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or []):
                missing = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
                if missing > 0:
                    await ctx.heal(min(amount, missing), pokemon)
    return effect


def gust_then_confuse():
    """Switch in one of the opponent's Benched Basic Pokemon; the new Active
    is now Confused."""
    async def effect(ctx):
        bench = [p for p in ctx.opponent_bench() if is_basic_pokemon(p)]
        if not bench or ctx.opponent_active() is None:
            return
        target = await ctx.choose_pokemon(
            bench, "Choose the opponent's new Active Pokémon") or bench[0]
        if await ctx.switch_active(ctx.opponent_id, target):
            await ctx.apply_special_condition(target, SpecialConditions.CONFUSED)
    return effect


def move_energy_to_active(count: int = 2):
    """Move up to `count` Energy from your Benched Pokemon to your Active."""
    async def effect(ctx):
        active = ctx.my_active()
        if active is None:
            return
        sources = [p for p in ctx.my_bench() if ctx.attached_energies(p)]
        if not sources:
            return
        source = await ctx.choose_pokemon(
            sources, "Choose a Benched Pokémon to move Energy from") \
            if len(sources) > 1 else sources[0]
        if source is None:
            return
        energies = ctx.attached_energies(source)
        take = min(count, len(energies))
        picked = await ctx.choose_cards(
            energies, take, minimum=1,
            prompt="Choose Energy to move to your Active") \
            if len(energies) > 1 else energies[:take]
        for card in picked:
            await ctx.move_energy(card, active)
    return effect


def discard_stadium_then_opponent_discards(count: int = 3):
    """Discard the Stadium in play; if you did, the opponent discards `count`
    cards from their hand."""
    async def effect(ctx):
        stadium = await ctx.discard_stadium()
        if stadium is None:
            return
        hand = ctx.hand(ctx.opponent_id)
        if not hand:
            return
        picks = await ctx.choose_cards(
            hand, count, minimum=min(count, len(hand)),
            prompt=f"Your opponent discards {count} cards",
            player_id=ctx.opponent_id)
        if picks:
            await ctx.discard_cards(picks)
    return effect


def opponent_bench_from_hand_then_switch():
    """Your opponent reveals their hand; you put a Basic Pokemon from it onto
    their Bench and switch it into the Active Spot."""
    async def effect(ctx):
        hand = ctx.hand(ctx.opponent_id)
        await ctx.reveal_hand(ctx.opponent_id)
        basics = [c for c in hand if is_basic_pokemon(c)]
        if not basics:
            return
        picks = await ctx.choose_cards(
            basics, 1, minimum=1,
            prompt="Choose a Basic Pokémon to put onto their Bench")
        if not picks:
            return
        if await ctx.bench_pokemon(picks[0]):
            await ctx.switch_active(ctx.opponent_id, picks[0])
    return effect


def choose_one(options):
    """Offer the card's printed "Choose 1" bullets and run the picked one.

    `options` is a list of (label, effect) pairs, built from the printed text
    so the player sees the card's own wording."""
    async def effect(ctx):
        if not options:
            return
        picked = await ctx.choose("Choose 1", [label for label, _ in options])
        if picked is None or not 0 <= picked < len(options):
            return
        await options[picked][1](ctx)
    return effect


def choose_any(options):
    """"Choose 1 or both": offer every option plus a combined choice."""
    async def effect(ctx):
        labels = [label for label, _ in options] + ["Both"]
        picked = await ctx.choose("Choose 1 or both", labels)
        if picked is None:
            return
        if picked == len(options):
            for _label, inner in options:
                await inner(ctx)
            return
        if 0 <= picked < len(options):
            await options[picked][1](ctx)
    return effect


def holder_retreat_free():
    """The Pokemon this card is attached to has no Retreat Cost."""
    return retreat_free_when(
        lambda pokemon, carrier: carrier_pokemon(carrier) is pokemon)


def holder_takes_less_basic(amount: int):
    """If the holder is a Basic Pokemon, damage done to it by attacks is
    reduced by `amount`."""
    return takes_less_passive(
        amount, protects=lambda target, carrier: carrier_pokemon(carrier) is target
        and is_basic_pokemon(target))


def holder_damage_boost_vs(amount: int, kind: str = "ex"):
    """The holder's attacks do `amount` more damage to matching opposing
    Active Pokemon; kind is 'ex', 'v', 'vmax', 'gx' or 'any'."""
    target_pred = {
        "ex": is_pokemon_ex,
        "v": lambda card: is_pokemon_v(card.archetype_id),
        "vmax": lambda card: is_pokemon_vmax(card.archetype_id),
        "gx": is_pokemon_gx,
    }.get(kind, lambda card: True)
    return typed_damage_boost_tool(target_pred, amount)



# --- Holder-gated tools, both-sides stadiums, stadium abilities -------------

def owned_by(owner: str):
    """Predicate: a card printed as "<Owner>'s ..." (Hop's Wooloo). A short
    owner like N or Hop never matches an unrelated name (Hoppip, Snorlax)."""
    prefix = owner.lower() + "'s "

    def predicate(card):
        definition = def_for(card.archetype_id)
        name = (getattr(definition, "display_name", "") or "").lower()
        return name.replace("\u2019", "'").startswith(prefix)
    return predicate


def _holds(holder):
    """(target, carrier) pred: target is the tool's holder and matches holder."""
    def protects(target, carrier):
        return carrier_pokemon(carrier) is target and (holder is None or holder(target))
    return protects


def gated_hp_bonus(amount: int, holder=None):
    """The <holder> this card is attached to gets +amount HP."""
    return hp_bonus_tool(amount, holder)


def gated_no_weakness(holder=None):
    """The <holder> this card is attached to has no Weakness."""
    return no_weakness_passive(_holds(holder))


def gated_retreat_free(holder=None):
    """The <holder> this card is attached to has no Retreat Cost."""
    return retreat_free_when(_holds(holder))


def gated_takes_less(amount: int, holder=None, attacker=None):
    """The <holder> this card is attached to takes amount less damage from
    attacks of the opponent's <attacker> Pokemon."""
    return takes_less_passive(amount, protects=_holds(holder), attacker_pred=attacker)


class GatedDamageBoostPassive(Passive):
    """The holder's attacks do +amount to the opponent's Active Pokemon, when
    the holder matches `holder` and the Active matches `target`."""

    def __init__(self, amount, holder=None, target=None):
        self.amount = amount
        self.holder = holder
        self.target = target

    def modify_damage_dealt(self, calc, carrier):
        attacker = calc.attacker
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if carrier_pokemon(carrier) is not attacker:
            return
        if self.holder is not None and not self.holder(attacker):
            return
        if self.target is not None and not self.target(calc.target):
            return
        calc.amount += self.amount


def gated_damage_boost(amount: int, holder=None, target=None):
    """Attacks used by the <holder> this card is attached to do +amount to
    the opponent's Active (<target>) Pokemon."""
    return GatedDamageBoostPassive(amount, holder, target)


class EveryoneDamageBoostPassive(Passive):
    """Stadium: attacks of matching Pokemon (both sides) do +amount to the
    opponent's Active (matching `target`) Pokemon."""

    def __init__(self, amount, attacker, target=None):
        self.amount = amount
        self.attacker = attacker
        self.target = target

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if not self.attacker(calc.attacker):
            return
        if self.target is not None and not self.target(calc.target):
            return
        calc.amount += self.amount


def stadium_damage_boost(amount: int, attacker, target=None):
    """The attacks of <attacker> Pokemon (both yours and your opponent's) do
    +amount to the opponent's Active Pokemon."""
    return EveryoneDamageBoostPassive(amount, attacker, target)


def stadium_takes_less_for(amount: int, protects):
    """<protects> Pokemon (both sides) take amount less damage from the
    opponent's attacks."""
    return takes_less_passive(amount, protects=lambda target, carrier: protects(target))


def stadium_no_retreat(pred):
    """<pred> Pokemon in play (both sides) have no Retreat Cost."""
    return retreat_free_when(lambda pokemon, carrier: pred(pokemon))


class RetreatShiftPassive(Passive):
    """Retreat Cost of matching Pokemon (both sides) shifts by delta."""

    def __init__(self, delta, pred):
        self.delta = delta
        self.pred = pred

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if not self.pred(pokemon):
            return cost
        return max(0, cost + self.delta)


def stadium_retreat_shift(delta: int, pred):
    """The Retreat Cost of each <pred> Pokemon (both sides) is |delta|
    Colorless more (delta > 0) or less (delta < 0)."""
    return RetreatShiftPassive(delta, pred)


def stadium_no_resistance():
    """Each Pokemon in play has no Resistance."""
    return no_resistance_passive(when=lambda calc, carrier: True)


def stadium_ability(title: str, effect):
    """"Once during each player's turn, that player may ..." on a Stadium."""
    return Ability(title=title, activation=Activations.ONCE_PER_TURN, effect=effect)



def is_pokemon_EX(card) -> bool:
    """Black & White / XY era "Pokemon-EX" (printed subtype "EX"), which the
    Scarlet & Violet "Pokemon ex" predicate deliberately does not match."""
    return is_pokemon_card(card) and "EX" in subtypes_for(card.archetype_id)


# --- Bespoke tool shapes on existing engine hooks ---------------------------

def named_rule_box(name: str, suffix: str):
    """Predicate: the named Pokemon with a printed rule-box suffix ("pikachu",
    "ex" matches Pikachu ex; "ex" also covers the older Pokemon-EX)."""
    name_pred = named(*name.split())
    suffix_pred = {"ex": any_of(is_pokemon_ex, is_pokemon_EX), "gx": is_pokemon_gx,
                   "v": lambda card: is_pokemon_v(card.archetype_id)}[suffix]
    return lambda card: is_pokemon_card(card) and name_pred(card) and suffix_pred(card)


class GatedTypePassive(Passive):
    """The <holder> this card is attached to is a <type> Pokemon."""

    def __init__(self, type_name, holder=None):
        self.value = POKEMON_TYPE_NAMES[type_name]
        self.holder = holder

    def modify_pokemon_types(self, types, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return types
        if self.holder is not None and not self.holder(pokemon):
            return types
        return [self.value]


def gated_type(type_name: str, holder=None):
    return GatedTypePassive(type_name, holder)


class LowHpRetreatPassive(Passive):
    """Rescue Board: the holder retreats for [C] less, or for free while its
    remaining HP is `threshold` or less."""

    def __init__(self, count, threshold):
        self.count = count
        self.threshold = threshold

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        if pokemon.get_attribute(AttrID.HP, 0) <= self.threshold:
            return 0
        return max(0, cost - self.count)


def low_hp_retreat(count: int, threshold: int):
    return LowHpRetreatPassive(count, threshold)


class ActiveHolderRetreatTaxPassive(Passive):
    """Gravity Gemstone: while the holder is Active, both Active Pokemon's
    Retreat Cost is `count` more."""

    def __init__(self, count):
        self.count = count

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier)
        if holder is None or not is_in_active_spot(holder) or not is_in_active_spot(pokemon):
            return cost
        return cost + self.count


def active_holder_retreat_tax(count: int):
    return ActiveHolderRetreatTaxPassive(count)


class HolderAbilityShieldPassive(Passive):
    """Prevent all effects of the opponent's Abilities done to the holder."""

    def blocks_ability_effects(self, target, carrier):
        return carrier_pokemon(carrier) is target


def holder_ability_shield():
    return HolderAbilityShieldPassive()


class HolderCoinRerollPassive(Passive):
    """Trick Coin: once during your turn, after flipping coins for an attack
    of the holder, ignore them and flip again. The engine asks per player, so
    the offer stands while the holder is that player's Active Pokemon, which
    is the Pokemon attacking."""

    def __init__(self, holder=None):
        self.holder = holder

    def offers_attack_coin_reroll(self, player_id, carrier):
        pokemon = carrier_pokemon(carrier)
        if pokemon is None or pokemon.owning_player_id != player_id:
            return False
        if not is_in_active_spot(pokemon):
            return False
        return self.holder is None or self.holder(pokemon)


def holder_coin_reroll(holder=None):
    return HolderCoinRerollPassive(holder)



class TargetedTurnBoostPassive(Passive):
    """Rides each opposing Pokemon for one turn: attacks by `player_id`'s
    Pokemon do +amount to it while it is the Active and matches `target`."""

    def __init__(self, amount, player_id, target):
        self.amount = amount
        self.player_id = player_id
        self.target = target

    def modify_damage_dealt(self, calc, carrier):
        attacker = calc.attacker
        if not (calc.is_attack and calc.to_active and attacker is not None):
            return
        if attacker.owning_player_id != self.player_id:
            return
        if carrier_pokemon(carrier) is not calc.target or not self.target(calc.target):
            return
        calc.amount += self.amount


def turn_damage_boost_vs(amount: int, target):
    """During this turn, attacks used by your Pokemon do +amount to the
    opponent's Active Pokemon matching `target` (Black Belt's Training)."""
    async def effect(ctx):
        turn = ctx.session.turn_state.turn_number
        for pokemon in ctx.opponent_pokemon_in_play():
            ctx.add_temporary_passive(
                pokemon, TargetedTurnBoostPassive(amount, ctx.player_id, target),
                expires_after_turn=turn)
    return effect



def named_exactly(name: str):
    """Predicate: a card whose printed name is exactly `name` ("Judge", not
    "Judge Whistle"); punctuation and spacing are ignored, because canonical
    rules text has already dropped apostrophes."""
    wanted = re.sub(r"[^a-z0-9]", "", name.lower())

    def predicate(card):
        definition = def_for(card.archetype_id)
        name_now = re.sub(r"[^a-z0-9]", "",
                          (getattr(definition, "display_name", "") or "").lower())
        return name_now == wanted
    return predicate


def is_pokemon_v_card(card) -> bool:
    """Predicate: a Pokemon V of any kind (V, VSTAR, VMAX, V-UNION)."""
    return is_pokemon_card(card) and is_pokemon_v(card.archetype_id)


def _attack_ko_by_opponent(pokemon, ctx):
    """Whether `pokemon` was knocked out by damage from the opponent's attack."""
    if ctx is None or not ctx.is_attack_effect():
        return False
    attacker = getattr(ctx, "attacker", None)
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return False
    return pokemon.entity_id in getattr(ctx, "attack_damage", {})


class KnockoutPrizeShiftPassive(Passive):
    """The opponent takes `delta` more (or fewer) Prize cards when the holder
    (holder_only) or any matching Pokemon (stadium) is knocked out."""

    def __init__(self, delta, pred=None, holder_only=True, attack_only=True):
        self.delta = delta
        self.pred = pred
        self.holder_only = holder_only
        self.attack_only = attack_only

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if self.holder_only and carrier_pokemon(carrier) is not pokemon:
            return count
        if self.pred is not None and not self.pred(pokemon):
            return count
        if self.attack_only and not _attack_ko_by_opponent(pokemon, ctx):
            return count
        return max(0, count + self.delta)


def holder_prize_shift(delta: int, holder=None, attack_only: bool = True):
    """If the <holder> this card is attached to is Knocked Out (by damage from
    an opponent's attack), the opponent takes |delta| more/fewer Prize cards."""
    return KnockoutPrizeShiftPassive(delta, holder, True, attack_only)


def stadium_prize_shift(delta: int, pred):
    """Whenever a <pred> Pokemon (both sides) is Knocked Out by damage from an
    opponent's attack, that player takes |delta| more/fewer Prize cards."""
    return KnockoutPrizeShiftPassive(delta, pred, False, True)



def named_one_of(*names):
    """Predicate: a card whose printed name is one of `names` ("Regirock",
    ...), allowing a printed suffix."""
    wanted = tuple(name.lower() for name in names)

    def predicate(card):
        definition = def_for(card.archetype_id)
        name = (getattr(definition, "display_name", "") or "").lower()
        return any(name == w or name.startswith(w + " ") for w in wanted)
    return predicate


def _attacker_energy_count(attacker):
    special = basic = 0
    stack = list(attacker.children)
    while stack:
        entity = stack.pop()
        stack.extend(getattr(entity, "children", []) or [])
        if entity.get_attribute(AttrID.IS_SPECIAL_ENERGY):
            special += 1
        elif entity.get_attribute(AttrID.CARD_TYPE) == CardType.ENERGY.value:
            basic += 1
    return special, basic


def attacker_has_special_energy():
    """Attacker predicate: the attacker has Special Energy attached."""
    return lambda attacker: _attacker_energy_count(attacker)[0] > 0


def attacker_has_ability():
    """Attacker predicate: the attacker prints at least one Ability."""
    def predicate(attacker):
        definition = def_for(attacker.archetype_id)
        return bool(getattr(definition, "abilities", None))
    return predicate


def attacker_of_types(*type_names):
    """Attacker predicate: the attacker is one of the named types."""
    values = {POKEMON_TYPE_NAMES[name] for name in type_names}

    def predicate(attacker):
        return bool(values & set(attacker.get_attribute(AttrID.POKEMON_TYPES) or []))
    return predicate


def attacker_has_subtypes(*subtypes, exclude=()):
    """Attacker predicate: the attacker prints one of `subtypes` (lowercase
    compare, so "ex" matches both Pokemon ex and the older Pokemon-EX) and
    none of `exclude`."""
    wanted = [s.lower() for s in subtypes]
    banned = [s.lower() for s in exclude]

    def predicate(attacker):
        names = [s.lower() for s in subtypes_for(attacker.archetype_id)]
        if not any(w in names for w in wanted):
            return False
        return not any(b in names for b in banned)
    return predicate


class AttackerGatedPassive(Passive):
    """The holder takes `amount` less damage (or none at all) from attacks by
    attackers matching `attacker`; `holder` gates which Pokemon it protects
    and `effects_too` also shields it from the attack's effects."""

    def __init__(self, amount, holder=None, attacker=None, prevent=False,
                 effects_too=False):
        self.amount = amount
        self.holder = holder
        self.attacker = attacker
        self.prevent = prevent
        self.effects_too = effects_too

    def _applies(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        if self.holder is not None and not self.holder(calc.target):
            return False
        if self.attacker is None:
            return calc.attacker is not None
        return calc.attacker is not None and self.attacker(calc.attacker)

    def modify_damage_taken(self, calc, carrier):
        if self.amount and self._applies(calc, carrier):
            calc.amount = max(0, calc.amount - self.amount)

    def prevents_damage(self, calc, carrier):
        return bool(self.prevent and self._applies(calc, carrier))

    def blocks_attack_effects(self, target, carrier):
        return bool(self.effects_too and carrier_pokemon(carrier) is target)


def takes_less_from(amount: int, holder=None, attacker=None):
    """The holder takes `amount` less damage from attacks by `attacker`."""
    return AttackerGatedPassive(amount, holder, attacker)


def prevents_all_from(holder=None, attacker=None, effects_too=False):
    """Prevent all damage (and effects) done to the holder by `attacker`."""
    return AttackerGatedPassive(0, holder, attacker, prevent=True,
                                effects_too=effects_too)


def holder_condition_immunity(holder=None):
    """The holder can't be affected by any Special Condition."""
    return condition_immunity_passive(None, protects=_holds(holder))



class EveryoneHpBonusPassive(Passive):
    """Stadium: every in-play Pokemon matching `pred` gets +amount max HP."""

    def __init__(self, amount, pred):
        self.amount = amount
        self.pred = pred

    def max_hp_bonus(self, pokemon, carrier):
        return self.amount if self.pred(pokemon) else 0


def stadium_hp_bonus(amount: int, pred):
    """<pred> Pokemon in play (both sides) get +amount max HP."""
    return EveryoneHpBonusPassive(amount, pred)


def has_energy_of(*type_names):
    """Pokemon predicate: any attached Energy is one of the named types."""
    values = {POKEMON_TYPE_NAMES[name] for name in type_names}

    def predicate(pokemon):
        stack = list(pokemon.children)
        while stack:
            entity = stack.pop()
            stack.extend(getattr(entity, "children", []) or [])
            if entity.get_attribute(AttrID.CARD_TYPE) != CardType.ENERGY.value:
                continue
            if values & set(entity.get_attribute(AttrID.POKEMON_TYPES) or []):
                return True
        return False
    return predicate


def pokemon_named(word: str):
    """Pokemon predicate: the printed name contains `word` ("Psyduck")."""
    wanted = word.lower()

    def predicate(card):
        definition = def_for(card.archetype_id)
        return is_pokemon_card(card) and wanted in (
            getattr(definition, "display_name", "") or "").lower()
    return predicate


def attacker_named_team(phrase: str):
    """Attacker predicate: the printed name contains `phrase` and the attacker
    is not a Pokemon ex (Team Plasma's Pokemon)."""
    named_pred = pokemon_named(phrase)
    return lambda attacker: named_pred(attacker) and not is_pokemon_ex(attacker)


def trainer_card_other_than(name: str):
    """Predicate: any Trainer card whose printed name is not `name`."""
    excluded = named_exactly(name)
    return lambda card: is_trainer_card(card) and not excluded(card)


def protect_chosen_next_turn(count: int = 1, prevent: bool = True,
                             effects_too: bool = True):
    """Choose `count` of your Pokemon; through your opponent's next turn all
    damage (and effects) done to them by your opponent's Pokemon is prevented."""
    async def effect(ctx):
        targets = await ctx.choose_cards(
            ctx.my_pokemon_in_play(), count, minimum=count,
            prompt="Choose a Pokémon to protect next turn.")
        for target in targets:
            ctx.add_passive_through_opponents_turn(
                target, TempShieldPassive(prevent=prevent, effects_too=effects_too))
    return effect


def extra_prize_on_ko(attacker, prizes: int = 1):
    """During this turn, take `prizes` extra Prize cards when `attacker`'s
    attack knocks out the opponent's Active Pokemon (Briar)."""
    async def effect(ctx):
        ctx.add_extra_prize_watcher(attacker_predicate=attacker, prizes=prizes)
    return effect


def tera_attacker():
    """Predicate: a Tera Pokemon (the attacker that earns Briar's extra Prize)."""
    return pokemon_of_subtype("Tera")


def opponent_prizes_in(low: int, high: int):
    """Condition: the opponent has between `low` and `high` Prize cards left."""
    def check(board, player_id):
        area = board.find_player_area(_opponent_of(board, player_id), "prizePile")
        if area is None:
            return False
        return low <= len(area.children) <= high
    return check


def _opponent_of(board, player_id):
    players = list(getattr(board, "player_ids", []) or [])
    return next((p for p in players if p != player_id), None)


def search_rule_box_free_plus_students(extra_name: str = "Paldean Student"):
    """Search for 1 Rule-Box-free Pokemon, plus 1 more for each `extra_name`
    card in your discard pile (Paldean Student)."""
    tablet = named_exactly(extra_name)

    async def effect(ctx):
        extra = sum(1 for card in ctx.discard_pile() if tablet(card))
        count = 1 + extra
        picks = await ctx.search_deck(is_rule_box_free_pokemon, count=count,
                                      minimum=1)
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def switch_team_then_gust(owner: str):
    """Switch your Active <Owner>'s Pokemon with a Benched one of the same
    owner, then switch 1 of the opponent's Benched Pokemon to their Active."""
    owner_pred = owned_by(owner)

    async def effect(ctx):
        active = ctx.my_active()
        bench = [p for p in ctx.my_bench() if owner_pred(p)]
        if active is not None and owner_pred(active) and bench:
            target = await ctx.choose_play_target(
                bench, "Choose your new Active Pokémon")
            if target is None:
                return
            if not await ctx.switch_active(ctx.player_id, target):
                return
        opposing_bench = ctx.opponent_bench()
        if not opposing_bench:
            return
        chosen = await ctx.choose_play_target(
            opposing_bench, "Choose your opponent's new Active Pokémon")
        if chosen is not None:
            await ctx.switch_active(ctx.opponent_id, chosen)
    return effect


def draw_until_per_typed_pokemon(type_name: str):
    """Draw until your hand holds as many cards as you have Pokemon of
    `type_name` in play."""
    type_pred = pokemon_of(type_name)

    async def effect(ctx):
        wanted = sum(1 for p in ctx.my_pokemon_in_play() if type_pred(p))
        hand = len(ctx.hand())
        if wanted > hand:
            await ctx.draw_cards(wanted - hand)
    return effect


def card_named_contains(word: str):
    """Predicate: any card whose printed name contains `word`."""
    wanted = word.lower()

    def predicate(card):
        definition = def_for(card.archetype_id)
        return wanted in (getattr(definition, "display_name", "") or "").lower()
    return predicate


def shuffle_hand_flip_draw(heads: int, tails: int):
    """Shuffle your hand into your deck, flip a coin: heads draws `heads`,
    tails draws `tails` (Gambler)."""
    async def effect(ctx):
        hand = ctx.hand()
        if hand:
            await ctx.shuffle_into_deck(hand)
        if await ctx.flip_coins(1):
            await ctx.draw_cards(heads)
        else:
            await ctx.draw_cards(tails)
    return effect


def flip_search_basic_count(count: int, avoid_baby: bool = True):
    """Flip `count` coins; for each heads, search the deck for a Basic Pokemon
    and put it into your hand (Dual Ball)."""
    async def effect(ctx):
        heads = await ctx.flip_coins(count)
        wanted = sum(1 for result in heads if result)
        if wanted <= 0:
            return
        def eligible(card):
            if not is_basic_pokemon(card):
                return False
            return not (avoid_baby and "Baby" in subtypes_for(card.archetype_id))
        picks = await ctx.search_deck(eligible, count=wanted, minimum=0)
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


class RetaliateOnAttackPassive(Passive):
    """Rocky Helmet: while the holder is Active and was damaged by the
    opponent's attack, put `counters` damage counters on the attacker."""

    def __init__(self, counters: int):
        self.counters = counters
        self.attack_followup = self._followup

    async def _followup(self, ctx, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or not is_in_active_spot(holder):
            return
        entry = getattr(ctx, "attack_damage", {}).get(holder.entity_id)
        if not entry or entry[0] <= 0:
            return
        attacker = getattr(ctx, "attacker", None)
        if attacker is None or attacker.owning_player_id == holder.owning_player_id:
            return
        await ctx.set_damage_counters(attacker, self.counters)


def retaliate_on_attack(counters: int = 2):
    return RetaliateOnAttackPassive(counters)


def look_top_reorder(count: int):
    """Look at the top `count` cards and put them back on top in any order."""
    async def effect(ctx):
        await ctx.reorder_deck_top(count)
    return effect


def look_top_peek(count: int):
    """Look at the top `count` cards and put them back in the same order."""
    async def effect(ctx):
        ctx.deck_top(count)
    return effect


def pokemon_with_hp_at_most(limit: int):
    """Predicate: a Pokemon card whose printed HP is `limit` or less."""
    def predicate(card):
        return is_pokemon_card(card) and (card.get_attribute(AttrID.HP, 0) or 0) <= limit
    return predicate


def pokemon_with_retreat_at_least(minimum: int):
    """Predicate: a Pokemon card with a printed Retreat Cost of `minimum`+."""
    def predicate(card):
        return is_pokemon_card(card) and \
            (card.get_attribute(AttrID.RETREAT_COST, 0) or 0) >= minimum
    return predicate


def recycle_from_discard(count: int = 1):
    """Put `count` cards from your discard pile on top of your deck."""
    async def effect(ctx):
        cards = ctx.discard_pile()
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, count, minimum=0,
            prompt="Choose card(s) from your discard pile to put on top of your deck")
        for card in picks:
            await ctx.put_on_top_of_deck(card)
    return effect


def devolve_stage(stage: str = "stage 1"):
    """Choose one of your evolved Pokemon and discard its highest evolution
    card (devolve it one stage)."""
    async def effect(ctx):
        evolved = [p for p in ctx.my_pokemon_in_play()
                   if ctx.evolutions_of(p)] if hasattr(ctx, "evolutions_of") else []
        target = None
        if evolved:
            target = await ctx.choose_pokemon(
                evolved, "Choose a Pokémon to devolve") if len(evolved) > 1 else evolved[0]
        if target is None:
            return
        await ctx.devolve_pokemon(target, steps=1, destination="discard")
    return effect


class RetaliatePoisonPassive(Passive):
    """Poison Barb: while the holder is Active and was damaged by the
    opponent's attack, the attacking Pokemon is now Poisoned."""

    def __init__(self):
        self.attack_followup = self._followup

    async def _followup(self, ctx, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or not is_in_active_spot(holder):
            return
        entry = getattr(ctx, "attack_damage", {}).get(holder.entity_id)
        if not entry or entry[0] <= 0:
            return
        attacker = getattr(ctx, "attacker", None)
        if attacker is None or attacker.owning_player_id == holder.owning_player_id:
            return
        await ctx.apply_special_condition(attacker, SpecialConditions.POISONED)


def retaliate_poison():
    return RetaliatePoisonPassive()


def pokemon_type_subtype(type_name: str, subtype: str):
    """Predicate: a Pokemon of `type_name` with the printed `subtype`
    ("lightning pokemon gx")."""
    type_pred = pokemon_of(type_name)
    if subtype.lower() == "ex":
        suffix = any_of(is_pokemon_ex, is_pokemon_EX)
    elif subtype.lower() == "gx":
        suffix = is_pokemon_gx
    else:
        suffix = pokemon_of_subtype(subtype)
    return lambda card: type_pred(card) and suffix(card)


def opponent_active_is(pred):
    """Condition: the opponent's Active Pokemon matches `pred`."""
    def check(board, player_id):
        opponent = _other_player(board, player_id)
        area = board.find_player_area(opponent, "activePokemonArea") if opponent else None
        active = area.children[0] if area is not None and area.children else None
        return active is not None and pred(active)
    return check


class TrainerPlayLockPassive(Passive):
    """`player_id` cannot play any more Trainer cards this turn."""

    def __init__(self, player_id):
        self.player_id = player_id

    def blocks_trainer_play(self, card, player_id, carrier):
        return player_id == self.player_id


def shuffle_hand_draw_lock_trainers(draw: int):
    """Shuffle your hand into your deck, draw `draw` cards, then you cannot
    play any more Trainer cards this turn (Professor Elm)."""
    async def effect(ctx):
        hand = ctx.hand()
        if hand:
            await ctx.shuffle_into_deck(hand)
        await ctx.draw_cards(draw)
        holder = ctx.my_active() or next(iter(ctx.my_pokemon_in_play()), None)
        if holder is not None:
            ctx.add_temporary_passive(
                holder, TrainerPlayLockPassive(ctx.player_id),
                expires_after_turn=ctx.session.turn_state.turn_number)
    return effect


def discard_typed_pokemon_to_bench_then_draw(type_name: str, draw: int):
    """Put a matching Pokemon from your discard pile onto your Bench, then
    draw `draw` cards."""
    type_pred = pokemon_of(type_name)

    async def effect(ctx):
        pool = [card for card in ctx.discard_pile() if type_pred(card)]
        if pool and len(ctx.my_bench()) < BENCH_CAPACITY:
            picks = await ctx.choose_cards(
                pool, 1, minimum=0,
                prompt="Choose a Pokémon from your discard pile to put on your Bench")
            for card in picks:
                await ctx.bench_pokemon(card)
        await ctx.draw_cards(draw)
    return effect


def colress_draw():
    """Shuffle your hand into your deck, then draw 1 card for each Benched
    Pokemon, yours and your opponent's."""
    async def effect(ctx):
        hand = ctx.hand()
        if hand:
            await ctx.shuffle_into_deck(hand)
        count = len(ctx.my_bench()) + len(ctx.opponent_bench())
        if count > 0:
            await ctx.draw_cards(count)
    return effect


def discard_opponent_energy(count: int = 1):
    """Choose an Energy card attached to one of your opponent's Pokemon and
    discard it (Energy Removal)."""
    async def effect(ctx):
        candidates = [p for p in ctx.opponent_pokemon_in_play()
                      if ctx.attached_energies(p)]
        if not candidates:
            return
        target = (await ctx.choose_pokemon(
            candidates, "Choose an opponent's Pokémon with Energy")) if len(candidates) > 1 \
            else candidates[0]
        if target is None:
            return
        await ctx.discard_energy_from(target, count, minimum=count)
    return effect


def shuffle_hand_cards_draw(cards: int, draw: int):
    """Shuffle `cards` other cards from your hand into your deck, then draw
    `draw` (Maintenance)."""
    async def effect(ctx):
        pool = ctx.hand()
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, cards, minimum=min(cards, len(pool)),
            prompt="Choose cards to shuffle into your deck")
        if picks:
            await ctx.shuffle_into_deck(picks)
        await ctx.draw_cards(draw)
    return effect


def shuffle_discard_combo_into_deck(count: int, *predicates):
    """Shuffle `count` cards matching any of `predicates` from your discard
    pile back into your deck (Super Rod)."""
    def matches(card):
        return any(pred(card) for pred in predicates)

    async def effect(ctx):
        pool = [card for card in ctx.discard_pile() if matches(card)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, count, minimum=0,
            prompt="Choose cards from your discard pile to shuffle back in")
        if picks:
            await ctx.shuffle_into_deck(picks)
    return effect


def copycat_draw():
    """Shuffle your hand into your deck, then draw as many cards as your
    opponent holds."""
    async def effect(ctx):
        hand = ctx.hand()
        if hand:
            await ctx.shuffle_into_deck(hand)
        area = ctx.board.find_player_area(ctx.opponent_id, "hand")
        count = len(area.children) if area is not None else 0
        if count:
            await ctx.draw_cards(count)
    return effect


def draw_then_bottom(draw: int, count: int = 1):
    """Draw `draw` cards, then put `count` card from your hand on the bottom
    of your deck (Professor Oak's Visit)."""
    async def effect(ctx):
        await ctx.draw_cards(draw)
        pool = ctx.hand()
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, count, minimum=min(count, len(pool)),
            prompt="Choose a card to put on the bottom of your deck")
        for card in picks:
            await ctx.put_on_bottom_of_deck(card)
    return effect


def flip_heal_chosen(counters_per_head: int, coins: int = 2):
    """Choose one of your Pokemon and flip `coins`; remove
    `counters_per_head` damage counters for each heads (Moo-Moo Milk)."""
    async def effect(ctx):
        pool = [p for p in ctx.my_pokemon_in_play()
                if ctx.max_hp(p) > p.get_attribute(AttrID.HP, 0)]
        if not pool:
            return
        target = (await ctx.choose_pokemon(pool, "Choose a Pokémon to heal")) \
            if len(pool) > 1 else pool[0]
        if target is None:
            return
        results = await ctx.flip_coins(coins)
        heads = sum(1 for result in results if result)
        if heads:
            await ctx.heal(counters_per_head * heads * 10, target)
    return effect


def look_bottom_to_bench(count: int, predicate):
    """Look at the bottom `count` cards, put 1 matching Pokemon onto your
    Bench, then shuffle the rest back into your deck."""
    async def effect(ctx):
        deck = ctx.deck()
        bottom = deck[:count]
        if not bottom:
            return
        matches = [card for card in bottom if predicate(card)]
        picks = []
        if matches and len(ctx.my_bench()) < BENCH_CAPACITY:
            picks = await ctx.choose_cards(
                matches, 1, minimum=0,
                prompt="Put a Pokémon found there onto your Bench",
                display_cards=bottom if len(matches) < len(bottom) else None,
            )
        for card in picks:
            await ctx.bench_pokemon(card)
        await ctx.shuffle_deck()
    return effect


def look_bottom_to_hand(count: int, take: int, predicate):
    """Look at the bottom `count` cards, put `take` matching cards into your
    hand, and leave the rest on the bottom (Dusk Ball)."""
    async def effect(ctx):
        deck = ctx.deck()
        bottom = deck[:count]
        if not bottom:
            return
        matches = [card for card in bottom
                   if predicate is None or predicate(card)]
        picks = await ctx.choose_cards(
            matches, take, minimum=0,
            prompt="Choose a card from the bottom of your deck",
            display_cards=bottom if len(matches) < len(bottom) else None,
        )
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    return effect


def search_deck_or_discard_to_hand(predicate=None, count: int = 1):
    """Search your deck or your discard pile for up to `count` matching cards
    and put them into your hand."""
    async def effect(ctx):
        deck_matches = await ctx.search_deck(predicate, count=count, minimum=0,
                                             prompt="Choose cards from your deck")
        if deck_matches:
            await ctx.put_in_hand(deck_matches, reveal=True)
            await ctx.shuffle_deck()
        pool = [card for card in ctx.discard_pile()
                if predicate is None or predicate(card)]
        remaining = count - len(deck_matches)
        if pool and remaining > 0:
            picks = await ctx.choose_cards(
                pool, remaining, minimum=0,
                prompt="Choose cards from your discard pile")
            if picks:
                await ctx.put_in_hand(picks, reveal=True)
    return effect


def pokemon_lv_x():
    """Predicate: a Pokemon LV.X."""
    return pokemon_of_subtype("LV.X")


def discard_hand_draw(draw: int = 7):
    """Discard your whole hand, then draw `draw` cards (Professor Oak)."""
    async def effect(ctx):
        hand = ctx.hand()
        if hand:
            await ctx.discard_cards(hand)
        await ctx.draw_cards(draw)
    return effect


def reveal_until_pokemon_to_hand():
    """Reveal cards from the top of your deck until a Pokemon appears, put it
    into your hand, then shuffle the rest (Quick Ball)."""
    async def effect(ctx):
        deck = ctx.deck()
        for card in reversed(deck):
            if is_pokemon_card(card):
                await ctx.put_in_hand([card], reveal=True)
                break
        await ctx.shuffle_deck()
    return effect


def turn_damage_boost_per_prize(per: int):
    """During this turn, your Pokemon's attacks do `per` more damage to the
    opponent's Active for each Prize card the opponent has already taken
    (Iris)."""
    async def effect(ctx):
        area = ctx.board.find_player_area(ctx.opponent_id, "prizePile")
        remaining = len(area.children) if area is not None else 6
        taken = max(0, 6 - remaining)
        if taken <= 0:
            return
        ctx.add_turn_damage_modifier(TurnDamageModifier(
            per * taken, ctx.player_id, source_predicate=None))
    return effect


def rival_reveal(count: int = 5, take: int = 3):
    """Reveal the top `count` cards of your deck; your opponent chooses
    `take` of them for your hand, the rest go back on top (Rival)."""
    async def effect(ctx):
        top = ctx.deck_top(count)
        if not top:
            return
        picks = await ctx.choose_cards(
            top, take, minimum=take, player_id=ctx.opponent_id,
            prompt="Choose cards for your opponent's hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def keep_one_shuffle_rest_draw(draw: int):
    """Choose 1 card in your hand, shuffle the rest of your hand into your
    deck, then draw `draw` cards (Professor Rowan)."""
    async def effect(ctx):
        hand = ctx.hand()
        if not hand:
            return
        kept = await ctx.choose_cards(
            hand, 1, minimum=1, prompt="Choose a card to keep in your hand")
        rest = [c for c in hand if c not in kept]
        if rest:
            await ctx.shuffle_into_deck(rest)
        await ctx.draw_cards(draw)
    return effect


def discard_tool_or_special_energy(count: int = 1):
    """Discard `count` Pokemon Tool or Special Energy card attached to any
    Pokemon in play, yours or your opponent's (Xerosic)."""
    async def effect(ctx):
        cards = [card for card, _ in ctx.tools_in_play()]
        for pokemon in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
            cards += [e for e in ctx.attached_energies(pokemon) if is_special_energy(e)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, count, minimum=min(count, len(cards)),
            prompt="Choose a Pokémon Tool or Special Energy to discard")
        if picks:
            await ctx.discard_cards(picks)
    return effect


def confuse_both_actives(predicate=None):
    """Both Active Pokemon (that match) are now Confused (Dark Bell)."""
    async def effect(ctx):
        for pokemon in (ctx.my_active(), ctx.opponent_active()):
            if pokemon is not None and (predicate is None or predicate(pokemon)):
                await ctx.apply_special_condition(pokemon, SpecialConditions.CONFUSED)
    return effect


def heal_where(amount: int, where: str = "choice", predicate=None, min_energy: int = 0):
    """Heal `amount` from your matching Pokemon: "choice" (1 chosen), "active",
    "each_own", or "each_both" (every Pokemon in play, both sides)."""
    async def effect(ctx):
        if where == "active":
            pool = [ctx.my_active()]
        elif where == "each_both":
            pool = ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
        else:
            pool = ctx.my_pokemon_in_play()
        pool = [p for p in pool
                if p is not None and (predicate is None or predicate(p))
                and len(ctx.attached_energies(p)) >= min_energy
                and ctx.max_hp(p) > p.get_attribute(AttrID.HP, 0)]
        if not pool:
            return
        if where == "choice":
            target = await ctx.choose_pokemon(pool, "Choose a Pokémon to heal") \
                if len(pool) > 1 else pool[0]
            pool = [target] if target is not None else []
        for pokemon in pool:
            await ctx.heal(amount, pokemon)
    return effect


def discard_opponent_hand_to(keep: int):
    """Your opponent discards cards from their hand until they have `keep`
    cards left (Xerosic's Machinations)."""
    async def effect(ctx):
        hand = ctx.hand(ctx.opponent_id)
        excess = len(hand) - keep
        if excess <= 0:
            return
        await ctx.discard_from_hand(
            excess, minimum=excess, player_id=ctx.opponent_id,
            prompt=f"Discard down to {keep} cards")
    return effect


def mill_opponent_per_heads(coins: int, per: int = 2):
    """Flip `coins` coins; each heads puts `per` cards from the top of the
    opponent's deck into their discard pile (Team Rocket's Handiwork)."""
    async def effect(ctx):
        heads = sum(1 for face in await ctx.flip_coins(coins, title="Discard from the deck")
                    if face)
        if not heads:
            return
        top = ctx.deck_top(per * heads, ctx.opponent_id)
        if top:
            await ctx.discard_cards(top)
    return effect


def discard_tool_and_special_energy_from_opponent():
    """Discard a Pokemon Tool and a Special Energy from 1 of the opponent's
    Pokemon (Ruffian)."""
    async def effect(ctx):
        for pokemon in ctx.opponent_pokemon_in_play():
            tool = next((c for c in pokemon.children if is_tool_card(c)), None)
            energy = next((c for c in ctx.attached_energies(pokemon)
                           if is_special_energy(c)), None)
            if tool is not None and energy is not None:
                await ctx.discard_cards([tool, energy])
                return
    return effect


def super_potion(amount: int):
    """Heal `amount` from 1 of your Pokemon, then discard an Energy attached
    to it (Super Potion)."""
    async def effect(ctx):
        pool = [p for p in ctx.my_pokemon_in_play()
                if ctx.attached_energies(p)
                and ctx.max_hp(p) > p.get_attribute(AttrID.HP, 0)]
        if not pool:
            return
        target = await ctx.choose_pokemon(pool, "Choose a Pokémon to heal") \
            if len(pool) > 1 else pool[0]
        if target is None:
            return
        await ctx.heal(amount, target)
        energies = ctx.attached_energies(target)
        if not energies:
            return
        picks = await ctx.choose_cards(
            energies, 1, minimum=1, prompt="Choose an Energy to discard")
        if picks:
            await ctx.discard_cards(picks)
    return effect


def switch_then_optional_discard_heal(count: int, amount: int):
    """Switch your Active with a Benched Pokemon; you may discard `count`
    other cards from your hand to heal `amount` from the Pokemon that went to
    the Bench (Mallow & Lana)."""
    async def effect(ctx):
        bench = ctx.my_bench()
        active = ctx.my_active()
        if active is None or not bench:
            return
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon") \
            if len(bench) > 1 else bench[0]
        if target is None or not await ctx.switch_active(ctx.player_id, target):
            return
        picks = await ctx.discard_from_hand(
            count, minimum=0, prompt=f"Discard {count} cards to heal {amount} damage")
        if len(picks) == count:
            await ctx.heal(amount, active)
    return effect


def gust_bench_gx_ex(count: int = 1):
    """Switch `count` of the opponent's Benched Pokemon-GX or Pokemon-EX into
    their Active Spot (Great Catcher)."""
    async def effect(ctx):
        bench = [p for p in ctx.opponent_bench()
                 if is_pokemon_gx(p) or is_pokemon_ex(p)]
        if not bench or ctx.opponent_active() is None:
            return
        picks = await ctx.choose_cards(
            bench, count, minimum=min(count, len(bench)),
            prompt="Choose the opponent's new Active Pokémon")
        for card in picks:
            if not await ctx.switch_active(ctx.opponent_id, card):
                break
    return effect


def flip_draw(heads: int, tails: int, coins: int = 1):
    """Flip a coin: heads draws `heads`, tails draws `tails`."""
    async def effect(ctx):
        faces = await ctx.flip_coins(coins, title="Draw cards")
        await ctx.draw_cards(heads if faces and faces[0] else tails)
    return effect


def draw_then_opponent_discard(draw: int, count: int, random: bool = False):
    """Draw `draw` cards, then your opponent discards `count` cards from
    their hand; `random` picks them without their choice (Mars)."""
    async def effect(ctx):
        await ctx.draw_cards(draw)
        hand = ctx.hand(ctx.opponent_id)
        if not hand:
            return
        if random:
            await ctx.discard_cards(hand[:count])
            return
        await ctx.discard_from_hand(
            count, minimum=min(count, len(hand)), player_id=ctx.opponent_id,
            prompt=f"Discard {count} card(s) from your hand")
    return effect


def draw_then_flip_bonus(base: int, bonus: int, coins: int = 1):
    """Draw `base` cards, then flip a coin and draw `bonus` more on heads
    (Bug Catcher)."""
    async def effect(ctx):
        await ctx.draw_cards(base)
        if (await ctx.flip_coins(coins, title="Draw more cards"))[0]:
            await ctx.draw_cards(bonus)
    return effect


def draw_then_if_hand_at_least(base: int, threshold: int, bonus: int):
    """Draw `base` cards, then `bonus` more when your hand holds at least
    `threshold` cards (Billy & O'Nare)."""
    async def effect(ctx):
        await ctx.draw_cards(base)
        if len(ctx.hand()) >= threshold:
            await ctx.draw_cards(bonus)
    return effect


def draw_then_shuffle_hand(draw: int, count: int):
    """Draw `draw` cards, then shuffle `count` cards from your hand into your
    deck (Mary)."""
    async def effect(ctx):
        await ctx.draw_cards(draw)
        hand = ctx.hand()
        if not hand:
            return
        picks = await ctx.choose_cards(
            hand, count, minimum=min(count, len(hand)),
            prompt=f"Choose {count} card(s) to shuffle into your deck")
        if picks:
            await ctx.shuffle_into_deck(picks)
    return effect


def draw_then_opponent_may_draw(draw: int, count: int):
    """Draw `draw` cards; your opponent may then draw `count` (Fieldworker)."""
    async def effect(ctx):
        await ctx.draw_cards(draw)
        await ctx.draw_cards(count, ctx.opponent_id)
    return effect


def draw_per_subtype(subtype: str, per: int = 1, opponent: bool = False):
    """Draw `per` card for each Pokemon of the printed subtype in play, yours
    or the opponent's (Awakening Drum, Jett)."""
    async def effect(ctx):
        pool = ctx.opponent_pokemon_in_play() if opponent else ctx.my_pokemon_in_play()
        count = sum(1 for p in pool if subtype in subtypes_for(p.archetype_id))
        if count:
            await ctx.draw_cards(per * count)
    return effect


def draw_per_opponent_bench_basic(per: int = 1):
    """Draw `per` card for each of the opponent's Benched Basic Pokemon."""
    async def effect(ctx):
        count = sum(1 for p in ctx.opponent_bench() if is_basic_pokemon(p))
        if count:
            await ctx.draw_cards(per * count)
    return effect


def draw_if_same_active_type(base: int, bonus: int):
    """Draw `base` cards, plus `bonus` when both Active Pokemon share a type
    (Samson Oak)."""
    async def effect(ctx):
        mine, theirs = ctx.my_active(), ctx.opponent_active()
        same = (mine is not None and theirs is not None
                and set(mine.get_attribute(AttrID.POKEMON_TYPES) or [])
                & set(theirs.get_attribute(AttrID.POKEMON_TYPES) or []))
        await ctx.draw_cards(base + (bonus if same else 0))
    return effect


def draw_if_opponent_active(predicate, base: int, bonus: int):
    """Draw `base` cards, or `base + bonus` when the opponent's Active matches
    `predicate` (Norman)."""
    async def effect(ctx):
        active = ctx.opponent_active()
        await ctx.draw_cards(base + (bonus if active is not None and predicate(active) else 0))
    return effect


def draw_if_stadium(base: int, bonus: int):
    """Draw `base` cards, plus `bonus` while a Stadium is in play (Falkner)."""
    async def effect(ctx):
        await ctx.draw_cards(base + (bonus if ctx.stadium_in_play() is not None else 0))
    return effect


def draw_then_recover_basic_energy(draw: int, count: int = 1):
    """Draw `draw` cards, then put up to `count` basic Energy cards from your
    discard pile into your hand (Roark)."""
    async def effect(ctx):
        await ctx.draw_cards(draw)
        cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, count, minimum=0,
            prompt="Choose basic Energy cards to put into your hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    return effect


def draw_then_turn_boost(draw: int, amount: int):
    """Draw `draw` cards; this turn your Pokemon's attacks do `amount` more
    damage to the opponent's Active (Professor Kukui)."""
    async def effect(ctx):
        await ctx.draw_cards(draw)
        ctx.add_turn_damage_modifier(TurnDamageModifier(amount, ctx.player_id))
    return effect


def draw_from_bottom(count: int):
    """Draw `count` cards from the bottom of your deck (Looker)."""
    async def effect(ctx):
        deck = ctx.deck()
        if not deck:
            return
        picks = deck[-count:]
        for card in picks:
            await ctx.put_in_hand([card], reveal=False)
    return effect


def draw_until_opponent_hand():
    """Draw cards until your hand holds as many cards as your opponent's
    (Battle Reporter)."""
    async def effect(ctx):
        target = len(ctx.hand(ctx.opponent_id))
        if len(ctx.hand()) < target:
            await ctx.draw_until(target)
    return effect


def count_hand_shuffle_draw_plus(plus: int):
    """Count the cards in your hand, shuffle them into your deck, then draw
    that many plus `plus` (Brassius)."""
    async def effect(ctx):
        hand = ctx.hand()
        count = len(hand)
        if hand:
            await ctx.shuffle_into_deck(hand)
        await ctx.draw_cards(count + plus)
    return effect


def flip_top_or_bottom_draw(heads: int, tails: int):
    """Flip a coin: heads draws `heads` from the bottom of your deck, tails
    draws `tails` from the top (Professor Cozmo's Discovery)."""
    async def effect(ctx):
        if (await ctx.flip_coins(1, title="Draw from the bottom"))[0]:
            deck = ctx.deck()
            for card in deck[-heads:]:
                await ctx.put_in_hand([card], reveal=False)
        else:
            await ctx.draw_cards(tails)
    return effect


def hand_to_bottom_draw(count: int, draw: int):
    """Put `count` cards from your hand on the bottom of your deck, then draw
    `draw` (Kofu)."""
    async def effect(ctx):
        hand = ctx.hand()
        if len(hand) < count:
            return
        picks = await ctx.choose_cards(
            hand, count, minimum=count,
            prompt=f"Choose {count} cards to put on the bottom of your deck")
        if len(picks) < count:
            return
        for card in picks:
            await ctx.put_on_bottom_of_deck(card)
        await ctx.draw_cards(draw)
    return effect


def each_may_draw_up_to(count: int):
    """You may draw up to `count` cards, then your opponent may draw up to
    `count` (Erika)."""
    async def effect(ctx):
        for player_id in (ctx.player_id, ctx.opponent_id):
            picks = await ctx.choose_cards(
                ctx.deck_top(count, player_id), count, minimum=0,
                player_id=player_id, prompt=f"Choose up to {count} cards to draw")
            for card in picks:
                await ctx.put_in_hand([card], reveal=False)
    return effect


def flip_search_per_head(coins: int, predicate=None, per: int = 1, both: bool = False):
    """Flip `coins` coins; each heads searches the deck for `per` matching
    cards into hand (Timer Ball, Energy Ark); `both` requires every coin to
    come up heads (Delivery Drone)."""
    async def effect(ctx):
        faces = await ctx.flip_coins(coins, title="Search your deck")
        heads = sum(1 for face in faces if face)
        if both:
            if heads != coins:
                return
            wanted = per
        else:
            wanted = heads * per
        if wanted <= 0:
            return
        picks = await ctx.search_deck(
            predicate, count=wanted, minimum=0,
            prompt="Choose cards to put into your hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def reveal_hand_to_top_then_search(put_predicate, find_predicate):
    """Put a matching card from your hand on top of your deck, then search the
    deck for a matching card into your hand (Pokemon Communication)."""
    async def effect(ctx):
        hand = [c for c in ctx.hand() if put_predicate(c)]
        if not hand:
            return
        picks = await ctx.choose_cards(
            hand, 1, minimum=1, prompt="Choose a Pokémon to put on top of your deck")
        if not picks:
            return
        for card in picks:
            await ctx.put_on_top_of_deck(card)
        found = await ctx.search_deck(
            find_predicate, count=1, minimum=0,
            prompt="Choose a Pokémon to put into your hand")
        if found:
            await ctx.put_in_hand(found, reveal=True)
        await ctx.shuffle_deck()
    return effect


def search_two_kinds_to_bench(ex_count: int, plain_count: int):
    """Search the deck for Pokemon onto the Bench: `ex_count` Pokemon ex, or
    `plain_count` Pokemon that aren't ex (Brigette)."""
    async def effect(ctx):
        space = BENCH_CAPACITY - len(ctx.my_bench())
        if space <= 0:
            return
        ex_picks = await ctx.search_deck(
            is_pokemon_ex, count=min(ex_count, space), minimum=0,
            prompt=f"Choose up to {ex_count} Pokémon ex for your Bench")
        benched = 0
        for card in ex_picks:
            if await ctx.bench_pokemon(card):
                benched += 1
        space -= benched
        if space > 0:
            plain = await ctx.search_deck(
                excluding(is_pokemon_ex), count=min(plain_count, space), minimum=0,
                prompt=f"Choose up to {plain_count} Basic Pokémon for your Bench")
            for card in plain:
                if await ctx.bench_pokemon(card):
                    break
        await ctx.shuffle_deck()
    return effect


def each_player_count_shuffle_draw():
    """Each player counts their hand, shuffles it into their deck, and draws
    that many cards (Wicke)."""
    async def effect(ctx):
        for player_id in ctx.board.player_ids:
            count = len(ctx.hand(player_id))
            if count:
                await ctx.shuffle_into_deck(ctx.hand(player_id), player_id)
                await ctx.draw_cards(count, player_id)
    return effect


def opponent_hand_trainer_to_deck(count: int = 1):
    """Look at the opponent's hand and shuffle `count` Trainer cards from it
    into their deck (Rocket's Sneak Attack)."""
    async def effect(ctx):
        hand = ctx.hand(ctx.opponent_id)
        await ctx.reveal_hand(ctx.opponent_id)
        trainers = [c for c in hand if is_trainer_card(c)]
        if not trainers:
            return
        picks = await ctx.choose_cards(
            trainers, count, minimum=min(count, len(trainers)),
            prompt="Choose Trainer cards to shuffle into their deck")
        if picks:
            await ctx.shuffle_into_deck(picks, ctx.opponent_id)
    return effect


def move_energy_special_between_opponents(count: int = 1):
    """Move `count` Special Energy from 1 of the opponent's Pokemon to another
    of their Pokemon (Eneporter)."""
    async def effect(ctx):
        pool = ctx.opponent_pokemon_in_play()
        sources = [p for p in pool
                   if any(is_special_energy(e) for e in ctx.attached_energies(p))]
        if not sources:
            return
        source = await ctx.choose_pokemon(
            sources, "Choose a Pokémon with Special Energy") \
            if len(sources) > 1 else sources[0]
        if source is None:
            return
        energies = [e for e in ctx.attached_energies(source) if is_special_energy(e)]
        picks = await ctx.choose_cards(
            energies, count, minimum=min(count, len(energies)),
            prompt="Choose Special Energy to move")
        targets = [p for p in pool if p is not source]
        if not picks or not targets:
            return
        dest = await ctx.choose_pokemon(
            targets, "Choose a Pokémon to move the Energy to") or targets[0]
        for card in picks:
            await ctx.attach_energy(card, dest)
    return effect


def move_energy_from_holder(predicate, count: int = 2):
    """Move up to `count` Energy from 1 of your (matching) Pokemon to another
    of your Pokemon (Tag Switch)."""
    async def effect(ctx):
        pool = [p for p in ctx.my_pokemon_in_play()
                if ctx.attached_energies(p) and (predicate is None or predicate(p))]
        if not pool:
            return
        source = await ctx.choose_pokemon(
            pool, "Choose a Pokémon to move Energy from") \
            if len(pool) > 1 else pool[0]
        if source is None:
            return
        energies = ctx.attached_energies(source)
        picks = await ctx.choose_cards(
            energies, count, minimum=0,
            prompt=f"Choose up to {count} Energy to move")
        targets = [p for p in ctx.my_pokemon_in_play() if p is not source]
        if not picks or not targets:
            return
        dest = await ctx.choose_pokemon(
            targets, "Choose a Pokémon to move the Energy to") or targets[0]
        for card in picks:
            await ctx.attach_energy(card, dest)
    return effect


def both_shuffle_trainers_into_decks():
    """You and your opponent show hands, then shuffle every Trainer card from
    those hands into your decks (Lass)."""
    async def effect(ctx):
        for player_id in ctx.board.player_ids:
            trainers = [c for c in ctx.hand(player_id) if is_trainer_card(c)]
            if trainers:
                await ctx.shuffle_into_deck(trainers, player_id)
    return effect


def opponent_active_energy_to_deck_top(count: int = 1):
    """Put `count` Energy from the opponent's Active Pokemon on top of their
    deck (Nita)."""
    async def effect(ctx):
        active = ctx.opponent_active()
        if active is None:
            return
        energies = ctx.attached_energies(active)
        if not energies:
            return
        picks = await ctx.choose_cards(
            energies, count, minimum=min(count, len(energies)),
            prompt="Choose Energy to put on top of their deck")
        for card in picks:
            await ctx.put_on_top_of_deck(card)
    return effect


def evolve_from_deck_matching(predicate=None, exclude=None):
    """Search your deck for a card that evolves from 1 of your Pokemon, put it
    onto that Pokemon to evolve it, then shuffle (Evosoda shapes)."""
    from ptcgo.game.content.definitions import evolves_from

    async def effect(ctx):
        pool = ctx.my_pokemon_in_play()
        if not pool:
            return
        target = await ctx.choose_pokemon(
            pool, "Choose a Pokémon to evolve") if len(pool) > 1 else pool[0]
        if target is None:
            return
        logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)

        def eligible(card):
            if predicate is not None and not predicate(card):
                return False
            if exclude is not None and exclude(card):
                return False
            return bool(logic_name) and evolves_from(
                getattr(card, "archetype_id", None) or "", logic_name)

        picks = await ctx.search_deck(
            eligible, count=1, minimum=0,
            prompt="Choose an Evolution card for this Pokémon")
        if picks:
            await ctx.evolve_pokemon(target, picks[0])
        await ctx.shuffle_deck()
    return effect


def search_distinct_types(predicate, count: int, to_bench: bool = False):
    """Search the deck for up to `count` matching cards of different types
    (Lady Outing, Professor Oak's Setup)."""
    async def effect(ctx):
        remaining = count
        taken: List = []
        while remaining > 0:
            used = {frozenset(c.get_attribute(AttrID.POKEMON_TYPES) or []) for c in taken}
            pool = [c for c in ctx.deck() if predicate(c)
                    and frozenset(c.get_attribute(AttrID.POKEMON_TYPES) or []) not in used]
            if not pool:
                break
            picks = await ctx.choose_cards(
                pool, 1, minimum=0, ordered=False,
                prompt="Choose cards of different types")
            if not picks:
                break
            taken.extend(picks)
            remaining -= 1
        if not taken:
            return
        if to_bench:
            for card in taken:
                await ctx.bench_pokemon(card)
        else:
            await ctx.put_in_hand(taken, reveal=True)
        await ctx.shuffle_deck()
    return effect


def discard_typed_from_hand_then(predicate, count: int, inner):
    """Discard `count` matching cards from your hand, then run `inner`
    (Scorched Earth, Prism Tower, Cycling Road)."""
    async def effect(ctx):
        hand = [c for c in ctx.hand() if predicate is None or predicate(c)]
        if len(hand) < count:
            return
        picks = await ctx.choose_cards(
            hand, count, minimum=count, prompt=f"Discard {count} card(s) from your hand")
        if len(picks) < count:
            return
        await ctx.discard_cards(picks)
        await inner(ctx)
    return effect


def switch_typed_active(predicate):
    """Switch your Active Pokemon for a Benched one of the same kind
    (Surfing Beach)."""
    async def effect(ctx):
        active = ctx.my_active()
        if active is None or not predicate(active):
            return
        bench = [p for p in ctx.my_bench() if predicate(p)]
        if not bench:
            return
        target = await ctx.choose_pokemon(
            bench, "Choose your new Active Pokémon") if len(bench) > 1 else bench[0]
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    return effect


def move_energy_of_type_between(*types):
    """Move 1 matching Energy from 1 of your Pokemon to another of your Pokemon
    (Stark Mountain)."""
    wanted = {POKEMON_TYPE_NAMES[name] for name in types}

    async def effect(ctx):
        pool = [p for p in ctx.my_pokemon_in_play()
                if any(wanted & set(e.get_attribute(AttrID.POKEMON_TYPES) or [])
                       for e in ctx.attached_energies(p))]
        if not pool:
            return
        source = await ctx.choose_pokemon(
            pool, "Choose a Pokémon to move Energy from") \
            if len(pool) > 1 else pool[0]
        if source is None:
            return
        energies = [e for e in ctx.attached_energies(source)
                    if wanted & set(e.get_attribute(AttrID.POKEMON_TYPES) or [])]
        picks = await ctx.choose_cards(
            energies, 1, minimum=1, prompt="Choose an Energy to move")
        targets = [p for p in ctx.my_pokemon_in_play() if p is not source]
        if not picks or not targets:
            return
        dest = await ctx.choose_pokemon(
            targets, "Choose a Pokémon to move the Energy to") or targets[0]
        await ctx.attach_energy(picks[0], dest)
    return effect


def hand_card_to_top():
    """Put 1 card from your hand on top of your deck (Academy at Night)."""
    async def effect(ctx):
        hand = ctx.hand()
        if not hand:
            return
        picks = await ctx.choose_cards(
            hand, 1, minimum=1, prompt="Choose a card to put on top of your deck")
        if picks:
            await ctx.put_on_top_of_deck(picks[0])
    return effect


def flip_until_tails_draw(per: int = 1):
    """Flip coins until tails; draw `per` card for each heads (Speed
    Stadium)."""
    async def effect(ctx):
        heads = 0
        while True:
            if not (await ctx.flip_coins(1, title="Draw for each heads"))[0]:
                break
            heads += 1
            if heads > 20:
                break
        if heads:
            await ctx.draw_cards(per * heads)
    return effect


def draw_after(count: int, inner):
    """Run `inner`, then draw `count` cards."""
    async def effect(ctx):
        await inner(ctx)
        await ctx.draw_cards(count)
    return effect


def discard_after(count: int, inner):
    """Run `inner`, then discard `count` cards from your hand."""
    async def effect(ctx):
        await inner(ctx)
        await ctx.discard_from_hand(
            count, minimum=min(count, len(ctx.hand())),
            prompt=f"Discard {count} card(s) from your hand")
    return effect


def shuffle_random_from_opponent_hand(count: int):
    """Choose `count` random cards from the opponent's hand; they shuffle them
    into their deck (The Rocket's Trap, Hooligans Jim & Cas)."""
    async def effect(ctx):
        hand = ctx.hand(ctx.opponent_id)
        if not hand:
            return
        picks = hand[:count]
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)
    return effect


def each_player_shuffle_discard_into_deck(exclude_source: bool = True):
    """Each player shuffles their discard pile into their deck (Lysandre's
    Trump Card); `exclude_source` keeps the card being played out of it."""
    async def effect(ctx):
        source = getattr(ctx, "source", None) if exclude_source else None
        for player_id in ctx.board.player_ids:
            area = ctx.board.find_player_area(player_id, "discardPile")
            cards = [c for c in (area.children if area is not None else [])
                     if source is None or c.entity_id != source.entity_id]
            if cards:
                await ctx.shuffle_into_deck(list(cards), player_id)
    return effect


def search_one_of_each(kinds, draw_only: bool = False):
    """Search the deck for 1 card of each named kind and put them into your
    hand (Castaway, Cyrus's Conspiracy)."""
    async def effect(ctx):
        taken = []
        for predicate in kinds:
            picks = await ctx.search_deck(
                predicate, count=1, minimum=0,
                prompt="Choose a card to put into your hand")
            taken.extend(picks)
        if taken:
            await ctx.put_in_hand(taken, reveal=True)
        await ctx.shuffle_deck()
    return effect


def search_going_second(predicate, count: int, bigger: int):
    """Search the deck for `count` matching cards into hand — or `bigger` when
    you went second and this is your first turn (Jasmine, Energy Spinner)."""
    async def effect(ctx):
        turn_state = getattr(ctx.board, "turn_state", None)
        first_turn = turn_state is not None and turn_state.turn_number <= 2
        picks = await ctx.search_deck(
            predicate, count=bigger if first_turn else count, minimum=0,
            prompt="Choose cards to put into your hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def flip_recover_discard(coins: int, predicate=None, per: int = 1):
    """Flip `coins` coins; each heads takes `per` matching card from the
    discard pile into your hand (Lure Ball)."""
    async def effect(ctx):
        heads = sum(1 for face in await ctx.flip_coins(coins, title="Recover from the discard pile")
                    if face)
        if heads <= 0:
            return
        cards = [c for c in ctx.discard_pile()
                 if predicate is None or predicate(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, heads * per, minimum=0,
            prompt="Choose cards to put into your hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    return effect


def top_card_energy_attach():
    """Reveal the top card of your deck; if it is a basic Energy card, attach
    it to 1 of your Pokemon, otherwise put it back (Ether)."""
    async def effect(ctx):
        top = ctx.deck_top(1)
        if not top:
            return
        card = top[0]
        if not is_basic_energy_card(card):
            return
        pool = ctx.my_pokemon_in_play()
        if not pool:
            return
        target = await ctx.choose_pokemon(
            pool, "Choose a Pokémon to attach the Energy to") \
            if len(pool) > 1 else pool[0]
        if target is not None:
            await ctx.attach_energy(card, target)
    return effect


def discard_own_energy_opponent_two():
    """Discard an Energy attached to 1 of your Pokemon, then discard up to 2
    Energy from 1 of the opponent's Pokemon (Super Energy Removal)."""
    async def effect(ctx):
        mine = [p for p in ctx.my_pokemon_in_play() if ctx.attached_energies(p)]
        if not mine:
            return
        source = await ctx.choose_pokemon(
            mine, "Choose a Pokémon to discard Energy from") \
            if len(mine) > 1 else mine[0]
        if source is None:
            return
        picks = await ctx.choose_cards(
            ctx.attached_energies(source), 1, minimum=1,
            prompt="Discard an Energy card from your Pokémon")
        if picks:
            await ctx.discard_cards(picks)
        await discard_opponent_energy(2)(ctx)
    return effect


def both_sides_switch():
    """Your opponent switches their Active for a Benched Pokemon, then you
    switch yours (Warp Point)."""
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if bench and ctx.opponent_active() is not None:
            target = await ctx.choose_pokemon(
                bench, "Choose your new Active Pokémon",
                player_id=ctx.opponent_id) or bench[0]
            await ctx.switch_active(ctx.opponent_id, target)
        mine = ctx.my_bench()
        if mine and ctx.my_active() is not None:
            target = await ctx.choose_pokemon(
                mine, "Choose your new Active Pokémon") if len(mine) > 1 else mine[0]
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)
    return effect


def look_top_discard_rest_back(count: int, discard_max=None):
    """Look at the top `count` cards, discard any number of them, and put the
    rest back on top in any order (Raifort)."""
    async def effect(ctx):
        top = ctx.deck_top(count)
        if not top:
            return
        picks = await ctx.choose_cards(
            top, discard_max or count, minimum=0,
            prompt="Choose any number of cards to discard")
        if picks:
            await ctx.discard_cards(picks)
    return effect


def flip_heal_cure(predicate, amount: int, coins: int = 1):
    """Flip a coin; on heads heal `amount` and remove all Special Conditions
    from 1 of your (matching) Pokemon (Life Herb)."""
    async def effect(ctx):
        if not (await ctx.flip_coins(coins, title="Heal a Pokémon"))[0]:
            return
        pool = [p for p in ctx.my_pokemon_in_play()
                if predicate is None or predicate(p)]
        if not pool:
            return
        target = await ctx.choose_pokemon(
            pool, "Choose a Pokémon to heal") if len(pool) > 1 else pool[0]
        if target is None:
            return
        await ctx.heal(amount, target)
        await ctx.cure_all_conditions(target)
    return effect


def search_top_energy_attach(count: int, predicate=None):
    """Look at the top `count` cards and attach 1 matching Energy card you find
    there to 1 of your Pokemon, then shuffle the rest back (Waitress)."""
    async def effect(ctx):
        top = ctx.deck_top(count)
        if not top:
            return
        matches = [c for c in top
                   if (predicate or is_basic_energy_card)(c)]
        if matches:
            picks = await ctx.choose_cards(
                matches, 1, minimum=0,
                prompt="Choose an Energy card to attach",
                display_cards=top)
            if picks:
                pool = ctx.my_pokemon_in_play()
                if pool:
                    target = await ctx.choose_pokemon(
                        pool, "Choose a Pokémon to attach the Energy to") \
                        if len(pool) > 1 else pool[0]
                    if target is not None:
                        await ctx.attach_energy(picks[0], target)
        await ctx.shuffle_deck()
    return effect


def flip_both_recover(heads_predicate, tails_predicate):
    """Flip 2 coins: both heads recovers a `heads_predicate` card from the
    discard pile, both tails a `tails_predicate` one (Old Rod)."""
    async def effect(ctx):
        faces = await ctx.flip_coins(2, title="Recover from the discard pile")
        predicate = heads_predicate if all(faces) else (
            tails_predicate if not any(faces) else None)
        if predicate is None:
            return
        cards = [c for c in ctx.discard_pile() if predicate(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, 1, minimum=0, prompt="Choose a card to put into your hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    return effect


def search_for_shared_name(count: int, need: int):
    """Reveal the top `count` cards; if at least `need` share a name, put all
    cards with that name into your hand (Arcade Game)."""
    async def effect(ctx):
        await ctx.shuffle_deck()
        top = ctx.deck_top(count)
        names = {}
        for card in top:
            key = getattr(card, "archetype_id", None) or card.entity_id
            names.setdefault(key, []).append(card)
        best = max(names.values(), key=len) if names else []
        if len(best) >= need:
            await ctx.put_in_hand(best, reveal=True)
        await ctx.shuffle_deck()
    return effect


def search_and_discard(count: int, predicate=None):
    """Search your deck for up to `count` matching cards and discard them, then
    shuffle (Battle Compressor)."""
    async def effect(ctx):
        picks = await ctx.search_deck(
            predicate, count=count, minimum=0,
            prompt=f"Choose up to {count} cards to discard")
        if picks:
            await ctx.discard_cards(picks)
        await ctx.shuffle_deck()
    return effect


def move_all_energy_named(word: str):
    """Move every Energy from 1 of your Pokemon named `word` to another of them
    (Sabrina)."""
    def named_holder(pokemon):
        return pokemon_named(word)(pokemon)

    async def effect(ctx):
        sources = [p for p in ctx.my_pokemon_in_play()
                   if named_holder(p) and ctx.attached_energies(p)]
        if not sources:
            return
        source = await ctx.choose_pokemon(
            sources, "Choose a Pokémon to move Energy from") \
            if len(sources) > 1 else sources[0]
        targets = [p for p in ctx.my_pokemon_in_play()
                   if named_holder(p) and p is not source]
        if source is None or not targets:
            return
        dest = await ctx.choose_pokemon(
            targets, "Choose a Pokémon to move the Energy to") or targets[0]
        for card in list(ctx.attached_energies(source)):
            await ctx.attach_energy(card, dest)
    return effect


def opponent_discard_to_hand(count: int = 1):
    """Put `count` cards from the opponent's discard pile into their hand
    (Surprise Box)."""
    async def effect(ctx):
        area = ctx.board.find_player_area(ctx.opponent_id, "discardPile")
        cards = list(area.children) if area is not None else []
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, count, minimum=min(count, len(cards)),
            prompt="Choose cards to put into your opponent's hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
    return effect


def heal_active_or(predicate, base: int, better: int):
    """Heal `base` from your Active Pokemon, or `better` when it matches
    `predicate` (Arven's Sandwich)."""
    async def effect(ctx):
        active = ctx.my_active()
        if active is None:
            return
        await ctx.heal(better if predicate(active) else base, active)
    return effect


def stadium_retreat_discount_typed(*types):
    """Pokemon of the named types pay less to retreat (High Pressure System)."""
    wanted = [POKEMON_TYPE_NAMES[name] for name in types]
    return retreat_discount(
        len(types),
        target_pred=lambda target, carrier: bool(
            set(wanted) & set(target.get_attribute(AttrID.POKEMON_TYPES) or [])))
