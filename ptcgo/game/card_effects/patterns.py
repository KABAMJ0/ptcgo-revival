"""Wording-driven attack/ability effects for Pokemon card scripts.

Card scripts stay thin data definitions, and most Pokemon attack and ability
texts in the 19k-card catalogue are one of a few hundred recurring phrasings
("Flip a coin. If heads, the Defending Pokemon is now Paralyzed.", "This
attack does 20 damage times the number of heads."). This module maps that
wording onto the shared factories in `attacks_common` / `support_common` /
`passives_common` at load time, so one pattern covers every card printed with
it instead of one hand-written coroutine per card.

`bind(ability)` only ever replaces the `unimplemented` marker: a card whose
script already carries a real effect is never touched, which is why this can
add coverage without changing behaviour that already worked.

Every pattern is a full match on the normalized text (lowercase, ASCII,
collapsed whitespace), so a text that merely contains a familiar phrase can
never be bound to the wrong shape.
"""

import json
import random
import re
import unicodedata
from typing import Callable, List, Optional, Tuple

from ptcgo.game.attributes import (
    AttrID, CLIENT_SPECIAL_CONDITION_NAMES, PokemonTypes, SpecialConditions,
    TrainerType,
)
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.attacks_common import (
    bonus_if,
    energy_move_attack,
    condition_attack,
    count_bench,
    count_discard,
    count_energy,
    count_hand,
    count_in_play,
    count_prizes_remaining,
    count_prizes_taken,
    damage_all_opponents,
    defender_is_evolved,
    self_has_energy_of_type,
    has_damage,
    defender_retreat_cost,
    evolve_from_deck_attack,
    discard_stadium_attack,
    lock_chosen_defender_attack,
    reveal_hand_attack,
    damage_per,
    damage_counters_on,
    defender_has_condition,
    discard_opponent_energy_attack,
    discard_random_hand_attack,
    energy_move_attack,
    flip_bonus,
    flip_choice,
    flip_damage,
    flip_defender_lock_attack,
    flip_gate,
    flip_or_nothing,
    hand_sizes_equal,
    heal_dealt_attack,
    ignore_modifier_attack,
    lock_self_attack,
    mill_attack,
    no_retreat_attack,
    place_counters,
    recoil_attack,
    self_energy_discard_attack,
    smokescreen_attack,
    snipe_attack,
    spread_damage,
)
from ptcgo.game.card_effects.passives_common import (
    boost_own_next_turn,
    debuff_defender_attacks,
    carrier_pokemon,
    no_energy_free_retreat_passive,
    opponent_retreat_tax_passive,
    active_vs_active_debuff_passive,
    benched_full_shield_passive,
    condition_immunity_passive,
    opponent_attack_tax,
    guts_survive_passive,
    retreat_discount,
    typed_energy_free_retreat_passive,
    no_retreat_passive,
    hp_per_typed_energy_passive,
    team_damage_boost_passive,
    additive_damage_taken_passive,
    retaliate_counters_passive,
    retreat_free_when,
    flip_prevent_damage_passive,
    is_in_active_spot,
    prevent_damage_when,
    flip_protection,
    no_resistance_passive,
    no_weakness_passive,
    protect_next_turn,
    takes_less_passive,
)
from ptcgo.game.card_effects.trainers import (
    is_basic_energy_card, is_energy_card, is_tool_card,
)
from ptcgo.game.card_effects.support_common import (
    cure_conditions_effect,
    opponent_switches,
    discard_then_draw,
    attach_from_discard,
    draw_attack,
    remove_self_from_play,
    recover_from_discard,
    search_attach_energy,
    shuffle_hand_into_deck_draw,
    draw_until_effect,
    gust_attack,
    heal_attack,
    heal_targets,
    is_basic,
    distribute_energy,
    search_to_bench,
    search_to_hand,
    switch_self_attack,
)
from ptcgo.game.data_utils import (
    Activations, Attack, EnergyCardDef, PokemonCardDef, Triggers, def_for,
    unimplemented,
)
from ptcgo.game.session.effects import is_special_energy
from ptcgo.game.session.passives import Passive

CONDITIONS = {
    "asleep": SpecialConditions.ASLEEP,
    "burned": SpecialConditions.BURNED,
    "confused": SpecialConditions.CONFUSED,
    "paralyzed": SpecialConditions.PARALYZED,
    "poisoned": SpecialConditions.POISONED,
}
_CONDITION_WORDS = "|".join(CONDITIONS)

TYPE_WORDS = {
    "colorless": PokemonTypes.COLORLESS,
    "darkness": PokemonTypes.DARKNESS,
    "dragon": PokemonTypes.DRAGON,
    "fairy": PokemonTypes.FAIRY,
    "fighting": PokemonTypes.FIGHTING,
    "fire": PokemonTypes.FIRE,
    "grass": PokemonTypes.GRASS,
    "lightning": PokemonTypes.LIGHTNING,
    "metal": PokemonTypes.METAL,
    "psychic": PokemonTypes.PSYCHIC,
    "water": PokemonTypes.WATER,
}
_TYPE_WORDS = "|".join(TYPE_WORDS)

# "1 of your opponent's Benched Pokemon" / "that Pokemon" tails.
# "this Pokemon" or the attacker's own printed name (old wording), never a
# phrase naming another Pokemon.
_SELF_NAME = (r"(?:this pokemon|(?!the |your |each |that |all |any )"
              r"[a-z][\w' -]*)")
_SNIPE_TAIL = (r"\. \(don't apply weakness and resistance for benched pokemon\.\)")
_BENCH_SPREAD_TAIL = _SNIPE_TAIL


def normalize(text: Optional[str]) -> str:
    """Lowercase ASCII with single spaces: the form every pattern matches."""
    value = unicodedata.normalize("NFKD", text or "")
    value = value.encode("ascii", "ignore").decode()
    value = value.replace("\u2019", "'").replace("\u2018", "'")
    return re.sub(r"\s+", " ", value.strip().lower())


def _count(word: Optional[str]) -> int:
    """'a'/'an' -> 1, 'all' -> 99, digits as written."""
    if word in (None, "", "a", "an"):
        return 1
    if word == "all":
        return 99
    return int(word)


async def _discard_defender_energy(ctx, count: int = 1, special_only: bool = False):
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, count, predicate=is_special_energy if special_only else None,
        prompt="Choose Energy to discard from the Defending Pokémon")


# ----------------------------------------------------------------------
# Builders (regex match -> async effect)
# ----------------------------------------------------------------------

def _flip_heads_damage(m, ability):
    return flip_bonus(int(m.group(1)))


def _flip_tails_nothing(m, ability):
    return flip_or_nothing()


def _flip_all_heads_nothing(m, ability):
    return flip_or_nothing(coins=_count(m.group(1)))


def _flip_damage_times_heads(m, ability):
    return flip_damage(coins=_count(m.group(1)), per_heads=int(m.group(2)))


def _flip_damage_per_heads(m, ability):
    return flip_damage(coins=_count(m.group(1)), per_heads=int(m.group(2)))


def _flip_until_tails_times(m, ability):
    return flip_damage(until_tails=True, per_heads=int(m.group(1)))


def _flip_until_tails_bonus(m, ability):
    return flip_damage(until_tails=True, bonus_per_heads=int(m.group(1)))


def _flip_bonus_per_heads(m, ability):
    return flip_damage(coins=_count(m.group(1)),
                       bonus_per_heads=int(m.group(2)))


def _flip_plus_bonus(m, ability):
    return flip_damage(base=int(m.group(1)), bonus=int(m.group(2)))


def _flip_heads_plus_bonus_per_heads(m, ability):
    return flip_damage(coins=_count(m.group(1)), base=int(m.group(2)),
                       bonus_per_heads=int(m.group(3)))


def _flip_choice_damage(m, ability):
    return flip_choice(int(m.group(1)) + int(m.group(2)), int(m.group(3)))


def _flip_condition(m, ability):
    return condition_attack(CONDITIONS[m.group(1)], flip=True)


def _condition(m, ability):
    return condition_attack(CONDITIONS[m.group(1)])


def _two_conditions(m, ability):
    return condition_attack(CONDITIONS[m.group(1)], CONDITIONS[m.group(2)])


def _self_condition(m, ability):
    return condition_attack(self_conditions=(CONDITIONS[m.group(1)],))


def _poison_counters(m, ability):
    return condition_attack(SpecialConditions.POISONED, counters=int(m.group(1)))


def _recoil(m, ability):
    return recoil_attack(int(m.group(1)))


def _flip_tails_recoil(m, ability):
    return flip_damage(tails_self_damage=int(m.group(1)))


def _heal_self(m, ability):
    return heal_attack(amount=int(m.group(1)), target="self")


def _heal_each_own(m, ability):
    return heal_targets(int(m.group(1)), scope="each_own")


def _heal_choice(m, ability):
    return heal_targets(int(m.group(1)), scope="choice")


def _heal_dealt(m, ability):
    return heal_dealt_attack()


def _draw(m, ability):
    return draw_attack(_count(m.group(1) if m.groups() else None))


def _draw_until(m, ability):
    return draw_until_effect(int(m.group(1)))


def _mill_opponent(m, ability):
    return mill_attack(_count(m.group(1)))


def _mill_own(m, ability):
    return mill_attack(_count(m.group(1)), opponent=False)


def _self_energy_discard(m, ability):
    return self_energy_discard_attack(count=_count(m.group(1)))


def _self_energy_discard_type(m, ability):
    return self_energy_discard_attack(
        count=_count(m.group(1)), energy_type=TYPE_WORDS[m.group(2)])


def _self_energy_discard_all(m, ability):
    return self_energy_discard_attack(all_energy=True)


def _defender_energy_discard(m, ability):
    return discard_opponent_energy_attack(count=_count(m.group(1)))


def _defender_special_energy_discard(m, ability):
    count = _count(m.group(1)) if m.groups() else 1
    return discard_opponent_energy_attack(count=count, special_only=True)


def _flip_defender_energy_discard(m, ability):
    count = _count(m.group(1))

    async def discard(ctx):
        await _discard_defender_energy(ctx, count)
    return flip_gate(discard)


def _flip_defender_special_energy_discard(m, ability):
    async def discard(ctx):
        await _discard_defender_energy(ctx, 1, special_only=True)
    return flip_gate(discard)


def _snipe(m, ability):
    return snipe_attack(int(m.group(1)), pool="any", count=_count(m.group(2)))


def _snipe_choose(m, ability):
    return snipe_attack(int(m.group(2)), pool="any", count=_count(m.group(1)))


def _snipe_bench(m, ability):
    return snipe_attack(int(m.group(1)), pool="bench", count=_count(m.group(2)))


def _snipe_bench_also_base(m, ability):
    return snipe_attack(int(m.group(1)), pool="bench", count=_count(m.group(2)),
                        also_base=True)


def _spread_opponent(m, ability):
    return damage_all_opponents(int(m.group(1)))


def _spread_opponent_bench_also_base(m, ability):
    return spread_damage(int(m.group(1)), side="opponent", also_base=True)


def _spread_opponent_bench(m, ability):
    return spread_damage(int(m.group(1)), side="opponent")


def _spread_own_bench(m, ability):
    return spread_damage(int(m.group(1)), side="mine")


def _spread_both_benches(m, ability):
    return spread_damage(int(m.group(1)), side="both")


def _lock_self(m, ability):
    return lock_self_attack()


def _no_retreat(m, ability):
    return no_retreat_attack()


def _flip_defender_lock(m, ability):
    return flip_defender_lock_attack()


def _smokescreen(m, ability):
    return smokescreen_attack()


def _ignore_resistance(m, ability):
    return ignore_modifier_attack(ignore_resistance=True)


def _ignore_weakness_and_resistance(m, ability):
    return ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True)


def _ignore_target_effects(m, ability):
    return ignore_modifier_attack(ignore_target_effects=True)


def _ignore_all(m, ability):
    return ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True,
                                  ignore_target_effects=True)


def _take_less(m, ability):
    return protect_next_turn(reduce=int(m.group(1)))


def _flip_prevent(m, ability):
    return flip_protection(prevent=True)


def _flip_prevent_all(m, ability):
    return flip_protection(prevent=True, effects_too=True)


def _more(count_fn, ability, per):
    """"This attack does N more damage for each ...": printed damage plus per*count."""
    return damage_per(count_fn, per, base=getattr(ability, "damage", 0) or 0)


def _more_per_energy_self(m, ability):
    return _more(count_energy("self"), ability, int(m.group(1)))


def _more_per_energy_self_type(m, ability):
    return _more(count_energy("self", TYPE_WORDS[m.group(2)]), ability,
                 int(m.group(1)))


def _more_per_energy_defender(m, ability):
    return _more(count_energy("defender"), ability, int(m.group(1)))


def _more_per_counter_self(m, ability):
    return _more(damage_counters_on("self"), ability, int(m.group(1)))


def _more_per_counter_defender(m, ability):
    return _more(damage_counters_on("defender"), ability, int(m.group(1)))


def _more_per_bench(m, ability):
    return _more(count_bench("opponent"), ability, int(m.group(1)))


def _more_per_prizes_taken(m, ability):
    return _more(count_prizes_taken("opponent"), ability, int(m.group(1)))


def _damage_per_counter_self(m, ability):
    return damage_per(damage_counters_on("self"), int(m.group(1)), base=0)


def _bonus_condition(m, ability):
    return bonus_if(defender_has_condition(CONDITIONS[m.group(1)]),
                    int(m.group(2)))


def _bonus_stadium(m, ability):
    from ptcgo.game.card_effects.attacks_common import stadium_in_play_cond
    return bonus_if(stadium_in_play_cond, int(m.group(1)))


def _bonus_hand_equal(m, ability):
    from ptcgo.game.card_effects.attacks_common import hand_sizes_equal
    return bonus_if(hand_sizes_equal, int(m.group(1)))


def _bonus_any_condition(m, ability):
    from ptcgo.game.card_effects.attacks_common import defender_has_any_condition
    return bonus_if(defender_has_any_condition, int(m.group(1)))


def _bonus_own_energy(m, ability):
    from ptcgo.game.card_effects.attacks_common import self_has_energy_of_type
    return bonus_if(self_has_energy_of_type(TYPE_WORDS[m.group(1)]),
                    int(m.group(2)))


def _bonus_defender_is_ex(m, ability):
    from ptcgo.game.card_effects.attacks_common import defender_is_ex
    return bonus_if(defender_is_ex, int(m.group(1)))


def _bonus_defender_is_ex_or_v(m, ability):
    from ptcgo.game.card_effects.attacks_common import defender_is_ex_or_v
    return bonus_if(defender_is_ex_or_v, int(m.group(1)))


def _bonus_defender_has_damage(m, ability):
    from ptcgo.game.card_effects.attacks_common import has_damage
    return bonus_if(has_damage("defender"), int(m.group(1)))


def _bonus_self_has_damage(m, ability):
    from ptcgo.game.card_effects.attacks_common import has_damage
    return bonus_if(has_damage("self"), int(m.group(1)))


def _bonus_own_bench_damaged(m, ability):
    from ptcgo.game.card_effects.attacks_common import bench_has_damage_counters
    return bonus_if(bench_has_damage_counters, int(m.group(1)))


def _switch_self(m, ability):
    return switch_self_attack()


def _switch_self_optional(m, ability):
    return switch_self_attack(optional=True)


def _gust_opponent_chooses(m, ability):
    return gust_attack(opponent_chooses=True)


def _discard_random_opponent(m, ability):
    return discard_random_hand_attack(_count(m.group(1)))


def _search_basic_to_bench(m, ability):
    return search_to_bench(count=_count(m.group(1)))


def _place_counters_any(m, ability):
    return place_counters(int(m.group(1)), target="choose_any_opponent")


def _energy_move(m, ability):
    return energy_move_attack(count=_count(m.group(1)))



def _is_basic_energy(card) -> bool:
    return is_basic_energy_card(card)


def _is_pokemon_card(card) -> bool:
    return isinstance(def_for(getattr(card, "archetype_id", None) or ""),
                      PokemonCardDef)


def _search_any_to_hand(m, ability):
    return search_to_hand(None, count=_count(m.group(1)))


def _search_basic_energy_to_hand(m, ability):
    return search_to_hand(_is_basic_energy, count=_count(m.group(1)),
                          reveal=True)


def _search_pokemon_to_hand(m, ability):
    return search_to_hand(_is_pokemon_card, count=_count(m.group(1)),
                          reveal=True)


def _evolve_from_deck(m, ability):
    return evolve_from_deck_attack()


def _attach_energy_from_discard(m, ability):
    count = _count(m.group(1) if m.groups() else None)
    target = (lambda pokemon: not is_in_active_spot(pokemon)) \
        if "benched pokemon" in m.string else "self"
    return attach_from_discard(predicate=_is_basic_energy, count=count,
                               target=target)


def _less_per_counter_self(m, ability):
    return damage_per(damage_counters_on("self"), -int(m.group(1)),
                      base=getattr(ability, "damage", 0) or 0)


def _base_plus_per_counter_defender(m, ability):
    return damage_per(damage_counters_on("defender"), int(m.group(2)),
                      base=int(m.group(1)))


def _base_plus_per_energy_defender(m, ability):
    return damage_per(count_energy("defender"), int(m.group(2)),
                      base=int(m.group(1)))


def _scale_retreat_cost(m, ability):
    per = int(m.group(1))
    base = getattr(ability, "damage", 0) or 0 if "more damage" in m.string else 0
    return damage_per(defender_retreat_cost, per, base=base)


def _base_plus_if_defender_evolved(m, ability):
    return bonus_if(defender_is_evolved, int(m.group(2)), base=int(m.group(1)))


def _base_plus_if_defender_ex(m, ability):
    from ptcgo.game.card_effects.attacks_common import defender_is_ex
    return bonus_if(defender_is_ex, int(m.group(2)), base=int(m.group(1)))


def _reveal_hand(m, ability):
    return reveal_hand_attack()


def _discard_stadium(m, ability):
    return discard_stadium_attack()


def _discard_stadium_bonus(m, ability):
    return discard_stadium_attack(optional=True, bonus=int(m.group(1)))


def _no_weakness_next_turn(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            ctx.add_passive_through_opponents_turn(
                ctx.attacker, no_weakness_passive(protects="carrier"))
    return effect


def _no_resistance_next_turn(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            ctx.add_passive_through_opponents_turn(
                ctx.attacker, no_resistance_passive())
    return effect


def _lock_chosen_attack(m, ability):
    return lock_chosen_defender_attack()


def _passive_takes_less(m, ability):
    return takes_less_passive(int(m.group(1)), protects="carrier")


def _passive_flip_prevent(m, ability):
    return flip_prevent_damage_passive(title=getattr(ability, "title", ""))



def _more_times_type_energy(m, ability):
    return _more(count_energy("self", TYPE_WORDS[m.group(2)]), ability,
                 int(m.group(1)))


def _damage_per_energy_self(m, ability):
    return damage_per(count_energy("self"), int(m.group(1)), base=0)


def _damage_per_bench_opponent(m, ability):
    return damage_per(count_bench("opponent"), int(m.group(1)), base=0)


def _more_per_both_benches(m, ability):
    return _more(count_bench("both"), ability, int(m.group(1)))


def _debuff_defender_attacks(m, ability):
    return debuff_defender_attacks(int(m.group(1)))


def _prevent_from_basic(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is None:
            return
        from ptcgo.game.session.effects import is_basic_pokemon
        ctx.add_passive_through_opponents_turn(
            ctx.attacker,
            prevent_damage_when(
                lambda calc, carrier: calc.attacker is not None
                and is_basic_pokemon(calc.attacker)))
    return effect


def _snipe_choose_ignore_all(m, ability):
    amount = int(m.group(2))
    count = _count(m.group(1))

    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        picks = candidates if len(candidates) <= count else await ctx.choose_cards(
            candidates, count, prompt=f"Choose a Pokémon to take {amount} damage")
        for target in picks:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False,
                                  ignore_target_effects=True)
    return effect


def _snipe_bench_choose(m, ability):
    return snipe_attack(int(m.group(2)), pool="bench", count=_count(m.group(1)))


def _bonus_evolved(m, ability):
    return bonus_if(defender_is_evolved, int(m.group(1)))


def _random_hand_card_into_deck(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        hand = ctx.hand(ctx.opponent_id)
        if not hand:
            return
        card = random.choice(hand)
        await ctx.reveal_cards([card], to_player=ctx.player_id)
        await ctx.shuffle_into_deck([card], ctx.opponent_id)
    return effect


def _bench_snipe_if_any(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.opponent_bench()
        if not bench:
            return
        amount = int(m.group(1))
        count = _count(m.group(2)) if m.lastindex and m.lastindex >= 2 else 1
        picks = bench if len(bench) <= count else await ctx.choose_cards(
            bench, count, prompt=f"Choose a Pokémon to take {amount} damage")
        for target in picks:
            await ctx.deal_damage(amount, target=target,
                                  apply_modifiers=False)
    return effect


def _search_one_pokemon(m, ability):
    return search_to_hand(_is_pokemon_card, count=1, reveal=True)


def _search_supporter(m, ability):
    return search_to_hand(_is_supporter, count=1, reveal=True)


def _shuffle_hand_draw(m, ability):
    return shuffle_hand_into_deck_draw(int(m.group(1)))


def _search_energy_attach_any(m, ability):
    return search_attach_energy(_is_basic_energy, count=_count(m.group(1)),
                                distribute=True)


def _discard_defender_tools(m, ability):
    async def effect(ctx):
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            from ptcgo.game.attributes import TrainerType
            tools = [card for card in defender.children
                     if card.get_attribute(AttrID.TRAINER_TYPE) in
                     (TrainerType.POKEMON_TOOL.value,
                      TrainerType.POKEMON_TOOL_F.value)]
            if tools:
                await ctx.discard_cards(tools)
        await ctx.deal_damage()
    return effect


def _optional_bonus_self_damage(m, ability):
    bonus, recoil = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        amount = getattr(ability, "damage", 0) or 0
        if await ctx.ask_yes_no(f"Do {bonus} more damage to this Pokémon "
                                f"and take {recoil} damage yourself?"):
            await ctx.deal_damage(amount + bonus)
            await ctx.deal_damage(recoil, target=ctx.attacker,
                                  apply_modifiers=False)
        else:
            await ctx.deal_damage(amount)
    return effect


def _recover_from_discard(m, ability):
    return recover_from_discard(count=_count(m.group(1)), minimum=1)


def _lock_chosen_attack_opponent_active(m, ability):
    return lock_chosen_defender_attack()


def _base_plus_if_defender_damaged(m, ability):
    from ptcgo.game.card_effects.attacks_common import has_damage
    return bonus_if(has_damage("defender"), int(m.group(2)), base=int(m.group(1)))


def _base_plus_per_energy_defender_short(m, ability):
    return damage_per(count_energy("defender"), int(m.group(2)),
                      base=int(m.group(1)))


def _more_per_energy_defender_short(m, ability):
    return _more(count_energy("defender"), ability, int(m.group(1)))


def _is_supporter(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", None) or "")
    return type(definition).__name__ == "SupporterCardDef"



def _more_per_type_energy_short(m, ability):
    return _more(count_energy("self", TYPE_WORDS[m.group(2)]), ability,
                 int(m.group(1)))


def _more_with_tool(m, ability):
    from ptcgo.game.card_effects.attacks_common import has_tool
    return bonus_if(lambda ctx: ctx.attacker is not None
                    and has_tool(ctx.attacker), int(m.group(1)))


def _spread_own_bench_also_base(m, ability):
    return spread_damage(int(m.group(1)), side="mine", also_base=True)


def _flip_prevent_damage_short(m, ability):
    return flip_protection(prevent=True)


def _counters_on_opponent_bench(m, ability):
    return place_counters(int(m.group(1)), target="choose_any_opponent")


def _no_retreat_next_turn_long(m, ability):
    return no_retreat_attack()


def _entered_active_bonus(m, ability):
    return bonus_if(lambda ctx: ctx.attacker is not None
                    and ctx.entered_active_this_turn(ctx.attacker),
                    int(m.group(1)))


def _more_times_amount_energy_defender(m, ability):
    return _more(count_energy("defender"), ability, int(m.group(1)))


def _damage_per_prizes_self(m, ability):
    return damage_per(count_prizes_taken("mine"), int(m.group(1)), base=0)


def _damage_per_energy_opponent_all(m, ability):
    return damage_per(count_energy("opponent"), int(m.group(1)), base=0)


def _poison_counters_on_defender(m, ability):
    return condition_attack(SpecialConditions.POISONED, counters=int(m.group(1)))


def _discard_any_stadium(m, ability):
    return discard_stadium_attack()


def _ignore_all_except_weakness(m, ability):
    return ignore_modifier_attack(ignore_resistance=True,
                                  ignore_target_effects=True)


def _no_retreat_passive_team(m, ability):
    def pred(pokemon, carrier):
        from ptcgo.game.session.effects import is_basic_pokemon
        return pokemon.owning_player_id == carrier.owning_player_id \
            and is_basic_pokemon(pokemon)
    return retreat_free_when(pred)



def _snipe_choose_ignore_two(m, ability):
    """'... isn't affected by weakness and resistance.' / '... or any other
    effects on the Defending Pokemon.' -- both need their own damage flags."""
    amount, count = int(m.group(2)), _count(m.group(1))
    ignore_effects = "effects" in m.string

    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        picks = candidates if len(candidates) <= count else await ctx.choose_cards(
            candidates, count, prompt=f"Choose a Pokémon to take {amount} damage")
        for target in picks:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False,
                                  ignore_target_effects=ignore_effects)
    return effect


def _copy_defender_attack(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        from ptcgo.game.content.definitions import ABILITIES_BY_ID
        choices = [ABILITIES_BY_ID.get(entry["abilityID"])
                   for entry in _attack_entries(defender)]
        choices = [choice for choice in choices if choice is not None]
        if not choices:
            return
        chosen = await ctx.choose_attack_to_copy(
            [(defender, choice) for choice in choices],
            "Choose an attack to use")
        if chosen is None:
            return
        await ctx.use_attack(chosen[1])
    return effect


def _attack_entries(pokemon) -> list:
    return [entry for entry in (pokemon.get_attribute(AttrID.PIE_ABILITIES) or [])
            if isinstance(entry, dict) and entry.get("abilityType") == "Attack"
            and entry.get("abilityID")]


def _energy_discard_then_snipe(m, ability):
    discard_count = _count(m.group(1))
    amount, targets = int(m.group(3)), _count(m.group(2))

    async def effect(ctx):
        await ctx.discard_energy_from(
            ctx.attacker, discard_count,
            prompt="Choose Energy to discard from this Pokémon")
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        picks = candidates if len(candidates) <= targets else \
            await ctx.choose_cards(
                candidates, targets,
                prompt=f"Choose a Pokémon to take {amount} damage")
        for target in picks:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False)
    return effect


def _heal_bench_choice(m, ability):
    return heal_targets(int(m.group(1)), scope="bench_choice")


def _more_per_both_actives_energy(m, ability):
    def count(ctx) -> int:
        return count_energy("my_active")(ctx) + count_energy("defender")(ctx)
    return _more(count, ability, int(m.group(1)))


def _counters_active(m, ability):
    return place_counters(int(m.group(1)), target="opponent_active")


def _flip_two_heads_bonus(m, ability):
    return flip_bonus(int(m.group(1)), coins=2)


def _lock_defender_attacks_plain(m, ability):
    """'During your opponent's next turn, the Defending Pokemon can't use
    attacks' (no flip, no coin)."""
    async def effect(ctx):
        await ctx.deal_damage()
        from ptcgo.game.card_effects.attacks_common import lock_defender_attacks
        lock_defender_attacks(ctx)
    return effect


def _ignore_resistance_is_not(m, ability):
    return ignore_modifier_attack(ignore_resistance=True)


def _three_conditions(m, ability):
    return condition_attack(CONDITIONS[m.group(1)], CONDITIONS[m.group(2)],
                            CONDITIONS[m.group(3)])


def _switch_in_opponent_bench(m, ability):
    return gust_attack()


def _lock_basic_defender(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        from ptcgo.game.session.effects import is_basic_pokemon
        if is_basic_pokemon(defender):
            from ptcgo.game.card_effects.attacks_common import lock_defender_attacks
            lock_defender_attacks(ctx)
    return effect


def _return_self_to_hand(m, ability):
    return remove_self_from_play(destination="hand")


def _shuffle_self_into_deck(m, ability):
    return remove_self_from_play(destination="deck", optional=True)


def _bonus_then_discard_stadium(m, ability):
    async def effect(ctx):
        amount = getattr(ability, "damage", 0) or 0
        if ctx.stadium_in_play() is not None:
            await ctx.deal_damage(amount + int(m.group(1)))
            await ctx.discard_stadium()
        else:
            await ctx.deal_damage(amount)
    return effect


def _ignore_all_plain(m, ability):
    return ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True)


def _discard_top_attach_energy(m, ability):
    async def effect(ctx):
        cards = ctx.deck_top(_count(m.group(1)))
        await ctx.discard_cards(cards)
        energies = [card for card in cards if is_basic_energy_card(card)]
        for card in energies:
            if ctx.attacker is not None:
                await ctx.attach_energy(card, ctx.attacker)
    return effect


def _reveal_hand_per_trainer(m, ability):
    async def effect(ctx):
        cards = await ctx.reveal_hand(ctx.opponent_id)
        from ptcgo.game.card_effects.trainers import is_trainer_card
        amount = int(m.group(1)) * sum(1 for card in cards
                                       if is_trainer_card(card))
        if amount > 0:
            await ctx.deal_damage(amount)
    return effect


def _bonus_kos_last_turn(m, ability):
    return bonus_if(lambda ctx: ctx.kos_suffered_last_turn(ctx.player_id) > 0,
                    int(m.group(1)))


def _bonus_healed_this_turn(m, ability):
    def cond(ctx) -> bool:
        attacker = ctx.attacker
        return attacker is not None and \
            attacker.entity_id in ctx.session.turn_state.healed_entities
    return bonus_if(cond, int(m.group(1)))



# ----------------------------------------------------------------------
# Phrase tables: the long tail of "for each <phrase>" and "if <phrase>"
# wordings, resolved by exact phrase so an unknown phrase is never guessed.
# ----------------------------------------------------------------------

def _energy_attached(scope: str, type_word: Optional[str] = None):
    energy_type = TYPE_WORDS[type_word] if type_word else None
    return count_energy(scope, energy_type)


COUNT_PHRASES = {}


def _register_counts():
    from ptcgo.game.card_effects.attacks_common import (
        bench_has_damage_counters, has_tool,
    )

    def tools_in_play(ctx) -> int:
        return len(ctx.tools_in_play())

    def conditions_on_defender(ctx) -> int:
        defender = ctx.defender
        return len(defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []) \
            if defender is not None else 0

    def bench_types(ctx) -> int:
        types = set()
        for pokemon in ctx.my_bench():
            raw = pokemon.get_attribute(AttrID.POKEMON_TYPES)
            values = json.loads(raw) if isinstance(raw, str) else (raw or [])
            types.update(tuple(value for value in values))
        return len(types)

    def discard_matching(pred):
        return count_discard("mine", pred)

    def in_play_with_ability(side: str):
        def count(ctx) -> int:
            pool = ctx.opponent_pokemon_in_play() if side == "opponent" \
                else ctx.my_pokemon_in_play()
            total = 0
            for pokemon in pool:
                definition = def_for(pokemon.archetype_id)
                if any(getattr(ability, "ability_type", None) != 2
                       and not hasattr(ability, "damage")
                       for ability in getattr(definition, "abilities", []) or []):
                    total += 1
            return total
        return count

    COUNT_PHRASES.update({
        "energy attached to both active pokemon":
            lambda ctx: count_energy("my_active")(ctx)
            + count_energy("defender")(ctx),
        "energy attached to this pokemon and the defending pokemon":
            lambda ctx: count_energy("self")(ctx)
            + count_energy("defender")(ctx),
        "energy attached to all of your pokemon": _energy_attached("mine"),
        "energy attached to all of your opponent's pokemon":
            _energy_attached("opponent"),
        "energy attached to your opponent's active pokemon":
            _energy_attached("defender"),
        "energy attached to the defending pokemon": _energy_attached("defender"),
        "energy attached to this pokemon": _energy_attached("self"),
        "damage counter on your opponent's active pokemon":
            damage_counters_on("defender"),
        "damage counter on this pokemon": damage_counters_on("self"),
        "damage counter on the defending pokemon": damage_counters_on("defender"),
        "of your benched pokemon": count_bench("mine"),
        "of your pokemon in play": count_in_play("mine"),
        "of your remaining prize cards": count_prizes_remaining("mine"),
        "prize card your opponent has taken": count_prizes_taken("opponent"),
        "prize card you have taken": count_prizes_taken("mine"),
        "card in your opponent's hand": count_hand("opponent"),
        "your benched pokemon": count_bench("mine"),
        "item card in your opponent's discard pile":
            count_discard("opponent", _is_item),
        "supporter card in your discard pile": count_discard("mine", _is_supporter),
        "card in your hand": count_hand("mine"),
        "special condition affecting your opponent's active pokemon":
            conditions_on_defender,
        "pokemon tool attached to all of your pokemon": tools_in_play,
        "pokemon tool attached to your pokemon": tools_in_play,
        "pokemon on your bench": count_bench("mine"),
        "different type of pokemon on your bench": bench_types,
        "pokemon in your discard pile": discard_matching(_is_pokemon_card),
        "energy card in your discard pile": discard_matching(_is_basic_energy),
        "card in your discard pile": count_discard("mine"),
        "card in the lost zone": lambda ctx: ctx.lost_zone_count(ctx.player_id),
        "card in your opponent's lost zone":
            lambda ctx: ctx.lost_zone_count(ctx.opponent_id),
    })
    for word in TYPE_WORDS:
        COUNT_PHRASES[f"{word} energy attached to all of your pokemon"] = \
            _energy_attached("mine", word)
        COUNT_PHRASES[f"{word} energy attached to this pokemon"] = \
            _energy_attached("self", word)
        COUNT_PHRASES[f"{word} pokemon in your discard pile"] = \
            discard_matching(lambda card, w=word: is_pokemon_of_type(card, w))
        COUNT_PHRASES[f"{word} pokemon on your bench"] = \
            count_bench("mine", lambda p, w=word: is_pokemon_of_type(p, w))
    COUNT_PHRASES["pokemon in play that has the round attack"] = \
        lambda ctx: 0  # needs per-card attack inspection; left unbound


CONDITION_PHRASES = {}


def _condition_values(pokemon) -> list:
    values = []
    for entry in pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []:
        values.append(getattr(entry, "value", entry))
    return values


def _defender_stage(stage: int):
    from ptcgo.game.attributes import PokemonStage
    wanted = (PokemonStage.STAGE1 if stage == 1 else PokemonStage.STAGE2).value

    def cond(ctx) -> bool:
        defender = ctx.defender
        return defender is not None and \
            defender.get_attribute(AttrID.STAGE) == wanted
    return cond


def _register_conditions():
    from ptcgo.game.card_effects.attacks_common import (
        defender_has_any_condition, defender_has_condition, defender_is_ex,
        defender_is_v, has_damage, has_tool, stadium_in_play_cond,
    )

    def played_supporter(ctx) -> bool:
        return ctx.supporters_played_this_turn() > 0

    def opponent_one_prize(ctx) -> bool:
        return count_prizes_remaining("opponent")(ctx) == 1

    def self_condition(ctx) -> bool:
        attacker = ctx.attacker
        return attacker is not None and \
            bool(attacker.get_attribute(AttrID.SPECIAL_CONDITIONS))

    def self_has_special_energy(ctx) -> bool:
        attacker = ctx.attacker
        if attacker is None:
            return False
        return any(is_special_energy(energy)
                   for energy in ctx.attached_energies(attacker))

    def self_has_tool(ctx) -> bool:
        return ctx.attacker is not None and has_tool(ctx.attacker)

    def self_has_special_energy_too(ctx) -> bool:
        return self_has_special_energy(ctx)

    def entered_active(ctx) -> bool:
        return ctx.attacker is not None and \
            ctx.entered_active_this_turn(ctx.attacker)

    CONDITION_PHRASES.update({
        "this pokemon has any special energy attached to it":
            self_has_special_energy_too,
        "this pokemon was on the bench and became your active pokemon this turn":
            entered_active,
        "any of your pokemon were knocked out by damage from an opponent's "
        "attack during their last turn":
            lambda ctx: ctx.kos_suffered_last_turn(ctx.player_id) > 0,
        "any of your pokemon were knocked out by damage from an opponent's "
        "attack during his or her last turn":
            lambda ctx: ctx.kos_suffered_last_turn(ctx.player_id) > 0,
        "you have the same number of cards in your hand as your opponent":
            hand_sizes_equal,
        "you have more prize cards remaining than your opponent":
            _prize_comparison("more"),
        "you have fewer prize cards remaining than your opponent":
            _prize_comparison("fewer"),
        "your opponent has exactly 1 prize card remaining":
            lambda ctx: count_prizes_remaining("opponent")(ctx) == 1,
        "there is any stadium card in play": stadium_in_play_cond,
        "you played a supporter card from your hand during this turn":
            played_supporter,
        "the defending pokemon is affected by a special condition":
            defender_has_any_condition,
        "the defending pokemon already has any damage counters on it":
            has_damage("defender"),
        "this pokemon has any damage counters on it": has_damage("self"),
        "this pokemon is affected by a special condition": self_condition,
        "your opponent's active pokemon is affected by a special condition":
            defender_has_any_condition,
        "your opponent has only 1 prize card left": opponent_one_prize,
        "this pokemon has a pokemon tool attached": self_has_tool,
        "this pokemon has any special energy attached": self_has_special_energy,
        "your opponent's active pokemon is a pokemon v": defender_is_v,
        "your opponent's active pokemon is a pokemon-ex": defender_is_ex,
        "this pokemon is burned or poisoned":
            lambda ctx: ctx.attacker is not None and bool(
                {SpecialConditions.BURNED.value, SpecialConditions.POISONED.value}
                & set(_condition_values(ctx.attacker))),
        "your opponent's active pokemon is a basic pokemon":
            lambda ctx: ctx.defender is not None
            and not defender_is_evolved(ctx),
        "your opponent's active pokemon is a stage 1 pokemon":
            _defender_stage(1),
        "your opponent's active pokemon is a stage 2 pokemon":
            _defender_stage(2),
        "this pokemon has no damage counters on it":
            lambda ctx: not has_damage("self")(ctx),
        "your opponent's active pokemon has a pokemon tool card attached to it":
            lambda ctx: ctx.opponent_active() is not None
            and has_tool(ctx.opponent_active()),
        "the defending pokemon is a pokemon-ex": defender_is_ex,
    })
    for limit in range(0, 11):
        CONDITION_PHRASES[
            f"your opponent has {limit} or fewer cards in their hand"] =             (lambda ctx, _limit=limit: len(ctx.hand(ctx.opponent_id)) <= _limit)
    for word in TYPE_WORDS:
        CONDITION_PHRASES[f"your opponent's active pokemon is a {word} pokemon"] = \
            _defender_of_type(word)
        CONDITION_PHRASES[f"the defending pokemon is a {word} pokemon"] = \
            _defender_of_type(word)
    for word, condition in CONDITIONS.items():
        CONDITION_PHRASES[f"the defending pokemon is {word}"] = \
            defender_has_condition(condition)
        CONDITION_PHRASES[f"your opponent's active pokemon is {word}"] = \
            defender_has_condition(condition)


def is_pokemon_of_type(card_or_pokemon, type_word: str) -> bool:
    type_value = TYPE_WORDS[type_word].value
    raw = card_or_pokemon.get_attribute(AttrID.POKEMON_TYPES)
    if isinstance(raw, str):
        try:
            values = json.loads(raw)
        except (TypeError, ValueError):
            return False
    else:
        values = raw or []
    return type_value in values



def _defender_of_type(type_word: str):
    def cond(ctx) -> bool:
        defender = ctx.defender
        return defender is not None and is_pokemon_of_type(defender, type_word)
    return cond


def _defender_counters_at_least(count: int):
    def cond(ctx) -> bool:
        return damage_counters_on("defender")(ctx) >= count
    return cond


def _extra_energy_attached(required: int, type_word: Optional[str]):
    """"At least N extra [type] Energy attached (in addition to this attack's
    cost)" — the shared count in attacks_common, with patterns' type words."""
    from ptcgo.game.card_effects.attacks_common import extra_energy_attached
    type_value = TYPE_WORDS[type_word].value if type_word else None
    return extra_energy_attached(required, type_value)


def _prize_comparison(kind: str):
    def cond(ctx) -> bool:
        mine = count_prizes_remaining("mine")(ctx)
        theirs = count_prizes_remaining("opponent")(ctx)
        if kind == "more":
            return mine > theirs
        if kind == "fewer":
            return mine < theirs
        return mine == theirs
    return cond


def _entered_active_condition(ctx) -> bool:
    from ptcgo.game.card_effects.attacks_common import entered_active_cond
    return entered_active_cond(ctx)


def _kos_last_turn_condition(ctx) -> bool:
    return ctx.kos_suffered_last_turn(ctx.player_id) > 0


def _bonus_threshold_counters(m, ability):
    return bonus_if(_defender_counters_at_least(int(m.group(1))),
                    int(m.group(2)))


def _bonus_extra_energy(m, ability):
    return bonus_if(_extra_energy_attached(int(m.group(1)), m.group(2)),
                    int(m.group(3)))


def _bonus_prize_comparison(m, ability):
    kind = "more" if "more" in m.group(1) else (
        "fewer" if "fewer" in m.group(1) else "equal")
    return bonus_if(_prize_comparison(kind), int(m.group(2)))



def _energy_pools(kind: str):
    if kind == "self":
        return lambda ctx: list(ctx.attached_energies(ctx.attacker)) \
            if ctx.attacker is not None else []
    if kind == "bench":
        return lambda ctx: [energy for pokemon in ctx.my_bench()
                            for energy in ctx.attached_energies(pokemon)]
    if kind == "mine":
        return lambda ctx: [energy for pokemon in ctx.my_pokemon_in_play()
                            for energy in ctx.attached_energies(pokemon)]
    return lambda ctx: list(ctx.hand())


def _discard_for_damage(m, ability):
    """'Discard <any amount|all|up to N> of <cards> from <zone>. This attack
    does N damage for each card you discarded in this way.'"""
    text = m.string
    base = getattr(ability, "damage", 0) or 0 if "more damage" in text else 0
    per = int(m.group(m.lastindex))
    cap = int(m.group(1)) if m.group(1) and m.group(1).isdigit() else None
    if "from your hand" in text:
        pool = _energy_pools("hand")
        if "supporter" in text:
            predicate = _is_supporter
        elif "basic energy" in text:
            predicate = _is_basic_energy
        else:
            predicate = is_energy_card
    else:
        pool = _energy_pools("bench" if "benched pokemon" in text else
                             ("self" if "from this pokemon" in text and
                              "your pokemon" not in text else "mine"))
        type_word = m.group("type") if "type" in (m.re.groupindex or {}) else None
        type_value = TYPE_WORDS[type_word].value if type_word else None
        basic_only = "basic energy" in text

        def predicate(card, _type=type_value, _basic=basic_only) -> bool:
            if _basic and not is_basic_energy_card(card):
                return False
            return _type is None or energy_provides_type(card, _type)

    everything = " all " in f" {text} " or text.startswith("discard all ")

    async def effect(ctx):
        candidates = [card for card in pool(ctx) if predicate(card)]
        if everything:
            picks = candidates
        elif candidates:
            picks = await ctx.choose_cards(
                candidates, cap or 99, minimum=0,
                prompt="Choose cards to discard")
        else:
            picks = []
        if picks:
            await ctx.discard_cards(picks)
        amount = base + per * len(picks)
        if amount > 0:
            await ctx.deal_damage(amount)
    return effect



def _peek_opponent_hand_card(m, ability):
    """'Choose a card from your opponent's hand without looking, then have
    them shuffle it into their deck.'"""
    async def effect(ctx):
        await ctx.deal_damage()
        hand = ctx.hand(ctx.opponent_id)
        if not hand:
            return
        picked = random.choice(hand)
        await ctx.reveal_cards([picked], to_player=ctx.player_id)
        await ctx.shuffle_into_deck([picked], ctx.opponent_id)
    return effect


def _flip_bonus_or_self_damage(m, ability):
    bonus, recoil = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        base = getattr(ability, "damage", 0) or 0
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await ctx.deal_damage(base + bonus)
        else:
            await ctx.deal_damage(base)
            await ctx.deal_damage(recoil, target=ctx.attacker,
                                  apply_modifiers=False)
    return effect


def _attach_from_discard_distributed(m, ability):
    count = int(m.group(1))
    type_word = m.group(2)

    def predicate(card) -> bool:
        if not is_basic_energy_card(card):
            return False
        return type_word is None or energy_provides_type(
            card, TYPE_WORDS[type_word].value)

    async def effect(ctx):
        await ctx.deal_damage()
        cards = [card for card in ctx.discard_pile() if predicate(card)]
        if not cards:
            return
        picks = await ctx.choose_cards(cards, count, minimum=0,
                                       prompt="Choose Energy to attach")
        candidates = [pokemon for pokemon in ctx.my_pokemon_in_play()]
        for card in picks:
            if not candidates:
                break
            target = await ctx.choose_pokemon(
                candidates, "Choose a Pokémon to attach the Energy to")
            if target is not None:
                await ctx.attach_energy(card, target)
    return effect


def _flip_draw_one(m, ability):
    async def draw(ctx):
        await ctx.draw_cards(1)
    return flip_gate(draw)


def _heal_each_bench(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_bench():
            await ctx.heal(amount, pokemon)
    return effect


def _counters_on_chosen(m, ability):
    counters, targets = int(m.group(1)), _count(m.group(2))

    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        picks = candidates if len(candidates) <= targets else \
            await ctx.choose_cards(candidates, targets,
                                   prompt="Choose a Pokémon to put damage counters on")
        for target in picks:
            await ctx.deal_damage(counters * 10, target=target, as_counters=True)
    return effect


def _spread_over_chosen(m, ability):
    amount, targets = int(m.group(2)), _count(m.group(1))

    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        picks = candidates if len(candidates) <= targets else \
            await ctx.choose_cards(candidates, targets,
                                   prompt=f"Choose up to {targets} Pokémon")
        for target in picks:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False)
    return effect


def _spread_opponent_bench_damaged(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        for pokemon in ctx.opponent_bench():
            if ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0) > 0:
                await ctx.deal_damage(amount, target=pokemon,
                                      apply_modifiers=False)
    return effect


def _snipe_own_bench(m, ability):
    amount, targets = int(m.group(1)), _count(m.group(2))

    async def effect(ctx):
        bench = ctx.my_bench()
        if not bench:
            return
        picks = bench if len(bench) <= targets else await ctx.choose_cards(
            bench, targets, prompt=f"Choose a Pokémon to take {amount} damage")
        for target in picks:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False)
    return effect


def _discard_attack_title_count(attack_title: str, side: str = "discard"):
    """'... for each Pokemon in your discard pile that has the <attack> attack'."""
    from ptcgo.game.card_effects.attacks_common import has_attack_titled
    predicate = has_attack_titled(attack_title)

    def count(ctx) -> int:
        return sum(1 for card in ctx.discard_pile() if predicate(card))
    return count


def _scale_united_wings(m, ability):
    return _more(_discard_attack_title_count("United Wings"), ability,
                 int(m.group(1)))


def _scale_round_attack(m, ability):
    from ptcgo.game.card_effects.attacks_common import has_attack_titled
    predicate = has_attack_titled("Round")

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.my_pokemon_in_play()
                   if predicate(pokemon))
    return damage_per(count, int(m.group(1)), base=0)


def _shuffle_hand_draw_opponent_size(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.shuffle_into_deck(list(ctx.hand()), ctx.player_id)
        await ctx.draw_cards(ctx.hand_size(ctx.opponent_id))
    return effect


def _gust_damage_new_active(m, ability):
    return gust_attack(damage_before=0, damage_to_new_active=int(m.group(2)))


def _discard_stadium_optional(m, ability):
    return discard_stadium_attack(optional=True)


def _heal_all_self(m, ability):
    return heal_attack(all_damage=True, target="self")


def _cure_self_conditions(m, ability):
    return cure_conditions_effect(scope="active")


def _lock_this_attack(m, ability):
    """'This Pokemon can't use <this attack> during your next turn.' -- the
    named attack must be the one being resolved, or nothing is bound."""
    named = normalize(m.group(1))
    title = normalize(getattr(ability, "title", ""))
    if named != title:
        return None

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None and ability.ability_id:
            ctx.session.turn_state.lock_attack(ctx.attacker.entity_id,
                                               ability.ability_id)
    return effect



def _mill_by_heads(m, ability):
    """'Flip a coin until you get tails. For each heads, discard the top card
    of your opponent's deck.'"""
    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_until_tails(getattr(ability, "title", ""))
        if heads > 0:
            await ctx.discard_cards(ctx.deck_top(heads, player_id=ctx.opponent_id))
    return effect


def _peek_opponent_hand_discard(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        hand = ctx.hand(ctx.opponent_id)
        if not hand:
            return
        picked = random.choice(hand)
        await ctx.reveal_cards([picked], to_player=ctx.player_id)
        await ctx.discard_cards([picked])
    return effect


def _flip_two_conditions(m, ability):
    heads_condition = CONDITIONS[m.group(1)]
    tails_condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        condition = heads_condition if (results and results[0])             else tails_condition
        await ctx.apply_special_condition(ctx.defender, condition)
    return effect


def _damage_per_round_in_play(m, ability):
    from ptcgo.game.card_effects.attacks_common import has_attack_titled
    predicate = has_attack_titled("Round")

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.my_pokemon_in_play()
                   if predicate(pokemon))
    return damage_per(count, int(m.group(1)), base=0)


def _lock_opponent_items(m, ability):
    from ptcgo.game.attributes import CardType, TrainerType

    async def effect(ctx):
        await ctx.deal_damage()
        ctx.lock_plays(
            ctx.opponent_id,
            lambda card: card.get_attribute(AttrID.CARD_TYPE) == CardType.TRAINER.value
            and card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.ITEM.value)
    return effect


def _extra_prize_on_ko(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        ctx.add_extra_prize_watcher(prizes=int(m.group(1)))
    return effect


def _snipe_bench_damaged_also_base(m, ability):
    amount, targets = int(m.group(1)), _count(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = [pokemon for pokemon in ctx.opponent_bench()
                      if ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0) > 0]
        if not candidates:
            return
        picks = candidates if len(candidates) <= targets else \
            await ctx.choose_cards(candidates, targets,
                                   prompt=f"Choose a Pokémon to take {amount} damage")
        for target in picks:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False)
    return effect


def _discard_any_opponent_energy(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                      if ctx.attached_energies(pokemon)
                      and not ctx.effects_blocked(pokemon)]
        if not candidates:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates,
                                     "Choose a Pokémon to discard Energy from")
        if target is not None:
            await ctx.discard_energy_from(target, count)
    return effect


def _prevent_from_basic_noncolorless(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is None:
            return
        from ptcgo.game.session.effects import is_basic_pokemon
        from ptcgo.game.session.passives import effective_pokemon_types

        def pred(calc, carrier) -> bool:
            attacker = calc.attacker
            if attacker is None or not is_basic_pokemon(attacker):
                return False
            types = effective_pokemon_types(ctx.board, attacker)
            return bool(types) and types[0] != PokemonTypes.COLORLESS.value
        ctx.add_passive_through_opponents_turn(
            ctx.attacker, prevent_damage_when(pred))
    return effect



def _opponent_discards(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.discard_from_hand(count, minimum=0, player_id=ctx.opponent_id,
                                    prompt="Choose cards to discard")
    return effect


def _remove_counter_each_own(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_pokemon_in_play():
            await ctx.heal(count * 10, pokemon)
    return effect


def _flip_tails_self_lock(m, ability):
    async def lock(ctx):
        from ptcgo.game.card_effects.attacks_common import lock_all_attacks
        if ctx.attacker is not None:
            lock_all_attacks(ctx, ctx.attacker)
    return flip_gate(lock)


def _switch_both_actives(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.my_bench()
        if bench:
            target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)
        await opponent_switches(ctx)
    return effect


def _discard_hand_draw_n(m, ability):
    return discard_then_draw(0, int(m.group(1)), whole_hand=True)


def _search_any_card_old(m, ability):
    return search_to_hand(None, count=1, reveal=False)


def _search_item_to_hand(m, ability):
    return search_to_hand(_is_item, count=1, reveal=True)


def _search_basic_energy_show(m, ability):
    return search_to_hand(_is_basic_energy, count=1, reveal=True)


def _search_energy_attach_self(m, ability):
    type_word = m.groupdict().get("type")
    predicate = _is_basic_energy if type_word is None else (
        lambda card, word=type_word: is_basic_energy_card(card)
        and energy_provides_type(card, TYPE_WORDS[word].value))
    return search_attach_energy(predicate, count=1, to_self=True)


def _attach_discard_plain(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        cards = [card for card in ctx.discard_pile()
                 if is_basic_energy_card(card)]
        if not cards:
            return
        picks = await ctx.choose_cards(cards, count, minimum=0,
                                       prompt="Choose Energy to attach")
        bench = ctx.my_bench()
        if not picks or not bench:
            return
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose a Pokémon to attach the Energy to")
        if target is None:
            return
        for card in picks:
            await ctx.attach_energy(card, target)
    return effect


def _flip_random_discard(m, ability):
    async def discard(ctx):
        from ptcgo.game.card_effects.attacks_common import discard_random_from_hand
        await discard_random_from_hand(ctx, ctx.opponent_id, 1)
    return flip_gate(discard)


def _both_actives_condition(m, ability):
    return condition_attack(CONDITIONS[m.group(1)], both_actives=True)


def _spread_own_bench_plain(m, ability):
    return spread_damage(int(m.group(1)), side="mine")


def _flip_confused_poisoned(m, ability):
    return condition_attack(SpecialConditions.CONFUSED,
                            SpecialConditions.POISONED, flip=True)


def _is_item(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", None) or "")
    return type(definition).__name__ == "ItemCardDef"



def _lock_defender_attacks_and_retreat(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        from ptcgo.game.card_effects.attacks_common import lock_defender_attacks
        lock_defender_attacks(ctx)
        ctx.lock_retreat(defender)
    return effect


def _flip_spread_bench(m, ability):
    amount = int(m.group(1))

    async def spread(ctx):
        for pokemon in ctx.opponent_bench():
            await ctx.deal_damage(amount, target=pokemon, apply_modifiers=False)
    return flip_gate(spread)


def _optional_all_energy_bonus(m, ability):
    bonus = int(m.group(1))

    async def effect(ctx):
        base = getattr(ability, "damage", 0) or 0
        energies = list(ctx.attached_energies(ctx.attacker)) \
            if ctx.attacker is not None else []
        if not energies:
            await ctx.deal_damage(base)
            return
        if not await ctx.ask_yes_no(
                "Discard all Energy from this Pokémon for extra damage?"):
            await ctx.deal_damage(base)
            return
        await ctx.discard_cards(energies)
        await ctx.deal_damage(base + bonus)
    return effect


def _flip_self_energy_discard(m, ability):
    type_word = m.groupdict().get("type")
    type_value = TYPE_WORDS[type_word].value if type_word else None

    async def discard(ctx):
        attacker = ctx.attacker
        if attacker is None:
            return
        pool = [energy for energy in ctx.attached_energies(attacker)
                if type_value is None or energy_provides_type(energy, type_value)]
        if pool:
            await ctx.discard_energy_from(attacker, 1, predicate=(
                (lambda card: energy_provides_type(card, type_value))
                if type_value is not None else None))
    return flip_gate(discard)


def _move_basic_energy(m, ability):
    return energy_move_attack(count=1)


def _self_condition_then_heal(m, ability):
    condition = CONDITIONS[m.group(1)]
    amount = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.apply_special_condition(ctx.attacker, condition)
        if ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
    return effect


def _flip_bonus_else_condition(m, ability):
    bonus = int(m.group(1))
    condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        base = getattr(ability, "damage", 0) or 0
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await ctx.deal_damage(base + bonus)
        else:
            await ctx.deal_damage(base)
            await ctx.apply_special_condition(ctx.defender, condition)
    return effect


def _flip_paralyze_else_nothing(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await ctx.deal_damage()
            await ctx.apply_special_condition(ctx.defender, condition)
    return effect


def _snipe_damaged_only(m, ability):
    amount, targets = int(m.group(2)), _count(m.group(1))

    async def effect(ctx):
        candidates = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                      if ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0) > 0]
        if not candidates:
            return
        picks = candidates if len(candidates) <= targets else \
            await ctx.choose_cards(candidates, targets,
                                   prompt=f"Choose a Pokémon to take {amount} damage")
        for target in picks:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False)
    return effect


def _condition_then_no_retreat(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        await ctx.apply_special_condition(defender, condition)
        if defender is not None and not ctx.effects_blocked(defender):
            ctx.lock_retreat(defender)
    return effect


def _heal_all_bench_choice(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        bench = [pokemon for pokemon in ctx.my_bench()
                 if ctx.max_hp(pokemon) > pokemon.get_attribute(AttrID.HP, 0)]
        if not bench:
            return
        target = await ctx.choose_pokemon(bench, "Choose a Pokémon to heal")
        if target is not None:
            await ctx.heal(ctx.max_hp(target)
                           - target.get_attribute(AttrID.HP, 0), target)
    return effect



def _flip_two_target_conditions(m, ability):
    return condition_attack(CONDITIONS[m.group(1)], CONDITIONS[m.group(2)],
                            flip=True)


def _checkup_poison_counters(m, ability):
    return condition_attack(SpecialConditions.POISONED, counters=int(m.group(1)))


def _flip_bonus_and_condition(m, ability):
    bonus, condition = int(m.group(2)), CONDITIONS[m.group(3)]

    async def effect(ctx):
        base = getattr(ability, "damage", 0) or 0
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await ctx.deal_damage(base + bonus)
            await ctx.apply_special_condition(ctx.defender, condition)
        else:
            await ctx.deal_damage(base)
    return effect


def _energy_cost_then_condition(m, ability):
    count, condition = _count(m.group(1)), CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.discard_energy_from(
            ctx.attacker, count,
            prompt="Choose Energy to discard from this Pokémon")
        await ctx.apply_special_condition(ctx.defender, condition)
    return effect


def _flip_damage_then_self_condition(m, ability):
    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await ctx.deal_damage()
        await ctx.apply_special_condition(ctx.attacker,
                                         SpecialConditions.CONFUSED)
    return effect



def _energy_to_hand(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        pool = list(ctx.attached_energies(attacker))
        if not pool:
            return
        picks = pool if len(pool) <= count else await ctx.choose_cards(
            pool, count, prompt="Choose Energy to put into your hand")
        await ctx.put_in_hand(picks, reveal=False)
    return effect


def _own_next_turn_title_boost(m, ability):
    named = m.group(1)
    amount = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        from ptcgo.game.card_effects.passives_common import (
            apply_own_next_turn_boost,
        )
        await apply_own_next_turn_boost(ctx, amount, attack_title=named)
    return effect


def _discard_energy_each_opponent(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_pokemon_in_play():
            if ctx.effects_blocked(pokemon):
                continue
            for _ in range(count):
                energies = ctx.attached_energies(pokemon)
                if not energies:
                    break
                await ctx.discard_energy_from(pokemon, 1)
    return effect


def _optional_gust_opponent(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if not ctx.opponent_bench():
            return
        if not await ctx.ask_yes_no(
                "Have your opponent switch their Active Pokémon?"):
            return
        await opponent_switches(ctx)
    return effect


def _heal_counter_from_chosen(m, ability):
    amount = int(m.group(1)) * 10

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = [pokemon for pokemon in ctx.my_pokemon_in_play()
                      if ctx.max_hp(pokemon) > pokemon.get_attribute(AttrID.HP, 0)]
        if not candidates:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal")
        if target is not None:
            await ctx.heal(amount, target)
    return effect


def _reorder_either_deck(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        own = await ctx.ask_yes_no("Look at your own deck? (No: your "
                                   "opponent's deck)")
        await ctx.reorder_deck_top(count, ctx.player_id if own
                                   else ctx.opponent_id,
                                   "Rearrange the top cards")

    return effect


def _move_opponent_energy_to_bench(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        active = ctx.opponent_active()
        bench = ctx.opponent_bench()
        if active is None or not bench or ctx.effects_blocked(active):
            return
        await ctx.move_energy_freely([active], bench,
                                     prompt="Choose Energy to move")

    return effect


def _move_counters_to_opponent(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        candidates = [pokemon for pokemon in ctx.my_bench()
                      if ctx.max_hp(pokemon) > pokemon.get_attribute(AttrID.HP, 0)]
        defender = ctx.defender
        if not candidates or defender is None:
            return
        source = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates,
                                     "Choose a Pokémon to move counters from")
        if source is not None:
            await ctx.move_damage_counters(source, [defender])
    return effect


def _prevent_from_evolution(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is None:
            return
        from ptcgo.game.session.effects import is_evolution_pokemon
        ctx.add_passive_through_opponents_turn(
            ctx.attacker,
            prevent_damage_when(
                lambda calc, carrier: calc.attacker is not None
                and is_evolution_pokemon(calc.attacker)))
    return effect


def _attach_hand_energy_distributed(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        hand = [card for card in ctx.hand() if is_basic_energy_card(card)]
        if not hand:
            return
        picks = await ctx.choose_cards(hand, 99, minimum=0,
                                       prompt="Choose Energy to attach")
        candidates = ctx.my_pokemon_in_play()
        for card in picks:
            if not candidates:
                break
            target = await ctx.choose_pokemon(
                candidates, "Choose a Pokémon to attach the Energy to")
            if target is not None:
                await ctx.attach_energy(card, target)
    return effect


def _attach_hand_energy_one(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        hand = [card for card in ctx.hand() if is_energy_card(card)]
        if not hand:
            return
        picks = await ctx.choose_cards(hand, 1, minimum=0,
                                       prompt="Choose an Energy to attach")
        candidates = ctx.my_pokemon_in_play()
        if not picks or not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon to attach the Energy to")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _search_energy_attach_one_target(m, ability):
    count = int(m.group(1))
    type_word = m.groupdict().get("type")
    predicate = (lambda card: is_basic_energy_card(card)
                 and energy_provides_type(card, TYPE_WORDS[type_word].value)) \
        if type_word else is_basic_energy_card
    return search_attach_energy(predicate, count=count, distribute=False)


def _prevent_all_no_flip(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        from ptcgo.game.card_effects.passives_common import apply_protection
        await apply_protection(ctx, prevent=True, effects_too=True)
    return effect


def _heal_block_defender(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.defender is None:
            return
        from ptcgo.game.card_effects.passives_common import healing_block_passive
        ctx.add_passive_through_opponents_turn(
            ctx.defender, healing_block_passive(lambda target, carrier: True))
    return effect


def _search_stadium_to_hand(m, ability):
    return search_to_hand(_is_stadium, count=1, reveal=True)


def _take_extra_turn(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        ctx.take_extra_turn()
    return effect


def _move_bench_energy_to_self(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        bench = ctx.my_bench()
        if attacker is None or not bench:
            return
        await ctx.move_energy_freely(bench, [attacker],
                                     prompt="Choose Energy to move")
    return effect


def _usable_first_turn(m, ability):
    ability.usable_first_turn = True

    async def effect(ctx):
        await ctx.deal_damage()
    return effect


def _snipe_multi_ignore_all(m, ability):
    amount, targets = int(m.group(1)), _count(m.group(2))

    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        picks = candidates if len(candidates) <= targets else \
            await ctx.choose_cards(candidates, targets,
                                   prompt=f"Choose {targets} Pokémon")
        for target in picks:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False,
                                  ignore_target_effects=True)
    return effect


def _is_stadium(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", None) or "")
    return type(definition).__name__ == "StadiumCardDef"



def _snipe_ignore_weakness_or_resistance(m, ability):
    amount, count = int(m.group(2)), _count(m.group(1))

    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        picks = candidates if len(candidates) <= count else \
            await ctx.choose_cards(candidates, count,
                                   prompt=f"Choose a Pokémon to take {amount} damage")
        for target in picks:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False)
    return effect


def _flip_tails_nothing_heads_shield(m, ability):
    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if not (results and results[0]):
            return
        from ptcgo.game.card_effects.passives_common import apply_protection
        await ctx.deal_damage()
        await apply_protection(ctx, prevent=True, effects_too=True)
    return effect


def _discard_all_defender_energy(m, ability):
    return discard_opponent_energy_attack(count=99)


def _ko_defender_self_damage(m, ability):
    recoil = int(m.group(1))

    async def effect(ctx):
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        await ctx.knock_out(defender)
        if ctx.attacker is not None:
            await ctx.deal_damage(recoil, target=ctx.attacker,
                                  apply_modifiers=False)
    return effect


def _shuffle_opponent_energy_into_deck(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_pokemon_in_play():
            if ctx.effects_blocked(pokemon):
                continue
            energies = list(ctx.attached_energies(pokemon))
            if energies:
                await ctx.shuffle_into_deck(energies, ctx.opponent_id)
    return effect


def _flip_tails_named_self_damage(m, ability):
    return flip_damage(tails_self_damage=int(m.group(1)))


def _recover_item(m, ability):
    return recover_from_discard(predicate=_is_item, count=1, minimum=0)


def _smokescreen_worded(m, ability):
    return smokescreen_attack()


def _lock_opponent_items_v2(m, ability):
    return _lock_opponent_items(m, ability)



def _condition_gate(m, ability):
    required = CONDITIONS[m.group(1)]

    async def effect(ctx):
        defender = ctx.defender
        present = defender is not None and required.name in (
            defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
        if present:
            await ctx.deal_damage()
    return effect


def _both_this_and_defender(m, ability):
    return condition_attack(CONDITIONS[m.group(1)], both_actives=True)


def _flip_two_heads_discard_all(m, ability):
    async def discard(ctx):
        target = ctx.opponent_active()
        if target is None or ctx.effects_blocked(target):
            return
        await ctx.discard_energy_from(target, 99,
                                      prompt="Choose Energy to discard")
    return flip_gate(discard, coins=2)


def _move_own_energy_around(m, ability):
    type_word = m.groupdict().get("type")
    predicate = ((lambda card: energy_provides_type(card,
                                                    TYPE_WORDS[type_word].value))
                 if type_word else None)

    async def effect(ctx):
        await ctx.deal_damage()
        pool = ctx.my_pokemon_in_play()
        if len(pool) < 2:
            return
        await ctx.move_energy_freely(pool, pool, predicate=predicate,
                                     prompt="Choose Energy to move")
    return effect


def _search_energy_attach_any_old(m, ability):
    return search_attach_energy(_is_basic_energy, count=1, distribute=False)


def _prevent_incoming_next_turn(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is None:
            return
        from ptcgo.game.card_effects.passives_common import apply_protection
        await apply_protection(ctx, prevent=True)
    return effect


def _search_energy_attach_self_two(m, ability):
    count = int(m.group(1))
    type_word = m.groupdict().get("type")
    predicate = ((lambda card: energy_provides_type(card,
                                                    TYPE_WORDS[type_word].value))
                 if type_word else is_basic_energy_card)
    return _search_attach_self_factory(predicate, count)


def _search_attach_self_factory(predicate, count):
    async def effect(ctx):
        picks = await ctx.search_deck(predicate, count=count, minimum=0,
                                      prompt=f"Choose up to {count} Energy to attach")
        if picks and ctx.attacker is not None:
            for card in picks:
                await ctx.attach_energy(card, ctx.attacker)
        await ctx.shuffle_deck()
    return effect


def _search_supporter_show(m, ability):
    return search_to_hand(_is_supporter, count=1, reveal=True)



def _lock_this_attack_reversed(m, ability):
    named = normalize(m.group(1))
    if named != normalize(getattr(ability, "title", "")):
        return None

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None and ability.ability_id:
            ctx.session.turn_state.lock_attack(ctx.attacker.entity_id,
                                               ability.ability_id)
    return effect


def _search_energy_show_any(m, ability):
    return search_to_hand(is_energy_card, count=1, reveal=True)


def _move_energy_between_opponents(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        active = ctx.opponent_active()
        bench = [pokemon for pokemon in ctx.opponent_bench() if pokemon is not active]
        if active is None or not bench or ctx.effects_blocked(active):
            return
        await ctx.move_energy_freely([active], bench,
                                     prompt="Choose Energy to move")
    return effect


def _flip_until_tails_draw(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_until_tails(getattr(ability, "title", ""))
        if heads > 0:
            await ctx.draw_cards(heads)
    return effect


def _discard_defender_trainers(m, ability):
    async def effect(ctx):
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            from ptcgo.game.attributes import CardType
            trainers = [card for card in defender.children
                        if card.get_attribute(AttrID.CARD_TYPE) == CardType.TRAINER.value]
            if trainers:
                await ctx.discard_cards(trainers)
        await ctx.deal_damage()
    return effect


def _move_opponent_counters(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pool = ctx.opponent_pokemon_in_play()
        if len(pool) < 2:
            return
        source = await ctx.choose_pokemon(pool, "Choose a Pokémon to move counters from")
        if source is None:
            return
        dests = [pokemon for pokemon in pool if pokemon is not source]
        await ctx.move_damage_counters(source, dests)
    return effect


def _search_energy_each_bench(m, ability):
    type_word = m.groupdict().get("type")
    predicate = ((lambda card: is_basic_energy_card(card)
                  and energy_provides_type(card, TYPE_WORDS[type_word].value))
                 if type_word else is_basic_energy_card)

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in list(ctx.my_bench()):
            picks = await ctx.search_deck(predicate, count=1, minimum=0,
                                          prompt="Choose Energy to attach")
            if picks:
                await ctx.attach_energy(picks[0], pokemon)
        await ctx.shuffle_deck()
    return effect


def _copy_own_bench_attack(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.my_bench()
        candidates = []
        from ptcgo.game.content.definitions import ABILITIES_BY_ID
        for pokemon in bench:
            for entry in _attack_entries(pokemon):
                attack = ABILITIES_BY_ID.get(entry["abilityID"])
                if attack is not None:
                    candidates.append((pokemon, attack))
        if not candidates:
            return
        chosen = await ctx.choose_attack_to_copy(candidates,
                                                 "Choose an attack to use")
        if chosen is None:
            return
        await ctx.use_attack(chosen[1])
    return effect


def _flip_condition_and_discard(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if not (results and results[0]):
            await ctx.deal_damage()
            return
        await ctx.deal_damage()
        defender = ctx.defender
        await ctx.apply_special_condition(defender, condition)
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.discard_energy_from(defender, 1)
    return effect


def _search_energy_attach_distributed(m, ability):
    count = int(m.group(1))
    return search_attach_energy(is_energy_card, count=count, distribute=True)


def _attach_hand_energy_capped(m, ability):
    cap = int(m.group(1))
    type_word = m.groupdict().get("type")

    def predicate(card) -> bool:
        if not is_basic_energy_card(card):
            return False
        return type_word is None or energy_provides_type(
            card, TYPE_WORDS[type_word].value)

    async def effect(ctx):
        await ctx.deal_damage()
        hand = [card for card in ctx.hand() if predicate(card)]
        if not hand:
            return
        picks = await ctx.choose_cards(hand, cap, minimum=0,
                                       prompt="Choose Energy to attach")
        candidates = ctx.my_pokemon_in_play()
        for card in picks:
            if not candidates:
                break
            target = await ctx.choose_pokemon(
                candidates, "Choose a Pokémon to attach the Energy to")
            if target is not None:
                await ctx.attach_energy(card, target)
    return effect


def _smokescreen_use_attack(m, ability):
    return smokescreen_attack()



def _switch_self_typed(m, ability):
    type_word = m.groupdict().get("type")
    if not type_word:
        return switch_self_attack()
    type_value = TYPE_WORDS[type_word].value

    def predicate(pokemon) -> bool:
        return is_pokemon_of_type(pokemon, type_word)
    return switch_self_attack(bench_predicate=predicate)


def _ultra_beast_count(m, ability):
    from ptcgo.game.data_utils import subtypes_for

    def predicate(pokemon) -> bool:
        return any(subtype.lower() == "ultra beast"
                   for subtype in subtypes_for(pokemon.archetype_id))
    return _more(count_in_play("mine", predicate), ability, int(m.group(1)))


def _heal_all_own(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_pokemon_in_play():
            damage = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
            if damage > 0:
                await ctx.heal(damage, pokemon)
    return effect


def _attach_discard_typed_self(m, ability):
    count = int(m.group(1))
    type_word = m.groupdict().get("type")

    def predicate(card) -> bool:
        if not is_energy_card(card):
            return False
        return type_word is None or energy_provides_type(
            card, TYPE_WORDS[type_word].value)

    async def effect(ctx):
        await ctx.deal_damage()
        cards = [card for card in ctx.discard_pile() if predicate(card)]
        if not cards or ctx.attacker is None:
            return
        picks = await ctx.choose_cards(cards, count, minimum=0,
                                       prompt="Choose Energy to attach")
        for card in picks:
            await ctx.attach_energy(card, ctx.attacker)
    return effect


def _discard_all_typed_self(m, ability):
    type_word = m.groupdict().get("type")
    return self_energy_discard_attack(
        all_energy=True,
        energy_type=TYPE_WORDS[type_word] if type_word else None)


def _move_all_energy_to_bench(m, ability):
    return energy_move_attack(count=99)


def _flip_tails_nothing_else_shield(m, ability):
    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if not (results and results[0]):
            return
        from ptcgo.game.card_effects.passives_common import apply_protection
        await ctx.deal_damage()
        await apply_protection(ctx, prevent=True)
    return effect


def _lock_opponent_energy_stadium(m, ability):
    from ptcgo.game.attributes import CardType, TrainerType

    async def effect(ctx):
        await ctx.deal_damage()
        ctx.lock_plays(
            ctx.opponent_id,
            lambda card: (card.get_attribute(AttrID.CARD_TYPE) == CardType.TRAINER.value
                          and card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value)
            or (card.get_attribute(AttrID.CARD_TYPE) == CardType.ENERGY.value
                and is_special_energy(card)),)
    return effect


def _flip_recover_up_to_heads(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_until_tails(getattr(ability, "title", ""))
        if heads <= 0:
            return
        cards = [card for card in ctx.discard_pile()]
        if not cards:
            return
        picks = await ctx.choose_cards(cards, heads, minimum=0,
                                       prompt="Choose cards to put into your hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
    return effect


def _ko_if_condition(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        present = condition.name in (
            defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
        if present:
            await ctx.knock_out(defender)
    return effect


def _ko_any_condition(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        if defender.get_attribute(AttrID.SPECIAL_CONDITIONS):
            await ctx.knock_out(defender)
    return effect


def _gate_if_damaged(m, ability):
    async def effect(ctx):
        defender = ctx.defender
        if defender is None:
            return
        if ctx.max_hp(defender) > defender.get_attribute(AttrID.HP, 0):
            await ctx.deal_damage()
    return effect


def _base_plus_if_any_condition(m, ability):
    from ptcgo.game.card_effects.attacks_common import defender_has_any_condition
    return bonus_if(defender_has_any_condition, int(m.group(2)),
                    base=int(m.group(1)))


def _base_plus_if_condition(m, ability):
    return bonus_if(defender_has_condition(CONDITIONS[m.group(1)]),
                    int(m.group(3)), base=int(m.group(2)))


def _flip_times_heads(m, ability):
    return flip_damage(coins=_count(m.group(1)), per_heads=int(m.group(2)))


def _base_plus_if_hand_equal(m, ability):
    return bonus_if(hand_sizes_equal, int(m.group(2)), base=int(m.group(1)))


def _base_plus_stadium_then_discard(m, ability):
    async def effect(ctx):
        base = int(m.group(1)) + int(m.group(2))
        if ctx.stadium_in_play() is not None:
            await ctx.deal_damage(base)
            await ctx.discard_stadium()
        else:
            await ctx.deal_damage(int(m.group(1)))
    return effect


def _snipe_undamaged(m, ability):
    amount, count = int(m.group(2)), _count(m.group(1))

    async def effect(ctx):
        candidates = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                      if ctx.max_hp(pokemon) == pokemon.get_attribute(AttrID.HP, 0)]
        if not candidates:
            return
        picks = candidates if len(candidates) <= count else \
            await ctx.choose_cards(candidates, count,
                                   prompt=f"Choose a Pokémon to take {amount} damage")
        for target in picks:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False)
    return effect


def _flip_heads_spread_all(m, ability):
    async def spread(ctx):
        for pokemon in ctx.opponent_pokemon_in_play():
            await ctx.deal_damage(int(m.group(1)), target=pokemon,
                                  apply_modifiers=False)
    return flip_gate(spread)


def _search_evolution_to_hand(m, ability):
    return search_to_hand(_is_evolution_card, count=1, reveal=True)


def _remove_counters_each_bench(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_bench():
            await ctx.heal(count * 10, pokemon)
    return effect


def _base_plus_per_energy_cards_defender(m, ability):
    return damage_per(count_energy("defender"), int(m.group(2)),
                      base=int(m.group(1)))


def _base_plus_threshold_counters(m, ability):
    return bonus_if(_defender_counters_at_least(int(m.group(1))),
                    int(m.group(3)), base=int(m.group(2)))


def _search_trainer_show(m, ability):
    return search_to_hand(_is_trainer_card, count=1, reveal=True)


def _is_evolution_card(card) -> bool:
    from ptcgo.game.attributes import PokemonStage
    stage = card.get_attribute(AttrID.STAGE)
    return stage not in (None, PokemonStage.BASIC.value, PokemonStage.UNSET.value)


def _is_trainer_card(card) -> bool:
    from ptcgo.game.attributes import CardType
    return card.get_attribute(AttrID.CARD_TYPE) == CardType.TRAINER.value


def _counters_on_bench_chosen(m, ability):
    counters = int(m.group(1))
    targets = _count(m.group(2)) if m.lastindex and m.lastindex >= 2 else 1

    async def effect(ctx):
        bench = ctx.opponent_bench()
        if not bench:
            return
        picks = bench if len(bench) <= targets else await ctx.choose_cards(
            bench, targets, prompt="Choose a Benched Pokémon")
        for target in picks:
            await ctx.deal_damage(counters * 10, target=target, as_counters=True)
    return effect


def _lock_until_leaves(m, ability):
    """'This Pokemon can't use <this attack> again until it leaves the Active
    spot': attack locks are cleared when the Pokemon leaves the Active spot,
    so a far turn number is exactly that lifetime."""
    named = normalize(m.group(1))
    if named != normalize(getattr(ability, "title", "")):
        return None

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None and ability.ability_id:
            state = ctx.session.turn_state
            state.attack_locks[(ctx.attacker.entity_id,
                                ability.ability_id)] = state.turn_number + 999
    return effect


def _gate_entered_active(m, ability):
    async def effect(ctx):
        if ctx.attacker is not None and ctx.entered_active_this_turn(ctx.attacker):
            await ctx.deal_damage()
    return effect


def _ko_chosen_basic_non_gx(m, ability):
    from ptcgo.game.data_utils import subtypes_for
    from ptcgo.game.session.effects import is_basic_pokemon

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                      if is_basic_pokemon(pokemon)
                      and not any(subtype.lower() == "gx"
                                  for subtype in subtypes_for(pokemon.archetype_id))
                      and not ctx.effects_blocked(pokemon)]
        if not candidates:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Pokémon to knock out")
        if target is not None:
            await ctx.knock_out(target)
    return effect


def _opponent_bench_to_hand(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.opponent_bench()
        if not bench:
            return
        picks = bench if len(bench) <= count else await ctx.choose_cards(
            bench, count, prompt="Choose Benched Pokémon to return to hand")
        for pokemon in picks:
            await ctx.put_in_hand([pokemon] + list(pokemon.children or []),
                                  reveal=True)
    return effect


def _evolve_from_deck_any(m, ability):
    from ptcgo.game.content.definitions import evolves_from

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = ctx.my_pokemon_in_play()
        if not candidates:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Pokémon to evolve")
        if target is None:
            return
        logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        if not logic_name:
            return
        picks = await ctx.search_deck(
            lambda card: evolves_from(getattr(card, "archetype_id", None) or "",
                                      logic_name),
            count=1, minimum=0, prompt="Choose an Evolution card")
        if picks:
            await ctx.evolve_pokemon(target, picks[0])
        await ctx.shuffle_deck()
    return effect


def _damage_times_both_actives_energy(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        count = count_energy("my_active")(ctx) + count_energy("defender")(ctx)
        amount = per * count
        if amount > 0:
            await ctx.deal_damage(amount, ignore_weakness=True,
                                  ignore_resistance=True)
    return effect


def _flip_tails_nothing_heads_shield_all(m, ability):
    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if not (results and results[0]):
            return
        from ptcgo.game.card_effects.passives_common import apply_protection
        await ctx.deal_damage()
        await apply_protection(ctx, prevent=True, effects_too=True)
    return effect


def _bonus_extra_energy_snipe(m, ability):
    required = int(m.group(1))
    type_word = m.groupdict().get("type")
    amount = int(m.group(3))

    async def effect(ctx):
        if not _extra_energy_attached(required, type_word)(ctx):
            return
        bench = ctx.opponent_bench()
        if not bench:
            return
        target = bench[0] if len(bench) == 1 else await ctx.choose_cards(
            bench, 1, prompt=f"Choose a Pokémon to take {amount} damage")
        for pick in (target if isinstance(target, list) else [target]):
            await ctx.deal_damage(amount, target=pick, apply_modifiers=False)
    return effect


def _attacker_subtypes(calc):
    from ptcgo.game.data_utils import subtypes_for
    if calc.attacker is None:
        return set()
    return {subtype.lower() for subtype in subtypes_for(calc.attacker.archetype_id)}


def _passive_prevent_from_ex_or_v(m, ability):
    def pred(calc, carrier) -> bool:
        return bool(_attacker_subtypes(calc) & {"ex", "v", "vmax", "vstar"})
    return prevent_damage_when(pred)


def _passive_prevent_from_type(m, ability):
    type_word = m.group(1)
    type_value = TYPE_WORDS[type_word].value

    def pred(calc, carrier) -> bool:
        attacker = calc.attacker
        if attacker is None:
            return False
        return is_pokemon_of_type(attacker, type_word)
    return prevent_damage_when(pred)


def _passive_prevent_from_ability_holders(m, ability):
    def pred(calc, carrier) -> bool:
        attacker = calc.attacker
        if attacker is None:
            return False
        definition = def_for(getattr(attacker, "archetype_id", None) or "")
        return any(not isinstance(a, Attack)
                   for a in getattr(definition, "abilities", []) or [])
    return prevent_damage_when(pred)


def _passive_effect_shield(m, ability):
    from ptcgo.game.card_effects.passives_common import attack_effect_shield_passive
    return attack_effect_shield_passive(protects="carrier")


def _passive_effect_shield_no_damage(m, ability):
    from ptcgo.game.card_effects.passives_common import attack_effect_shield_passive
    return attack_effect_shield_passive(protects="carrier")



def _damaging_attacker(ctx):
    return getattr(ctx, "damaged_by", None) or getattr(ctx, "ko_attacker", None)


def _counters_on_attacker(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        attacker = _damaging_attacker(ctx)
        if attacker is not None:
            await ctx.deal_damage(counters * 10, target=attacker,
                                  as_counters=True)
    return effect


def _condition_on_attacker(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        attacker = _damaging_attacker(ctx)
        if attacker is not None:
            await ctx.apply_special_condition(attacker, condition)
    return effect


def _knock_out_attacker(m, ability):
    async def effect(ctx):
        attacker = _damaging_attacker(ctx)
        if attacker is not None:
            await ctx.knock_out(attacker)
    return effect


def _passive_takes_less_flat(m, ability):
    return takes_less_passive(int(m.group(1)))


def _passive_flip_prevent_all(m, ability):
    return flip_prevent_damage_passive()


def _passive_basic_free_retreat(m, ability):
    return retreat_free_when(
        lambda pokemon, carrier: pokemon.owning_player_id
        == carrier.owning_player_id
        and pokemon.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value)


def _search_attach_basic_energy_distributed(m, ability):
    count = int(m.group(1))
    type_word = m.groupdict().get("type")
    predicate = (lambda card: is_basic_energy_card(card)
                 and energy_provides_type(card, TYPE_WORDS[type_word].value)) \
        if type_word else is_basic_energy_card
    return search_attach_energy(predicate, count=count, distribute=True)


def _counters_on_chosen_opponents(m, ability):
    targets = _count(m.group(1)) if m.group(1) else 1
    counters = int(m.group(2))

    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        picks = candidates if len(candidates) <= targets else \
            await ctx.choose_cards(candidates, targets,
                                   prompt=f"Choose {targets} Pokémon")
        for target in picks:
            if not ctx.effects_blocked(target):
                await ctx.deal_damage(counters * 10, target=target,
                                      as_counters=True)
    return effect


def _reorder_own_top(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.reorder_deck_top(count, ctx.player_id,
                                   "Put the top cards back in any order")
    return effect


def _raise_defender_retreat(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        from ptcgo.game.card_effects.passives_common import (
            apply_defender_retreat_cost_raise,
        )
        await apply_defender_retreat_cost_raise(ctx, extra=1)
    return effect


def _bonus_if_opponent_prizes_at_most(m, ability):
    limit, bonus = int(m.group(1)), int(m.group(2))
    return bonus_if(
        lambda ctx: count_prizes_remaining("opponent")(ctx) <= limit, bonus)


def _less_per_defender_retreat_colorless(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        amount = max(0, printed - per * defender_retreat_cost(ctx))
        await ctx.deal_damage(amount)
    return effect


def _switch_active_with_bench(m, ability):
    async def effect(ctx):
        bench = ctx.my_bench()
        if not bench:
            return
        if len(bench) == 1:
            target = bench[0]
        else:
            target = await ctx.choose_pokemon(
                bench, "Choose a Benched Pokémon to switch in")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    return effect


def _flip_bonus_and_heal_self(m, ability):
    bonus, heal = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await ctx.deal_damage(printed + bonus)
            if ctx.attacker is not None:
                await ctx.heal(heal, ctx.attacker)
        else:
            await ctx.deal_damage(printed)
    return effect


def _own_next_turn_all_boost(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        from ptcgo.game.card_effects.passives_common import (
            apply_own_next_turn_boost,
        )
        await apply_own_next_turn_boost(ctx, amount)
    return effect


def _passive_survive_full_hp(m, ability):
    from ptcgo.game.card_effects.passives_common import guts_survive_passive
    return guts_survive_passive(hp_floor=int(m.group(1)), flip=False,
                                require_full_hp=True)


def _passive_bench_damage_shield(m, ability):
    return prevent_damage_when(
        lambda calc, carrier: calc.target is carrier_pokemon(carrier)
        and not is_in_active_spot(calc.target), any_side=True)


def _passive_opponent_retreat_tax(m, ability):
    return opponent_retreat_tax_passive(1)


def _flip_per_self_energy(m, ability):
    per = int(m.group(1))
    return flip_damage(coins_from=count_energy("self", cards=True), per_heads=per)


def _prevent_attack_damage_next_turn(m, ability):
    return protect_next_turn(prevent=True)


def _retaliate_counters_rider(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            ctx.add_passive_through_opponents_turn(
                ctx.attacker, retaliate_counters_passive(counters))
    return effect


def _prevent_damage_at_most_next_turn(m, ability):
    limit = int(m.group(1))
    return _prevent_attack_damage_next_turn_limited(m, ability, limit)


def _prevent_attack_damage_next_turn_limited(m, ability, limit=None):
    if limit is None:
        limit = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            ctx.add_passive_through_opponents_turn(
                ctx.attacker,
                prevent_damage_when(
                    lambda calc, carrier: calc.amount <= limit))
    return effect


def _self_bench_spread(m, ability):
    amount = int(m.group(1))
    count = _count(m.group(2)) if m.group(2) else 1

    async def effect(ctx):
        await ctx.deal_damage()
        bench = [pokemon for pokemon in ctx.my_bench()
                 if not ctx.effects_blocked(pokemon)]
        if not bench:
            return
        picks = bench if len(bench) <= count else \
            await ctx.choose_cards(bench, count,
                                   prompt=f"Choose {count} Benched Pokémon")
        for target in picks:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False)
    return effect


def _base_plus_per_bench(m, ability):
    return damage_per(count_bench("mine"), int(m.group(2)),
                      base=int(m.group(1)))


def _snipe_chosen_plain(m, ability):
    count = _count(m.group(1))
    amount = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        picks = candidates if len(candidates) <= count else \
            await ctx.choose_cards(candidates, count,
                                   prompt=f"Choose {count} Pokémon")
        for target in picks:
            if target is ctx.opponent_active():
                await ctx.deal_damage(amount, target=target)
            elif not ctx.effects_blocked(target):
                await ctx.deal_damage(amount, target=target,
                                      apply_modifiers=False)
    return effect


def _discard_self_energy_then_spread(m, ability):
    cost, amount = int(m.group(1)), int(m.group(2))
    count = _count(m.group(3)) if m.group(3) else 1

    async def effect(ctx):
        attacker = ctx.attacker
        if attacker is None:
            return
        if len(ctx.attached_energies(attacker)) < cost:
            return
        await ctx.discard_energy_from(attacker, cost,
                                      prompt=f"Choose {cost} Energy to discard")
        await ctx.deal_damage()
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        targets = candidates if len(candidates) <= count else \
            await ctx.choose_cards(candidates, count,
                                   prompt=f"Choose {count} Pokémon")
        for target in targets:
            if target is ctx.opponent_active():
                await ctx.deal_damage(amount, target=target)
            elif not ctx.effects_blocked(target):
                await ctx.deal_damage(amount, target=target,
                                      apply_modifiers=False)
    return effect


def _flip_per_typed_energy(m, ability):
    per = int(m.group(2))
    type_word = m.group(1)
    predicate = count_energy("self", TYPE_WORDS[type_word]) if type_word else \
        count_energy("self", cards=True)

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        coins = predicate(ctx)
        results = await ctx.flip_coins(coins, getattr(ability, "title", "")) \
            if coins else []
        heads = sum(1 for result in results or [] if result)
        await ctx.deal_damage(printed + per * heads)
    return effect


def _times_self_damage_counters(m, ability):
    per = int(m.group(1))

    def counters(ctx) -> int:
        attacker = ctx.attacker
        if attacker is None:
            return 0
        missing = ctx.max_hp(attacker) - attacker.get_attribute(AttrID.HP, 0)
        return max(0, missing // 10)

    return damage_per(counters, per)


def _next_turn_boost_opposing_active(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        from ptcgo.game.card_effects.passives_common import (
            apply_own_next_turn_boost,
        )
        await apply_own_next_turn_boost(ctx, amount)
    return effect


def _named_self_damage(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.deal_damage(amount, target=ctx.attacker,
                                  apply_modifiers=False)
    return effect


def _spread_ignore_weakness_resistance(m, ability):
    amount = int(m.group(1))
    count = _count(m.group(2)) if m.group(2) else 1

    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        picks = candidates if len(candidates) <= count else \
            await ctx.choose_cards(candidates, count,
                                   prompt=f"Choose {count} Pokémon")
        for target in picks:
            if not ctx.effects_blocked(target):
                await ctx.deal_damage(amount, target=target,
                                      ignore_weakness=True,
                                      ignore_resistance=True)
    return effect


def _bonus_if_opponent_prizes_exactly(m, ability):
    limit, bonus = int(m.group(1)), int(m.group(2))
    return bonus_if(
        lambda ctx: count_prizes_remaining("opponent")(ctx) == limit, bonus)


def _bonus_if_deck_at_most(m, ability):
    limit, bonus = int(m.group(1)), int(m.group(2))
    return bonus_if(lambda ctx: len(ctx.deck()) <= limit, bonus)


def _bench_chosen_spread(m, ability):
    count = _count(m.group(1))
    amount = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        bench = [pokemon for pokemon in ctx.opponent_bench()
                 if not ctx.effects_blocked(pokemon)]
        if not bench:
            return
        picks = bench if len(bench) <= count else \
            await ctx.choose_cards(bench, count,
                                   prompt=f"Choose {count} Benched Pokémon")
        for target in picks:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False)
    return effect


def _search_typed_basic_to_bench(m, ability):
    type_value = TYPE_WORDS[m.group(2)].value

    def predicate(card) -> bool:
        return is_basic(card) and type_value in (
            card.get_attribute(AttrID.POKEMON_TYPES) or [])
    return search_to_bench(predicate=predicate, count=_count(m.group(1)))


def _counters_then_self_knock_out(m, ability):
    counters = int(m.group(1))
    targets = _count(m.group(2)) if m.group(2) else 1

    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        picks = candidates if len(candidates) <= targets else \
            await ctx.choose_cards(candidates, targets,
                                   prompt=f"Choose {targets} Pokémon")
        for target in picks:
            await ctx.deal_damage(counters * 10, target=target,
                                  as_counters=True)
        await ctx.knock_out(ctx.source)
    return effect


def _bench_self_switch_in(m, ability):
    async def effect(ctx):
        if ctx.source in ctx.my_bench():
            await ctx.switch_active(ctx.player_id, ctx.source)
    return effect


def _passive_no_energy_free_retreat(m, ability):
    return no_energy_free_retreat_passive()


def _passive_opponent_active_retreat_tax(m, ability):
    return opponent_retreat_tax_passive(1, active_only=True)


def _flip_plus_bonus_else_condition(m, ability):
    base, bonus, tails = int(m.group(1)), int(m.group(2)), int(m.group(3))
    condition = CONDITIONS[m.group(4)]

    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await ctx.deal_damage(base + bonus)
            return
        await ctx.deal_damage(tails)
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _heal_and_cure_self(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
            await ctx.cure_all_conditions(ctx.attacker)
    return effect


def _damage_each_defending(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage(amount)
    return effect


def _discard_hand_card_then_draw(m, ability):
    count = int(m.group(1))
    if ability.activation is None and ability.trigger is None:
        ability.activation = Activations.ONCE_PER_TURN

    async def effect(ctx):
        if not ctx.hand():
            return
        discarded = await ctx.discard_from_hand(
            1, minimum=1, prompt="Discard a card to use this Ability")
        if discarded:
            await ctx.draw_cards(count)
    return effect


def _gate_hand_exactly(m, ability):
    required = int(m.group(1))

    async def effect(ctx):
        if len(ctx.hand()) != required:
            return
        await ctx.deal_damage()
    return effect


def _discard_hand_card_if_do_draw(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        if ctx.is_attack_effect():
            await ctx.deal_damage()
        if not ctx.hand():
            return
        discarded = await ctx.discard_from_hand(
            1, minimum=0, prompt="You may discard a card to draw")
        if discarded:
            await ctx.draw_cards(count)
    return effect


def _discard_all_self_then_spread(m, ability):
    amount = int(m.group(1))
    count = _count(m.group(2)) if m.group(2) else 1

    async def effect(ctx):
        attacker = ctx.attacker
        if attacker is not None:
            energies = ctx.attached_energies(attacker)
            if energies:
                await ctx.discard_energy_from(attacker, len(energies))
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        picks = candidates if len(candidates) <= count else \
            await ctx.choose_cards(candidates, count,
                                   prompt=f"Choose {count} Pokémon")
        for target in picks:
            if target is ctx.opponent_active():
                await ctx.deal_damage(amount, target=target)
            elif not ctx.effects_blocked(target):
                await ctx.deal_damage(amount, target=target,
                                      apply_modifiers=False)
    return effect


def _bonus_vs_evolved_discard_all(m, ability):
    bonus = int(m.group(1))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        evolved = defender_is_evolved(ctx)
        await ctx.deal_damage(printed + bonus if evolved else printed)
        attacker = ctx.attacker
        if evolved and attacker is not None:
            energies = ctx.attached_energies(attacker)
            if energies:
                await ctx.discard_energy_from(attacker, len(energies))
    return effect


def _minus_per_self_counter(m, ability):
    base, per = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        attacker = ctx.attacker
        counters = 0
        if attacker is not None:
            counters = max(0, (ctx.max_hp(attacker)
                               - attacker.get_attribute(AttrID.HP, 0)) // 10)
        amount = max(0, base - per * counters)
        if amount > 0:
            await ctx.deal_damage(amount)
    return effect


def _optional_discard_energy_bonus(m, ability):
    bonus = int(m.group(1))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        attacker = ctx.attacker
        extra = 0
        if attacker is not None and ctx.attached_energies(attacker) and \
                await ctx.ask_yes_no(
                    f"Discard an Energy from this Pokémon for {bonus} more "
                    f"damage?"):
            if await ctx.discard_energy_from(attacker, 1):
                extra = bonus
        if printed + extra > 0:
            await ctx.deal_damage(printed + extra)
    return effect


def _flip_until_tails_base_plus(m, ability):
    return flip_damage(until_tails=True, base=int(m.group(1)),
                       bonus_per_heads=int(m.group(2)))


def _flip_condition_else_nothing(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if not (results and results[0]):
            return
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _gust_you_choose(m, ability):
    return gust_attack()


def _condition_each_defending(m, ability):
    return condition_attack(CONDITIONS[m.group(1)])


def _gust_switch_then_damage_new(m, ability):
    return gust_attack(damage_before=0, damage_to_new_active=int(m.group(1)))


def _flip_two_both_tails_nothing(m, ability):
    coins = _count(m.group(1))

    async def effect(ctx):
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        if results and not any(results):
            return
        await ctx.deal_damage()
    return effect


def _flip_heal_self(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0] and ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
    return effect


def _search_any_pokemon_reveal(m, ability):
    return search_to_hand(_is_pokemon_card, count=1, reveal=True)


def _opponent_draws(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.draw_cards(count, ctx.opponent_id)
    return effect


def _recover_basic_energy_up_to(m, ability):
    return recover_from_discard(predicate=is_basic_energy_card,
                                count=int(m.group(1)), minimum=0)


def _recover_trainer(m, ability):
    return recover_from_discard(predicate=_is_trainer_card, count=1)


def _heal_if_defender_condition(m, ability):
    condition = CONDITIONS[m.group(1)]
    amount = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.attacker is None:
            return
        if getattr(condition, "value", condition) in _condition_values(defender):
            await ctx.heal(amount, ctx.attacker)
    return effect


def _base_plus_if_more_prizes(m, ability):
    base, bonus = int(m.group(1)), int(m.group(2))
    return bonus_if(_prize_comparison("more"), bonus, base=base)


def _typed_energy_to_hand(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        pool = [energy for energy in ctx.attached_energies(attacker)
                if energy_provides_type(energy, type_value)]
        if not pool:
            return
        picks = pool if len(pool) <= count else await ctx.choose_cards(
            pool, count, prompt="Choose Energy to put into your hand")
        await ctx.put_in_hand(picks, reveal=False)
    return effect


def _shuffle_self_into_deck_forced(m, ability):
    return remove_self_from_play(destination="deck", optional=False)


def _extra_prize_vs_gx_ex(m, ability):
    prizes = int(m.group(1))
    from ptcgo.game.data_utils import subtypes_for

    def target_predicate(pokemon) -> bool:
        subtypes = {subtype.lower()
                    for subtype in subtypes_for(pokemon.archetype_id)}
        return bool(subtypes & {"gx", "ex"})

    async def effect(ctx):
        await ctx.deal_damage()
        ctx.add_extra_prize_watcher(target_predicate=target_predicate,
                                    prizes=prizes)
    return effect


def _shield_effects_only(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        from ptcgo.game.card_effects.passives_common import apply_protection
        await apply_protection(ctx, effects_too=True)
    return effect


def _shield_from_gx_ex_next_turn(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            ctx.add_passive_through_opponents_turn(
                ctx.attacker,
                prevent_damage_when(lambda calc, carrier: carrier_pokemon(
                    carrier) is calc.target and bool(
                        _attacker_subtypes(calc) & {"gx", "ex"})))
    return effect


def _flip_prevent_next_turn(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            ctx.add_passive_through_opponents_turn(
                ctx.attacker, flip_prevent_damage_passive(
                    getattr(ability, "title", "")))
    return effect


def _flip_tails_lock_self(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and not results[0] and ctx.attacker is not None:
            from ptcgo.game.card_effects.attacks_common import lock_all_attacks
            lock_all_attacks(ctx, ctx.attacker)
    return effect


def _ko_if_exact_counters(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        defender = ctx.defender
        before = None
        if defender is not None:
            before = (ctx.max_hp(defender)
                      - defender.get_attribute(AttrID.HP, 0)) // 10
        await ctx.deal_damage()
        if defender is None or before != counters or \
                ctx.effects_blocked(defender):
            return
        await ctx.knock_out(defender)
    return effect


def _heal_everyone(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
            if ctx.max_hp(pokemon) > pokemon.get_attribute(AttrID.HP, 0):
                await ctx.heal(amount, pokemon)
    return effect


def _opponent_shuffles_hand_draws(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        hand = ctx.hand(ctx.opponent_id)
        if hand:
            await ctx.shuffle_into_deck(list(hand), ctx.opponent_id)
        await ctx.draw_cards(count, ctx.opponent_id)
    return effect


def _search_any_card_optional(m, ability):
    return search_to_hand(None, count=1, minimum=0, reveal=False)


def _counters_each_damaged_opponent(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_pokemon_in_play():
            if ctx.max_hp(pokemon) <= pokemon.get_attribute(AttrID.HP, 0):
                continue
            if ctx.effects_blocked(pokemon):
                continue
            await ctx.deal_damage(counters * 10, target=pokemon,
                                  as_counters=True)
    return effect


def _spread_every_bench(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_bench() + ctx.opponent_bench():
            if pokemon in ctx.opponent_bench() and ctx.effects_blocked(pokemon):
                continue
            await ctx.deal_damage(amount, target=pokemon, apply_modifiers=False)
    return effect


def _entered_active_bonus_condition(m, ability):
    bonus = int(m.group(1))
    condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        entered = ctx.attacker is not None and \
            ctx.entered_active_this_turn(ctx.attacker)
        await ctx.deal_damage(printed + bonus if entered else printed)
        defender = ctx.defender
        if entered and defender is not None and \
                not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _only_while_active(inner):
    """Ability text gated on 'if this Pokemon is in the Active Spot'."""
    async def effect(ctx):
        if ctx.source is None or not is_in_active_spot(ctx.source):
            return
        await inner(ctx)
    return effect


def _passive_bench_team_shield(m, ability):
    return prevent_damage_when(
        lambda calc, carrier: calc.target.owning_player_id
        == carrier.owning_player_id and not is_in_active_spot(calc.target))


def _passive_flip_survive(m, ability):
    return guts_survive_passive(hp_floor=int(m.group(1)),
                                title=getattr(ability, "title", ""), flip=True)


def _passive_special_energy_hp(m, ability):
    from ptcgo.game.card_effects.passives_common import hp_bonus_tool
    return hp_bonus_tool(int(m.group(1)), holder_pred=lambda pokemon: any(
        is_special_energy(card) for card in (pokemon.children or [])))


def _passive_active_team_takes_less(m, ability):
    return takes_less_passive(
        int(m.group(1)),
        protects=lambda target, carrier: target.owning_player_id
        == carrier.owning_player_id
        and is_in_active_spot(carrier_pokemon(carrier)))


def _passive_active_vs_active_debuff(m, ability):
    return active_vs_active_debuff_passive(int(m.group(1)))


def _passive_condition_immunity(m, ability):
    return condition_immunity_passive(CONDITIONS[m.group(1)])


def _passive_typed_energy_free_retreat(m, ability):
    return typed_energy_free_retreat_passive(TYPE_WORDS[m.group(1)].value)


def _passive_team_typed_energy_free_retreat(m, ability):
    return typed_energy_free_retreat_passive(TYPE_WORDS[m.group(1)].value,
                                             team=True)


def _passive_bench_active_retreat_discount(m, ability):
    amount = m.group(1).count("colorless")
    return retreat_discount(
        amount, target_pred=lambda pokemon, carrier: pokemon.owning_player_id
        == carrier.owning_player_id and is_in_active_spot(pokemon)
        and not is_in_active_spot(carrier_pokemon(carrier)))


def _passive_benched_full_shield(m, ability):
    return benched_full_shield_passive()


def _discard_pokemon_heal_self(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        if not any(_is_pokemon_card(card) for card in ctx.hand()):
            return
        discarded = await ctx.discard_from_hand(
            1, minimum=0, predicate=_is_pokemon_card,
            prompt="You may discard a Pokémon to heal")
        if discarded and ctx.source is not None:
            await ctx.heal(amount, ctx.source)
    return effect


def _attach_typed_hand_energy_to_one(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        hand = [card for card in ctx.hand() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_pokemon_in_play()
        if not hand or not candidates:
            return
        picks = await ctx.choose_cards(hand, 1, minimum=0,
                                       prompt="Choose an Energy to attach")
        if not picks:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates,
                                     "Choose a Pokémon to attach the Energy to")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _top_pick_rest_bottom(m, ability):
    look, keep = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        top = ctx.deck_top(look)
        if not top:
            return
        picks = top if len(top) <= keep else await ctx.choose_cards(
            top, keep, prompt=f"Choose {keep} card(s) to put into your hand")
        await ctx.put_in_hand(list(picks), reveal=False)
        for card in top:
            if card not in picks:
                await ctx.put_on_bottom_of_deck(card)
    return effect


def _base_plus_from_phrase(m, ability):
    counter = COUNT_PHRASES.get(m.group(3).strip())
    if counter is None:
        return None
    return damage_per(counter, int(m.group(2)), base=int(m.group(1)))


def _times_number_from_phrase(m, ability):
    counter = COUNT_PHRASES.get(m.group(2).strip())
    if counter is None:
        return None
    return damage_per(counter, int(m.group(1)))


def _flip_protect_all(m, ability):
    return flip_protection(prevent=True, effects_too=True)


def _flip_protect_damage(m, ability):
    return flip_protection(prevent=True)


def _remove_self_counters(m, ability):
    amount = int(m.group(1)) * 10

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
    return effect


def _flip_remove_self_counters(m, ability):
    amount = int(m.group(1)) * 10

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0] and ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
    return effect


def _cure_self(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.cure_all_conditions(ctx.attacker)
    return effect


def _cure_heal_sleep_self(m, ability):
    amount = int(m.group(1)) * 10

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        await ctx.cure_all_conditions(attacker)
        await ctx.heal(amount, attacker)
        await ctx.apply_special_condition(attacker, SpecialConditions.ASLEEP)
    return effect


def _energy_cost_then_damage(m, ability):
    text = m.group(0)
    everything = m.group("all") is not None
    count = 0 if everything else _count(m.group("count"))
    type_word = m.group("type")
    type_value = TYPE_WORDS[type_word].value if type_word else None
    basic = m.group("basic") is not None

    def matches(card) -> bool:
        if basic and not is_basic_energy_card(card):
            return False
        return type_value is None or energy_provides_type(card, type_value)

    async def effect(ctx):
        attacker = ctx.attacker
        if attacker is None:
            return
        pool = [energy for energy in ctx.attached_energies(attacker)
                if matches(energy)]
        if everything:
            if pool:
                await ctx.discard_energy_from(attacker, len(pool),
                                              predicate=matches)
        else:
            if len(pool) < count:
                return
            await ctx.discard_energy_from(
                attacker, count, predicate=matches,
                prompt=f"Choose {count} Energy to discard")
        await ctx.deal_damage()
    return effect


def _flip_times_heads_self_condition(m, ability):
    return flip_damage(coins=int(m.group(1)), per_heads=int(m.group(2)),
                       also=_self_condition_rider(CONDITIONS[m.group(3)]))


def _self_condition_rider(condition):
    async def rider(ctx):
        if ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker, condition)
    return rider


def _flip_plus_else_self_damage(m, ability):
    base, bonus, recoil = int(m.group(1)), int(m.group(2)), int(m.group(3))

    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await ctx.deal_damage(base + bonus)
            return
        await ctx.deal_damage(base)
        if ctx.attacker is not None:
            await ctx.deal_damage(recoil, target=ctx.attacker,
                                  apply_modifiers=False)
    return effect


def _optional_base_plus_self_damage(m, ability):
    base, bonus, recoil = int(m.group(1)), int(m.group(2)), int(m.group(3))

    async def effect(ctx):
        if await ctx.ask_yes_no(f"Do {bonus} more damage and take {recoil} "
                                f"damage yourself?"):
            await ctx.deal_damage(base + bonus)
            if ctx.attacker is not None:
                await ctx.deal_damage(recoil, target=ctx.attacker,
                                      apply_modifiers=False)
        else:
            await ctx.deal_damage(base)
    return effect


def _vulnerable_next_turn(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        from ptcgo.game.card_effects.passives_common import apply_protection
        await apply_protection(ctx, reduce=-amount)
    return effect


def _reduce_next_turn(m, ability):
    return protect_next_turn(reduce=int(m.group(1)))


def _attach_discard_energy_to_self(m, ability):
    type_word = m.group(1)
    type_value = TYPE_WORDS[type_word].value if type_word else None

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        pool = [card for card in ctx.discard_pile() if is_energy_card(card)
                and (type_value is None
                     or energy_provides_type(card, type_value))]
        if attacker is None or not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0,
                                       prompt="Choose an Energy to attach")
        if picks:
            await ctx.attach_energy(picks[0], attacker)
    return effect


def _flip_tails_counters_self(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and not results[0] and ctx.attacker is not None:
            await ctx.deal_damage(counters * 10, target=ctx.attacker,
                                  as_counters=True)
    return effect


def _counters_on_self(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.deal_damage(counters * 10, target=ctx.attacker,
                                  as_counters=True)
    return effect


def _each_player_draws(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.draw_cards(count)
        await ctx.draw_cards(count, ctx.opponent_id)
    return effect


def _flip_times_self_counters(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        attacker = ctx.attacker
        if not (results and results[0]) or attacker is None:
            return
        counters = max(0, (ctx.max_hp(attacker)
                           - attacker.get_attribute(AttrID.HP, 0)) // 10)
        if counters:
            await ctx.deal_damage(per * counters)
    return effect


def _attach_typed_hand_energy_to_self(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        hand = [card for card in ctx.hand() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        if attacker is None or not hand:
            return
        picks = await ctx.choose_cards(hand, 1, minimum=0,
                                       prompt="Choose an Energy to attach")
        if picks:
            await ctx.attach_energy(picks[0], attacker)
    return effect


def _flip_switch_self(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        bench = ctx.my_bench()
        if not (results and results[0]) or not bench:
            return
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to switch in")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    return effect



def _both_benches_and_recoil(m, ability):
    amount, recoil = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_bench() + ctx.opponent_bench():
            if pokemon in ctx.opponent_bench() and ctx.effects_blocked(pokemon):
                continue
            await ctx.deal_damage(amount, target=pokemon, apply_modifiers=False)
        if ctx.attacker is not None:
            await ctx.deal_damage(recoil, target=ctx.attacker,
                                  apply_modifiers=False)
    return effect


def _base_plus_if_less_energy(m, ability):
    base, bonus = int(m.group(1)), int(m.group(2))

    def cond(ctx) -> bool:
        attacker, defender = ctx.attacker, ctx.defender
        if attacker is None or defender is None:
            return False
        return len(ctx.attached_energies(attacker)) < \
            len(ctx.attached_energies(defender))
    return bonus_if(cond, bonus, base=base)


def _flip_tails_discard_self_energy(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and not results[0] and ctx.attacker is not None:
            await ctx.discard_energy_from(ctx.attacker, count)
    return effect


def _per_self_counter_then_flip_confuse(m, ability):
    base, per = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        attacker = ctx.attacker
        counters = 0
        if attacker is not None:
            counters = max(0, (ctx.max_hp(attacker)
                               - attacker.get_attribute(AttrID.HP, 0)) // 10)
        await ctx.deal_damage(base + per * counters)
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and not results[0] and ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker,
                                              SpecialConditions.CONFUSED)
    return effect


def _discard_card_to_deck_top(m, ability):
    return recover_from_discard(count=1, minimum=1, to="deck_top")


def _move_bench_energy_to_self_one(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        bench = [pokemon for pokemon in ctx.my_bench()
                 if ctx.attached_energies(pokemon)]
        if attacker is None or not bench:
            return
        source = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to move Energy from")
        if source is None:
            return
        energies = ctx.attached_energies(source)
        picks = energies if len(energies) == 1 else await ctx.choose_cards(
            energies, 1, prompt="Choose an Energy to move")
        if picks:
            await ctx.attach_energy(picks[0], attacker)
    return effect


def _flip_attach_basic_from_discard_self(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        pool = [card for card in ctx.discard_pile()
                if is_basic_energy_card(card)]
        if not (results and results[0]) or not pool or ctx.attacker is None:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0,
                                       prompt="Choose an Energy to attach")
        if picks:
            await ctx.attach_energy(picks[0], ctx.attacker)
    return effect


def _gate_bench_at_most(m, ability):
    limit = int(m.group(1))

    async def effect(ctx):
        if len(ctx.my_bench()) <= limit:
            return
        await ctx.deal_damage()
    return effect


def _flip_heads_bench_snipe(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        bench = [pokemon for pokemon in ctx.opponent_bench()
                 if not ctx.effects_blocked(pokemon)]
        if not (results and results[0]) or not bench:
            return
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon")
        if target is not None:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False)
    return effect


def _attach_discard_energy_to_bench(m, ability):
    type_word = m.groupdict().get("type")
    type_value = TYPE_WORDS[type_word].value if type_word else None
    basic = m.groupdict().get("basic") is not None

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.discard_pile() if is_energy_card(card)
                and (not basic or is_basic_energy_card(card))
                and (type_value is None
                     or energy_provides_type(card, type_value))]
        bench = ctx.my_bench()
        if not pool or not bench:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0,
                                       prompt="Choose an Energy to attach")
        if not picks:
            return
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to attach the Energy to")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _optional_typed_energy_move(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        bench = ctx.my_bench()
        pool = [energy for energy in ctx.attached_energies(attacker)
                if energy_provides_type(energy, type_value)] \
            if attacker is not None else []
        if not pool or not bench:
            return
        if not await ctx.ask_yes_no("Move an Energy to a Benched Pokémon?"):
            return
        picks = pool if len(pool) == 1 else await ctx.choose_cards(
            pool, 1, prompt="Choose an Energy to move")
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon")
        if picks and target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _flip_per_typed_energy_base_plus(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    base, per = int(m.group(2)), int(m.group(3))
    return flip_damage(coins_from=count_energy("self", TYPE_WORDS[m.group(1)]),
                       base=base, bonus_per_heads=per)


def _optional_trade_energy_discard(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker, defender = ctx.attacker, ctx.defender
        if attacker is None or defender is None:
            return
        if not ctx.attached_energies(attacker) or \
                not await ctx.ask_yes_no("Discard an Energy from this Pokémon "
                                         "to discard one from the opponent?"):
            return
        if await ctx.discard_energy_from(attacker, 1) and \
                not ctx.effects_blocked(defender):
            await ctx.discard_energy_from(defender, 1)
    return effect


def _flip_base_plus_heal_counters(m, ability):
    base, bonus, counters = int(m.group(1)), int(m.group(2)), int(m.group(3))

    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await ctx.deal_damage(base + bonus)
            if ctx.attacker is not None:
                await ctx.heal(counters * 10, ctx.attacker)
        else:
            await ctx.deal_damage(base)
    return effect


def _flip_lock_supporters(m, ability):
    from ptcgo.game.attributes import CardType, TrainerType

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            ctx.lock_plays(
                ctx.opponent_id,
                lambda card: card.get_attribute(AttrID.CARD_TYPE)
                == CardType.TRAINER.value
                and card.get_attribute(AttrID.TRAINER_TYPE)
                == TrainerType.SUPPORTER.value)
    return effect


def _lock_opponent_special_energy(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        ctx.lock_plays(ctx.opponent_id, is_special_energy)
    return effect


def _flip_discard_random_opponent(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        hand = ctx.hand(ctx.opponent_id)
        if results and results[0] and hand:
            picks = random.sample(hand, min(count, len(hand)))
            await ctx.discard_cards(picks)
    return effect


def _flip_discard_defender_energy(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or not ctx.attached_energies(defender):
            return
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0] and not ctx.effects_blocked(defender):
            await ctx.discard_energy_from(defender, 1)
    return effect


def _counters_on_own_chosen(m, ability):
    counters = int(m.group(1))
    count = _count(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = ctx.my_pokemon_in_play()
        if not candidates:
            return
        picks = candidates if len(candidates) <= count else \
            await ctx.choose_cards(candidates, count,
                                   prompt=f"Choose {count} of your Pokémon")
        for target in picks:
            await ctx.deal_damage(counters * 10, target=target,
                                  as_counters=True)
    return effect


def _heal_each_typed(m, ability):
    amount = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_pokemon_in_play():
            if type_value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or []) \
                    and ctx.max_hp(pokemon) > pokemon.get_attribute(AttrID.HP, 0):
                await ctx.heal(amount, pokemon)
    return effect


def _recover_supporter(m, ability):
    return recover_from_discard(predicate=_is_supporter, count=1)


def _ko_if_counters_at_least(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        if (ctx.max_hp(defender) - defender.get_attribute(AttrID.HP, 0)) \
                // 10 >= counters:
            await ctx.knock_out(defender)
    return effect


def _gate_on_healthy(inner):
    async def effect(ctx):
        pokemon = ctx.source
        if pokemon is None or pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
            return
        await inner(ctx)
    return effect


def _passive_asleep_shield(m, ability):
    asleep = SpecialConditions.ASLEEP.value
    return prevent_damage_when(
        lambda calc, carrier: asleep in _condition_values(
            carrier_pokemon(carrier)) if carrier_pokemon(carrier) else False)


def _passive_condition_immune_all(m, ability):
    return condition_immunity_passive()


def _passive_ultra_beast_takes_less(m, ability):
    from ptcgo.game.data_utils import subtypes_for
    amount = int(m.group(1))

    def protects(target, carrier) -> bool:
        if target.owning_player_id != carrier.owning_player_id:
            return False
        return any(subtype.lower() == "ultra beast"
                   for subtype in subtypes_for(target.archetype_id))
    return takes_less_passive(amount, protects=protects)


def _passive_basic_attack_tax_active(m, ability):
    from ptcgo.game.session.effects import is_basic_pokemon
    amount = m.group(1).count("colorless")

    def pred(pokemon) -> bool:
        return is_basic_pokemon(pokemon)
    passive = opponent_attack_tax(amount, target_pred=pred)
    return _while_active(passive)


def _while_active(passive):
    class _ActiveOnly(type(passive)):
        def modify_attack_cost(self, cost, pokemon, carrier, board):
            if not is_in_active_spot(carrier_pokemon(carrier)):
                return cost
            return super().modify_attack_cost(cost, pokemon, carrier, board)
    active = _ActiveOnly.__new__(_ActiveOnly)
    active.__dict__.update(passive.__dict__)
    return active


def _discard_special_energy_chosen(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        candidates = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                      if any(is_special_energy(card)
                             for card in ctx.attached_energies(pokemon))
                      and not ctx.effects_blocked(pokemon)]
        if not candidates:
            return
        picks = candidates if len(candidates) <= count else \
            await ctx.choose_cards(candidates, count,
                                   prompt=f"Choose {count} Pokémon")
        for target in picks:
            await ctx.discard_energy_from(target, 1,
                                          predicate=is_special_energy)
    return effect


def _both_actives_conditions(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        for pokemon in (ctx.attacker, ctx.defender):
            if pokemon is not None:
                await ctx.apply_special_condition(pokemon, condition)
    return effect


def _heal_equal_to_damage(m, ability):
    return heal_dealt_attack()


def _more_if_self_on_bench(m, ability):
    amount = int(m.group(1))
    return bonus_if(lambda ctx: ctx.attacker is not None
                    and not is_in_active_spot(ctx.attacker), amount)


def _more_if_all_bench_damaged(m, ability):
    amount = int(m.group(1))

    def cond(ctx) -> bool:
        bench = ctx.my_bench()
        return bool(bench) and all(
            ctx.max_hp(pokemon) > pokemon.get_attribute(AttrID.HP, 0)
            for pokemon in bench)
    return bonus_if(cond, amount)


def _base_becomes_if_energy_differs(m, ability):
    new_base = int(m.group(1))

    async def effect(ctx):
        attacker, defender = ctx.attacker, ctx.defender
        differs = attacker is not None and defender is not None and \
            len(ctx.attached_energies(attacker)) != \
            len(ctx.attached_energies(defender))
        await ctx.deal_damage(new_base if differs else None)
    return effect


def _counters_then_damage_per_placed(m, ability):
    up_to, per = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        attacker = ctx.attacker
        if attacker is None:
            return
        placed = await ctx.move_damage_counters(
            None, [attacker], max_count=up_to,
            prompt=f"Put up to {up_to} damage counters on this Pokémon")
        if placed:
            await ctx.deal_damage(per * placed)
    return effect


def _half_defender_hp(m, ability):
    async def effect(ctx):
        defender = ctx.defender
        if defender is None:
            return
        remaining = defender.get_attribute(AttrID.HP, 0)
        await ctx.deal_damage(((remaining + 19) // 20) * 10)
    return effect


def _mill_own_then_damage_per_energy(m, ability):
    count, per = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        top = ctx.deck_top(count)
        if not top:
            return
        energy = [card for card in top if is_energy_card(card)]
        await ctx.discard_cards(top)
        if energy:
            await ctx.deal_damage(per * len(energy))
    return effect


def _flip_both_tails_else_discard_energy(m, ability):
    coins = _count(m.group(1))

    async def effect(ctx):
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        if not heads:
            return
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        for _ in range(heads):
            if not ctx.attached_energies(defender):
                break
            await ctx.discard_energy_from(defender, 1)
    return effect


def _search_named_energy_attach_self(m, ability):
    wanted = normalize(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        picks = await ctx.search_deck(
            lambda card: is_energy_card(card) and wanted in normalize(
                getattr(card, "name", "") or getattr(card, "display_name", "")),
            count=1, minimum=0, prompt=f"Choose a {m.group(1)} Energy card")
        if picks:
            await ctx.attach_energy(picks[0], attacker)
        await ctx.shuffle_deck()
    return effect


def _more_per_prizes_taken_discard_energy(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        taken = count_prizes_taken("opponent")(ctx)
        printed = getattr(ctx.ability, "damage", 0) or 0
        await ctx.deal_damage(printed + per * taken)
        attacker = ctx.attacker
        if attacker is not None and ctx.attached_energies(attacker):
            await ctx.discard_energy_from(attacker, 1)
    return effect


def _swap_all_damage_counters(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker, defender = ctx.attacker, ctx.defender
        if attacker is None or defender is None:
            return
        mine = (ctx.max_hp(attacker)
                - attacker.get_attribute(AttrID.HP, 0)) // 10
        theirs = (ctx.max_hp(defender)
                  - defender.get_attribute(AttrID.HP, 0)) // 10
        if mine:
            await ctx.move_damage_counters(attacker, [defender],
                                           max_count=mine,
                                           prompt="Move damage to the "
                                                  "Defending Pokémon")
        if theirs and not ctx.effects_blocked(defender):
            await ctx.move_damage_counters(defender, [attacker],
                                           max_count=theirs,
                                           prompt="Move damage to this Pokémon")
    return effect


def _more_if_defender_resistance(m, ability):
    type_word = m.group(1)
    type_value = TYPE_WORDS[type_word].value
    amount = int(m.group(2))

    def cond(ctx) -> bool:
        defender = ctx.defender
        if defender is None:
            return False
        resist = defender.get_attribute(AttrID.RESISTANCE_TYPES)
        if isinstance(resist, (list, tuple, set)):
            return type_value in resist
        return resist == type_value
    return bonus_if(cond, amount)


def _shuffle_opponent_deck(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.shuffle_deck(ctx.opponent_id)
    return effect


def _flip_lock_defender_retreat(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            from ptcgo.game.card_effects.attacks_common import (
                no_retreat_attack as _no_retreat,
            )
            rider = _no_retreat(damage=0)
            await rider(ctx)
    return effect


def _rearrange_either_top(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        own = await ctx.ask_yes_no("Rearrange your own deck? (No: your "
                                   "opponent's deck)")
        await ctx.reorder_deck_top(count, ctx.player_id if own
                                   else ctx.opponent_id,
                                   "Rearrange the top cards")
    return effect


def _flip_both_confused(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in (ctx.defender, ctx.attacker):
            if pokemon is not None and not ctx.effects_blocked(pokemon):
                await ctx.apply_special_condition(pokemon,
                                                  SpecialConditions.CONFUSED)
    return effect


def _passive_free_retreat_with_any_energy(m, ability):
    return no_energy_free_retreat_passive()


def _free_retreat_with_energy(m, ability):
    from ptcgo.game.card_effects.passives_common import (
        NoEnergyFreeRetreatPassive,
    )
    return NoEnergyFreeRetreatPassive(inverted=True)


def _passive_typed_energy_retreat_cost(m, ability):
    return typed_energy_free_retreat_passive(TYPE_WORDS[m.group(1)].value,
                                             amount=int(m.group(2)))


def _passive_team_typed_boost(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    amount = int(m.group(2))
    return team_damage_boost_passive(
        amount, attacker_pred=lambda pokemon: type_value in (
            pokemon.get_attribute(AttrID.POKEMON_TYPES) or []))


def _passive_effects_shield(m, ability):
    from ptcgo.game.card_effects.passives_common import (
        attack_effect_shield_passive,
    )
    return attack_effect_shield_passive()


def _passive_reduce_from_types_joined(m, ability):
    types = {TYPE_WORDS[m.group(1)].value, TYPE_WORDS[m.group(2)].value}
    amount = int(m.group(3))

    def attacker_pred(pokemon) -> bool:
        return bool(types & set(pokemon.get_attribute(AttrID.POKEMON_TYPES) or []))
    return takes_less_passive(amount, attacker_pred=attacker_pred)


def _passive_hp_per_typed_energy(m, ability):
    return hp_per_typed_energy_passive(int(m.group(1)),
                                       TYPE_WORDS[m.group(2)].value)


def _recover_basics_and_evolutions(m, ability):
    from ptcgo.game.content.definitions import evolves_from
    count = _count(m.group(1))

    def predicate(card) -> bool:
        return bool(evolves_from(getattr(card, "archetype_id", None) or "", ""))

    async def effect(ctx):
        pool = [card for card in ctx.discard_pile()
                if _is_pokemon_card(card) or predicate(card)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, count, minimum=0,
                                       prompt="Choose cards to put into hand")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=False)
    return effect


def _passive_condition_immunity_list(m, ability):
    names = re.split(r", | and ", m.group(1))
    conditions = [CONDITIONS[name] for name in names]
    return condition_immunity_passive(conditions)


def _passive_evolve_early(m, ability):
    from ptcgo.game.card_effects.trainers import evolve_early_passive
    return evolve_early_passive()


def _passive_team_free_retreat_no_gx_ex(m, ability):
    from ptcgo.game.data_utils import subtypes_for

    def pred(pokemon, carrier) -> bool:
        if pokemon.owning_player_id != carrier.owning_player_id:
            return False
        subtypes = {subtype.lower()
                    for subtype in subtypes_for(pokemon.archetype_id)}
        return not (subtypes & {"gx", "ex"})
    return retreat_free_when(pred)


def _self_to_hand(m, ability):
    return remove_self_from_play(destination="hand", optional=False)


def _discard_hand_energy_then_damage_swap(m, ability):
    up_to, per = int(m.group(1)), int(m.group(3))
    type_word = m.group("type")
    type_value = TYPE_WORDS[type_word].value if type_word else None

    def matches(card) -> bool:
        return is_basic_energy_card(card) and (
            type_value is None or energy_provides_type(card, type_value))

    async def effect(ctx):
        pool = [card for card in ctx.hand() if matches(card)]
        picks = await ctx.choose_cards(pool, up_to, minimum=0,
                                       prompt="Choose Energy to discard")
        if picks:
            await ctx.discard_cards(list(picks))
            await ctx.deal_damage(per * len(picks))
        else:
            await ctx.deal_damage(0)
    return effect


def _per_named_in_play(m, ability):
    per = int(m.group(2))
    wanted = normalize(m.group(3))

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.my_pokemon_in_play()
                   if normalize(getattr(pokemon, "display_name", "") or "")
                   == wanted)
    return damage_per(count, per)


def _defender_takes_more_next_turn(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None:
            ctx.add_passive_through_opponents_turn(
                defender, additive_damage_taken_passive(amount))
    return effect


def _move_any_energy_between_own(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pokemon = ctx.my_pokemon_in_play()
        if pokemon:
            await ctx.move_energy_freely(pokemon, pokemon,
                                         prompt="Choose Energy to move")
    return effect


def _move_all_energy_to_bench_any(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker, bench = ctx.attacker, ctx.my_bench()
        if attacker is None or not bench:
            return
        await ctx.move_energy_freely([attacker], bench,
                                     prompt="Choose Energy to move")
    return effect


def _counters_until_hp(m, ability):
    target_hp = int(m.group(1))

    async def effect(ctx):
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        remaining = defender.get_attribute(AttrID.HP, 0)
        counters = max(0, (remaining - target_hp) // 10)
        if counters:
            await ctx.deal_damage(counters * 10, target=defender,
                                  as_counters=True)
    return effect


def _counters_per_opponent_hand(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        counters = per * len(ctx.hand(ctx.opponent_id))
        if defender is not None and counters:
            await ctx.deal_damage(counters * 10, target=defender,
                                  as_counters=True)
    return effect


def _per_cards_with_attack_in_discard(m, ability):
    from ptcgo.game.card_effects.attacks_common import has_attack_titled
    per = int(m.group(1))
    title = m.group(2)
    return damage_per(count_discard("mine", has_attack_titled(title)), per)


def _times_hand_size(m, ability):
    return damage_per(count_hand("mine"), int(m.group(1)))


def _bonus_capped_per_supporter_discard(m, ability):
    per, cap = int(m.group(1)), int(m.group(2))

    def bonus(ctx) -> int:
        supporters = count_discard("mine", _is_supporter)(ctx)
        return min(cap, per * supporters)
    return bonus_if(lambda ctx: True, 0) if False else _bonus_from_counter(
        bonus)


def _bonus_from_counter(count_fn):
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        await ctx.deal_damage(printed + count_fn(ctx))
    return effect


def _bonus_capped_per_energy_type(m, ability):
    per, cap = int(m.group(1)), int(m.group(2))

    def bonus(ctx) -> int:
        types = set()
        for card in ctx.discard_pile():
            if is_basic_energy_card(card):
                for value in (card.get_attribute(AttrID.POKEMON_TYPES) or []):
                    types.add(value)
        return min(cap, per * len(types))
    return _bonus_from_counter(bonus)


def _bonus_per_opponent_gx_ex(m, ability):
    per = int(m.group(1))

    def bonus(ctx) -> int:
        return per * count_in_play("opponent", _is_gx_or_ex_pokemon)(ctx)
    return _bonus_from_counter(bonus)


def _is_gx_or_ex_pokemon(pokemon) -> bool:
    from ptcgo.game.data_utils import subtypes_for
    subtypes = {subtype.lower() for subtype in subtypes_for(pokemon.archetype_id)}
    return bool(subtypes & {"gx", "ex"})


def _search_energy_attach_bench(m, ability):
    count = int(m.group(1))
    type_word = m.groupdict().get("type")
    type_value = TYPE_WORDS[type_word].value if type_word else None

    def predicate(card) -> bool:
        return is_basic_energy_card(card) and (
            type_value is None or energy_provides_type(card, type_value))

    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.my_bench()
        picks = await ctx.search_deck(predicate, count=count, minimum=0,
                                      prompt=f"Choose up to {count} Energy")
        if picks and bench:
            await distribute_energy(ctx, picks, bench)
        await ctx.shuffle_deck()
    return effect


def _flip_attach_typed_discard_self(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        pool = [card for card in ctx.discard_pile() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        if not (results and results[0]) or not pool or ctx.attacker is None:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0,
                                       prompt="Choose an Energy to attach")
        if picks:
            await ctx.attach_energy(picks[0], ctx.attacker)
    return effect


def _opponent_may_draw(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.draw_cards(count, ctx.opponent_id)
    return effect


def _base_plus_if_self_damaged(m, ability):
    base, bonus = int(m.group(1)), int(m.group(2))
    return bonus_if(has_damage("self"), bonus, base=base)


def _base_plus_if_self_has_typed_energy(m, ability):
    type_word, base, bonus = m.group(1), int(m.group(2)), int(m.group(3))
    return bonus_if(self_has_energy_of_type(TYPE_WORDS[type_word]), bonus,
                    base=base)


def _base_becomes_if_defender_damaged(m, ability):
    new_base = int(m.group(1))

    async def effect(ctx):
        defender = ctx.defender
        damaged = defender is not None and defender.get_attribute(
            AttrID.HP, 0) < ctx.max_hp(defender)
        await ctx.deal_damage(new_base if damaged else None)
    return effect


def _heal_self_then_lock_retreat(m, ability):
    amount = int(m.group(1)) * 10

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
        rider = no_retreat_attack(damage=0)
        await rider(ctx)
    return effect


def _attach_many_discard_energy_self(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        pool = [card for card in ctx.discard_pile() if is_energy_card(card)]
        if attacker is None or not pool:
            return
        picks = await ctx.choose_cards(pool, count, minimum=0,
                                       prompt=f"Choose up to {count} Energy")
        for card in picks:
            await ctx.attach_energy(card, attacker)
    return effect


def _base_plus_if_opponent_one_prize(m, ability):
    base, bonus = int(m.group(1)), int(m.group(2))
    return bonus_if(lambda ctx: count_prizes_remaining("opponent")(ctx) == 1,
                    bonus, base=base)


def _flip_heads_chosen_spread(m, ability):
    amount = int(m.group(1))
    count = _count(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        candidates = ctx.opponent_pokemon_in_play()
        if not (results and results[0]) or not candidates:
            return
        picks = candidates if len(candidates) <= count else \
            await ctx.choose_cards(candidates, count,
                                   prompt=f"Choose {count} Pokémon")
        for target in picks:
            if not ctx.effects_blocked(target):
                await ctx.deal_damage(amount, target=target,
                                      apply_modifiers=False)
    return effect


def _take_energy_from_own_other(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pokemon = ctx.my_pokemon_in_play()
        if pokemon:
            await ctx.move_energy_freely(pokemon, pokemon, max_count=1,
                                         prompt="Choose an Energy to move")
    return effect


def _switch_self_if_any(m, ability):
    return _switch_active_with_bench(m, ability)


def _base_plus_per_defender_retreat_colorless(m, ability):
    base, per = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage(base + per * defender_retreat_cost(ctx))
    return effect


def _condition_if_defender_evolved(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and defender_is_evolved(ctx) and \
                not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _recover_energy_reveal(m, ability):
    return recover_from_discard(predicate=is_energy_card, count=1, reveal=True)


def _draw_from_bottom(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        deck = ctx.deck()
        if not deck:
            return
        picks = deck[-count:]
        await ctx.put_in_hand(picks, reveal=False)
    return effect


def _damage_own_bench(m, ability):
    amount = int(m.group(1))
    count = _count(m.group(2)) if m.group(2) else 1

    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.my_bench()
        if not bench:
            return
        picks = bench if len(bench) <= count else await ctx.choose_cards(
            bench, count, prompt=f"Choose {count} Benched Pokémon")
        for target in picks:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False)
    return effect


def _discard_opponent_hand_down_to(m, ability):
    keep = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        hand = ctx.hand(ctx.opponent_id)
        while len(hand) > keep:
            card = random.choice(hand)
            await ctx.discard_cards([card])
            hand = [c for c in hand if c is not card]
    return effect


def _base_plus_if_empty_hand(m, ability):
    base, bonus = int(m.group(1)), int(m.group(2))
    return bonus_if(lambda ctx: not ctx.hand(), bonus, base=base)


def _more_per_damaged_bench(m, ability):
    per = int(m.group(1))

    def bonus(ctx) -> int:
        return per * sum(1 for pokemon in ctx.my_bench()
                         if ctx.max_hp(pokemon)
                         > pokemon.get_attribute(AttrID.HP, 0))
    return _bonus_from_counter(bonus)


def _more_per_all_opponent_counters(m, ability):
    per = int(m.group(1))

    def bonus(ctx) -> int:
        counters = 0
        for pokemon in ctx.opponent_pokemon_in_play():
            counters += max(0, (ctx.max_hp(pokemon)
                                - pokemon.get_attribute(AttrID.HP, 0)) // 10)
        return per * counters
    return _bonus_from_counter(bonus)


def _heal_self_no_period(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
    return effect


def _search_any_cards_up_to(m, ability):
    return search_to_hand(None, count=int(m.group(1)), minimum=0, reveal=False)


def _gate_no_stadium(m, ability):
    from ptcgo.game.card_effects.attacks_common import stadium_in_play_cond

    async def effect(ctx):
        if stadium_in_play_cond(ctx):
            return
        await ctx.deal_damage()
    return effect


def _reorder_opponent_top(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.reorder_deck_top(count, ctx.opponent_id,
                                   "Rearrange the top cards")
    return effect


def _peek_and_optional_discard(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(1)
        if not top:
            return
        if await ctx.ask_yes_no("Discard the top card of your deck?"):
            await ctx.discard_cards(top)
    return effect


def _search_name_onto_bench(m, ability):
    return _search_name_onto_bench_count(m, ability, _count(m.group(1)))


def _search_name_onto_bench_count(m, ability, count):

    async def effect(ctx):
        source = ctx.source
        if source is None:
            return
        wanted = getattr(source, "archetype_id", None)
        picks = await ctx.search_deck(
            lambda card: getattr(card, "archetype_id", None) == wanted,
            count=count, minimum=0, prompt="Choose the Pokémon to Bench")
        for card in picks:
            await ctx.bench_pokemon(card)
        await ctx.shuffle_deck()
    return effect


def _search_name_onto_bench_one(m, ability):
    return _search_name_onto_bench_count(m, ability, 1)


def _switch_self_then_opponent_switches(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.my_bench()
        if bench:
            target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
                bench, "Choose a Benched Pokémon to switch in")
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)
        if ctx.opponent_bench():
            await opponent_switches(ctx)
    return effect


def _heal_if_damage_landed(m, ability):
    amount = int(m.group(1)) * 10

    async def effect(ctx):
        dealt = await ctx.deal_damage()
        if dealt and ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
    return effect


def _reorder_either_top_plain(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        own = await ctx.ask_yes_no("Look at your own deck? (No: your "
                                   "opponent's deck)")
        await ctx.reorder_deck_top(count, ctx.player_id if own
                                   else ctx.opponent_id,
                                   "Rearrange the top cards")
    return effect


def _more_per_opponent_with_ability(m, ability):
    per = int(m.group(1))
    from ptcgo.game.data_utils import def_for

    def count(ctx) -> int:
        total = 0
        for pokemon in ctx.opponent_pokemon_in_play():
            definition = def_for(getattr(pokemon, "archetype_id", None) or "")
            if getattr(definition, "abilities", None):
                total += 1
        return total
    return _bonus_from_counter(lambda ctx: per * count(ctx))


def _flip_per_opponent_spread(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_pokemon_in_play():
            if ctx.effects_blocked(pokemon):
                continue
            results = await ctx.flip_coins(1, getattr(ability, "title", ""))
            if results and results[0]:
                if pokemon is ctx.opponent_active():
                    await ctx.deal_damage(amount, target=pokemon)
                else:
                    await ctx.deal_damage(amount, target=pokemon,
                                          apply_modifiers=False)
    return effect


def _flip_times_heads_spread_all(m, ability):
    coins, per = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        if not heads:
            return
        for pokemon in ctx.opponent_pokemon_in_play():
            if ctx.effects_blocked(pokemon):
                continue
            if pokemon is ctx.opponent_active():
                await ctx.deal_damage(per * heads, target=pokemon)
            else:
                await ctx.deal_damage(per * heads, target=pokemon,
                                      apply_modifiers=False)
    return effect


def _top_pokemon_to_bench(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(count)
        if not top:
            return
        pokemon = [card for card in top if _is_pokemon_card(card)]
        rest = [card for card in top if card not in pokemon]
        chosen = pokemon
        if pokemon:
            free = max(0, 5 - len(ctx.my_bench()))
            if len(pokemon) > free:
                chosen = await ctx.choose_cards(
                    pokemon, free, minimum=0,
                    prompt="Choose Pokémon to put onto your Bench")
            for card in chosen:
                await ctx.bench_pokemon(card)
        leftover = [card for card in rest if card not in chosen]
        if leftover:
            await ctx.shuffle_into_deck(leftover, ctx.player_id)
    return effect


def _bonus_stadium_then_discard_plain(m, ability):
    bonus = int(m.group(1))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        from ptcgo.game.card_effects.attacks_common import stadium_in_play_cond

        has_stadium = stadium_in_play_cond(ctx)
        await ctx.deal_damage(printed + bonus if has_stadium else printed)
        if has_stadium:
            await ctx.discard_stadium()
    return effect


def _more_per_prizes_taken_recoil(m, ability):
    per, recoil = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        taken = count_prizes_taken("opponent")(ctx)
        printed = getattr(ctx.ability, "damage", 0) or 0
        await ctx.deal_damage(printed + per * taken)
        if ctx.attacker is not None:
            await ctx.deal_damage(recoil, target=ctx.attacker,
                                  apply_modifiers=False)
    return effect


def _times_energy_both_actives(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        total = 0
        for pokemon in (ctx.attacker, ctx.defender):
            if pokemon is not None:
                total += len(ctx.attached_energies(pokemon))
        return total
    return damage_per(count, per)


def _lock_opponent_non_supporters(m, ability):
    from ptcgo.game.attributes import CardType, TrainerType

    async def effect(ctx):
        await ctx.deal_damage()
        ctx.lock_plays(
            ctx.opponent_id,
            lambda card: card.get_attribute(AttrID.CARD_TYPE)
            == CardType.TRAINER.value
            and card.get_attribute(AttrID.TRAINER_TYPE)
            != TrainerType.SUPPORTER.value)
    return effect


def _optional_discard_energy_then_base_plus(m, ability):
    base, bonus = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        attacker = ctx.attacker
        extra = 0
        if attacker is not None and ctx.attached_energies(attacker) and                 await ctx.ask_yes_no(f"Discard an Energy for {bonus} more "
                                     f"damage?"):
            if await ctx.discard_energy_from(attacker, 1):
                extra = bonus
        await ctx.deal_damage(base + extra)
    return effect


def _base_plus_if_self_has_tool(m, ability):
    from ptcgo.game.card_effects.attacks_common import has_tool
    base, bonus = int(m.group(1)), int(m.group(2))

    def cond(ctx) -> bool:
        return ctx.attacker is not None and has_tool(ctx.attacker)
    return bonus_if(cond, bonus, base=base)


def _counters_equal_opponent_hand(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        counters = len(ctx.hand(ctx.opponent_id))
        if defender is not None and counters:
            await ctx.deal_damage(counters * 10, target=defender,
                                  as_counters=True)
    return effect


def _search_typed_energy_to_hand(m, ability):
    count = int(m.group(1))
    type_word = m.group(2)
    if type_word is None or type_word not in TYPE_WORDS:
        return None
    type_value = TYPE_WORDS[type_word].value

    def predicate(card) -> bool:
        return is_energy_card(card) and energy_provides_type(card, type_value)
    return search_to_hand(predicate, count=count, reveal=True)


def _peek_opponent_prizes(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        area = ctx.board.find_player_area(ctx.opponent_id, "prizePile")
        prizes = list(area.children) if area else []
        if prizes:
            await ctx.reveal_cards(prizes[:count], to_player=ctx.player_id)
    return effect


def _flip_heads_discard_defender_energy_each(m, ability):
    coins = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        for _ in range(heads):
            if not ctx.attached_energies(defender):
                break
            await ctx.discard_energy_from(defender, 1)
    return effect


def _reveal_hand_discard_chosen(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        hand = ctx.hand(ctx.opponent_id)
        if not hand:
            return
        await ctx.reveal_hand(ctx.opponent_id)
        picks = await ctx.choose_cards(hand, 1,
                                       prompt="Choose a card to discard")
        if picks:
            await ctx.discard_cards(list(picks))
    return effect


def _bonus_if_own_prizes_exactly(m, ability):
    limit, bonus = int(m.group(1)), int(m.group(2))
    return bonus_if(
        lambda ctx: count_prizes_remaining("mine")(ctx) == limit, bonus)


def _opponent_shuffles_hand_cards(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        hand = ctx.hand(ctx.opponent_id)
        if not hand:
            return
        picks = await ctx.choose_cards(hand, count,
                                       prompt=f"Choose {count} cards to shuffle")
        if picks:
            await ctx.shuffle_into_deck(list(picks), ctx.opponent_id)
    return effect


def _per_basic_energy_in_opponent_discard(m, ability):
    return damage_per(count_discard("opponent", is_basic_energy_card),
                      int(m.group(1)))


def _discard_all_self_then_condition(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is not None:
            energies = ctx.attached_energies(attacker)
            if energies:
                await ctx.discard_energy_from(attacker, len(energies))
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _per_named_team_in_play(m, ability):
    per = int(m.group(1))
    owned = normalize(m.group(2))

    def count(ctx) -> int:
        total = 0
        for pokemon in ctx.my_pokemon_in_play():
            name = normalize(getattr(pokemon, "display_name", "") or "")
            if owned in name:
                total += 1
        return total
    return damage_per(count, per)


def _discard_all_opponent_tools_and_special(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_pokemon_in_play():
            if ctx.effects_blocked(pokemon):
                continue
            tools = [card for card in ctx.attached_energies(pokemon)
                     if not is_energy_card(card)]
            energies = [card for card in ctx.attached_energies(pokemon)
                        if is_special_energy(card)]
            if tools:
                await ctx.discard_cards(tools)
            if energies:
                await ctx.discard_energy_from(pokemon, len(energies),
                                              predicate=is_special_energy)
    return effect


def _bonus_if_empty_hand_printed(m, ability):
    return bonus_if(lambda ctx: not ctx.hand(), int(m.group(1)))


def _self_damage_per_counters(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        counters = max(0, (ctx.max_hp(attacker)
                           - attacker.get_attribute(AttrID.HP, 0)) // 10)
        if counters:
            await ctx.deal_damage(per * counters, target=attacker,
                                  apply_modifiers=False)
    return effect


def _more_times_opponent_energy(m, ability):
    per = int(m.group(1))

    def bonus(ctx) -> int:
        defender = ctx.defender
        return per * (len(ctx.attached_energies(defender))
                      if defender is not None else 0)
    return _bonus_from_counter(bonus)


def _bonus_if_defender_gx_or_ex(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        defender = ctx.defender
        if defender is None:
            return False
        return _is_gx_or_ex_pokemon(defender)
    return bonus_if(cond, bonus)


def _more_per_bench_typed(m, ability):
    per = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    def bonus(ctx) -> int:
        return per * sum(1 for pokemon in ctx.my_bench()
                         if type_value in (
                             pokemon.get_attribute(AttrID.POKEMON_TYPES) or []))
    return _bonus_from_counter(bonus)


def _shuffle_hand_draw_opponent_hand(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        hand = ctx.hand()
        if hand:
            await ctx.shuffle_into_deck(list(hand), ctx.player_id)
        await ctx.draw_cards(len(ctx.hand(ctx.opponent_id)))
    return effect


def _more_per_team_typed_energy(m, ability):
    per, type_word = int(m.group(1)), m.group(2)
    type_value = TYPE_WORDS[type_word].value

    def bonus(ctx) -> int:
        total = 0
        for pokemon in ctx.my_pokemon_in_play():
            for energy in ctx.attached_energies(pokemon):
                if energy_provides_type(energy, type_value):
                    total += 1
        return per * total
    return _bonus_from_counter(bonus)


def _flip_base_plus_else_base(m, ability):
    base, bonus = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        await ctx.deal_damage(base + bonus if results and results[0] else base)
    return effect


def _flip_snipe_chosen_no_tail(m, ability):
    count = _count(m.group(1))
    amount = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        candidates = ctx.opponent_pokemon_in_play()
        if not (results and results[0]) or not candidates:
            return
        picks = candidates if len(candidates) <= count else \
            await ctx.choose_cards(candidates, count,
                                   prompt=f"Choose {count} Pokémon")
        for target in picks:
            if not ctx.effects_blocked(target):
                await ctx.deal_damage(amount, target=target,
                                      ignore_weakness=True,
                                      ignore_resistance=True)
    return effect


def _top_pick_then_shuffle(m, ability):
    look, keep = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        top = ctx.deck_top(look)
        if not top:
            return
        picks = top if len(top) <= keep else await ctx.choose_cards(
            top, keep, prompt=f"Choose {keep} card(s) to keep")
        await ctx.put_in_hand(list(picks), reveal=False)
        rest = [card for card in top if card not in picks]
        if rest:
            await ctx.shuffle_into_deck(rest, ctx.player_id)
    return effect


def _search_basic_typed_energy_to_hand(m, ability):
    count = int(m.group(1))
    type_word = m.group("type")
    type_value = TYPE_WORDS[type_word].value if type_word else None

    def predicate(card) -> bool:
        return is_basic_energy_card(card) and (
            type_value is None or energy_provides_type(card, type_value))
    return search_to_hand(predicate, count=count, reveal=True)


def _heal_own_with_energy(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        candidates = [pokemon for pokemon in ctx.my_pokemon_in_play()
                      if ctx.attached_energies(pokemon)
                      and ctx.max_hp(pokemon)
                      > pokemon.get_attribute(AttrID.HP, 0)]
        if not candidates:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal")
        if target is not None:
            await ctx.heal(amount, target)
    return effect


def _move_typed_energy_between_own(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        sources = [pokemon for pokemon in ctx.my_pokemon_in_play()
                   if any(energy_provides_type(energy, type_value)
                          for energy in ctx.attached_energies(pokemon))]
        dests = ctx.my_pokemon_in_play()
        if not sources or len(dests) < 2:
            return
        await ctx.move_energy_freely(
            sources, dests, max_count=1,
            predicate=lambda energy: energy_provides_type(energy, type_value),
            prompt="Choose Energy to move")
    return effect


def _passive_attacks_boost_at_low_hp(m, ability):
    limit, amount = int(m.group(1)), int(m.group(2))

    def attacker_pred(pokemon) -> bool:
        return pokemon.get_attribute(AttrID.HP, 0) <= limit
    return team_damage_boost_passive(amount, attacker_pred=attacker_pred)


def _draw_one(m, ability):
    async def effect(ctx):
        await ctx.draw_cards(1, ctx.player_id)
    return effect


def _attach_discard_energy_self(m, ability):
    count = _count(m.group("count"))
    type_word = m.group("type")
    type_value = TYPE_WORDS[type_word].value if type_word else None
    flip = bool(m.groupdict().get("flip")) or "flip a coin" in m.group(0)

    def predicate(card) -> bool:
        return is_energy_card(card) and (
            type_value is None or energy_provides_type(card, type_value))

    async def effect(ctx):
        await ctx.deal_damage()
        if flip:
            results = await ctx.flip_coins(1, getattr(ability, "title", ""))
            if not (results and results[0]):
                return
        attacker = ctx.attacker
        pool = [card for card in ctx.discard_pile() if predicate(card)]
        if attacker is None or not pool:
            return
        picks = await ctx.choose_cards(pool, count, minimum=0,
                                       prompt=f"Choose up to {count} Energy")
        for card in picks:
            await ctx.attach_energy(card, attacker)
    return effect


def _flip_recover_one(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        pile = ctx.discard_pile()
        if not (results and results[0]) or not pile:
            return
        picks = await ctx.choose_cards(pile, 1, minimum=0,
                                       prompt="Choose a card to put into hand")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=False)
    return effect


def _discard_energy_to_one_target(m, ability):
    type_word = m.groupdict().get("type")
    type_value = TYPE_WORDS[type_word].value if type_word else None

    def predicate(card) -> bool:
        return is_basic_energy_card(card) and (
            type_value is None or energy_provides_type(card, type_value))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.discard_pile() if predicate(card)]
        candidates = ctx.my_pokemon_in_play()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0,
                                       prompt="Choose an Energy to attach")
        if not picks:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates,
                                     "Choose a Pokémon to attach the Energy to")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _search_typed_pokemon_to_hand(m, ability):
    type_word = m.group(1)
    if type_word not in TYPE_WORDS:
        return None
    from ptcgo.game.card_effects.trainers import pokemon_of
    return search_to_hand(pokemon_of(type_word), count=1, reveal=True)


def _search_stadium_then_discard_any(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        await search_to_hand(_is_stadium, count=1, reveal=True)(ctx)
        if ctx.stadium_in_play() if hasattr(ctx, "stadium_in_play") else False:
            await ctx.discard_stadium()
    return effect


def _optional_typed_energy_to_hand_for_bonus(m, ability):
    type_word = m.group(1)
    bonus = int(m.group(2))
    type_value = TYPE_WORDS[type_word].value

    async def effect(ctx):
        attacker = ctx.attacker
        printed = getattr(ctx.ability, "damage", 0) or 0
        pool = [energy for energy in ctx.attached_energies(attacker)
                if energy_provides_type(energy, type_value)] \
            if attacker is not None else []
        extra = 0
        if pool and await ctx.ask_yes_no(
                f"Put an Energy into your hand for {bonus} more damage?"):
            picks = pool if len(pool) == 1 else await ctx.choose_cards(
                pool, 1, prompt="Choose an Energy to put into your hand")
            if picks:
                await ctx.put_in_hand(list(picks), reveal=False)
                extra = bonus
        await ctx.deal_damage(printed + extra)
    return effect


def _flip_search_any_card(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if not (results and results[0]):
            return
        picks = await ctx.search_deck(None, count=1, minimum=0,
                                      prompt="Choose a card")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=False)
        await ctx.shuffle_deck()
    return effect


def _recover_one_unconditional(m, ability):
    return recover_from_discard(count=1, minimum=1)


def _attach_many_typed_discard_self(m, ability):
    count = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        pool = [card for card in ctx.discard_pile() if is_basic_energy_card(card)
                and energy_provides_type(card, type_value)]
        if attacker is None or not pool:
            return
        picks = await ctx.choose_cards(pool, count, minimum=0,
                                       prompt=f"Choose up to {count} Energy")
        for card in picks:
            await ctx.attach_energy(card, attacker)
    return effect


def _shuffle_own_energy_for_damage(m, ability):
    per = int(m.group(2))
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        pool = [energy for pokemon in ctx.my_pokemon_in_play()
                for energy in ctx.attached_energies(pokemon)
                if energy_provides_type(energy, type_value)]
        if not pool:
            await ctx.deal_damage(0)
            return
        picks = await ctx.choose_cards(pool, len(pool), minimum=0,
                                       prompt="Choose Energy to shuffle back")
        if picks:
            await ctx.shuffle_into_deck(list(picks), ctx.player_id)
            await ctx.deal_damage(per * len(picks))
        else:
            await ctx.deal_damage(0)
    return effect


def _delayed_checkup_rider(ctx, session_target_id, apply):
    """Schedules `apply(ctx2)` at the checkup ending the opponent's next turn,
    dropped if the Pokemon has left the Active spot."""
    owner_id, target_id = session_target_id

    def _guard(board):
        active = board.active_pokemon(owner_id) if owner_id else None
        return active is not None and active.entity_id == target_id

    async def _fire(session):
        pokemon = session.board_state.get_entity(target_id)
        if pokemon is None:
            return
        from ptcgo.game.session.effects import EffectContext
        ctx2 = EffectContext(session, owner_id, pokemon, None)
        await apply(ctx2, pokemon)

    ctx.schedule_at_checkup(1, _fire, guard=_guard)


def _schedule_counters_on_defender(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return

        async def apply(ctx2, pokemon):
            await ctx2.deal_damage(counters * 10, target=pokemon,
                                   as_counters=True)
        _delayed_checkup_rider(
            ctx, (defender.owning_player_id, defender.entity_id), apply)
    return effect


def _schedule_condition_on_defender(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return

        async def apply(ctx2, pokemon):
            await ctx2.apply_special_condition(pokemon, condition)
        _delayed_checkup_rider(
            ctx, (defender.owning_player_id, defender.entity_id), apply)
    return effect


def _schedule_knock_out_defender(m, ability):
    discard_all = m.groupdict().get("discard") is not None

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        if discard_all and ctx.attacker is not None:
            energies = ctx.attached_energies(ctx.attacker)
            if energies:
                await ctx.discard_energy_from(ctx.attacker, len(energies))

        async def apply(ctx2, pokemon):
            await ctx2.session._resolve_raw_knockout(pokemon)
        _delayed_checkup_rider(
            ctx, (defender.owning_player_id, defender.entity_id), apply)
    return effect


def _last_turn_damage(ctx) -> int:
    attacker = ctx.attacker
    if attacker is None:
        return 0
    return ctx.damage_taken_last_turn(attacker)


def _bonus_last_turn_damage(m, ability):
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        await ctx.deal_damage(printed + _last_turn_damage(ctx))
    return effect


def _condition_if_damaged_last_turn(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if not _last_turn_damage(ctx) or defender is None or \
                ctx.effects_blocked(defender):
            return
        await ctx.apply_special_condition(defender, condition)
    return effect


def _repeat_last_turn_damage(m, ability):
    async def effect(ctx):
        taken = _last_turn_damage(ctx)
        if taken:
            await ctx.deal_damage(taken)
    return effect


def _ko_flip_active_or_bench_basic(m, ability):
    from ptcgo.game.session.effects import is_basic_pokemon

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        heads = bool(results and results[0])
        if heads:
            active = ctx.opponent_active()
            candidates = [active] if active is not None and \
                is_basic_pokemon(active) and not ctx.effects_blocked(active) else []
        else:
            candidates = [pokemon for pokemon in ctx.opponent_bench()
                          if is_basic_pokemon(pokemon)
                          and not ctx.effects_blocked(pokemon)]
        if candidates:
            await ctx.knock_out(candidates[0])
    return effect


def _gate_must_be_asleep(m, ability):
    asleep = SpecialConditions.ASLEEP.value

    async def effect(ctx):
        attacker = ctx.attacker
        if attacker is None or asleep not in _condition_values(attacker):
            return
        await ctx.deal_damage()
    return effect


def _flip_prevent_all_damage_next_turn(m, ability):
    return flip_protection(prevent=True)


def _spread_ex_only(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_pokemon_in_play():
            if not _is_gx_or_ex_pokemon(pokemon) or ctx.effects_blocked(pokemon):
                continue
            if pokemon is ctx.opponent_active():
                await ctx.deal_damage(amount, target=pokemon)
            else:
                await ctx.deal_damage(amount, target=pokemon,
                                      apply_modifiers=False)
    return effect


def _place_counters_chosen_any(m, ability):
    counters = int(m.group(1))
    count = _count(m.group(2)) if m.group(2) else 1

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        picks = candidates if len(candidates) <= count else \
            await ctx.choose_cards(candidates, count,
                                   prompt=f"Choose {count} Pokémon")
        for target in picks:
            if not ctx.effects_blocked(target):
                await ctx.deal_damage(counters * 10, target=target,
                                      as_counters=True)
    return effect


def _return_defender_unless_ko(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        if defender.get_attribute(AttrID.HP, 0) <= 0:
            return
        cards = [defender]
        for child in list(defender.children or []):
            cards.append(child)
        await ctx.put_in_hand(cards, reveal=False)
    return effect


def _search_basic_energy_to_bench_one(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.my_bench()
        if not bench:
            return
        picks = await ctx.search_deck(is_basic_energy_card, count=1, minimum=0,
                                      prompt="Choose an Energy card")
        if not picks:
            await ctx.shuffle_deck()
            return
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to attach the Energy to")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
        await ctx.shuffle_deck()
    return effect


def _flip_heads_bonus_and_condition(m, ability):
    bonus = int(m.group(1))
    condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        printed = getattr(ctx.ability, "damage", 0) or 0
        if not (results and results[0]):
            await ctx.deal_damage(printed)
            return
        await ctx.deal_damage(printed + bonus)
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _stadium_bonus_and_heal(m, ability):
    bonus, heal = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        from ptcgo.game.card_effects.attacks_common import stadium_in_play_cond
        printed = getattr(ctx.ability, "damage", 0) or 0
        has_stadium = stadium_in_play_cond(ctx)
        await ctx.deal_damage(printed + bonus if has_stadium else printed)
        if has_stadium and ctx.attacker is not None:
            await ctx.heal(heal, ctx.attacker)
    return effect


def _times_prizes_taken_mine(m, ability):
    return damage_per(lambda ctx: count_prizes_taken("mine")(ctx),
                      int(m.group(1)))


def _recover_items(m, ability):
    return recover_from_discard(predicate=_is_item, count=_count(m.group(1)))


def _bonus_if_more_hand(m, ability):
    bonus = int(m.group(1))
    return bonus_if(
        lambda ctx: len(ctx.hand()) > len(ctx.hand(ctx.opponent_id)), bonus)


def _times_special_energy_in_opponent_discard(m, ability):
    return damage_per(
        count_discard("opponent", lambda card: is_energy_card(card)
                      and is_special_energy(card)), int(m.group(1)))


def _bonus_per_opponent_bench(m, ability):
    return _bonus_from_counter(
        lambda ctx: int(m.group(1)) * len(ctx.opponent_bench()))


def _bonus_per_distinct_energy_type(m, ability):
    per = int(m.group(1))

    def bonus(ctx) -> int:
        attacker = ctx.attacker
        if attacker is None:
            return 0
        energies = ctx.attached_energies(attacker)
        types = 0
        for type_value in {word.value for word in PokemonTypes}:
            if any(energy_provides_type(energy, type_value)
                   for energy in energies):
                types += 1
        return per * types
    return _bonus_from_counter(bonus)


def _flip_heal_per_heads(m, ability):
    coins, amount = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        if heads and ctx.attacker is not None:
            await ctx.heal(amount * heads, ctx.attacker)
    return effect


def _discard_defender_tool(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        tools = [card for card in ctx.attached_energies(defender)
                 if not is_energy_card(card)]
        if tools:
            await ctx.discard_cards(tools[:1])
    return effect


def _times_defender_counters(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        defender = ctx.defender
        if defender is None:
            return 0
        return max(0, (ctx.max_hp(defender)
                       - defender.get_attribute(AttrID.HP, 0)) // 10)
    return damage_per(count, per)


def _move_counters_any_direction(m, ability):
    up_to = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        mine = [pokemon for pokemon in ctx.my_pokemon_in_play()
                if ctx.max_hp(pokemon) > pokemon.get_attribute(AttrID.HP, 0)]
        theirs = ctx.opponent_pokemon_in_play()
        if not mine or not theirs:
            return
        source = mine[0] if len(mine) == 1 else await ctx.choose_pokemon(
            mine, "Choose a Pokémon to move damage from")
        target = theirs[0] if len(theirs) == 1 else await ctx.choose_pokemon(
            theirs, "Choose a Pokémon to move damage to")
        if source is not None and target is not None:
            await ctx.move_damage_counters(source, [target], max_count=up_to)
    return effect


def _self_damage_then_switch(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.deal_damage(amount, target=ctx.attacker,
                                  apply_modifiers=False)
        bench = ctx.my_bench()
        if bench:
            target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
                bench, "Choose a Benched Pokémon to switch in")
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)
    return effect


def _defender_condition_self_asleep(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
        if ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker,
                                              SpecialConditions.ASLEEP)
    return effect


def _heal_team_with_energy(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_pokemon_in_play():
            if ctx.attached_energies(pokemon) and ctx.max_hp(pokemon) > \
                    pokemon.get_attribute(AttrID.HP, 0):
                await ctx.heal(amount, pokemon)
    return effect


def _bonus_if_opponent_has_typed(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    base, bonus = int(m.group(2)), int(m.group(3))

    def cond(ctx) -> bool:
        return any(type_value in (pokemon.get_attribute(AttrID.POKEMON_TYPES)
                                  or [])
                   for pokemon in ctx.opponent_pokemon_in_play())
    return bonus_if(cond, bonus, base=base)


def _counters_equal_self_counters(m, ability):
    count = _count(m.group(1)) if m.group(1) else 1

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        counters = max(0, (ctx.max_hp(attacker)
                           - attacker.get_attribute(AttrID.HP, 0)) // 10)
        candidates = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                      if not ctx.effects_blocked(pokemon)]
        if not counters or not candidates:
            return
        picks = candidates if len(candidates) <= count else \
            await ctx.choose_cards(candidates, count,
                                   prompt=f"Choose {count} Pokémon")
        for target in picks:
            await ctx.deal_damage(counters * 10, target=target,
                                  as_counters=True)
    return effect


def _flip_counters_each_bench(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if not (results and results[0]):
            return
        for pokemon in ctx.opponent_bench():
            if not ctx.effects_blocked(pokemon):
                await ctx.deal_damage(counters * 10, target=pokemon,
                                      as_counters=True)
    return effect


def _search_any_one_card(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(None, count=1, minimum=0,
                                      prompt="Choose a card")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=False)
        await ctx.shuffle_deck()
    return effect


def _shuffle_hand_only(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        hand = ctx.hand()
        if hand:
            await ctx.shuffle_into_deck(list(hand), ctx.player_id)
    return effect


def _ignore_wr_then_self_asleep(m, ability):
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        await ctx.deal_damage(printed, ignore_weakness=True,
                              ignore_resistance=True)
        if ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker,
                                              SpecialConditions.ASLEEP)
    return effect


def _flip_tails_discard_all_typed(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        attacker = ctx.attacker
        if results and results[0]:
            return
        if attacker is None:
            return
        pool = [energy for energy in ctx.attached_energies(attacker)
                if energy_provides_type(energy, type_value)]
        if pool:
            await ctx.discard_energy_from(
                attacker, len(pool),
                predicate=lambda energy: energy_provides_type(energy,
                                                              type_value))
    return effect


def _move_typed_energy_to_bench(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker, bench = ctx.attacker, ctx.my_bench()
        if attacker is None or not bench:
            return
        await ctx.move_energy_freely(
            [attacker], bench, max_count=1,
            predicate=lambda energy: energy_provides_type(energy, type_value),
            prompt="Choose Energy to move")
    return effect


def _draw_then_self_condition(m, ability):
    count = int(m.group(1))
    condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.draw_cards(count)
        if ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker, condition)
    return effect


def _heal_then_self_condition(m, ability):
    amount = int(m.group(1))
    condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
            await ctx.apply_special_condition(ctx.attacker, condition)
    return effect


def _heal_then_switch(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
        bench = ctx.my_bench()
        if bench:
            target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
                bench, "Choose a Benched Pokémon to switch in")
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)
    return effect


def _heal_then_defender_no_retreat(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
        await no_retreat_attack(damage=0)(ctx)
    return effect


def _condition_then_defender_no_retreat(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
        await no_retreat_attack(damage=0)(ctx)
    return effect


def _discard_energy_then_defender_locked(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is not None and ctx.attached_energies(attacker):
            await ctx.discard_energy_from(attacker, 1)
        await _lock_defender_attacks_plain(m, ability)(ctx)
    return effect


def _search_energy_attach_any_one(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        candidates = ctx.my_pokemon_in_play()
        picks = await ctx.search_deck(is_basic_energy_card, count=1, minimum=0,
                                      prompt="Choose an Energy card")
        if not picks or not candidates:
            await ctx.shuffle_deck()
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates,
                                     "Choose a Pokémon to attach the Energy to")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
        await ctx.shuffle_deck()
    return effect


def _shuffle_hand_then_draw(m, ability):
    count = int(m.group(1))
    then_sleep = m.groupdict().get("sleep") is not None

    async def effect(ctx):
        await ctx.deal_damage()
        hand = ctx.hand()
        if hand:
            await ctx.shuffle_into_deck(list(hand), ctx.player_id)
        await ctx.draw_cards(count)
        if then_sleep and ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker,
                                              SpecialConditions.ASLEEP)
    return effect


def _damage_own_any_ignore_mods(m, ability):
    amount = int(m.group(1))
    count = _count(m.group(2)) if m.group(2) else 1

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = ctx.my_pokemon_in_play()
        if not candidates:
            return
        picks = candidates if len(candidates) <= count else \
            await ctx.choose_cards(candidates, count,
                                   prompt=f"Choose {count} of your Pokémon")
        for target in picks:
            await ctx.deal_damage(amount, target=target,
                                  ignore_weakness=True, ignore_resistance=True)
    return effect


def _flip_mill_opponent_or_self(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        pid = ctx.opponent_id if results and results[0] else ctx.player_id
        top = ctx.deck_top(count, pid)
        if top:
            await ctx.discard_cards(top)
    return effect


def _gate_defender_not_condition(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        defender = ctx.defender
        if defender is None or getattr(condition, "value", condition) \
                not in _condition_values(defender):
            return
        await ctx.deal_damage()
    return effect


def _bonus_if_counters_at_least(m, ability):
    limit, bonus = int(m.group(1)), int(m.group(2))

    def cond(ctx) -> bool:
        attacker = ctx.attacker
        if attacker is None:
            return False
        return (ctx.max_hp(attacker)
                - attacker.get_attribute(AttrID.HP, 0)) // 10 >= limit
    return bonus_if(cond, bonus)


def _flip_prevent_damage_plain(m, ability):
    return flip_protection(prevent=True)


def _condition_and_no_retreat(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
            await no_retreat_attack(damage=0)(ctx)
    return effect


def _flip_defender_or_self_condition(m, ability):
    defender_condition = CONDITIONS[m.group(1)]
    self_condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            defender = ctx.defender
            if defender is not None and not ctx.effects_blocked(defender):
                await ctx.apply_special_condition(defender, defender_condition)
        elif ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker, self_condition)
    return effect


def _flip_condition_else_self_damage(m, ability):
    condition = CONDITIONS[m.group(1)]
    recoil = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            defender = ctx.defender
            if defender is not None and not ctx.effects_blocked(defender):
                await ctx.apply_special_condition(defender, condition)
        elif ctx.attacker is not None:
            await ctx.deal_damage(recoil, target=ctx.attacker,
                                  apply_modifiers=False)
    return effect


def _times_named_self_in_play(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        source = ctx.source
        name = normalize(getattr(source, "display_name", "") or "")
        if not name:
            return 0
        return sum(1 for pokemon in ctx.my_pokemon_in_play()
                   if normalize(getattr(pokemon, "display_name", "") or "")
                   == name)
    return damage_per(count, per)


def _times_both_in_play(m, ability):
    return damage_per(count_in_play("both"), int(m.group(1)))


def _flip_times_heads_then_confused(m, ability):
    return flip_damage(coins=int(m.group(1)), per_heads=int(m.group(2)),
                       also=_self_condition_rider(SpecialConditions.CONFUSED))


def _base_on_tails(m, ability):
    new_base = int(m.group(1))

    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and not results[0]:
            await ctx.deal_damage(new_base)
        else:
            await ctx.deal_damage()
    return effect


def _return_defender_to_hand_flip(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        defender = ctx.defender
        if not (results and results[0]) or defender is None or \
                ctx.effects_blocked(defender):
            return
        cards = [defender] + list(defender.children or [])
        await ctx.put_in_hand(cards, reveal=False)
    return effect


def _reduce_damage_next_turn_plain(m, ability):
    return protect_next_turn(reduce=int(m.group(1)))


def _ignore_wr_then_self_lock(m, ability):
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        await ctx.deal_damage(printed, ignore_weakness=True,
                              ignore_resistance=True)
        if ctx.attacker is not None:
            from ptcgo.game.card_effects.attacks_common import lock_all_attacks
            lock_all_attacks(ctx, ctx.attacker)
    return effect


def _lock_this_attack_short(m, ability):
    return _lock_this_attack(m, ability)


def _typed_energy_return_to_hand(m, ability):
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        pool = [energy for energy in ctx.attached_energies(attacker)
                if energy_provides_type(energy, type_value)]
        if not pool:
            return
        picks = pool if len(pool) <= _count(m.group(1)) else \
            await ctx.choose_cards(pool, _count(m.group(1)),
                                   prompt="Choose Energy to return to hand")
        await ctx.put_in_hand(list(picks), reveal=False)
    return effect


def _flip_tails_self_attack_lock(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and not results[0] and ctx.attacker is not None:
            from ptcgo.game.card_effects.attacks_common import lock_all_attacks
            lock_all_attacks(ctx, ctx.attacker)
    return effect


def _discard_typed_defender_energy(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        pool = [energy for energy in ctx.attached_energies(defender)
                if energy_provides_type(energy, type_value)]
        if pool:
            await ctx.discard_energy_from(
                defender, 1,
                predicate=lambda energy: energy_provides_type(energy,
                                                              type_value))
    return effect


def _search_typed_pokemon_many(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    def predicate(card) -> bool:
        return _is_pokemon_card(card) and type_value in (
            card.get_attribute(AttrID.POKEMON_TYPES) or [])
    return search_to_hand(predicate, count=count, reveal=True)


def _search_typed_energy_attach_any(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = ctx.my_pokemon_in_play()
        picks = await ctx.search_deck(
            lambda card: is_energy_card(card)
            and energy_provides_type(card, type_value),
            count=1, minimum=0, prompt="Choose an Energy card")
        if picks and candidates:
            target = candidates[0] if len(candidates) == 1 else \
                await ctx.choose_pokemon(
                    candidates, "Choose a Pokémon to attach the Energy to")
            if target is not None:
                await ctx.attach_energy(picks[0], target)
        await ctx.shuffle_deck()
    return effect


def _attach_discard_basic_distributed(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.discard_pile() if is_basic_energy_card(card)]
        candidates = ctx.my_pokemon_in_play()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, count, minimum=0,
                                       prompt=f"Choose up to {count} Energy")
        if picks:
            await distribute_energy(ctx, list(picks), candidates)
    return effect


def _draw_then_asleep(m, ability):
    count = 1

    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.draw_cards(count)
        if ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker,
                                              SpecialConditions.ASLEEP)
    return effect


def _condition_then_bench_counters(m, ability):
    condition = CONDITIONS[m.group(1)]
    counters = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
        for pokemon in ctx.opponent_bench():
            if not ctx.effects_blocked(pokemon):
                await ctx.deal_damage(counters * 10, target=pokemon,
                                      as_counters=True)
    return effect


def _flip_counters_until_hp(m, ability):
    target_hp = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        defender = ctx.defender
        if not (results and results[0]) or defender is None or \
                ctx.effects_blocked(defender):
            return
        remaining = defender.get_attribute(AttrID.HP, 0)
        counters = max(0, (remaining - target_hp) // 10)
        if counters:
            await ctx.deal_damage(counters * 10, target=defender,
                                  as_counters=True)
    return effect


def _bonus_capped_per_discard(m, ability):
    per, cap = int(m.group(1)), int(m.group(2))

    def bonus(ctx) -> int:
        return min(cap, per * len(ctx.discard_pile()))
    return _bonus_from_counter(bonus)


def _per_damaged_own(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.my_pokemon_in_play()
                   if ctx.max_hp(pokemon)
                   > pokemon.get_attribute(AttrID.HP, 0))
    return damage_per(count, per)


def _recover_typed_energy(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value
    return recover_from_discard(
        predicate=lambda card: is_energy_card(card)
        and energy_provides_type(card, type_value), count=count)


def _discard_energy_trade_plain(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker, defender = ctx.attacker, ctx.defender
        if attacker is None or defender is None:
            return
        if not ctx.attached_energies(attacker):
            return
        if await ctx.discard_energy_from(attacker, 1) and \
                not ctx.effects_blocked(defender):
            await ctx.discard_energy_from(defender, 1)
    return effect


def _ko_defender_if_basic(m, ability):
    from ptcgo.game.session.effects import is_basic_pokemon

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and is_basic_pokemon(defender) and \
                not ctx.effects_blocked(defender):
            await ctx.knock_out(defender)
    return effect


def _ko_defender_if_all_heads(m, ability):
    coins = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        defender = ctx.defender
        if results and all(results) and defender is not None and \
                not ctx.effects_blocked(defender):
            await ctx.knock_out(defender)
    return effect


def _per_named_in_discard(m, ability):
    per = int(m.group(1))
    wanted = normalize(m.group(2))

    def count(ctx) -> int:
        return sum(1 for card in ctx.discard_pile()
                   if normalize(getattr(card, "display_name", "")
                                or getattr(card, "name", "") or "") == wanted)
    return damage_per(count, per)


def _flip_mill_per_heads(m, ability):
    coins, per = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        if heads:
            top = ctx.deck_top(per * heads, ctx.opponent_id)
            if top:
                await ctx.discard_cards(top)
    return effect


def _heal_then_self_no_retreat(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        await ctx.heal(amount, attacker)
        ctx.add_passive_through_opponents_turn(
            attacker, no_retreat_passive(lambda p, c: p is carrier_pokemon(c)))
    return effect


def _bench_from_discard(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.discard_pile() if _is_pokemon_card(card)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0,
                                       prompt="Choose a Pokémon to Bench")
        for card in picks:
            await ctx.bench_pokemon(card)
    return effect


def _recover_pokemon(m, ability):
    return recover_from_discard(predicate=_is_pokemon_card,
                                count=_count(m.group(1)))




def _lock_defender_if_evolved(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if not defender_is_evolved(ctx):
            return
        await _lock_defender_attacks_plain(m, ability)(ctx)
    return effect


def _discard_opponent_tools(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        tools = []
        for pokemon in ctx.opponent_pokemon_in_play():
            for card in ctx.attached_energies(pokemon):
                if not is_energy_card(card):
                    tools.append(card)
        if tools:
            picks = tools if len(tools) <= limit else await ctx.choose_cards(
                tools, limit, prompt=f"Choose up to {limit} Pokémon Tools")
            if picks:
                await ctx.discard_cards(list(picks))
    return effect


def _bonus_if_self_condition(m, ability):
    bonus = int(m.group(2))
    return bonus_if(
        lambda ctx: ctx.attacker is not None and bool(
            ctx.attacker.get_attribute(AttrID.SPECIAL_CONDITIONS)), bonus)


def _condition_if_defender_type(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        if type_value in (defender.get_attribute(AttrID.POKEMON_TYPES) or []):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _opponent_switches_chosen(m, ability):
    return gust_attack(damage_before=0, opponent_chooses=True)


def _counters_each_opponent_with_energy(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_pokemon_in_play():
            if not ctx.attached_energies(pokemon) or \
                    ctx.effects_blocked(pokemon):
                continue
            await ctx.deal_damage(counters * 10, target=pokemon,
                                  as_counters=True)
    return effect


def _gate_defender_condition(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        defender = ctx.defender
        if defender is None or getattr(condition, "value", condition) \
                not in _condition_values(defender):
            return
        await ctx.deal_damage()
    return effect


def _lock_all_trainers(m, ability):
    from ptcgo.game.attributes import CardType

    async def effect(ctx):
        await ctx.deal_damage()
        ctx.lock_plays(
            ctx.opponent_id,
            lambda card: card.get_attribute(AttrID.CARD_TYPE)
            == CardType.TRAINER.value)
    return effect


def _times_defender_energy_cards(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        defender = ctx.defender
        return len(ctx.attached_energies(defender)) if defender else 0
    return damage_per(count, per)


def _discard_energy_heal_all(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        if ctx.attached_energies(attacker):
            await ctx.discard_energy_from(attacker, 1)
        await ctx.heal(9990, attacker)
    return effect


def _flip_recover_per_heads(m, ability):
    coins = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        pile = ctx.discard_pile()
        if not heads or not pile:
            return
        picks = await ctx.choose_cards(pile, heads, minimum=0,
                                       prompt="Choose cards to put into hand")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=False)
    return effect


def _bonus_if_lower_hp(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        attacker, defender = ctx.attacker, ctx.defender
        if attacker is None or defender is None:
            return False
        return attacker.get_attribute(AttrID.HP, 0) < \
            defender.get_attribute(AttrID.HP, 0)
    return bonus_if(cond, bonus)


def _times_typed_in_play(m, ability):
    per = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.my_pokemon_in_play()
                   if type_value in (pokemon.get_attribute(AttrID.POKEMON_TYPES)
                                     or []))
    return damage_per(count, per)


def _flip_discard_energy_chosen(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if not (results and results[0]):
            return
        candidates = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                      if ctx.attached_energies(pokemon)
                      and not ctx.effects_blocked(pokemon)]
        if not candidates:
            return
        picks = candidates if len(candidates) <= count else \
            await ctx.choose_cards(candidates, count,
                                   prompt=f"Choose {count} Pokémon")
        for target in picks:
            await ctx.discard_energy_from(target, 1)
    return effect


def _flip_times_heads_then_self_lock(m, ability):
    coins, per = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        if heads:
            await ctx.deal_damage(per * heads)
        if ctx.attacker is not None:
            from ptcgo.game.card_effects.attacks_common import lock_all_attacks
            lock_all_attacks(ctx, ctx.attacker)
    return effect


def _flip_base_plus_per_heads(m, ability):
    coins, base, per = int(m.group(1)), int(m.group(2)), int(m.group(3))

    async def effect(ctx):
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        await ctx.deal_damage(base + per * heads)
    return effect


def _attach_hand_basic_self(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        pool = [card for card in ctx.hand()
                if is_basic_energy_card(card)]
        if pool:
            picks = await ctx.choose_cards(pool, len(pool), prompt=(
                "Choose any number of basic Energy cards"))
            for card in picks:
                await ctx.attach_energy(card, attacker)
    return effect


def _attach_hand_basic_distributed(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_basic_energy_card(card)]
        candidates = ctx.my_pokemon_in_play()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, len(pool), prompt=(
            "Choose any number of basic Energy cards"))
        if picks:
            await distribute_energy(ctx, list(picks), candidates)
    return effect


def _heal_if_damaged(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is not None and ctx.max_hp(attacker) > \
                attacker.get_attribute(AttrID.HP, 0):
            await ctx.heal(amount, attacker)
    return effect


def _flip_topdeck_from_discard(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        pile = ctx.discard_pile()
        if not (results and results[0]) or not pile:
            return
        picks = await ctx.choose_cards(pile, 1, prompt=(
            "Choose a card to put on top of your deck"))
        for card in picks:
            await ctx.put_on_top_of_deck(card)
    return effect


def _heal_all_then_self_lock(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        await ctx.heal(9990, attacker)
        from ptcgo.game.card_effects.attacks_common import lock_all_attacks
        lock_all_attacks(ctx, attacker)
    return effect


def _flip_all_defenders_condition(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if not (results and results[0]):
            return
        for pokemon in ctx.opponent_pokemon_in_play():
            if ctx.attacker is not None and \
                    pokemon.entity_id == ctx.attacker.entity_id:
                continue
            if not ctx.effects_blocked(pokemon):
                await ctx.apply_special_condition(pokemon, condition)
    return effect


def _flip_all_defenders_lock(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await _lock_defender_attacks_plain(m, ability)(ctx)
    return effect


def _base_damage_if_resistance(m, ability):
    changed, base = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        defender = ctx.defender
        resists = defender is not None and bool(
            defender.get_attribute(AttrID.RESISTANCE_TYPES))
        await ctx.deal_damage(changed if resists else base)
    return effect


def _attach_basic_from_discard_self(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        pile = [card for card in ctx.discard_pile() if is_basic_energy_card(card)]
        if attacker is None or not pile:
            return
        picks = await ctx.choose_cards(pile, 1, prompt=(
            "Choose a basic Energy card"))
        for card in picks:
            await ctx.attach_energy(card, attacker)
    return effect


def _discard_special_energy_defender(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        special = [energy for energy in ctx.attached_energies(defender)
                   if is_special_energy(energy)]
        if special:
            await ctx.discard_cards(special[:1])
    return effect


def _base_damage_if_defender_type(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    changed, base = int(m.group(2)), int(m.group(3))

    async def effect(ctx):
        defender = ctx.defender
        matches = defender is not None and type_value in (
            defender.get_attribute(AttrID.POKEMON_TYPES) or [])
        await ctx.deal_damage(changed if matches else base)
    return effect


def _delayed_counters_after_opponent_turn(m, ability):
    return _schedule_counters_on_defender(m, ability)


def _bonus_if_defender_stage(m, ability):
    stage = int(m.group(1))
    bonus = int(m.group(3))

    def cond(ctx) -> bool:
        defender = ctx.defender
        return defender is not None and \
            _stage_of(defender) == stage
    return bonus_if(cond, bonus)


def _bonus_if_defender_typed_resistance(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    bonus = int(m.group(3))

    def cond(ctx) -> bool:
        defender = ctx.defender
        if defender is None:
            return False
        # A single resistance is stored as a bare type value, not a list.
        resist = defender.get_attribute(AttrID.RESISTANCE_TYPES)
        if isinstance(resist, (list, tuple, set)):
            return type_value in resist
        return resist == type_value
    return bonus_if(cond, bonus)


def _per_all_in_play_minus_self(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        total = len(ctx.my_pokemon_in_play()) + \
            len(ctx.opponent_pokemon_in_play())
        return max(0, total - 1)
    return damage_per(count, per)


def _typed_energy_threshold_condition(m, ability):
    needed = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value
    condition = CONDITIONS[m.group(3)]

    async def effect(ctx):
        await ctx.deal_damage()
        attacker, defender = ctx.attacker, ctx.defender
        if attacker is None or defender is None or ctx.effects_blocked(defender):
            return
        count = sum(1 for energy in ctx.attached_energies(attacker)
                    if energy_provides_type(energy, type_value))
        if count >= needed:
            await ctx.apply_special_condition(defender, condition)
    return effect


def _per_energy_all_own(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return sum(len(ctx.attached_energies(pokemon))
                   for pokemon in ctx.my_pokemon_in_play())
    return damage_per(count, per)


def _self_mill(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(count, ctx.player_id)
        if top:
            await ctx.discard_cards(top)
    return effect


def _per_distinct_basic_type(m, ability):
    per = int(m.group(1))
    extra = int(m.group(2))

    async def effect(ctx):
        attacker = ctx.attacker
        types = set()
        if attacker is not None:
            for energy in ctx.attached_energies(attacker):
                if not is_basic_energy_card(energy):
                    continue
                for candidate in PokemonTypes:
                    if candidate in (PokemonTypes.NO_COLOR,
                                     PokemonTypes.STRONG, PokemonTypes.HERBAL,
                                     PokemonTypes.UNSET):
                        continue
                    if energy_provides_type(energy, candidate.value):
                        types.add(candidate)
        await ctx.deal_damage(per + extra * len(types))
    return effect


def _flip_attach_basic_from_discard(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        attacker = ctx.attacker
        pile = [card for card in ctx.discard_pile() if is_basic_energy_card(card)]
        if not (results and results[0]) or attacker is None or not pile:
            return
        picks = await ctx.choose_cards(pile, 1, prompt=(
            "Choose a basic Energy card"))
        for card in picks:
            await ctx.attach_energy(card, attacker)
    return effect


def _heal_each_own_including_self(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_pokemon_in_play():
            await ctx.heal(amount, pokemon)
    return effect


def _condition_if_defender_damaged(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        if ctx.max_hp(defender) > defender.get_attribute(AttrID.HP, 0):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _bonus_if_more_hand_than_opponent(m, ability):
    bonus = int(m.group(2))

    def cond(ctx) -> bool:
        return len(ctx.hand()) > len(ctx.hand(ctx.opponent_id))
    return bonus_if(cond, bonus)


def _counters_on_defender_plain(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.deal_damage(counters * 10, target=defender,
                                  as_counters=True)
    return effect


def _shuffle_hand_draw_up_to(m, ability):
    return shuffle_hand_into_deck_draw(int(m.group(1)))


def _bonus_if_stadium_plain(m, ability):
    from ptcgo.game.card_effects.attacks_common import stadium_in_play_cond
    return bonus_if(stadium_in_play_cond, int(m.group(2)))


def _typed_energy_from_discard_to_self(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        pile = [card for card in ctx.discard_pile()
                if is_energy_card(card) and energy_provides_type(card, type_value)]
        if attacker is None or not pile:
            return
        picks = await ctx.choose_cards(pile, count, minimum=0, prompt=(
            f"Choose up to {count} Energy cards"))
        for card in picks:
            await ctx.attach_energy(card, attacker)
    return effect


def _self_asleep_after_damage(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker,
                                              SpecialConditions.ASLEEP)
    return effect


def _self_attack_lock_plain(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            from ptcgo.game.card_effects.attacks_common import lock_all_attacks
            lock_all_attacks(ctx, ctx.attacker)
    return effect


def _flip_trainer_lock(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await _lock_all_trainers(m, ability)(ctx)
    return effect


def _recoil_no_weakness(m, ability):
    return recoil_attack(int(m.group(1)))


def _heal_self_then_no_retreat(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        await ctx.heal(amount, attacker)
        ctx.add_passive_through_opponents_turn(
            attacker, no_retreat_passive(lambda p, c: p is carrier_pokemon(c)))
    return effect


def _draw_to_match_opponent(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        deficit = len(ctx.hand(ctx.opponent_id)) - len(ctx.hand())
        if deficit > 0:
            await ctx.draw_cards(deficit)
    return effect


def _search_tool_to_hand(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(
            lambda card: is_tool_card(card), count=1, minimum=0,
            prompt="Choose a Pokémon Tool card")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=True)
        await ctx.shuffle_deck()
    return effect


def _double_opponent_counters(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_pokemon_in_play():
            if ctx.effects_blocked(pokemon):
                continue
            counters = (ctx.max_hp(pokemon)
                        - pokemon.get_attribute(AttrID.HP, 0)) // 10
            if counters > 0:
                await ctx.deal_damage(counters * 10, target=pokemon,
                                      as_counters=True)
    return effect


def _reveal_hand_per_energy(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        cards = list(ctx.hand(ctx.opponent_id))
        await ctx.reveal_cards(cards, to_player=ctx.player_id)
        energy = sum(1 for card in cards if is_energy_card(card))
        await ctx.deal_damage(per * energy)
    return effect


def _mill_then_recover(m, ability):
    milled, take = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(milled, ctx.player_id)
        if not top:
            return
        await ctx.discard_cards(top)
        picks = await ctx.choose_cards(list(top), min(take, len(top)),
                                       minimum=0, prompt=(
                                           f"Choose up to {take} cards"))
        if picks:
            await ctx.put_in_hand(list(picks), reveal=False)
    return effect


def _search_energy_to_hand_plain(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(is_energy_card, count=1, minimum=0,
                                      prompt="Choose an Energy card")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=True)
        await ctx.shuffle_deck()
    return effect


def _search_basic_bench_any(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(is_basic, count=len(ctx.my_bench()) + 5,
                                      minimum=0,
                                      prompt="Choose any number of Basic Pokémon")
        for card in picks:
            await ctx.bench_pokemon(card)
        await ctx.shuffle_deck()
    return effect


def _half_remaining_hp(m, ability):
    unit = int(m.group(1))

    async def effect(ctx):
        defender = ctx.defender
        remaining = defender.get_attribute(AttrID.HP, 0) if defender else 0
        await ctx.deal_damage((remaining // 2 // unit) * unit)
    return effect


def _attach_hand_basic_one(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_basic_energy_card(card)]
        candidates = [pokemon for pokemon in ctx.my_pokemon_in_play()
                      if pokemon is not None]
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt=(
            "Choose a basic Energy card"))
        if not picks:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates,
                                     "Choose a Pokémon to attach the Energy to")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _shuffle_one_discard_into_deck(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pile = ctx.discard_pile()
        if not pile:
            return
        picks = await ctx.choose_cards(pile, 1, prompt=(
            "Choose a card to shuffle into your deck"))
        if picks:
            await ctx.shuffle_into_deck(list(picks), ctx.player_id)
    return effect


def _bonus_if_defender_special_energy(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        defender = ctx.defender
        if defender is None:
            return False
        return any(is_special_energy(energy)
                   for energy in ctx.attached_energies(defender))
    return bonus_if(cond, bonus)


def _bonus_if_defender_tool(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        defender = ctx.defender
        if defender is None:
            return False
        return any(not is_energy_card(card)
                   for card in ctx.attached_energies(defender))
    return bonus_if(cond, bonus)


def _opponent_switches_self(m, ability):
    return gust_attack(opponent_chooses=True)


def _recover_one_pokemon(m, ability):
    return recover_from_discard(predicate=_is_pokemon_card, count=1,
                                minimum=0)


def _reveal_opponent_top_card(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(1, ctx.opponent_id)
        if top:
            await ctx.reveal_cards(list(top))
    return effect


def _recover_basic_energy(m, ability):
    count = _count(m.group(1))
    return recover_from_discard(predicate=is_basic_energy_card, count=count,
                                minimum=0)


def _recover_typed_basic_energy(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    def predicate(card) -> bool:
        return is_basic_energy_card(card) and \
            energy_provides_type(card, type_value)
    return recover_from_discard(predicate=predicate, count=count, minimum=0)


def _per_benched_both(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return len(ctx.my_bench()) + len(ctx.opponent_bench())
    return damage_per(count, per)


def _prize_gated_self_mill(m, ability):
    first, second, third, mill = (int(m.group(index))
                                  for index in (1, 2, 3, 4))

    async def effect(ctx):
        prizes = 6 - ctx.prizes_taken(ctx.player_id)
        if prizes in (first, second, third):
            top = ctx.deck_top(mill, ctx.player_id)
            if top:
                await ctx.discard_cards(top)
        await ctx.deal_damage()
    return effect


def _discard_any_then_draw_to(m, ability):
    target = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = list(ctx.hand())
        if pool:
            picks = await ctx.choose_cards(pool, len(pool), minimum=0,
                                           prompt="Choose any cards to discard")
            if picks:
                await ctx.discard_cards(list(picks))
        deficit = target - len(ctx.hand())
        if deficit > 0:
            await ctx.draw_cards(deficit)
    return effect


def _shuffle_hand_draw_per_bench(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        hand = list(ctx.hand())
        if hand:
            await ctx.shuffle_into_deck(hand, ctx.player_id)
        count = len(ctx.my_bench()) + len(ctx.opponent_bench())
        if count:
            await ctx.draw_cards(count)
    return effect


def _search_typed_basic_energy_self(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        picks = await ctx.search_deck(
            lambda card: is_basic_energy_card(card)
            and energy_provides_type(card, type_value),
            count=count, minimum=0, prompt="Choose Energy cards")
        for card in picks:
            if attacker is not None:
                await ctx.attach_energy(card, attacker)
        await ctx.shuffle_deck()
    return effect


def _flip_until_tails_discard_energy(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        heads = 0
        while True:
            results = await ctx.flip_coins(1, getattr(ability, "title", ""))
            if not (results and results[0]):
                break
            heads += 1
            if heads > 10:
                break
        defender = ctx.defender
        if heads and defender is not None and not ctx.effects_blocked(defender):
            for _ in range(heads):
                if not ctx.attached_energies(defender):
                    break
                await ctx.discard_energy_from(defender, 1)
    return effect


def _return_defender_energy_to_hand(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        energies = ctx.attached_energies(defender)
        if not energies:
            return
        picks = energies if len(energies) == 1 else await ctx.choose_cards(
            energies, 1, prompt="Choose an Energy card")
        for card in picks:
            await ctx.put_in_hand([card], reveal=True)
    return effect


def _bonus_if_self_typed_energy(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    bonus = int(m.group(2))

    def cond(ctx) -> bool:
        attacker = ctx.attacker
        if attacker is None:
            return False
        return any(energy_provides_type(energy, type_value)
                   for energy in ctx.attached_energies(attacker))
    return bonus_if(cond, bonus)


def _attach_up_to_basic_distributed(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.discard_pile() if is_basic_energy_card(card)]
        candidates = ctx.my_pokemon_in_play()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, count, minimum=0, prompt=(
            f"Choose up to {count} Energy cards"))
        if picks:
            await distribute_energy(ctx, list(picks), candidates)
    return effect


def _attach_typed_hand_distributed(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_basic_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_pokemon_in_play()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, count, minimum=0, prompt=(
            f"Choose up to {count} Energy cards"))
        if picks:
            await distribute_energy(ctx, list(picks), candidates)
    return effect


def _flip_opponent_switch(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await gust_attack(opponent_chooses=False)(ctx)
    return effect


def _flip_all_tails_recoil(m, ability):
    coins, self_damage = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        if results and all(not result for result in results) and \
                ctx.attacker is not None:
            await ctx.deal_damage(self_damage, target=ctx.attacker,
                                  ignore_weakness=True)
    return effect


def _flip_tails_discard_all_energy(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        attacker = ctx.attacker
        if results and results[0] or attacker is None:
            return
        energies = ctx.attached_energies(attacker)
        if energies:
            await ctx.discard_cards(list(energies))
    return effect


def _counters_chosen_then_self_lock(m, ability):
    counters, targets = int(m.group(1)), _count(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                      if not ctx.effects_blocked(pokemon)]
        if not candidates:
            return
        picks = candidates if len(candidates) <= targets else \
            await ctx.choose_cards(candidates, targets,
                                   prompt=f"Choose {targets} Pokémon")
        for target in picks:
            await ctx.deal_damage(counters * 10, target=target,
                                  as_counters=True)
        if ctx.attacker is not None:
            from ptcgo.game.card_effects.attacks_common import lock_all_attacks
            lock_all_attacks(ctx, ctx.attacker)
    return effect


def _counters_damaged_opponent_bench(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_bench():
            if ctx.effects_blocked(pokemon):
                continue
            if ctx.max_hp(pokemon) > pokemon.get_attribute(AttrID.HP, 0):
                await ctx.deal_damage(counters * 10, target=pokemon,
                                      as_counters=True)
    return effect


def _ko_defender_if_condition(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        active = defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        if condition in active:
            await ctx.knock_out(defender)
    return effect


def _recover_items_up_to(m, ability):
    count = _count(m.group(1))

    def predicate(card) -> bool:
        return _trainer_kind(card) is TrainerType.ITEM or is_tool_card(card)
    return recover_from_discard(predicate=predicate, count=count, minimum=0)


def _attach_typed_discard_to_many(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value
    targets = _count(m.group(3)) if m.lastindex and m.lastindex >= 3 else count

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.discard_pile() if is_basic_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_pokemon_in_play()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, count, minimum=0, prompt=(
            f"Choose up to {count} Energy cards"))
        chosen = []
        for card in picks:
            target = candidates[0] if len(candidates) == 1 else \
                await ctx.choose_pokemon(candidates,
                                         "Choose a Pokémon for the Energy")
            if target is not None:
                chosen.append((card, target))
        for card, target in chosen:
            await ctx.attach_energy(card, target)
    return effect


def _attach_typed_discard_each_bench(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if is_basic_energy_card(card)
                and energy_provides_type(card, type_value)]
        if not pile:
            return
        for pokemon in ctx.my_bench():
            if not pile:
                break
            await ctx.attach_energy(pile.pop(0), pokemon)
    return effect


def _discard_typed_energy_own(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_pokemon_in_play():
            energies = [energy for energy in ctx.attached_energies(pokemon)
                        if energy_provides_type(energy, type_value)]
            take = min(count, len(energies))
            if take:
                await ctx.discard_cards(energies[:take])
    return effect


def _per_special_energy_self(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        attacker = ctx.attacker
        if attacker is None:
            return 0
        return sum(1 for energy in ctx.attached_energies(attacker)
                   if is_special_energy(energy))
    return damage_per(count, per)


def _bonus_if_typed_on_bench(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    bonus = int(m.group(2))

    def cond(ctx) -> bool:
        return any(type_value in (pokemon.get_attribute(AttrID.POKEMON_TYPES)
                                  or [])
                   for pokemon in ctx.my_bench())
    return bonus_if(cond, bonus)


def _shuffle_bench_into_deck(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.my_bench()
        if not bench:
            return
        picks = bench if len(bench) <= count else await ctx.choose_cards(
            bench, count, prompt=f"Choose up to {count} Pokémon")
        cards = []
        for pokemon in picks:
            cards.append(pokemon)
            cards.extend(ctx.attached_energies(pokemon))
        if cards:
            await ctx.shuffle_into_deck(cards, ctx.player_id)
    return effect


def _reveal_hand_discard_card(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        cards = list(ctx.hand(ctx.opponent_id))
        if not cards:
            return
        await ctx.reveal_cards(cards)
        picks = await ctx.choose_cards(cards, 1, prompt=(
            "Choose a card to discard"))
        if picks:
            await ctx.discard_cards(list(picks))
    return effect


def _per_typed_energy_opponent_all(m, ability):
    per = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.opponent_pokemon_in_play()
                   for energy in ctx.attached_energies(pokemon)
                   if energy_provides_type(energy, type_value))
    return damage_per(count, per)


def _discard_self_and_cards(m, ability):
    async def effect(ctx):
        if ctx.attacker is not None:
            await ctx.discard_cards([ctx.attacker])
    return effect


def _gate_hand_equal(m, ability):
    async def effect(ctx):
        if len(ctx.hand()) != len(ctx.hand(ctx.opponent_id)):
            return
        await ctx.deal_damage()
    return effect


def _discard_all_special_opponent(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        special = [energy for pokemon in ctx.opponent_pokemon_in_play()
                   for energy in ctx.attached_energies(pokemon)
                   if is_special_energy(energy)]
        if special:
            await ctx.discard_cards(special)
    return effect


def _counters_each_opponent(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_pokemon_in_play():
            if not ctx.effects_blocked(pokemon):
                await ctx.deal_damage(counters * 10, target=pokemon,
                                      as_counters=True)
    return effect


def _search_basic_energy_attach_distributed(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(is_basic_energy_card, count=count,
                                      minimum=0, prompt="Choose Energy cards")
        candidates = ctx.my_pokemon_in_play()
        if picks and candidates:
            await distribute_energy(ctx, list(picks), candidates)
        await ctx.shuffle_deck()
    return effect


def _ko_opponent_with_counters(m, ability):
    counters = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_pokemon_in_play():
            if ctx.effects_blocked(pokemon):
                continue
            on_it = (ctx.max_hp(pokemon)
                     - pokemon.get_attribute(AttrID.HP, 0)) // 10
            if on_it == counters:
                await ctx.knock_out(pokemon)
    return effect


def _discard_all_energy_take_prize(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        energies = ctx.attached_energies(attacker)
        if energies:
            await ctx.discard_cards(list(energies))
        await ctx.take_prizes(1, ctx.player_id)
    return effect


def _per_stage_on_bench(m, ability):
    stage = int(m.group(1))
    per = int(m.group(2))

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.my_bench()
                   if _stage_of(pokemon) == stage)
    return damage_per(count, per)


def _attach_typed_hand_to_bench(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_basic_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_bench()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt=(
            "Choose an Energy card"))
        if not picks:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates,
                                     "Choose a Benched Pokémon")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _per_counters_flip(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        attacker = ctx.attacker
        if attacker is None:
            return
        counters = (ctx.max_hp(attacker)
                    - attacker.get_attribute(AttrID.HP, 0)) // 10
        results = await ctx.flip_coins(max(1, counters),
                                       getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        await ctx.deal_damage(per * heads)
    return effect


def _refresh_hand(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pool = list(ctx.hand())
        picks = []
        if pool:
            picks = await ctx.choose_cards(pool, len(pool), minimum=0,
                                           prompt="Choose any cards to discard")
            if picks:
                await ctx.discard_cards(list(picks))
        if picks:
            await ctx.draw_cards(len(picks))
    return effect


def _bonus_if_self_special_energy(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        attacker = ctx.attacker
        if attacker is None:
            return False
        return any(is_special_energy(energy)
                   for energy in ctx.attached_energies(attacker))
    return bonus_if(cond, bonus)


def _per_hand_size(m, ability):
    per = int(m.group(1))
    return damage_per(lambda ctx: len(ctx.hand()), per)


def _per_opponent_hand_size(m, ability):
    per = int(m.group(1))
    return damage_per(lambda ctx: len(ctx.hand(ctx.opponent_id)), per)


def _cure_defender(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.cure_all_conditions(defender)
    return effect


def _flip_draw_per_heads(m, ability):
    coins = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        if heads:
            await ctx.draw_cards(heads)
    return effect


def _bonus_if_defender_resistance(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        defender = ctx.defender
        return defender is not None and bool(
            defender.get_attribute(AttrID.RESISTANCE_TYPES))
    return bonus_if(cond, bonus)


def _search_any_cards(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(None, count=count, minimum=0,
                                      prompt=f"Choose up to {count} cards")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=True)
        await ctx.shuffle_deck()
    return effect


def _per_defender_retreat_cost(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        defender = ctx.defender
        if defender is None:
            return 0
        cost = defender.get_attribute(AttrID.RETREAT_COST, 0)
        return int(cost) if isinstance(cost, (int, float)) else 0
    return damage_per(count, per)


def _flip_heal_each_own(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if not (results and results[0]):
            return
        for pokemon in ctx.my_pokemon_in_play():
            await ctx.heal(amount, pokemon)
    return effect


def _prevent_damage_from_ex(m, ability):
    from ptcgo.game.card_effects.passives_common import (
        PredicatePreventionPassive)
    from ptcgo.game.data_utils import subtypes_for

    def is_ex_attacker(calc) -> bool:
        attacker = getattr(calc, "attacker", None)
        if attacker is None:
            return False
        return any(subtype.lower() == "ex"
                   for subtype in subtypes_for(attacker.archetype_id))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        ctx.add_passive_through_opponents_turn(
            attacker, PredicatePreventionPassive(
                lambda calc, c: is_ex_attacker(calc)))
    return effect


def _stadium_discard_bonus(m, ability):
    bonus = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.stadium_in_play() is None:
            return
        if await ctx.ask_yes_no(prompt="Discard the Stadium card?"):
            await ctx.discard_stadium()
            await ctx.deal_damage(bonus, apply_modifiers=False)
    return effect


def _mill_per_typed_energy_self(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        count = sum(1 for energy in ctx.attached_energies(attacker)
                    if energy_provides_type(energy, type_value))
        if count:
            top = ctx.deck_top(count, ctx.opponent_id)
            if top:
                await ctx.discard_cards(top)
    return effect


def _stadium_bonus_and_discard(m, ability):
    from ptcgo.game.card_effects.attacks_common import stadium_in_play_cond
    bonus = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if stadium_in_play_cond(ctx):
            await ctx.deal_damage(bonus, apply_modifiers=False)
            await ctx.discard_stadium()
    return effect


def _reveal_hand_discard_items(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        cards = list(ctx.hand(ctx.opponent_id))
        if not cards:
            return
        await ctx.reveal_cards(cards)
        items = [card for card in cards if is_tool_card(card)]
        if items:
            await ctx.discard_cards(items)
    return effect


def _discard_energy_trade_condition(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None or not ctx.attached_energies(attacker):
            return
        if await ctx.ask_yes_no(prompt="Discard an Energy card?"):
            if await ctx.discard_energy_from(attacker, 1):
                defender = ctx.defender
                if defender is not None and not ctx.effects_blocked(defender):
                    await ctx.apply_special_condition(defender, condition)
    return effect


def _attach_discard_basic_to_many(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.discard_pile() if is_basic_energy_card(card)]
        candidates = ctx.my_pokemon_in_play()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, count, minimum=0, prompt=(
            f"Choose up to {count} Energy cards"))
        chosen = []
        for card in picks:
            target = candidates[0] if len(candidates) == 1 else \
                await ctx.choose_pokemon(candidates,
                                         "Choose a Pokémon for the Energy")
            if target is not None:
                chosen.append((card, target))
        for card, target in chosen:
            await ctx.attach_energy(card, target)
    return effect


def _discard_typed_hand_draw(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    draw = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, prompt=(
            "Choose an Energy card to discard"))
        if picks:
            await ctx.discard_cards(list(picks))
            await ctx.draw_cards(draw)
    return effect


def _discard_named_hand_draw(m, ability):
    wanted = normalize(m.group(1))
    draw = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand()
                if wanted in normalize(getattr(card, "display_name", "") or "")]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, prompt=(
            "Choose a card to discard"))
        if picks:
            await ctx.discard_cards(list(picks))
            await ctx.draw_cards(draw)
    return effect


def _per_tools_in_play(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        total = 0
        for pokemon in ctx.my_pokemon_in_play() + \
                ctx.opponent_pokemon_in_play():
            total += sum(1 for card in ctx.attached_energies(pokemon)
                         if not is_energy_card(card))
        return total
    return damage_per(count, per)


def _attach_hand_basic_to_many(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_basic_energy_card(card)]
        candidates = ctx.my_pokemon_in_play()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, count, minimum=0, prompt=(
            f"Choose up to {count} Energy cards"))
        chosen = []
        for card in picks:
            target = candidates[0] if len(candidates) == 1 else \
                await ctx.choose_pokemon(candidates,
                                         "Choose a Pokémon for the Energy")
            if target is not None:
                chosen.append((card, target))
        for card, target in chosen:
            await ctx.attach_energy(card, target)
    return effect


def _lock_supporters(m, ability):
    from ptcgo.game.attributes import TrainerType

    async def effect(ctx):
        await ctx.deal_damage()
        ctx.lock_plays(
            ctx.opponent_id,
            lambda card: _trainer_kind(card) is TrainerType.SUPPORTER)
    return effect


def _lock_defender_if_ex(m, ability):
    from ptcgo.game.card_effects.attacks_common import (
        defender_is_ex, lock_defender_attacks)

    async def effect(ctx):
        await ctx.deal_damage()
        if defender_is_ex(ctx):
            lock_defender_attacks(ctx)
    return effect


def _heal_all_chosen_then_discard_energy(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        candidates = ctx.my_pokemon_in_play()
        if not candidates:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal")
        if target is not None:
            await ctx.heal(9990, target)
        if attacker is not None:
            energies = ctx.attached_energies(attacker)
            if energies:
                await ctx.discard_cards(list(energies))
    return effect


def _gate_undamaged_only(m, ability):
    async def effect(ctx):
        attacker = ctx.attacker
        if attacker is not None and ctx.max_hp(attacker) > \
                attacker.get_attribute(AttrID.HP, 0):
            return
        await ctx.deal_damage()
    return effect


def _per_defender_conditions(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        defender = ctx.defender
        if defender is None:
            return 0
        return len(defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    return damage_per(count, per)


def _per_lost_zone_own(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return ctx.lost_zone_count(ctx.player_id)
    return damage_per(count, per)


def _mill_opponent_lost_zone_then_asleep(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(1, ctx.opponent_id)
        if top:
            await ctx.move_to_lost_zone(list(top))
        if ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker,
                                              SpecialConditions.ASLEEP)
    return effect


def _bonus_if_evolved_from(m, ability):
    wanted = normalize(m.group(1))
    bonus = int(m.group(3))

    def cond(ctx) -> bool:
        attacker = ctx.attacker
        if attacker is None:
            return False
        previous = attacker.get_attribute(AttrID.EVOLVES_FROM)
        names = [previous] if isinstance(previous, str) else list(previous or [])
        return any(normalize(str(name)) == wanted for name in names)
    return bonus_if(cond, bonus)


def _condition_then_heal_chosen(m, ability):
    condition = CONDITIONS[m.group(1)]
    amount = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
        candidates = ctx.my_pokemon_in_play()
        if not candidates:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal")
        if target is not None:
            await ctx.heal(amount, target)
    return effect


def _heal_typed_own(m, ability):
    amount = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_pokemon_in_play():
            if type_value in (pokemon.get_attribute(AttrID.POKEMON_TYPES)
                              or []):
                await ctx.heal(amount, pokemon)
    return effect


def _per_typed_all_in_play(m, ability):
    per = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    def count(ctx) -> int:
        return sum(1 for pokemon in (ctx.my_pokemon_in_play()
                                     + ctx.opponent_pokemon_in_play())
                   if type_value in (pokemon.get_attribute(AttrID.POKEMON_TYPES)
                                     or []))
    return damage_per(count, per)


def _move_all_counters_to_defender(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker, defender = ctx.attacker, ctx.defender
        if attacker is None or defender is None or \
                ctx.effects_blocked(defender):
            return
        counters = (ctx.max_hp(attacker)
                    - attacker.get_attribute(AttrID.HP, 0)) // 10
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0] and counters > 0:
            await ctx.heal(9990, attacker)
            await ctx.deal_damage(counters * 10, target=defender,
                                  as_counters=True)
    return effect


def _counters_on_both_benches(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_bench() + ctx.opponent_bench():
            if not ctx.effects_blocked(pokemon):
                await ctx.deal_damage(counters * 10, target=pokemon,
                                      as_counters=True)
    return effect


def _scale_per_distinct_basic_type_self(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        attacker = ctx.attacker
        types = set()
        if attacker is not None:
            for energy in ctx.attached_energies(attacker):
                if not is_basic_energy_card(energy):
                    continue
                for candidate in PokemonTypes:
                    if candidate in (PokemonTypes.NO_COLOR,
                                     PokemonTypes.STRONG,
                                     PokemonTypes.HERBAL, PokemonTypes.UNSET):
                        continue
                    if energy_provides_type(energy, candidate.value):
                        types.add(candidate)
        await ctx.deal_damage(per * len(types))
    return effect


def _gate_self_condition_draw(m, ability):
    condition = CONDITIONS[m.group(1)]
    draw = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        active = attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        if condition in active:
            await ctx.draw_cards(draw)
    return effect


def _condition_if_defender_lower_hp(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        attacker, defender = ctx.attacker, ctx.defender
        if attacker is None or defender is None or \
                ctx.effects_blocked(defender):
            return
        if defender.get_attribute(AttrID.HP, 0) < \
                attacker.get_attribute(AttrID.HP, 0):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _base_plus_typed_energy_self(m, ability):
    base = int(m.group(1))
    per = int(m.group(2))
    type_value = TYPE_WORDS[m.group(3)].value

    async def effect(ctx):
        attacker = ctx.attacker
        count = 0
        if attacker is not None:
            count = sum(1 for energy in ctx.attached_energies(attacker)
                        if energy_provides_type(energy, type_value))
        await ctx.deal_damage(base + per * count)
    return effect


def _stadium_heal_self(m, ability):
    from ptcgo.game.card_effects.attacks_common import stadium_in_play_cond
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if stadium_in_play_cond(ctx) and ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
    return effect


def _reveal_top_conditional_draw(m, ability):
    draw = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(1, ctx.player_id)
        if not top:
            return
        await ctx.put_in_hand(list(top), reveal=True)
        if _is_pokemon_card(top[0]):
            await ctx.draw_cards(draw)
    return effect


def _mill_then_condition(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(1, ctx.player_id)
        if not top:
            return
        await ctx.discard_cards(list(top))
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _confused_and_no_retreat(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        await ctx.apply_special_condition(defender, SpecialConditions.CONFUSED)
        ctx.add_passive_through_opponents_turn(
            defender, no_retreat_passive(lambda p, c: p is carrier_pokemon(c)))
    return effect


def _flip_until_mill_opponent(m, ability):
    per = 1

    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_until_tails(getattr(ability, "title", ""))
        milled = heads + 1
        if milled > 1:
            top = ctx.deck_top(per * (milled - 1), ctx.opponent_id)
            if top:
                await ctx.discard_cards(top)
    return effect


def _flip_discard_energy_each_opponent(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if not (results and results[0]):
            return
        for pokemon in ctx.opponent_pokemon_in_play():
            if not ctx.effects_blocked(pokemon) and \
                    ctx.attached_energies(pokemon):
                await ctx.discard_energy_from(pokemon, 1)
    return effect


def _flip_until_heal_chosen(m, ability):
    amount = int(m.group(1))
    targets = _count(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_until_tails(getattr(ability, "title", ""))
        for _ in range(heads):
            candidates = [pokemon for pokemon in ctx.my_pokemon_in_play()
                          if ctx.max_hp(pokemon)
                          > pokemon.get_attribute(AttrID.HP, 0)]
            if not candidates:
                return
            picks = candidates if len(candidates) <= targets else \
                await ctx.choose_cards(candidates, targets,
                                       prompt="Choose Pokémon to heal")
            for pokemon in picks:
                await ctx.heal(amount, pokemon)
    return effect


def _discard_energy_any_own(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        energies = []
        for pokemon in ctx.my_pokemon_in_play():
            for energy in ctx.attached_energies(pokemon):
                energies.append((energy, pokemon))
        if not energies:
            return
        cards = [energy for energy, _ in energies]
        picks = await ctx.choose_cards(cards, count, minimum=0, prompt=(
            f"Choose up to {count} Energy cards to discard"))
        if picks:
            await ctx.discard_cards(list(picks))
    return effect


def _base_swap_if_lower_hp(m, ability):
    changed = int(m.group(1))

    async def effect(ctx):
        attacker, defender = ctx.attacker, ctx.defender
        lowered = attacker is not None and defender is not None and \
            defender.get_attribute(AttrID.HP, 0) < \
            attacker.get_attribute(AttrID.HP, 0)
        await ctx.deal_damage(changed if lowered else None)
    return effect


def _flip_multi_condition(m, ability):
    coins = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        defender = ctx.defender
        if not (results and all(results)) or defender is None or \
                ctx.effects_blocked(defender):
            return
        for condition in (SpecialConditions.BURNED, SpecialConditions.PARALYZED,
                          SpecialConditions.POISONED):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _move_counters_to_opponent_bench(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        candidates = [pokemon for pokemon in ctx.opponent_bench()
                      if not ctx.effects_blocked(pokemon)]
        if attacker is None or not candidates:
            return
        counters = min(limit, (ctx.max_hp(attacker)
                               - attacker.get_attribute(AttrID.HP, 0)) // 10)
        if counters <= 0:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Benched Pokémon")
        if target is None:
            return
        await ctx.heal(counters * 10, attacker)
        await ctx.deal_damage(counters * 10, target=target, as_counters=True)
    return effect


def _flip_tails_discard_self_energy_many(m, ability):
    coins = int(m.group(1))
    per = _count(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        tails = sum(1 for result in results or [] if not result)
        attacker = ctx.attacker
        if not tails or attacker is None:
            return
        energies = ctx.attached_energies(attacker)
        take = min(tails * per, len(energies))
        if take:
            await ctx.discard_cards(energies[:take])
    return effect


def _mill_opponent_heal_self(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(1, ctx.opponent_id)
        if top:
            await ctx.discard_cards(top)
        if ctx.attacker is not None:
            await ctx.heal(10, ctx.attacker)
    return effect


def _switch_defender_with_bench(m, ability):
    from ptcgo.game.card_effects.support_common import opponent_switches

    async def effect(ctx):
        await ctx.deal_damage()
        await opponent_switches(ctx)
    return effect


def _peek_opponent_top_cards(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(count, ctx.opponent_id)
        if top:
            await ctx.reveal_cards(list(top))
    return effect


def _nothing_on_tails(m, ability):
    return flip_or_nothing()


def _flip_heal_self_each_heads(m, ability):
    coins = int(m.group(1))
    amount = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        if heads and ctx.attacker is not None:
            await ctx.heal(amount * heads, ctx.attacker)
    return effect


def _shuffle_basic_energy_back(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if is_basic_energy_card(card)]
        if not pile:
            return
        picks = await ctx.choose_cards(pile, 1, prompt=(
            "Choose an Energy card to shuffle into your deck"))
        if picks:
            await ctx.shuffle_into_deck(list(picks), ctx.player_id)
    return effect


def _counter_on_defender_single(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.deal_damage(10, target=defender, as_counters=True)
    return effect


def _refresh_up_to(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = list(ctx.hand())
        picks = []
        if pool:
            picks = await ctx.choose_cards(pool, limit, minimum=0, prompt=(
                f"Choose up to {limit} cards to discard"))
            if picks:
                await ctx.discard_cards(list(picks))
        if picks:
            await ctx.draw_cards(len(picks))
    return effect


def _base_swap_if_damaged(m, ability):
    threshold, changed = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        attacker = ctx.attacker
        counters = 0
        if attacker is not None:
            counters = (ctx.max_hp(attacker)
                        - attacker.get_attribute(AttrID.HP, 0)) // 10
        await ctx.deal_damage(changed if counters >= threshold else None)
    return effect


def _heal_chosen_with_energy(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = [pokemon for pokemon in ctx.my_pokemon_in_play()
                      if ctx.attached_energies(pokemon)]
        if not candidates:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal")
        if target is not None:
            await ctx.heal(amount, target)
    return effect


def _heal_self_single_counter(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.heal(10, ctx.attacker)
    return effect


def _flip_times_heads_optional_period(m, ability):
    return flip_damage(coins=_count(m.group(1)), per_heads=int(m.group(2)))


def _counter_on_chosen_opponent(m, ability):
    count = 1

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                      if not ctx.effects_blocked(pokemon)]
        if not candidates:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Pokémon")
        if target is not None:
            await ctx.deal_damage(10, target=target, as_counters=True)
    return effect


def _flip_scaled_in_play(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await ctx.deal_damage(per * len(ctx.my_pokemon_in_play()))
    return effect


def _heal_each_own_plain(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_pokemon_in_play():
            await ctx.heal(amount, pokemon)
    return effect


def _attach_discard_energy_active(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        active = ctx.my_active()
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)]
        if active is None or not pile:
            return
        picks = await ctx.choose_cards(pile, count, minimum=0, prompt=(
            f"Choose up to {count} Energy cards"))
        for card in picks:
            await ctx.attach_energy(card, active)
    return effect


def _attach_up_to_discard_self(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)]
        if attacker is None or not pile:
            return
        picks = await ctx.choose_cards(pile, limit, minimum=0, prompt=(
            f"Choose up to {limit} Energy cards"))
        for card in picks:
            await ctx.attach_energy(card, attacker)
    return effect


def _gate_no_opponent_ex(m, ability):
    from ptcgo.game.card_effects.trainers import is_pokemon_ex

    async def effect(ctx):
        if any(is_pokemon_ex(pokemon)
               for pokemon in ctx.opponent_pokemon_in_play()):
            return
        await ctx.deal_damage()
    return effect


def _base_swap_if_defender_type_plain(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    changed = int(m.group(2))

    async def effect(ctx):
        defender = ctx.defender
        matches = defender is not None and type_value in (
            defender.get_attribute(AttrID.POKEMON_TYPES) or [])
        await ctx.deal_damage(changed if matches else None)
    return effect


def _energy_from_self_to_hand(m, ability):
    count = _count(m.group(1)) if m.lastindex else 1

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        energies = ctx.attached_energies(attacker)
        if not energies:
            return
        picks = energies if len(energies) <= count else \
            await ctx.choose_cards(energies, count, prompt=(
                "Choose Energy to return to hand"))
        if picks:
            await ctx.put_in_hand(list(picks), reveal=False)
    return effect


def _bonus_named_energy_attached(m, ability):
    per = int(m.group(1))
    wanted = normalize(m.group(2))

    def count(ctx) -> int:
        attacker = ctx.attacker
        if attacker is None:
            return 0
        return sum(1 for card in ctx.attached_energies(attacker)
                   if wanted in normalize(getattr(card, "display_name", "") or
                                          getattr(card, "name", "") or ""))
    return damage_per(count, per)


def _condition_then_optional_switch(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
        if ctx.my_bench() and await ctx.ask_yes_no(
                prompt="Switch this Pokémon with a Benched Pokémon?"):
            await switch_self_attack()(ctx)
    return effect


def _bonus_per_own_bench(m, ability):
    base, per = int(m.group(1)), int(m.group(2))
    return damage_per(lambda ctx: len(ctx.my_bench()), per, base=base)


def _condition_if_defender_special_energy(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        if any(is_special_energy(energy)
               for energy in ctx.attached_energies(defender)):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _condition_if_named_stadium(m, ability):
    wanted = normalize(m.group(1))
    condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        stadium = ctx.stadium_in_play()
        if stadium is None:
            return
        name = normalize(getattr(stadium, "display_name", "")
                         or getattr(stadium, "name", "") or "")
        defender = ctx.defender
        if wanted in name and defender is not None and \
                not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _flip_until_draw(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_until_tails(getattr(ability, "title", ""))
        if heads:
            await ctx.draw_cards(per * heads)
    return effect


def _lock_defender_if_basic(m, ability):
    from ptcgo.game.card_effects.attacks_common import lock_defender_attacks
    from ptcgo.game.session.effects import is_basic_pokemon

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and is_basic_pokemon(defender):
            lock_defender_attacks(ctx)
    return effect


def _per_benched_stage(m, ability):
    per = int(m.group(1))
    stage = int(m.group(2))

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.my_bench()
                   if _stage_of(pokemon) == stage)
    return damage_per(count, per)


def _opponent_chooses_counter_target(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                      if not ctx.effects_blocked(pokemon)]
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon", player_id=ctx.opponent_id)
        if target is not None:
            await ctx.deal_damage(counters * 10, target=target,
                                  as_counters=True)
    return effect


def _discard_two_typed_energy(m, ability):
    first = TYPE_WORDS[m.group(1)].value
    second = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        for type_value in (first, second):
            energies = [energy for energy in ctx.attached_energies(attacker)
                        if energy_provides_type(energy, type_value)]
            if energies:
                await ctx.discard_cards(energies[:1])
    return effect


def _counters_each_defender(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.deal_damage(counters * 10, target=defender,
                                  as_counters=True)
    return effect


def _per_counters_on_active(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        active = ctx.my_active()
        if active is None:
            return 0
        return (ctx.max_hp(active) - active.get_attribute(AttrID.HP, 0)) // 10
    return damage_per(count, per)


def _damage_each_active(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        for pokemon in (ctx.my_active(), ctx.opponent_active()):
            if pokemon is not None:
                await ctx.deal_damage(amount, target=pokemon,
                                      ignore_weakness=True,
                                      ignore_resistance=True)
    return effect


def _mill_attach_basic_energy(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(1, ctx.player_id)
        attacker = ctx.attacker
        if not top or attacker is None:
            return
        card = top[0]
        if is_basic_energy_card(card):
            await ctx.attach_energy(card, attacker)
        else:
            await ctx.discard_cards(top)
    return effect


def _condition_discard_defender_energy(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        active = defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        if condition in active and ctx.attached_energies(defender):
            await ctx.discard_energy_from(defender, 1)
    return effect


def _bonus_special_energy_in_opponent_discard(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return sum(1 for card in ctx.discard_pile(ctx.opponent_id)
                   if is_special_energy(card))
    return damage_per(count, per)


def _bonus_per_defender_distinct_type(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        defender = ctx.defender
        if defender is None:
            return 0
        types = set()
        for energy in ctx.attached_energies(defender):
            for candidate in PokemonTypes:
                if candidate in (PokemonTypes.NO_COLOR, PokemonTypes.STRONG,
                                 PokemonTypes.HERBAL, PokemonTypes.UNSET):
                    continue
                if energy_provides_type(energy, candidate.value):
                    types.add(candidate)
        return len(types)
    return damage_per(count, per)


def _recover_stadium(m, ability):
    def predicate(card) -> bool:
        return (card.get_attribute(AttrID.CARD_TYPE) or "") == "Stadium"
    return recover_from_discard(predicate=predicate, count=1, minimum=0)


def _pre_damage_heal_defender(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        defender = ctx.defender
        if defender is not None:
            await ctx.heal(amount, defender)
        await ctx.deal_damage()
    return effect


def _flip_attach_typed(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        pool = [card for card in ctx.hand() if is_basic_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_pokemon_in_play()
        if not (results and results[0]) or not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, 1, prompt=(
            "Choose an Energy card"))
        if not picks:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates,
                                     "Choose a Pokémon for the Energy")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _per_typed_energy_in_play(m, ability):
    base = int(m.group(1))
    per = int(m.group(2))
    type_value = TYPE_WORDS[m.group(3)].value

    def count(ctx) -> int:
        total = 0
        for pokemon in (ctx.my_pokemon_in_play()
                        + ctx.opponent_pokemon_in_play()):
            total += sum(1 for energy in ctx.attached_energies(pokemon)
                         if energy_provides_type(energy, type_value))
        return total
    return damage_per(count, per, base=base)


def _gate_all_tails_nothing(m, ability):
    coins = _count(m.group(1))

    async def effect(ctx):
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        if results and not any(results):
            return
        await ctx.deal_damage()
    return effect


def _flip_defender_condition_choice(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        defender = ctx.defender
        if not (results and results[0]) or defender is None or \
                ctx.effects_blocked(defender):
            return
        await _choose_condition(ctx, [SpecialConditions.ASLEEP,
                                      SpecialConditions.CONFUSED,
                                      SpecialConditions.PARALYZED,
                                      SpecialConditions.POISONED])
    return effect


def _flip_heal_if_damaged(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None or ctx.max_hp(attacker) <= \
                attacker.get_attribute(AttrID.HP, 0):
            return
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await ctx.heal(amount, attacker)
    return effect


def _typed_energy_discard_to_self(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        if attacker is None or not pile:
            return
        picks = await ctx.choose_cards(pile, count, minimum=0, prompt=(
            f"Choose up to {count} Energy cards"))
        for card in picks:
            await ctx.attach_energy(card, attacker)
    return effect


def _flip_condition_heads_any(m, ability):
    coins = _count(m.group(1))
    condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        defender = ctx.defender
        if not (results and any(results)) or defender is None or \
                ctx.effects_blocked(defender):
            return
        await ctx.apply_special_condition(defender, condition)
    return effect


def _flip_topdeck_opponent_discard(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        pile = ctx.discard_pile(ctx.opponent_id)
        if not (results and results[0]) or not pile:
            return
        picks = await ctx.choose_cards(pile, 1, prompt=(
            "Choose a card to put on top of the deck"))
        for card in picks:
            await ctx.put_on_top_of_deck(card)
    return effect


def _flip_switch_self_b58(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0] and ctx.my_bench():
            await switch_self_attack()(ctx)
    return effect


def _flip_recover_energy_per_heads(m, ability):
    coins = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        if not heads or not pile:
            return
        picks = await ctx.choose_cards(pile, heads, minimum=0, prompt=(
            "Choose Energy cards"))
        if picks:
            await ctx.put_in_hand(list(picks), reveal=False)
    return effect


def _recoil_then_discard_stadium(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.deal_damage(amount, target=ctx.attacker,
                                  ignore_weakness=True)
        if ctx.stadium_in_play() is not None:
            await ctx.discard_stadium()
    return effect


def _heal_both_sides_damaged(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in (ctx.my_pokemon_in_play()
                        + ctx.opponent_pokemon_in_play()):
            if ctx.max_hp(pokemon) > pokemon.get_attribute(AttrID.HP, 0):
                await ctx.heal(amount, pokemon)
    return effect


def _flip_defender_or_condition(m, ability):
    heads_condition = CONDITIONS[m.group(1)]
    tails_condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        condition = heads_condition if (results and results[0]) else \
            tails_condition
        await ctx.apply_special_condition(defender, condition)
    return effect


def _recoil_then_flip_condition(m, ability):
    amount = int(m.group(1))
    condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.deal_damage(amount, target=ctx.attacker,
                                  ignore_weakness=True)
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        defender = ctx.defender
        if results and results[0] and defender is not None and \
                not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _flip_two_conditions_b58(m, ability):
    first = CONDITIONS[m.group(2)]
    second = CONDITIONS[m.group(3)]

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        defender = ctx.defender
        if not (results and results[0]) or defender is None or \
                ctx.effects_blocked(defender):
            return
        await ctx.apply_special_condition(defender, first)
        await ctx.apply_special_condition(defender, second)
    return effect


def _flip_shuffle_self_into_deck(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await _shuffle_self_into_deck(m, ability)(ctx)
    return effect


def _flip_draw_plain(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await ctx.draw_cards(count)
    return effect


def _base_doubled_if_defender_type(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        defender = ctx.defender
        matches = defender is not None and type_value in (
            defender.get_attribute(AttrID.POKEMON_TYPES) or [])
        if matches:
            amount = (getattr(ctx.ability, "damage", 0) or 0) * 2
            await ctx.deal_damage(amount)
        else:
            await ctx.deal_damage()
    return effect


def _flip_tails_discard_all_energy_cards(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        attacker = ctx.attacker
        if (results and results[0]) or attacker is None:
            return
        energies = ctx.attached_energies(attacker)
        if energies:
            await ctx.discard_cards(list(energies))
    return effect


def _flip_tails_self_lock_b58(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and not results[0] and ctx.attacker is not None:
            from ptcgo.game.card_effects.attacks_common import lock_all_attacks
            lock_all_attacks(ctx, ctx.attacker)
    return effect


def _flip_defender_no_retreat(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        defender = ctx.defender
        if results and results[0] and defender is not None:
            ctx.add_passive_through_opponents_turn(
                defender, no_retreat_passive(
                    lambda p, c: p is carrier_pokemon(c)))
    return effect


def _flip_counters_until_hp_b58(m, ability):
    target_hp = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        defender = ctx.defender
        if not (results and results[0]) or defender is None or \
                ctx.effects_blocked(defender):
            return
        counters = (defender.get_attribute(AttrID.HP, 0) - target_hp) // 10
        if counters > 0:
            await ctx.deal_damage(counters * 10, target=defender,
                                  as_counters=True)
    return effect


def _each_player_draws_b58(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.draw_cards(count)
        await ctx.draw_cards(count, ctx.opponent_id)
    return effect


def _flip_all_heads_base_plus(m, ability):
    coins = _count(m.group(1))
    base, bonus = int(m.group(2)), int(m.group(3))

    async def effect(ctx):
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        success = results and all(results)
        await ctx.deal_damage(base + bonus if success else base)
    return effect


def _draw_per_typed_energy_all(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        count = sum(1 for pokemon in ctx.my_pokemon_in_play()
                    for energy in ctx.attached_energies(pokemon)
                    if energy_provides_type(energy, type_value))
        if count:
            await ctx.draw_cards(count)
    return effect


def _flip_bonus_or_recoil(m, ability):
    bonus, recoil = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            printed = getattr(ctx.ability, "damage", 0) or 0
            await ctx.deal_damage(printed + bonus)
        elif ctx.attacker is not None:
            await ctx.deal_damage(recoil, target=ctx.attacker,
                                  ignore_weakness=True)
    return effect


def _draw_per_typed_in_play(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        count = sum(1 for pokemon in ctx.my_pokemon_in_play()
                    if type_value in (pokemon.get_attribute(AttrID.POKEMON_TYPES)
                                      or []))
        if count:
            await ctx.draw_cards(count)
    return effect


def _condition_then_heal_self(m, ability):
    condition = CONDITIONS[m.group(1)]
    amount = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
        if ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
    return effect


def _discard_random_opponent_hand(m, ability):
    coins = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        for _ in range(heads):
            hand = ctx.hand(ctx.opponent_id)
            if not hand:
                return
            await ctx.discard_cards([random.choice(list(hand))])
    return effect


def _condition_then_flip_second(m, ability):
    first = CONDITIONS[m.group(1)]
    second = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        await ctx.apply_special_condition(defender, first)
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await ctx.apply_special_condition(defender, second)
    return effect


def _base_swap_if_opponent_typed(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    changed, base = int(m.group(2)), int(m.group(3))

    async def effect(ctx):
        has_typed = any(type_value in (pokemon.get_attribute(
            AttrID.POKEMON_TYPES) or [])
            for pokemon in ctx.opponent_pokemon_in_play())
        await ctx.deal_damage(changed if has_typed else base)
    return effect


def _mill_opponent_then_heal_self(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(1, ctx.opponent_id)
        if top:
            await ctx.discard_cards(top)
        if ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
    return effect


def _recover_typed_energy_distributed(m, ability):
    limit = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_pokemon_in_play()
        if not pile or not candidates:
            return
        picks = await ctx.choose_cards(pile, limit, minimum=0, prompt=(
            f"Choose up to {limit} Energy cards"))
        if picks:
            await distribute_energy(ctx, list(picks), candidates)
    return effect


def _recover_typed_energy_to_many(m, ability):
    limit = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_pokemon_in_play()
        if not pile or not candidates:
            return
        picks = await ctx.choose_cards(pile, limit, minimum=0, prompt=(
            f"Choose up to {limit} Energy cards"))
        chosen = []
        for card in picks:
            target = candidates[0] if len(candidates) == 1 else \
                await ctx.choose_pokemon(candidates,
                                         "Choose a Pokémon for the Energy")
            if target is not None:
                chosen.append((card, target))
        for card, target in chosen:
            await ctx.attach_energy(card, target)
    return effect


def _discard_typed_hand_then_draw(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    draw = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        if pool:
            picks = await ctx.choose_cards(pool, 1, prompt=(
                "Choose an Energy card to discard"))
            if picks:
                await ctx.discard_cards(list(picks))
        await ctx.draw_cards(draw)
    return effect


def _flip_per_typed_in_play(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    per = int(m.group(2))

    async def effect(ctx):
        count = sum(1 for pokemon in ctx.my_pokemon_in_play()
                    if type_value in (pokemon.get_attribute(AttrID.POKEMON_TYPES)
                                      or []))
        results = await ctx.flip_coins(max(1, count),
                                       getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        await ctx.deal_damage(per * heads)
    return effect


def _heal_each_with_energy(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_pokemon_in_play():
            if ctx.attached_energies(pokemon):
                await ctx.heal(amount, pokemon)
    return effect


def _flip_switch_defender(m, ability):
    from ptcgo.game.card_effects.support_common import opponent_switches

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0] and ctx.opponent_bench():
            await opponent_switches(ctx)
    return effect


def _cure_all_and_heal(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        await ctx.cure_all_conditions(attacker)
        await ctx.heal(amount, attacker)
    return effect


def _flip_per_own_in_play(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        count = len(ctx.my_pokemon_in_play())
        results = await ctx.flip_coins(max(1, count),
                                       getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        await ctx.deal_damage(per * heads)
    return effect


def _flip_bonus_plain(m, ability):
    bonus = int(m.group(2))

    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        printed = getattr(ctx.ability, "damage", 0) or 0
        await ctx.deal_damage(printed + (bonus if results and results[0]
                                         else 0))
    return effect


def _bonus_per_evolved_from(m, ability):
    per = int(m.group(1))
    wanted = normalize(m.group(2))

    def count(ctx) -> int:
        total = 0
        for pokemon in ctx.my_pokemon_in_play():
            previous = pokemon.get_attribute(AttrID.EVOLVES_FROM)
            names = [previous] if isinstance(previous, str) else \
                list(previous or [])
            if any(normalize(str(name)) == wanted for name in names):
                total += 1
        return total
    return damage_per(count, per)


def _discard_hand_gate(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        hand = list(ctx.hand())
        if len(hand) < count:
            return
        picks = await ctx.choose_cards(hand, count, prompt=(
            f"Discard {count} cards"))
        if len(picks) < count:
            return
        await ctx.discard_cards(list(picks))
        await ctx.deal_damage()
    return effect


def _mill_self_then_heal(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(1, ctx.player_id)
        if top:
            await ctx.discard_cards(top)
        if ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
    return effect


def _condition_and_defender_no_retreat(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        await ctx.apply_special_condition(defender, condition)
        ctx.add_passive_through_opponents_turn(
            defender, no_retreat_passive(lambda p, c: p is carrier_pokemon(c)))
    return effect


def _flip_opponent_discards_hand(m, ability):
    coins = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        if not (results and all(results)):
            return
        hand = list(ctx.hand(ctx.opponent_id))
        if hand:
            await ctx.discard_cards(hand)
    return effect


def _condition_then_switch_self(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
        if ctx.my_bench():
            await switch_self_attack()(ctx)
    return effect


def _two_conditions_then_heal_self(m, ability):
    first = CONDITIONS[m.group(1)]
    second = CONDITIONS[m.group(2)]
    amount = int(m.group(3))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, first)
            await ctx.apply_special_condition(defender, second)
        if ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
    return effect


def _flip_heal_self_per_heads(m, ability):
    coins = _count(m.group(1))
    amount = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        if heads and ctx.attacker is not None:
            await ctx.heal(amount * heads, ctx.attacker)
    return effect


def _flip_look_discard_hand(m, ability):
    amount = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        cards = list(ctx.hand(ctx.opponent_id))
        if not (results and results[0]) or not cards:
            return
        await ctx.reveal_cards(cards, to_player=ctx.player_id)
        picks = await ctx.choose_cards(cards, amount, prompt=(
            "Choose cards to discard"))
        if picks:
            await ctx.discard_cards(list(picks))
    return effect


def _counters_per_hand_card(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        counters = per * len(ctx.hand())
        if defender is not None and counters and \
                not ctx.effects_blocked(defender):
            await ctx.deal_damage(counters * 10, target=defender,
                                  as_counters=True)
    return effect


def _flip_all_heads_heal_all(m, ability):
    coins = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        if not (results and all(results)):
            return
        candidates = ctx.my_pokemon_in_play()
        if not candidates:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal")
        if target is not None:
            await ctx.heal(9990, target)
    return effect


def _bonus_if_typed_energy_in_play(m, ability):
    needed = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value
    bonus = int(m.group(3))

    def cond(ctx) -> bool:
        total = sum(1 for pokemon in (ctx.my_pokemon_in_play()
                                      + ctx.opponent_pokemon_in_play())
                    for energy in ctx.attached_energies(pokemon)
                    if energy_provides_type(energy, type_value))
        return total >= needed
    return bonus_if(cond, bonus)


def _less_per_defender_energy(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        defender = ctx.defender
        count = len(ctx.attached_energies(defender)) if defender else 0
        printed = getattr(ctx.ability, "damage", 0) or 0
        await ctx.deal_damage(max(0, printed - per * count))
    return effect


def _counters_chosen_opponents(m, ability):
    counters = int(m.group(1))
    targets = _count(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                      if not ctx.effects_blocked(pokemon)]
        if not candidates:
            return
        picks = candidates if len(candidates) <= targets else \
            await ctx.choose_cards(candidates, targets,
                                   prompt=f"Choose {targets} Pokémon")
        for target in picks:
            await ctx.deal_damage(counters * 10, target=target,
                                  as_counters=True)
    return effect


def _heal_benched_typed(m, ability):
    amount = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_bench():
            if type_value in (pokemon.get_attribute(AttrID.POKEMON_TYPES)
                              or []):
                await ctx.heal(amount, pokemon)
    return effect


def _self_asleep_draw(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker,
                                              SpecialConditions.ASLEEP)
        await ctx.draw_cards(count)
    return effect


def _discard_self_energy_then_condition(m, ability):
    count = _count(m.group(1))
    condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        energies = ctx.attached_energies(attacker)
        if energies:
            await ctx.discard_cards(energies[:min(len(energies), count)])
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _counters_on_defender_active(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.deal_damage(counters * 10, target=defender,
                                  as_counters=True)
    return effect


def _bonus_if_defender_no_retreat(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        defender = ctx.defender
        if defender is None:
            return False
        cost = defender.get_attribute(AttrID.RETREAT_COST, 0)
        return not isinstance(cost, (int, float)) or cost == 0
    return bonus_if(cond, bonus)


def _bench_basics_from_discard(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.discard_pile() if _is_pokemon_card(card)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, limit, minimum=0, prompt=(
            f"Choose up to {limit} Pokémon to Bench"))
        for card in picks:
            await ctx.bench_pokemon(card)
    return effect


def _counters_chosen_bench(m, ability):
    counters = int(m.group(1))
    targets = _count(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = [pokemon for pokemon in ctx.opponent_bench()
                      if not ctx.effects_blocked(pokemon)]
        if not candidates:
            return
        picks = candidates if len(candidates) <= targets else \
            await ctx.choose_cards(candidates, targets,
                                   prompt=f"Choose {targets} Pokémon")
        for target in picks:
            await ctx.deal_damage(counters * 10, target=target,
                                  as_counters=True)
    return effect


def _counters_until_hp_b58(m, ability):
    target_hp = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        counters = (defender.get_attribute(AttrID.HP, 0) - target_hp) // 10
        if counters > 0:
            await ctx.deal_damage(counters * 10, target=defender,
                                  as_counters=True)
    return effect


def _discard_all_energy_heal_bench(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        energies = ctx.attached_energies(attacker)
        if energies:
            await ctx.discard_cards(list(energies))
        candidates = ctx.my_bench()
        if not candidates:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Pokémon to heal")
        if target is not None:
            await ctx.heal(amount, target)
    return effect


def _flip_defender_cannot_retreat(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        defender = ctx.defender
        if results and results[0] and defender is not None:
            ctx.add_passive_through_opponents_turn(
                defender, no_retreat_passive(
                    lambda p, c: p is carrier_pokemon(c)))
    return effect


def _per_energy_all_pokemon(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return sum(len(ctx.attached_energies(pokemon))
                   for pokemon in (ctx.my_pokemon_in_play()
                                   + ctx.opponent_pokemon_in_play()))
    return damage_per(count, per)


def _discard_three_typed(m, ability):
    types = [TYPE_WORDS[m.group(index)].value for index in (1, 2, 3)]

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        for type_value in types:
            energies = [energy for energy in ctx.attached_energies(attacker)
                        if energy_provides_type(energy, type_value)]
            if energies:
                await ctx.discard_cards(energies[:1])
    return effect


def _reveal_item_to_bottom(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        cards = list(ctx.hand(ctx.opponent_id))
        if not cards:
            return
        await ctx.reveal_cards(cards)
        items = [card for card in cards if is_tool_card(card)]
        for card in items:
            await ctx.put_on_bottom_of_deck(card)
    return effect


def _shuffle_discard_types_back(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile()
                if _is_pokemon_card(card) or is_basic_energy_card(card)]
        if not pile:
            return
        picks = await ctx.choose_cards(pile, limit, minimum=0, prompt=(
            f"Choose up to {limit} cards to shuffle into your deck"))
        if picks:
            await ctx.shuffle_into_deck(list(picks), ctx.player_id)
    return effect


def _per_bench_max_hp(m, ability):
    per = int(m.group(1))
    threshold = int(m.group(2))

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.my_bench()
                   if ctx.max_hp(pokemon) == threshold)
    return damage_per(count, per)


def _t59_gust_then_condition(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        from ptcgo.game.card_effects.support_common import opponent_switches
        await opponent_switches(ctx)
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _t59_retreat_tax_defender(m, ability):
    from ptcgo.game.card_effects.passives_common import (
        OpponentRetreatTaxPassive)
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None:
            ctx.add_passive_through_opponents_turn(
                defender, OpponentRetreatTaxPassive(amount=amount,
                                                    active_only=True))
    return effect


def _t59_choose_condition(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        await _choose_condition(ctx, [SpecialConditions.BURNED,
                                      SpecialConditions.POISONED])
    return effect


def _t59_distribute_counters(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [pokemon for pokemon in (ctx.my_pokemon_in_play()
                                        + ctx.opponent_pokemon_in_play())
                if not ctx.effects_blocked(pokemon)]
        for _ in range(counters):
            if not pool:
                return
            picks = await ctx.choose_cards(pool, 1, prompt=(
                "Choose a Pokémon for a damage counter"))
            if not picks:
                return
            await ctx.deal_damage(10, target=picks[0], as_counters=True)
    return effect


def _t59_counters_on_own_bench(m, ability):
    counters = int(m.group(1))
    targets = _count(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = ctx.my_bench()
        if not pool:
            return
        picks = pool if len(pool) <= targets else await ctx.choose_cards(
            pool, targets, prompt="Choose Benched Pokémon")
        for pokemon in picks:
            await ctx.deal_damage(counters * 10, target=pokemon,
                                  as_counters=True)
    return effect


def _t59_draw_per_basic_opponent(m, ability):

    async def effect(ctx):
        await ctx.deal_damage()
        count = sum(1 for pokemon in ctx.opponent_pokemon_in_play()
                    if _stage_of(pokemon) == 0)
        if count:
            await ctx.draw_cards(count)
    return effect


def _t59_minus_per_defender_energy(m, ability):
    less = int(m.group(1))

    async def effect(ctx):
        defender = ctx.defender
        count = len(ctx.attached_energies(defender)) if defender else 0
        printed = getattr(ctx.ability, "damage", 0) or 0
        await ctx.deal_damage(max(0, printed - less * count))
    return effect


def _t59_discard_cards_heal(m, ability):
    discard = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        hand = list(ctx.hand())
        if len(hand) < discard:
            return
        picks = await ctx.choose_cards(hand, discard, prompt=(
            f"Discard {discard} cards"))
        if len(picks) < discard:
            return
        await ctx.discard_cards(list(picks))
        candidates = [pokemon for pokemon in ctx.my_pokemon_in_play()
                      if ctx.max_hp(pokemon) > pokemon.get_attribute(AttrID.HP, 0)]
        if candidates:
            await ctx.heal(10 * discard, candidates[0])
    return effect


def _t59_minus_per_hand(m, ability):
    less = int(m.group(1))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        await ctx.deal_damage(max(0, printed - less * len(ctx.hand())))
    return effect


def _t59_search_typed_basic_bench(m, ability):
    limit = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        from ptcgo.game.session.effects import is_basic_pokemon

        await ctx.deal_damage()
        picks = await ctx.search_deck(
            lambda card: _is_pokemon_card(card)
            and type_value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])
            and is_basic_pokemon(card, ctx.board),
            count=limit, minimum=0, prompt="Choose Basic Pokémon")
        for card in picks:
            await ctx.bench_pokemon(card)
        await ctx.shuffle_deck()
    return effect


def _t59_attach_typed_from_discard(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_pokemon_in_play()
        if not pile or not candidates:
            return
        picks = await ctx.choose_cards(pile, 1, prompt="Choose an Energy card")
        chosen = []
        for card in picks:
            target = candidates[0] if len(candidates) == 1 else \
                await ctx.choose_pokemon(candidates,
                                         "Choose a Pokémon for the Energy")
            if target is not None:
                chosen.append((card, target))
        for card, target in chosen:
            await ctx.attach_energy(card, target)
    return effect


def _t59_bonus_if_damaged_self(m, ability):
    threshold, bonus = int(m.group(1)), int(m.group(3))

    def cond(ctx) -> bool:
        attacker = ctx.attacker
        if attacker is None:
            return False
        counters = (ctx.max_hp(attacker)
                    - attacker.get_attribute(AttrID.HP, 0)) // 10
        return counters >= threshold
    return bonus_if(cond, bonus)


def _t59_typed_energy_from_discard_self(m, ability):
    limit = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        if attacker is None or not pile:
            return
        picks = await ctx.choose_cards(pile, limit, minimum=0, prompt=(
            f"Choose up to {limit} Energy cards"))
        for card in picks:
            await ctx.attach_energy(card, attacker)
    return effect


def _t59_bonus_defender_stage_plain(m, ability):
    stage = int(m.group(1))
    bonus = int(m.group(3))

    def cond(ctx) -> bool:
        defender = ctx.defender
        return defender is not None and _stage_of(defender) == stage
    return bonus_if(cond, bonus)


def _t59_flip_bonus_comma(m, ability):
    bonus = int(m.group(2))

    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        printed = getattr(ctx.ability, "damage", 0) or 0
        await ctx.deal_damage(printed + (bonus if results and results[0] else 0))
    return effect


def _t59_pre_switch_opponent(m, ability):
    from ptcgo.game.card_effects.support_common import opponent_switches

    async def effect(ctx):
        if await ctx.ask_yes_no(prompt="Switch the opponent's Active Pokémon?"):
            await opponent_switches(ctx)
        await ctx.deal_damage()
    return effect


def _t59_gate_stadium_present(m, ability):
    from ptcgo.game.card_effects.attacks_common import stadium_in_play_cond

    async def effect(ctx):
        if not stadium_in_play_cond(ctx):
            return
        await ctx.deal_damage()
    return effect


def _t59_flip_attach_discard_energy(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        attacker = ctx.attacker
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)]
        if not (results and results[0]) or attacker is None or not pile:
            return
        picks = await ctx.choose_cards(pile, 1, prompt="Choose an Energy card")
        for card in picks:
            await ctx.attach_energy(card, attacker)
    return effect


def _t59_draw_named_in_play(m, ability):
    wanted = normalize(m.group(1))
    instead = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        names = [normalize(getattr(pokemon, "display_name", "") or "")
                 for pokemon in ctx.my_pokemon_in_play()]
        await ctx.draw_cards(instead if wanted in names else 1)
    return effect


def _t59_discard_two_typed_plain(m, ability):
    first = TYPE_WORDS[m.group(1)].value
    second = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        for type_value in (first, second):
            energies = [energy for energy in ctx.attached_energies(attacker)
                        if energy_provides_type(energy, type_value)]
            if energies:
                await ctx.discard_cards(energies[:1])
    return effect


def _t59_gate_cant_discard(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        attacker = ctx.attacker
        if attacker is None:
            return
        energies = [energy for energy in ctx.attached_energies(attacker)
                    if is_basic_energy_card(energy)]
        if len(energies) < count:
            return
        await ctx.discard_cards(energies[:count])
        await ctx.deal_damage()
    return effect


def _t59_pre_heal_defender(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        defender = ctx.defender
        if defender is not None:
            await ctx.heal(amount, defender)
        await ctx.deal_damage()
    return effect


def _t59_evolved_this_turn_heal_all(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is not None:
            await ctx.heal(9990, attacker)
    return effect


def _t59_evolved_this_turn_condition(m, ability):
    condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _t59_evolved_this_turn_base_swap(m, ability):
    changed, base = int(m.group(2)), int(m.group(3))

    async def effect(ctx):
        await ctx.deal_damage(changed if base else None)
    return effect


def _t59_heal_self_amount(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
    return effect


def _t59_recover_supporter(m, ability):
    def predicate(card) -> bool:
        return _trainer_kind(card) is TrainerType.SUPPORTER
    return recover_from_discard(predicate=predicate, count=1, minimum=0)


def _t59_mill_attach_typed(m, ability):
    count = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        top = ctx.deck_top(count, ctx.player_id)
        if not top or attacker is None:
            return
        for card in list(top):
            if is_energy_card(card) and energy_provides_type(card, type_value):
                await ctx.attach_energy(card, attacker)
            else:
                await ctx.discard_cards([card])
    return effect


def _t59_bench_basic_each_side(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        for player_id in (ctx.player_id, ctx.opponent_id):
            pile = [card for card in ctx.discard_pile(player_id)
                    if _is_pokemon_card(card)]
            if pile and (player_id == ctx.player_id):
                picks = await ctx.choose_cards(pile, 1, minimum=0, prompt=(
                    "Choose a Basic Pokémon to Bench"))
                for card in picks:
                    await ctx.bench_pokemon(card)
    return effect


def _t59_bonus_lost_zone_typed(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    bonus = int(m.group(2))

    def cond(ctx) -> bool:
        return any(is_energy_card(card)
                   and energy_provides_type(card, type_value)
                   for card in ctx.lost_zone(ctx.player_id))
    return bonus_if(cond, bonus)


def _t59_gate_no_stadium(m, ability):
    async def effect(ctx):
        if ctx.stadium_in_play() is not None:
            return
        await ctx.deal_damage()
    return effect


def _t59_switch_then_confuse(m, ability):
    from ptcgo.game.card_effects.support_common import opponent_switches

    async def effect(ctx):
        await ctx.deal_damage()
        await opponent_switches(ctx)
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender,
                                              SpecialConditions.CONFUSED)
    return effect


def _t59_move_bench_energy_self(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        pool = []
        for pokemon in ctx.my_bench():
            pool.extend(ctx.attached_energies(pokemon))
        if not pool:
            return
        picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt=(
            "Choose Energy to move"))
        for card in picks:
            await ctx.attach_energy(card, attacker)
    return effect


def _t59_discard_opponent_tools(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        tools = [card for pokemon in ctx.opponent_pokemon_in_play()
                 for card in ctx.attached_energies(pokemon)
                 if not is_energy_card(card)]
        if not tools:
            return
        picks = tools if len(tools) <= limit else await ctx.choose_cards(
            tools, limit, prompt=f"Choose up to {limit} Pokémon Tools")
        if picks:
            await ctx.discard_cards(list(picks))
    return effect


def _t59_flip_recoil(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0] and ctx.attacker is not None:
            await ctx.deal_damage(amount, target=ctx.attacker,
                                  ignore_weakness=True)
    return effect


def _t59_heal_bench_then_discard(m, ability):
    amount = int(m.group(1))
    discard = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_bench():
            await ctx.heal(amount, pokemon)
        attacker = ctx.attacker
        if attacker is None:
            return
        energies = ctx.attached_energies(attacker)
        if energies:
            await ctx.discard_cards(energies[:min(discard, len(energies))])
    return effect


def _t59_per_opponent_in_play(m, ability):
    per = int(m.group(1))
    return damage_per(lambda ctx: len(ctx.opponent_pokemon_in_play()), per)


def _t59_bonus_defender_no_energy(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        defender = ctx.defender
        return defender is not None and not ctx.attached_energies(defender)
    return bonus_if(cond, bonus)


def _t59_search_items(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(is_tool_card, count=limit, minimum=0,
                                      prompt="Choose Item cards")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=True)
        await ctx.shuffle_deck()
    return effect


def _t59_draw_bench_named_more(m, ability):
    wanted = normalize(m.group(1))
    extra = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        names = [normalize(getattr(pokemon, "display_name", "") or "")
                 for pokemon in ctx.my_bench()]
        await ctx.draw_cards(1 + extra if wanted in names else 1)
    return effect


def _t59_mill_opponent_bonus_if_trainer(m, ability):
    bonus = int(m.group(1))

    async def effect(ctx):
        top = ctx.deck_top(1, ctx.opponent_id)
        if not top:
            return
        is_trainer = _trainer_kind(top[0]) in (
            TrainerType.TRAINER, TrainerType.SUPPORTER, TrainerType.ITEM,
            TrainerType.STADIUM)
        await ctx.discard_cards(list(top))
        printed = getattr(ctx.ability, "damage", 0) or 0
        await ctx.deal_damage(printed + (bonus if is_trainer else 0))
    return effect


def _t59_optional_bonus_mill_both(m, ability):
    bonus = int(m.group(1))
    mill = int(m.group(2))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if await ctx.ask_yes_no(prompt=f"Do {bonus} more damage and mill?"):
            await ctx.deal_damage(printed + bonus)
            for player_id in (ctx.player_id, ctx.opponent_id):
                top = ctx.deck_top(mill, player_id)
                if top:
                    await ctx.discard_cards(top)
        else:
            await ctx.deal_damage()
    return effect


def _t59_heal_both_active(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in (ctx.my_active(), ctx.opponent_active()):
            if pokemon is not None:
                await ctx.heal(amount, pokemon)
    return effect


def _t59_recover_stadiums(m, ability):
    count = _count(m.group(1))

    def predicate(card) -> bool:
        return (card.get_attribute(AttrID.CARD_TYPE) or "") == "Stadium"
    return recover_from_discard(predicate=predicate, count=count, minimum=0)


def _t59_bonus_per_opponent_ex(m, ability):
    from ptcgo.game.card_effects.trainers import is_pokemon_ex
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        return any(is_pokemon_ex(pokemon)
                   for pokemon in ctx.opponent_pokemon_in_play())
    return bonus_if(cond, bonus)


def _t59_bonus_per_defender_typed_energy(m, ability):
    per = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    def count(ctx) -> int:
        defender = ctx.defender
        if defender is None:
            return 0
        return sum(1 for energy in ctx.attached_energies(defender)
                   if energy_provides_type(energy, type_value))
    return damage_per(count, per)


def _t59_attach_typed_bench_chosen(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_bench()
        if not pile or not candidates:
            return
        for pokemon in candidates:
            if not pile:
                return
            await ctx.attach_energy(pile.pop(0), pokemon)
    return effect


def _t59_attach_hand_basic_self(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        pool = [card for card in ctx.hand() if is_basic_energy_card(card)]
        if attacker is None or not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt=(
            "Choose an Energy card"))
        if picks:
            await ctx.attach_energy(picks[0], attacker)
    return effect


def _t59_bonus_defender_type_plus(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    bonus = int(m.group(3))

    def cond(ctx) -> bool:
        defender = ctx.defender
        return defender is not None and type_value in (
            defender.get_attribute(AttrID.POKEMON_TYPES) or [])
    return bonus_if(cond, bonus)


def _t59_recover_typed_pokemon(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    def predicate(card) -> bool:
        return _is_pokemon_card(card) and type_value in (
            card.get_attribute(AttrID.POKEMON_TYPES) or [])
    return recover_from_discard(predicate=predicate, count=1, minimum=0)


def _t59_strip_defender_tools(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        tools = [card for card in ctx.attached_energies(defender)
                 if not is_energy_card(card)]
        if tools:
            await ctx.discard_cards(tools)
    return effect


def _t59_move_defender_energy_to_bench(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        energies = ctx.attached_energies(defender)
        candidates = [pokemon for pokemon in ctx.opponent_bench()
                      if not ctx.effects_blocked(pokemon)]
        if not energies or not candidates:
            return
        picks = await ctx.choose_cards(energies, 1, prompt=(
            "Choose an Energy to move"))
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Benched Pokémon")
        if picks and target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _t59_return_bench_to_hand(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        bench = ctx.my_bench()
        if not bench:
            return
        picks = bench if len(bench) <= count else await ctx.choose_cards(
            bench, count, prompt=f"Choose up to {count} Pokémon")
        for pokemon in picks:
            cards = [pokemon] + list(ctx.attached_energies(pokemon))
            await ctx.put_in_hand(cards, reveal=False)
    return effect


def _t59_heal_self_no_retreat_simple(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        await ctx.heal(amount, attacker)
        ctx.add_passive_through_opponents_turn(
            attacker, no_retreat_passive(lambda p, c: p is carrier_pokemon(c)))
    return effect


def _t59_attach_typed_discard_bench(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_bench()
        if not pile or not candidates:
            return
        picks = await ctx.choose_cards(pile, count, minimum=0, prompt=(
            f"Choose up to {count} Energy cards"))
        chosen = []
        for card in picks:
            target = candidates[0] if len(candidates) == 1 else \
                await ctx.choose_pokemon(candidates, "Choose a Benched Pokémon")
            if target is not None:
                chosen.append((card, target))
        for card, target in chosen:
            await ctx.attach_energy(card, target)
    return effect


def _t59_bonus_per_own_typed_energy(m, ability):
    per = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.my_pokemon_in_play()
                   if any(energy_provides_type(energy, type_value)
                          for energy in ctx.attached_energies(pokemon)))
    return damage_per(count, per)


def _t59_attach_hand_energy_bench(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_energy_card(card)]
        candidates = ctx.my_bench()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt=(
            "Choose an Energy card"))
        if not picks:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Benched Pokémon")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _t59_recover_energy_cards(m, ability):
    count = _count(m.group(1))
    return recover_from_discard(predicate=is_energy_card, count=count,
                                minimum=0)


def _t59_condition_if_defender_typed_energy(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        if any(energy_provides_type(energy, type_value)
               for energy in ctx.attached_energies(defender)):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _t59_discard_hand(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        hand = list(ctx.hand())
        if hand:
            await ctx.discard_cards(hand)
    return effect


def _t59_optional_energy_bonus(m, ability):
    bonus = int(m.group(1))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        attacker = ctx.attacker
        if attacker is not None and ctx.attached_energies(attacker) and \
                await ctx.ask_yes_no(prompt="Discard an Energy for more damage?"):
            if await ctx.discard_energy_from(attacker, 1):
                await ctx.deal_damage(printed + bonus)
                return
        await ctx.deal_damage()
    return effect


def _t59_bonus_per_basic_energy_self(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        attacker = ctx.attacker
        if attacker is None:
            return 0
        return sum(1 for energy in ctx.attached_energies(attacker)
                   if is_basic_energy_card(energy))
    return damage_per(count, per)


def _t59_bonus_per_opponent_ability(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.opponent_pokemon_in_play()
                   if pokemon.get_attribute(AttrID.PIE_ABILITIES))
    return damage_per(count, per)


def _t59_draw_per_retreat_cost(m, ability):
    cost = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        count = sum(1 for pokemon in ctx.my_pokemon_in_play()
                    if pokemon.get_attribute(AttrID.RETREAT_COST) == cost)
        if count:
            await ctx.draw_cards(count)
    return effect


def _t59_search_trainer(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(
            lambda card: _trainer_kind(card) in (
                TrainerType.TRAINER, TrainerType.SUPPORTER, TrainerType.ITEM), count=1, minimum=0,
            prompt="Choose a Trainer card")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=True)
        await ctx.shuffle_deck()
    return effect


def _t59_switch_if_evolved(m, ability):

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is not None and _stage_of(defender) >= 1 and \
                ctx.my_bench():
            await switch_self_attack()(ctx)
    return effect


def _t59_bonus_if_prizes_equal(m, ability):
    count, bonus = int(m.group(1)), int(m.group(2))

    def cond(ctx) -> bool:
        mine = 6 - ctx.prizes_taken(ctx.player_id)
        theirs = 6 - ctx.prizes_taken(ctx.opponent_id)
        return mine == count and theirs == count
    return bonus_if(cond, bonus)


def _t59_discard_tool_chosen(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pool = []
        for pokemon in ctx.opponent_pokemon_in_play():
            pool.extend(card for card in ctx.attached_energies(pokemon)
                        if not is_energy_card(card))
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, prompt=(
            "Choose a Pokémon Tool card"))
        if picks:
            await ctx.discard_cards(list(picks))
    return effect

def _trainer_kind(card):
    value = card.get_attribute(AttrID.TRAINER_TYPE)
    for kind in TrainerType:
        if kind.value == value:
            return kind
    return None


def _stage_of(pokemon) -> int:
    stage = pokemon.get_attribute(AttrID.STAGE)
    return int(stage) if isinstance(stage, (int, float)) else 0



def _t60_bonus_named_stadium(m, ability):
    wanted = normalize(m.group(1))
    bonus = int(m.group(2))

    def cond(ctx) -> bool:
        stadium = ctx.stadium_in_play()
        if stadium is None:
            return False
        name = normalize(getattr(stadium, "display_name", "")
                         or getattr(stadium, "name", "") or "")
        return wanted in name
    return bonus_if(cond, bonus)


def _t60_asleep_then_delayed_ko(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker,
                                              SpecialConditions.ASLEEP)
        _schedule_knock_out_defender(m, ability)
        await _schedule_knock_out_defender(m, ability)(ctx)
    return effect


def _t60_attach_basic_each_typed_bench(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if is_basic_energy_card(card)
                and energy_provides_type(card, type_value)]
        for pokemon in ctx.my_bench():
            if type_value not in (pokemon.get_attribute(AttrID.POKEMON_TYPES)
                                  or []):
                continue
            if not pile:
                return
            await ctx.attach_energy(pile.pop(0), pokemon)
    return effect


def _t60_bonus_per_other_in_play(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return max(0, len(ctx.my_pokemon_in_play())
                   + len(ctx.opponent_pokemon_in_play()) - 1)
    return damage_per(count, per)


def _t60_bonus_low_hp(m, ability):
    threshold, bonus = int(m.group(1)), int(m.group(2))

    def cond(ctx) -> bool:
        attacker = ctx.attacker
        return attacker is not None and \
            attacker.get_attribute(AttrID.HP, 0) <= threshold
    return bonus_if(cond, bonus)


def _t60_discard_energy_then_lock(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        if ctx.attached_energies(attacker):
            await ctx.discard_energy_from(attacker, 1)
        from ptcgo.game.card_effects.attacks_common import lock_all_attacks
        lock_all_attacks(ctx, attacker)
    return effect


def _t60_heal_all_then_lock_plain(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        await ctx.heal(9990, attacker)
        from ptcgo.game.card_effects.attacks_common import lock_all_attacks
        lock_all_attacks(ctx, attacker)
    return effect


def _t60_flip_per_own_in_play_any(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        count = max(1, len(ctx.my_pokemon_in_play()))
        results = await ctx.flip_coins(count, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        await ctx.deal_damage(per * heads)
    return effect


def _t60_flip_until_heal_self(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_until_tails(getattr(ability, "title", ""))
        if heads and ctx.attacker is not None:
            await ctx.heal(amount * heads, ctx.attacker)
    return effect


def _t60_move_typed_self_to_bench(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        pool = [energy for energy in ctx.attached_energies(attacker)
                if energy_provides_type(energy, type_value)]
        candidates = ctx.my_bench()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, count, minimum=0, prompt=(
            f"Choose up to {count} Energy cards"))
        chosen = []
        for card in picks:
            target = candidates[0] if len(candidates) == 1 else \
                await ctx.choose_pokemon(candidates, "Choose a Benched Pokémon")
            if target is not None:
                chosen.append((card, target))
        for card, target in chosen:
            await ctx.attach_energy(card, target)
    return effect


def _t60_scale_per_tools_all(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return sum(1 for pokemon in (ctx.my_pokemon_in_play()
                                     + ctx.opponent_pokemon_in_play())
                   for card in ctx.attached_energies(pokemon)
                   if not is_energy_card(card))
    return damage_per(count, per)


def _t60_shuffle_typed_pokemon_back(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if _is_pokemon_card(card)
                and type_value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])]
        if not pile:
            return
        picks = await ctx.choose_cards(pile, count, minimum=0, prompt=(
            f"Choose up to {count} Pokémon"))
        if picks:
            await ctx.shuffle_into_deck(list(picks), ctx.player_id)
    return effect


def _t60_opponent_bounce_active(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        active = ctx.opponent_active()
        if active is None:
            return
        cards = [active] + list(ctx.attached_energies(active))
        await ctx.put_in_hand(cards, reveal=False)
    return effect


def _t60_flip_trainer_lock_their(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            await _lock_all_trainers(m, ability)(ctx)
    return effect


def _t60_per_basic_energy_all_own(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.my_pokemon_in_play()
                   for energy in ctx.attached_energies(pokemon)
                   if is_basic_energy_card(energy))
    return damage_per(count, per)


def _t60_search_and_discard(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(None, count=count, minimum=0,
                                      prompt=f"Choose up to {count} cards")
        if picks:
            await ctx.discard_cards(list(picks))
        await ctx.shuffle_deck()
    return effect


def _t60_bonus_evolved_this_turn(m, ability):
    bonus = int(m.group(2))

    def cond(ctx) -> bool:
        attacker = ctx.attacker
        return attacker is not None and _stage_of(attacker) >= 1
    return bonus_if(cond, bonus)


def _t60_capped_per_pokemon_in_discard(m, ability):
    per, cap = int(m.group(1)), int(m.group(2))

    def count(ctx) -> int:
        pokemon = sum(1 for card in ctx.discard_pile() if _is_pokemon_card(card))
        return min(cap // per if per else 0, pokemon)
    return damage_per(count, per)


def _t60_reveal_supporter_to_bottom(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        cards = list(ctx.hand(ctx.opponent_id))
        if not cards:
            return
        await ctx.reveal_cards(cards)
        supporters = [card for card in cards
                      if _trainer_kind(card) is TrainerType.SUPPORTER]
        for card in supporters[:1]:
            await ctx.put_on_bottom_of_deck(card)
    return effect


def _t60_flip_lock_items(m, ability):
    from ptcgo.game.attributes import TrainerType

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if not (results and results[0]):
            return
        ctx.lock_plays(
            ctx.opponent_id,
            lambda card: _trainer_kind(card) is TrainerType.ITEM)
    return effect


def _t60_flip_per_typed_energy_self(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    per = int(m.group(2))

    async def effect(ctx):
        attacker = ctx.attacker
        count = 0
        if attacker is not None:
            count = sum(1 for energy in ctx.attached_energies(attacker)
                        if energy_provides_type(energy, type_value))
        results = await ctx.flip_coins(max(1, count),
                                       getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        await ctx.deal_damage(per * heads)
    return effect


def _t60_flip_mill_opponent_card(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0]:
            top = ctx.deck_top(1, ctx.opponent_id)
            if top:
                await ctx.discard_cards(top)
    return effect


def _t60_bonus_typed_energy_threshold(m, ability):
    needed = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value
    bonus = int(m.group(3))

    def cond(ctx) -> bool:
        attacker = ctx.attacker
        if attacker is None:
            return False
        count = sum(1 for energy in ctx.attached_energies(attacker)
                    if energy_provides_type(energy, type_value))
        return count >= needed
    return bonus_if(cond, bonus)


def _t60_search_basic_energy_attach_typed(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(
            lambda card: is_basic_energy_card(card)
            and energy_provides_type(card, type_value),
            count=1, minimum=0, prompt="Choose an Energy card")
        candidates = ctx.my_pokemon_in_play()
        if picks and candidates:
            target = candidates[0] if len(candidates) == 1 else \
                await ctx.choose_pokemon(candidates, "Choose a Pokémon")
            if target is not None:
                await ctx.attach_energy(picks[0], target)
        await ctx.shuffle_deck()
    return effect


def _t60_move_typed_energy_any(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [energy for pokemon in ctx.my_pokemon_in_play()
                for energy in ctx.attached_energies(pokemon)
                if energy_provides_type(energy, type_value)]
        candidates = ctx.my_pokemon_in_play()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt=(
            "Choose Energy to move"))
        if picks:
            await distribute_energy(ctx, list(picks), candidates)
    return effect


def _t60_discard_hand_opponent_discards(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        hand = list(ctx.hand())
        if not hand:
            return
        picks = await ctx.choose_cards(hand, 1, prompt="Choose a card to discard")
        if not picks:
            return
        await ctx.discard_cards(list(picks))
        theirs = list(ctx.hand(ctx.opponent_id))
        if theirs:
            await ctx.discard_cards([random.choice(theirs)])
    return effect


def _t60_gate_discard_hand(m, ability):
    async def effect(ctx):
        hand = list(ctx.hand())
        if not hand:
            return
        picks = await ctx.choose_cards(hand, 1, prompt="Choose a card to discard")
        if not picks:
            return
        await ctx.discard_cards(list(picks))
        await ctx.deal_damage()
    return effect


def _t60_search_supporters(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(
            lambda card: _trainer_kind(card) is TrainerType.SUPPORTER,
            count=limit, minimum=0, prompt="Choose Supporter cards")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=True)
        await ctx.shuffle_deck()
    return effect


def _t60_attach_typed_bench_up_to(m, ability):
    limit = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if is_basic_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_bench()
        if not pile or not candidates:
            return
        picks = await ctx.choose_cards(pile, limit, minimum=0, prompt=(
            f"Choose up to {limit} Energy cards"))
        chosen = []
        for card in picks:
            target = candidates[0] if len(candidates) == 1 else \
                await ctx.choose_pokemon(candidates, "Choose a Benched Pokémon")
            if target is not None:
                chosen.append((card, target))
        for card, target in chosen:
            await ctx.attach_energy(card, target)
    return effect


def _t60_bonus_prize_count(m, ability):
    first, second, bonus = int(m.group(1)), int(m.group(2)), int(m.group(3))

    def cond(ctx) -> bool:
        return (6 - ctx.prizes_taken(ctx.opponent_id)) in (first, second)
    return bonus_if(cond, bonus)


def _t60_flip_until_random_discard(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        heads = await ctx.flip_until_tails(getattr(ability, "title", ""))
        for _ in range(heads):
            hand = ctx.hand(ctx.opponent_id)
            if not hand:
                return
            await ctx.discard_cards([random.choice(list(hand))])
    return effect


def _t60_flip_tails_recoil_plain(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and not results[0] and ctx.attacker is not None:
            await ctx.deal_damage(amount, target=ctx.attacker,
                                  ignore_weakness=True)
    return effect


def _t60_recover_items_and_tools(m, ability):
    limit = _count(m.group(1))

    def predicate(card) -> bool:
        return _trainer_kind(card) in (TrainerType.ITEM, TrainerType.TRAINER) or \
            is_tool_card(card)
    return recover_from_discard(predicate=predicate, count=limit, minimum=0)


def _t60_attach_typed_basic_self(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        pile = [card for card in ctx.discard_pile() if is_basic_energy_card(card)
                and energy_provides_type(card, type_value)]
        if attacker is None or not pile:
            return
        picks = await ctx.choose_cards(pile, 1, prompt="Choose an Energy card")
        if picks:
            await ctx.attach_energy(picks[0], attacker)
    return effect


def _t60_gate_condition_absent(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        attacker = ctx.attacker
        if attacker is None:
            return
        active = attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        if getattr(condition, "value", condition) in active:
            return
        await ctx.deal_damage()
    return effect


def _t60_gate_evolved_this_turn(m, ability):
    async def effect(ctx):
        attacker = ctx.attacker
        if attacker is not None and _stage_of(attacker) >= 1:
            return
        await ctx.deal_damage()
    return effect


def _t60_scale_per_energy_opponent_discard(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return sum(1 for card in ctx.discard_pile(ctx.opponent_id)
                   if is_energy_card(card))
    return damage_per(count, per)


def _t60_flip_move_defender_energy(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        defender = ctx.defender
        if not (results and results[0]) or defender is None or \
                ctx.effects_blocked(defender):
            return
        energies = ctx.attached_energies(defender)
        candidates = [pokemon for pokemon in ctx.opponent_bench()
                      if not ctx.effects_blocked(pokemon)]
        if not energies or not candidates:
            return
        picks = await ctx.choose_cards(energies, 1, prompt=(
            "Choose an Energy to move"))
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Benched Pokémon")
        if picks and target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _t60_gate_damaged_only(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        attacker = ctx.attacker
        if attacker is None:
            return
        counters = (ctx.max_hp(attacker)
                    - attacker.get_attribute(AttrID.HP, 0)) // 10
        if counters >= count:
            return
        await ctx.deal_damage()
    return effect


def _t60_attach_typed_hand_bench_many(m, ability):
    limit = _count(m.group(2))
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_basic_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_bench()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, limit, minimum=0, prompt=(
            f"Choose up to {limit} Energy cards"))
        chosen = []
        for card in picks:
            target = candidates[0] if len(candidates) == 1 else \
                await ctx.choose_pokemon(candidates, "Choose a Benched Pokémon")
            if target is not None:
                chosen.append((card, target))
        for card, target in chosen:
            await ctx.attach_energy(card, target)
    return effect


def _t60_switch_then_asleep(m, ability):
    from ptcgo.game.card_effects.support_common import opponent_switches

    async def effect(ctx):
        await ctx.deal_damage()
        await opponent_switches(ctx)
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender,
                                              SpecialConditions.ASLEEP)
    return effect


def _t60_optional_bottom_of_deck(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(1, ctx.player_id)
        if not top:
            return
        if await ctx.ask_yes_no(prompt="Put that card on the bottom?"):
            await ctx.put_on_bottom_of_deck(top[0])
    return effect


def _t60_attach_typed_hand_any_distributed(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_basic_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_pokemon_in_play()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt=(
            "Choose any number of Energy cards"))
        if picks:
            await distribute_energy(ctx, list(picks), candidates)
    return effect


def _t60_move_energy_any_own(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pool = [energy for pokemon in ctx.my_pokemon_in_play()
                for energy in ctx.attached_energies(pokemon)]
        candidates = ctx.my_pokemon_in_play()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt=(
            "Choose Energy to move"))
        if picks:
            await distribute_energy(ctx, list(picks), candidates)
    return effect


def _t60_bonus_opponent_typed(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    bonus = int(m.group(2))

    def cond(ctx) -> bool:
        return any(type_value in (pokemon.get_attribute(AttrID.POKEMON_TYPES)
                                  or [])
                   for pokemon in ctx.opponent_pokemon_in_play())
    return bonus_if(cond, bonus)


def _t60_flip_tails_discard_energy_self(m, ability):
    coins = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        tails = sum(1 for result in results or [] if not result)
        attacker = ctx.attacker
        if not tails or attacker is None:
            return
        for _ in range(tails):
            if not ctx.attached_energies(attacker):
                return
            await ctx.discard_energy_from(attacker, 1)
    return effect


def _t60_recoil_per_counter(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        counters = (ctx.max_hp(attacker)
                    - attacker.get_attribute(AttrID.HP, 0)) // 10
        if counters:
            await ctx.deal_damage(per * counters, target=attacker,
                                  ignore_weakness=True)
    return effect


def _t60_recover_basic_energy_one(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    def predicate(card) -> bool:
        return is_basic_energy_card(card) and \
            energy_provides_type(card, type_value)
    return recover_from_discard(predicate=predicate, count=1, minimum=0)


def _t60_attach_hand_energy_heal(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        pool = [card for card in ctx.hand() if is_energy_card(card)]
        if attacker is None or not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt=(
            "Choose an Energy card"))
        if picks:
            await ctx.attach_energy(picks[0], attacker)
            await ctx.heal(amount, attacker)
    return effect


def _t60_optional_bonus_self_lock(m, ability):
    bonus = int(m.group(1))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if await ctx.ask_yes_no(prompt=f"Do {bonus} more damage and skip next turn?"):
            await ctx.deal_damage(printed + bonus)
            if ctx.attacker is not None:
                from ptcgo.game.card_effects.attacks_common import lock_all_attacks
                lock_all_attacks(ctx, ctx.attacker)
        else:
            await ctx.deal_damage()
    return effect


def _t60_gate_typed_discard(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        pool = [card for card in ctx.hand() if is_basic_energy_card(card)
                and energy_provides_type(card, type_value)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, prompt="Choose an Energy card")
        if not picks:
            return
        await ctx.discard_cards(list(picks))
        await ctx.deal_damage()
    return effect


def _t60_ko_if_defender_special_energy(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        if any(is_special_energy(energy)
               for energy in ctx.attached_energies(defender)):
            await ctx.knock_out(defender)
    return effect


def _t60_peek_optional_shuffle(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(1, ctx.opponent_id)
        if top:
            await ctx.reveal_cards(list(top))
        if ctx.stadium_in_play() is None and await ctx.ask_yes_no(
                prompt="Have the opponent shuffle their deck?"):
            await ctx.shuffle_deck(ctx.opponent_id)
    return effect


def _t60_scale_per_ex_and_v(m, ability):
    from ptcgo.game.data_utils import is_pokemon_v
    from ptcgo.game.card_effects.trainers import is_pokemon_ex
    per = int(m.group(1))

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.opponent_pokemon_in_play()
                   if is_pokemon_ex(pokemon) or is_pokemon_v(pokemon))
    return damage_per(count, per)


def _t60_scale_per_special_energy_opponent(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.opponent_pokemon_in_play()
                   for energy in ctx.attached_energies(pokemon)
                   if is_special_energy(energy))
    return damage_per(count, per)


def _t60_bonus_more_energy_than_defender(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        attacker, defender = ctx.attacker, ctx.defender
        if attacker is None or defender is None:
            return False
        return len(ctx.attached_energies(attacker)) > \
            len(ctx.attached_energies(defender))
    return bonus_if(cond, bonus)


def _t60_prize_gate_condition(m, ability):
    count = int(m.group(1))
    condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        if (6 - ctx.prizes_taken(ctx.player_id)) != count:
            return
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _t60_ko_both_active(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in (ctx.opponent_active(), ctx.my_active()):
            if pokemon is not None and not ctx.effects_blocked(pokemon):
                await ctx.knock_out(pokemon)
    return effect


def _t60_counters_each_with_ability(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in (ctx.my_pokemon_in_play()
                        + ctx.opponent_pokemon_in_play()):
            if pokemon.get_attribute(AttrID.PIE_ABILITIES) and \
                    not ctx.effects_blocked(pokemon):
                await ctx.deal_damage(counters * 10, target=pokemon,
                                      as_counters=True)
    return effect


def _t60_strip_tools_and_special(m, ability):
    async def effect(ctx):
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            cards = [card for card in ctx.attached_energies(defender)
                     if not is_energy_card(card) or is_special_energy(card)]
            if cards:
                await ctx.discard_cards(cards)
        await ctx.deal_damage()
    return effect


def _t61_asleep_usable_bonus(m, ability):
    bonus = int(m.group(1))

    async def effect(ctx):
        attacker = ctx.attacker
        asleep = False
        if attacker is not None:
            active = attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            asleep = SpecialConditions.ASLEEP in active
        printed = getattr(ctx.ability, "damage", 0) or 0
        await ctx.deal_damage(printed + (bonus if asleep else 0))
    return effect


def _t61_flip_mill_per_heads(m, ability):
    coins = _count(m.group(1))
    per = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        if heads:
            top = ctx.deck_top(per * heads, ctx.opponent_id)
            if top:
                await ctx.discard_cards(top)
    return effect


def _t61_both_active_conditions(m, ability):
    first = CONDITIONS[m.group(1)]
    second = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in (ctx.my_active(), ctx.opponent_active()):
            if pokemon is None or ctx.effects_blocked(pokemon):
                continue
            await ctx.apply_special_condition(pokemon, first)
            await ctx.apply_special_condition(pokemon, second)
    return effect


def _t61_lock_defender_if_typed_pair(m, ability):
    from ptcgo.game.card_effects.attacks_common import lock_defender_attacks
    first = TYPE_WORDS[m.group(1)].value
    second = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None:
            return
        types = defender.get_attribute(AttrID.POKEMON_TYPES) or []
        if first in types or second in types:
            lock_defender_attacks(ctx)
    return effect


def _t61_heal_then_lock(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        await ctx.heal(amount, attacker)
        from ptcgo.game.card_effects.attacks_common import lock_all_attacks
        lock_all_attacks(ctx, attacker)
    return effect


def _t61_attach_all_basic_hand(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_basic_energy_card(card)]
        candidates = ctx.my_pokemon_in_play()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, len(pool), minimum=0, prompt=(
            "Choose any number of Energy cards"))
        if picks:
            await distribute_energy(ctx, list(picks), candidates)
    return effect


def _t61_gate_opponent_ex_present(m, ability):
    from ptcgo.game.card_effects.trainers import is_pokemon_ex

    async def effect(ctx):
        if not any(is_pokemon_ex(pokemon)
                   for pokemon in ctx.opponent_pokemon_in_play()):
            return
        await ctx.deal_damage()
    return effect


def _t61_optional_item_bonus(m, ability):
    bonus = int(m.group(1))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        pool = [card for card in ctx.hand()
                if _trainer_kind(card) in (TrainerType.ITEM, TrainerType.TRAINER)]
        if pool and await ctx.ask_yes_no(prompt="Discard an Item for more damage?"):
            picks = await ctx.choose_cards(pool, 1, prompt="Choose an Item card")
            if picks:
                await ctx.discard_cards(list(picks))
                await ctx.deal_damage(printed + bonus)
                return
        await ctx.deal_damage()
    return effect


def _t61_move_defender_energy_bench(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        energies = ctx.attached_energies(defender)
        candidates = [pokemon for pokemon in ctx.opponent_bench()
                      if not ctx.effects_blocked(pokemon)]
        if not energies or not candidates:
            return
        picks = await ctx.choose_cards(energies, 1, prompt=(
            "Choose an Energy to move"))
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Benched Pokémon")
        if picks and target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _t61_discard_typed_heal(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    amount = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        energies = [energy for energy in ctx.attached_energies(attacker)
                    if energy_provides_type(energy, type_value)]
        if energies:
            await ctx.discard_cards(energies[:1])
            await ctx.heal(amount, attacker)
    return effect


def _t61_attach_opponent_discard_energy(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile(ctx.opponent_id)
                if is_energy_card(card)]
        candidates = ctx.opponent_pokemon_in_play()
        if not pile or not candidates:
            return
        picks = await ctx.choose_cards(pile, count, minimum=0, prompt=(
            f"Choose up to {count} Energy cards"))
        for card in picks:
            target = candidates[0] if len(candidates) == 1 else \
                await ctx.choose_pokemon(candidates, "Choose a Pokémon")
            if target is not None:
                await ctx.attach_energy(card, target)
    return effect


def _t61_search_pokemon_to_hand(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(lambda card: _is_pokemon_card(card),
                                      count=limit, minimum=0,
                                      prompt="Choose Pokémon")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=True)
        await ctx.shuffle_deck()
    return effect


def _t61_attach_typed_discard_distributed(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_pokemon_in_play()
        if not pile or not candidates:
            return
        picks = await ctx.choose_cards(pile, count, minimum=0, prompt=(
            f"Choose up to {count} Energy cards"))
        if picks:
            await distribute_energy(ctx, list(picks), candidates)
    return effect


def _t61_search_energy_attach_self(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        picks = await ctx.search_deck(is_energy_card, count=count, minimum=0,
                                      prompt="Choose Energy cards")
        for card in picks:
            if attacker is not None:
                await ctx.attach_energy(card, attacker)
        await ctx.shuffle_deck()
    return effect


def _t61_recover_typed_pokemon_many(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    def predicate(card) -> bool:
        return _is_pokemon_card(card) and type_value in (
            card.get_attribute(AttrID.POKEMON_TYPES) or [])
    return recover_from_discard(predicate=predicate, count=count, minimum=0)


def _t61_discard_typed_all_then_condition(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is not None:
            energies = [energy for energy in ctx.attached_energies(attacker)
                        if energy_provides_type(energy, type_value)]
            if energies:
                await ctx.discard_cards(energies)
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _t61_recoil_no_weakness_plain(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.deal_damage(amount, target=ctx.attacker,
                                  ignore_weakness=True)
    return effect


def _t61_attach_up_to_basic_hand_self(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        pool = [card for card in ctx.hand() if is_basic_energy_card(card)]
        if attacker is None or not pool:
            return
        picks = await ctx.choose_cards(pool, limit, minimum=0, prompt=(
            f"Choose up to {limit} Energy cards"))
        for card in picks:
            await ctx.attach_energy(card, attacker)
    return effect


def _t61_move_all_energy_to_bench(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        energies = list(ctx.attached_energies(attacker))
        candidates = ctx.my_bench()
        if not energies or not candidates:
            return
        if await ctx.ask_yes_no(prompt="Move all Energy to your Bench?"):
            await distribute_energy(ctx, energies, candidates)
    return effect


def _t61_scale_per_opponent_typed(m, ability):
    per = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.opponent_pokemon_in_play()
                   if type_value in (pokemon.get_attribute(AttrID.POKEMON_TYPES)
                                     or []))
    return damage_per(count, per)


def _t61_peek_then_optional_shuffle(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(1, ctx.player_id)
        if top:
            await ctx.reveal_cards(list(top), to_player=ctx.player_id)
        if await ctx.ask_yes_no(prompt="Shuffle your deck?"):
            await ctx.shuffle_deck()
    return effect


def _t61_counters_then_switch(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_pokemon_in_play():
            if not ctx.effects_blocked(pokemon):
                await ctx.deal_damage(counters * 10, target=pokemon,
                                      as_counters=True)
        if ctx.my_bench():
            await switch_self_attack()(ctx)
    return effect


def _t61_discard_special_chosen(m, ability):
    count = 1

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [energy for pokemon in ctx.opponent_pokemon_in_play()
                if not ctx.effects_blocked(pokemon)
                for energy in ctx.attached_energies(pokemon)
                if is_special_energy(energy)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, count, minimum=0, prompt=(
            "Choose special Energy to discard"))
        if picks:
            await ctx.discard_cards(list(picks))
    return effect


def _t61_draw_then_optional_switch(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.draw_cards(count)
        if ctx.my_bench() and await ctx.ask_yes_no(
                prompt="Switch this Pokémon with a Benched Pokémon?"):
            await switch_self_attack()(ctx)
    return effect


def _t61_shuffle_basic_energy_back_many(m, ability):
    count = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if is_basic_energy_card(card)]
        if not pile:
            return
        picks = await ctx.choose_cards(pile, count, minimum=0, prompt=(
            f"Choose up to {count} Energy cards"))
        if picks:
            await ctx.shuffle_into_deck(list(picks), ctx.player_id)
    return effect


def _t61_reveal_hand_discard_trainer(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        cards = list(ctx.hand(ctx.opponent_id))
        if not cards:
            return
        await ctx.reveal_cards(cards)
        trainers = [card for card in cards
                    if _trainer_kind(card) in (
                        TrainerType.TRAINER, TrainerType.SUPPORTER, TrainerType.ITEM)]
        if trainers:
            await ctx.discard_cards(trainers[:1])
    return effect


def _t61_mill_typed_attach_single(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        top = ctx.deck_top(1, ctx.player_id)
        if not top or attacker is None:
            return
        card = top[0]
        if is_energy_card(card) and energy_provides_type(card, type_value):
            await ctx.attach_energy(card, attacker)
        else:
            await ctx.discard_cards([card])
    return effect


def _t61_optional_typed_energy_bonus(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    bonus = int(m.group(2))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        attacker = ctx.attacker
        pool = []
        if attacker is not None:
            pool = [energy for energy in ctx.attached_energies(attacker)
                    if energy_provides_type(energy, type_value)]
        if pool and await ctx.ask_yes_no(
                prompt="Discard all that Energy for more damage?"):
            await ctx.discard_cards(pool)
            await ctx.deal_damage(printed + bonus)
            return
        await ctx.deal_damage()
    return effect


def _t61_discard_all_special_each_opponent(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_pokemon_in_play():
            if ctx.effects_blocked(pokemon):
                continue
            special = [energy for energy in ctx.attached_energies(pokemon)
                       if is_special_energy(energy)]
            if special:
                await ctx.discard_cards(special)
    return effect


def _t61_look_through_deck(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.shuffle_deck()
    return effect


def _t61_discard_defender_energy_if_ex(m, ability):
    from ptcgo.game.card_effects.attacks_common import defender_is_ex

    async def effect(ctx):
        await ctx.deal_damage()
        if defender_is_ex(ctx):
            defender = ctx.defender
            if defender is not None and ctx.attached_energies(defender):
                await ctx.discard_energy_from(defender, 1)
    return effect


def _t61_recover_pokemon_many(m, ability):
    count = _count(m.group(1))
    return recover_from_discard(predicate=_is_pokemon_card, count=count,
                                minimum=0)


def _t61_bonus_more_prizes_left(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        mine = 6 - ctx.prizes_taken(ctx.player_id)
        theirs = 6 - ctx.prizes_taken(ctx.opponent_id)
        return mine > theirs
    return bonus_if(cond, bonus)


def _t61_search_typed_energy_to_hand(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(
            lambda card: is_energy_card(card)
            and energy_provides_type(card, type_value),
            count=1, minimum=0, prompt="Choose an Energy card")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=True)
        await ctx.shuffle_deck()
    return effect


def _t61_switch_if_defender_ex(m, ability):
    from ptcgo.game.card_effects.attacks_common import defender_is_ex

    async def effect(ctx):
        await ctx.deal_damage()
        if defender_is_ex(ctx) and ctx.my_bench():
            await switch_self_attack()(ctx)
    return effect


def _t61_scale_revealed_items(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        mine = list(ctx.hand())
        theirs = list(ctx.hand(ctx.opponent_id))
        if mine:
            await ctx.reveal_cards(mine, to_player=ctx.opponent_id)
        if theirs:
            await ctx.reveal_cards(theirs, to_player=ctx.player_id)
        items = sum(1 for card in mine + theirs
                    if _trainer_kind(card) in (TrainerType.ITEM, TrainerType.TRAINER))
        await ctx.deal_damage(per * items)
    return effect


def _t61_bonus_mill_energy(m, ability):
    bonus = int(m.group(1))

    async def effect(ctx):
        top = ctx.deck_top(1, ctx.player_id)
        printed = getattr(ctx.ability, "damage", 0) or 0
        if not top:
            await ctx.deal_damage()
            return
        is_energy = is_energy_card(top[0])
        await ctx.discard_cards(list(top))
        await ctx.deal_damage(printed + (bonus if is_energy else 0))
    return effect


def _t61_recover_typed_energy_many(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    def predicate(card) -> bool:
        return is_energy_card(card) and \
            energy_provides_type(card, type_value)
    return recover_from_discard(predicate=predicate, count=count, minimum=0)


def _t61_pre_switch_opponent_imperative(m, ability):
    from ptcgo.game.card_effects.support_common import opponent_switches

    async def effect(ctx):
        await opponent_switches(ctx)
        await ctx.deal_damage()
    return effect


def _t61_flip_tails_return_self(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and not results[0]:
            await remove_self_from_play(destination="hand")(ctx)
    return effect


def _t61_mill_scale_per_energy(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        milled = ctx.deck_top(int(m.group(2)), ctx.player_id)
        energy = sum(1 for card in (milled or []) if is_energy_card(card))
        if milled:
            await ctx.discard_cards(milled)
        await ctx.deal_damage(per * energy)
    return effect


def _t61_mill_opponent_if_damaged(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None or ctx.max_hp(attacker) <= \
                attacker.get_attribute(AttrID.HP, 0):
            return
        top = ctx.deck_top(count, ctx.opponent_id)
        if top:
            await ctx.discard_cards(top)
    return effect


def _t61_attach_discard_energy_any_pokemon(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)]
        candidates = ctx.my_pokemon_in_play()
        if not pile or not candidates:
            return
        picks = await ctx.choose_cards(pile, 1, prompt="Choose an Energy card")
        if not picks:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Pokémon")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _t61_opponent_hand_to_bottom(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        hand = list(ctx.hand(ctx.opponent_id))
        if not hand:
            return
        await ctx.put_on_bottom_of_deck(random.choice(hand))
    return effect


def _t61_optional_typed_energy_return_bonus(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    bonus = int(m.group(2))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        attacker = ctx.attacker
        pool = []
        if attacker is not None:
            pool = [energy for energy in ctx.attached_energies(attacker)
                    if energy_provides_type(energy, type_value)]
        if pool and await ctx.ask_yes_no(
                prompt="Return that Energy to your hand for more damage?"):
            picks = await ctx.choose_cards(pool, 1, prompt=(
                "Choose an Energy card"))
            if picks:
                await ctx.put_in_hand(list(picks), reveal=False)
                await ctx.deal_damage(printed + bonus)
                return
        await ctx.deal_damage()
    return effect


def _t61_attach_hand_energy_bench_up_to(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_energy_card(card)]
        candidates = ctx.my_bench()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, limit, minimum=0, prompt=(
            f"Choose up to {limit} Energy cards"))
        chosen = []
        for card in picks:
            target = candidates[0] if len(candidates) == 1 else \
                await ctx.choose_pokemon(candidates, "Choose a Benched Pokémon")
            if target is not None:
                chosen.append((card, target))
        for card, target in chosen:
            await ctx.attach_energy(card, target)
    return effect


def _t61_condition_then_strip_tools(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        await ctx.apply_special_condition(defender, condition)
        tools = [card for card in ctx.attached_energies(defender)
                 if not is_energy_card(card)]
        if tools:
            await ctx.discard_cards(tools)
    return effect


def _t61_draw_then_switch(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.draw_cards(1)
        if ctx.my_bench():
            await switch_self_attack()(ctx)
    return effect


def _t61_flip_condition_or_nothing(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if not (results and results[0]):
            return
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _t61_optional_attach_hand_bench(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_energy_card(card)]
        candidates = ctx.my_bench()
        if not pool or not candidates:
            return
        if not await ctx.ask_yes_no(prompt="Attach an Energy to your Bench?"):
            return
        picks = await ctx.choose_cards(pool, 1, prompt="Choose an Energy card")
        if not picks:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Benched Pokémon")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _t61_bonus_per_evolution_in_play(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.my_pokemon_in_play()
                   if _stage_of(pokemon) >= 1)
    return damage_per(count, per)


def _t61_bonus_if_mega_on_bench(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        return any(_stage_of(pokemon) >= 1 for pokemon in ctx.my_bench())
    return bonus_if(cond, bonus)


def _t62_scale_per_opponent_ability(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.opponent_pokemon_in_play()
                   if pokemon.get_attribute(AttrID.PIE_ABILITIES))
    return damage_per(count, per)


def _t62_bonus_defender_v_or_gx(m, ability):
    from ptcgo.game.card_effects.attacks_common import defender_is_v
    from ptcgo.game.data_utils import subtypes_for
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        defender = ctx.defender
        if defender is None or defender_is_v(ctx):
            return defender is not None and defender_is_v(ctx)
        subtypes = [s.lower() for s in subtypes_for(defender.archetype_id)]
        return "gx" in subtypes
    return bonus_if(cond, bonus)


def _t62_attach_typed_discard_single_any(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_pokemon_in_play()
        if not pile or not candidates:
            return
        picks = await ctx.choose_cards(pile, 1, prompt="Choose an Energy card")
        if not picks:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Pokémon")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _t62_counters_per_discard_pokemon(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        count = sum(1 for card in ctx.discard_pile() if _is_pokemon_card(card))
        counters = per * count
        if counters:
            await ctx.deal_damage(counters * 10, target=defender,
                                  as_counters=True)
    return effect


def _t62_attach_hand_then_switch(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        pool = [card for card in ctx.hand() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        if attacker is None or not pool:
            return
        picks = await ctx.choose_cards(pool, 1, minimum=0, prompt=(
            "Choose an Energy card"))
        if picks:
            await ctx.attach_energy(picks[0], attacker)
            if ctx.my_bench():
                await switch_self_attack()(ctx)
    return effect


def _t62_optional_hand_bonus(m, ability):
    bonus = int(m.group(1))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        hand = list(ctx.hand())
        if hand and await ctx.ask_yes_no(prompt="Discard a card for more damage?"):
            picks = await ctx.choose_cards(hand, 1, prompt="Choose a card")
            if picks:
                await ctx.discard_cards(list(picks))
                await ctx.deal_damage(printed + bonus)
                return
        await ctx.deal_damage()
    return effect


def _t62_reveal_hand_bottom_card(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        cards = list(ctx.hand(ctx.opponent_id))
        if not cards:
            return
        await ctx.reveal_cards(cards)
        picks = await ctx.choose_cards(cards, 1, prompt=(
            "Choose a card to put on the bottom of the deck"))
        if picks:
            await ctx.put_on_bottom_of_deck(picks[0])
    return effect


def _t62_bonus_per_distinct_basic_type_all(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        types = set()
        for pokemon in ctx.my_pokemon_in_play():
            for energy in ctx.attached_energies(pokemon):
                if not is_basic_energy_card(energy):
                    continue
                for candidate in PokemonTypes:
                    if candidate in (PokemonTypes.NO_COLOR, PokemonTypes.STRONG,
                                     PokemonTypes.HERBAL, PokemonTypes.UNSET):
                        continue
                    if energy_provides_type(energy, candidate.value):
                        types.add(candidate)
        return len(types)
    return damage_per(count, per)


def _t62_counters_per_prizes_taken(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        counters = per * ctx.prizes_taken(ctx.opponent_id)
        if counters:
            await ctx.deal_damage(counters * 10, target=defender,
                                  as_counters=True)
    return effect


def _t62_attach_hand_bench_then_heal(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_energy_card(card)]
        candidates = ctx.my_bench()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, 1, prompt="Choose an Energy card")
        if not picks:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Benched Pokémon")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
            await ctx.heal(amount, target)
    return effect


def _t62_recoil_then_condition(m, ability):
    amount = int(m.group(1))
    condition = CONDITIONS[m.group(2)]

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.deal_damage(amount, target=ctx.attacker,
                                  ignore_weakness=True)
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _t62_gate_typed_hand_discard(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        pool = [card for card in ctx.hand() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        if len(pool) < count:
            return
        picks = await ctx.choose_cards(pool, count, prompt=(
            f"Discard {count} Energy cards"))
        if len(picks) < count:
            return
        await ctx.discard_cards(list(picks))
        await ctx.deal_damage()
    return effect


def _t62_heal_chosen_many(m, ability):
    amount = int(m.group(1))
    targets = _count(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [pokemon for pokemon in ctx.my_pokemon_in_play()
                if ctx.max_hp(pokemon) > pokemon.get_attribute(AttrID.HP, 0)]
        if not pool:
            return
        picks = pool if len(pool) <= targets else await ctx.choose_cards(
            pool, targets, prompt="Choose Pokémon to heal")
        for pokemon in picks:
            await ctx.heal(amount, pokemon)
    return effect


def _t62_flip_tails_discard_typed(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        attacker = ctx.attacker
        if (results and results[0]) or attacker is None:
            return
        energies = [energy for energy in ctx.attached_energies(attacker)
                    if energy_provides_type(energy, type_value)]
        if energies:
            await ctx.discard_cards(energies[:min(count, len(energies))])
    return effect


def _t62_optional_bonus_then_asleep(m, ability):
    bonus = int(m.group(1))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if await ctx.ask_yes_no(prompt=f"Do {bonus} more damage and fall asleep?"):
            await ctx.deal_damage(printed + bonus)
            if ctx.attacker is not None:
                await ctx.apply_special_condition(ctx.attacker,
                                                  SpecialConditions.ASLEEP)
        else:
            await ctx.deal_damage()
    return effect


def _t62_counters_each_opponent_all(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_pokemon_in_play():
            if not ctx.effects_blocked(pokemon):
                await ctx.deal_damage(counters * 10, target=pokemon,
                                      as_counters=True)
    return effect


def _t62_counters_both_active_to_hp(m, ability):
    target_hp = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in (ctx.my_active(), ctx.opponent_active()):
            if pokemon is None or ctx.effects_blocked(pokemon):
                continue
            counters = (pokemon.get_attribute(AttrID.HP, 0) - target_hp) // 10
            if counters > 0:
                await ctx.deal_damage(counters * 10, target=pokemon,
                                      as_counters=True)
    return effect


def _t62_optional_mill_bonus_typed(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    bonus = int(m.group(2))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        top = ctx.deck_top(1, ctx.player_id)
        if not top:
            await ctx.deal_damage()
            return
        matched = is_energy_card(top[0]) and \
            energy_provides_type(top[0], type_value)
        if matched and await ctx.ask_yes_no(prompt="Discard it for more damage?"):
            await ctx.discard_cards(list(top))
            await ctx.deal_damage(printed + bonus)
            return
        await ctx.deal_damage()
    return effect


def _t62_opponent_flips_discard_hand(m, ability):
    coins = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        tails = sum(1 for result in results or [] if not result)
        for _ in range(tails):
            hand = ctx.hand(ctx.opponent_id)
            if not hand:
                return
            await ctx.discard_cards([random.choice(list(hand))])
    return effect


def _t62_mill_typed_attach_nocard(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        top = ctx.deck_top(1, ctx.player_id)
        if not top or attacker is None:
            return
        card = top[0]
        if is_energy_card(card) and energy_provides_type(card, type_value):
            await ctx.attach_energy(card, attacker)
        else:
            await ctx.discard_cards([card])
    return effect


def _t62_discard_energy_heal_all_it(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        if ctx.attached_energies(attacker):
            await ctx.discard_energy_from(attacker, 1)
        await ctx.heal(9990, attacker)
    return effect


def _t62_choose_asleep_or_poisoned(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        await _choose_condition(ctx, [SpecialConditions.ASLEEP,
                                      SpecialConditions.POISONED])
    return effect


def _t62_attach_energy_discard_typed_target(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)]
        candidates = [pokemon for pokemon in ctx.my_pokemon_in_play()
                      if type_value in (pokemon.get_attribute(AttrID.POKEMON_TYPES)
                                        or [])]
        if not pile or not candidates:
            return
        picks = await ctx.choose_cards(pile, count, minimum=0, prompt=(
            f"Choose up to {count} Energy cards"))
        chosen = []
        for card in picks:
            target = candidates[0] if len(candidates) == 1 else \
                await ctx.choose_pokemon(candidates, "Choose a Pokémon")
            if target is not None:
                chosen.append((card, target))
        for card, target in chosen:
            await ctx.attach_energy(card, target)
    return effect


def _t62_scale_per_energy_all_in_play(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return sum(len(ctx.attached_energies(pokemon))
                   for pokemon in (ctx.my_pokemon_in_play()
                                   + ctx.opponent_pokemon_in_play()))
    return damage_per(count, per)


def _t62_delayed_discard_defender(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return

        async def apply(ctx2, pokemon):
            cards = [pokemon] + list(ctx2.attached_energies(pokemon))
            await ctx2.discard_cards(cards)
        _delayed_checkup_rider(
            ctx, (defender.owning_player_id, defender.entity_id), apply)
    return effect


def _t62_flip_opponent_switch_plain(m, ability):
    from ptcgo.game.card_effects.support_common import opponent_switches

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and results[0] and ctx.opponent_bench():
            await opponent_switches(ctx)
    return effect


def _t62_discard_tool_attached_any(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for pokemon in ctx.opponent_pokemon_in_play()
                if not ctx.effects_blocked(pokemon)
                for card in ctx.attached_energies(pokemon)
                if not is_energy_card(card)]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, 1, prompt=(
            "Choose a Pokémon Tool card"))
        if picks:
            await ctx.discard_cards(list(picks))
    return effect


def _t62_draw_then_bottom_card(m, ability):
    count = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.draw_cards(count)
        hand = list(ctx.hand())
        if not hand:
            return
        picks = await ctx.choose_cards(hand, 1, prompt=(
            "Choose a card to put on the bottom of your deck"))
        if picks:
            await ctx.put_on_bottom_of_deck(picks[0])
    return effect


def _t62_scale_per_special_energy_opponent_discard(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return sum(1 for card in ctx.discard_pile(ctx.opponent_id)
                   if is_special_energy(card))
    return damage_per(count, per)


def _t62_search_trainer_afterward(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(
            lambda card: _trainer_kind(card) in (
                TrainerType.TRAINER, TrainerType.SUPPORTER, TrainerType.ITEM), count=1, minimum=0,
            prompt="Choose a Trainer card")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=True)
        await ctx.shuffle_deck()
    return effect


def _t63_pokemon_in_play_of(board, player_id):
    try:
        return list(board.pokemon_in_play(player_id))
    except Exception:
        return []


def _t63_discard_cards(board, player_id):
    area = board.find_player_area(player_id, "discard")
    return list(area.children) if area is not None else []


def _t63_trainer_type(card):
    from ptcgo.game.attributes import TrainerType
    value = card.get_attribute(AttrID.TRAINER_TYPE)
    for candidate in TrainerType:
        if candidate.value == value:
            return candidate
    return None


def _grant_attacks_any_in_play(m, ability):
    from ptcgo.game.card_effects.passives_common import attack_grant_passive

    def sources(board, pokemon, carrier):
        out = []
        for player_id in getattr(board, "player_ids", []):
            out.extend(p for p in _t63_pokemon_in_play_of(board, player_id)
                       if p is not pokemon)
        return out
    return attack_grant_passive(sources)


def _grant_attacks_bench(m, ability):
    from ptcgo.game.card_effects.passives_common import attack_grant_passive

    def sources(board, pokemon, carrier):
        holder = carrier_pokemon(carrier) or pokemon
        owner = getattr(holder, "owning_player_id", None)
        return [p for p in _t63_pokemon_in_play_of(board, owner)
                if p is not pokemon and p is not holder]
    return attack_grant_passive(sources)


def _grant_attacks_discard_basics(m, ability):
    from ptcgo.game.card_effects.passives_common import attack_grant_passive
    from ptcgo.game.session.effects import is_basic_pokemon

    def sources(board, pokemon, carrier):
        holder = carrier_pokemon(carrier) or pokemon
        owner = getattr(holder, "owning_player_id", None)
        return [card for card in _t63_discard_cards(board, owner)
                if is_basic_pokemon(card)]
    return attack_grant_passive(sources)


def _grant_attacks_bench_discard_gx_ex(m, ability):
    from ptcgo.game.card_effects.passives_common import attack_grant_passive
    from ptcgo.game.data_utils import subtypes_for

    def is_gx_or_ex(card) -> bool:
        subtypes = [sub.lower() for sub in subtypes_for(card.archetype_id)]
        return "gx" in subtypes or "ex" in subtypes

    def sources(board, pokemon, carrier):
        holder = carrier_pokemon(carrier) or pokemon
        owner = getattr(holder, "owning_player_id", None)
        bench = [p for p in _t63_pokemon_in_play_of(board, owner)
                 if p is not pokemon]
        pile = _t63_discard_cards(board, owner)
        return [card for card in bench + pile if is_gx_or_ex(card)]
    return attack_grant_passive(sources)


def _grant_previous_evolutions(m, ability):
    from ptcgo.game.card_effects.passives_common import (
        previous_evolution_grant_passive)
    return previous_evolution_grant_passive()


def _free_cost_if_tools_in_discard(m, ability):
    from ptcgo.game.card_effects.passives_common import free_attack_cost_passive
    from ptcgo.game.attributes import TrainerType
    needed = int(m.group(1))

    def condition(board, pokemon, carrier):
        holder = carrier_pokemon(carrier) or pokemon
        owner = getattr(holder, "owning_player_id", None)
        tools = [card for card in _t63_discard_cards(board, owner)
                 if _t63_trainer_type(card) in (TrainerType.POKEMON_TOOL,
                                                TrainerType.POKEMON_TOOL_F)]
        return len(tools) >= needed
    return free_attack_cost_passive(condition=condition)


def _free_cost_if_stadiums_in_discard(m, ability):
    from ptcgo.game.card_effects.passives_common import free_attack_cost_passive
    from ptcgo.game.attributes import CardType
    needed = int(m.group(1))

    def condition(board, pokemon, carrier):
        holder = carrier_pokemon(carrier) or pokemon
        owner = getattr(holder, "owning_player_id", None)
        stadiums = [card for card in _t63_discard_cards(board, owner)
                    if card.get_attribute(AttrID.CARD_TYPE)
                    == CardType.STADIUM.value]
        return len(stadiums) >= needed
    return free_attack_cost_passive(condition=condition)


def _free_cost_if_named_in_play(m, ability):
    from ptcgo.game.card_effects.passives_common import free_attack_cost_passive
    wanted = normalize(m.group(1))

    def condition(board, pokemon, carrier):
        holder = carrier_pokemon(carrier) or pokemon
        owner = getattr(holder, "owning_player_id", None)
        return any(wanted in normalize(getattr(entity, "display_name", "") or "")
                   for entity in _t63_pokemon_in_play_of(board, owner))
    return free_attack_cost_passive(condition=condition)


def _free_cost_plain(m, ability):
    from ptcgo.game.card_effects.passives_common import free_attack_cost_passive
    return free_attack_cost_passive()


def _free_cost_team_with_attack(m, ability):
    from ptcgo.game.card_effects.passives_common import free_attack_cost_passive
    from ptcgo.game.session.passives import attacks_of
    wanted = normalize(m.group(1))

    def condition(board, pokemon, carrier):
        return any(normalize(getattr(attack, "title", "") or "") == wanted
                   for attack in attacks_of(pokemon))
    return free_attack_cost_passive(condition=condition, protects="team")


def _t63_free_next_attack(m, ability):
    async def effect(ctx):
        ctx.ignore_next_attack_cost()
        await ctx.deal_damage()
    return effect


def _t63_use_opponent_attack(m, ability):
    async def effect(ctx):
        pool = []
        for pokemon in ctx.opponent_pokemon_in_play():
            for attack in ctx.attacks_of(pokemon) or []:
                pool.append((pokemon, attack))
        if not pool:
            return
        choice = await ctx.choose_attack_to_copy(
            pool, prompt="Choose an attack to use")
        if choice is None:
            return
        pokemon, attack = choice
        await ctx.use_attack(attack, source=pokemon)
    return effect


def _t64_distribute_counters_opponent(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                if not ctx.effects_blocked(pokemon)]
        for _ in range(counters):
            if not pool:
                return
            picks = await ctx.choose_cards(pool, 1, prompt=(
                "Choose a Pokémon for a damage counter"))
            if not picks:
                return
            await ctx.deal_damage(10, target=picks[0], as_counters=True)
    return effect


def _t64_spread_damaged_bench(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_bench():
            if ctx.effects_blocked(pokemon):
                continue
            if ctx.max_hp(pokemon) > pokemon.get_attribute(AttrID.HP, 0):
                await ctx.deal_damage(amount, target=pokemon,
                                      ignore_weakness=True)
    return effect


def _t64_snipe_scaled_by_energy(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        candidates = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                      if not ctx.effects_blocked(pokemon)]
        if not candidates:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Pokémon")
        if target is None:
            return
        count = len(ctx.attached_energies(target))
        if count:
            await ctx.deal_damage(per * count, target=target,
                                  ignore_weakness=True)
    return effect


def _t64_search_self_to_bench(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        own = getattr(ctx.source, "display_name", "") or ""
        if not own:
            return
        picks = await ctx.search_deck(
            lambda card: normalize(getattr(card, "display_name", "") or "") ==
            normalize(own), count=1, minimum=0, prompt="Choose this Pokémon")
        for card in picks:
            await ctx.bench_pokemon(card)
        await ctx.shuffle_deck()
    return effect


def _t64_gate_named_energy(m, ability):
    wanted = normalize(m.group(1))

    async def effect(ctx):
        attacker = ctx.attacker
        if attacker is None:
            return
        has = any(wanted in normalize(getattr(card, "display_name", "") or "")
                  for card in ctx.attached_energies(attacker)
                  if is_energy_card(card))
        if not has:
            return
        energies = [card for card in ctx.attached_energies(attacker)
                    if is_energy_card(card)
                    and wanted in normalize(getattr(card, "display_name", "") or "")]
        if energies:
            await ctx.discard_cards(energies[:1])
        await ctx.deal_damage()
    return effect


def _t64_scale_two_typed_energy_own(m, ability):
    per = int(m.group(1))
    first = TYPE_WORDS[m.group(2)].value
    second = TYPE_WORDS[m.group(3)].value

    def count(ctx) -> int:
        total = 0
        for pokemon in ctx.my_pokemon_in_play():
            for energy in ctx.attached_energies(pokemon):
                if energy_provides_type(energy, first) or \
                        energy_provides_type(energy, second):
                    total += 1
        return total
    return damage_per(count, per)


def _t64_move_defender_energy_to_bench(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        energies = ctx.attached_energies(defender)
        candidates = [pokemon for pokemon in ctx.opponent_bench()
                      if not ctx.effects_blocked(pokemon)]
        if not energies or not candidates:
            return
        picks = await ctx.choose_cards(energies, 1, prompt=(
            "Choose an Energy to move"))
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Benched Pokémon")
        if picks and target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _t64_damage_own_chosen(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = ctx.my_pokemon_in_play()
        if not pool:
            return
        target = pool[0] if len(pool) == 1 else \
            await ctx.choose_pokemon(pool, "Choose one of your Pokémon")
        if target is not None:
            await ctx.deal_damage(amount, target=target,
                                  ignore_weakness=True)
    return effect


def _t64_mill_opponent_top(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(1, ctx.opponent_id)
        if top:
            await ctx.discard_cards(top)
    return effect


async def _choose_condition(ctx, choices, prompt="Choose a Special Condition"):
    """Asks the player for one Special Condition out of `choices` and applies it
    to the Defending Pokemon. Conditions are values, not cards, so the offer is
    a button dialog -- handing them to ctx.choose_cards crashes on
    `SpecialConditions.entity_id`."""
    if not choices:
        return None
    labels = [CLIENT_SPECIAL_CONDITION_NAMES[condition] for condition in choices]
    index = await ctx.choose(prompt, labels)
    condition = choices[index] if 0 <= index < len(choices) else choices[0]
    await ctx.apply_special_condition(ctx.defender, condition)
    return condition


def _t64_flip_choice_condition(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        defender = ctx.defender
        if not (results and results[0]) or defender is None or \
                ctx.effects_blocked(defender):
            return
        await _choose_condition(ctx, [SpecialConditions.ASLEEP,
                                      SpecialConditions.BURNED,
                                      SpecialConditions.CONFUSED,
                                      SpecialConditions.PARALYZED,
                                      SpecialConditions.POISONED])
    return effect


def _t64_stadium_bonus_then_discard(m, ability):
    from ptcgo.game.card_effects.attacks_common import stadium_in_play_cond
    bonus = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if stadium_in_play_cond(ctx):
            await ctx.deal_damage(bonus, apply_modifiers=False)
            await ctx.discard_stadium()
    return effect


def _t64_optional_shuffle_self(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if await ctx.ask_yes_no(prompt="Shuffle this Pokémon into your deck?"):
            await _shuffle_self_into_deck(m, ability)(ctx)
    return effect


def _t64_scale_per_active_energy(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        return sum(len(ctx.attached_energies(pokemon))
                   for pokemon in ctx.my_pokemon_in_play()
                   if pokemon is ctx.my_active())
    return damage_per(count, per)


def _t64_bonus_one_prize_left(m, ability):
    bonus = int(m.group(2))

    def cond(ctx) -> bool:
        return (6 - ctx.prizes_taken(ctx.player_id)) <= 1
    return bonus_if(cond, bonus)


def _t64_optional_typed_all_bonus(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    bonus = int(m.group(2))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        attacker = ctx.attacker
        pool = []
        if attacker is not None:
            pool = [energy for energy in ctx.attached_energies(attacker)
                    if energy_provides_type(energy, type_value)]
        if pool and await ctx.ask_yes_no(prompt="Discard that Energy for more damage?"):
            await ctx.discard_cards(pool)
            await ctx.deal_damage(printed + bonus)
            return
        await ctx.deal_damage()
    return effect


def _t64_discard_energy_then_lock_defender(m, ability):
    from ptcgo.game.card_effects.attacks_common import lock_defender_attacks

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is not None and ctx.attached_energies(attacker):
            await ctx.discard_energy_from(attacker, 1)
        lock_defender_attacks(ctx)
    return effect


def _t64_discard_energy_then_switch(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is not None and ctx.attached_energies(attacker):
            await ctx.discard_energy_from(attacker, 1)
            if ctx.my_bench():
                await switch_self_attack()(ctx)
    return effect


def _t64_condition_then_defender_no_retreat_word(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        await ctx.apply_special_condition(defender, condition)
        ctx.add_passive_through_opponents_turn(
            defender, no_retreat_passive(lambda p, c: p is carrier_pokemon(c)))
    return effect


def _t64_scale_night_march_discard(m, ability):
    per = int(m.group(1))

    def count(ctx) -> int:
        total = 0
        for card in ctx.discard_pile():
            for attack in ctx.attacks_of(card) or []:
                if normalize(getattr(attack, "title", "") or "") == \
                        normalize("Night March"):
                    total += 1
                    break
        return total
    return damage_per(count, per)


def _t64_flip_times_heads_then_confused(m, ability):
    coins = _count(m.group(1))
    per = int(m.group(2))

    async def effect(ctx):
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        heads = sum(1 for result in results or [] if result)
        await ctx.deal_damage(per * heads)
        if ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker,
                                              SpecialConditions.CONFUSED)
    return effect


def _t64_flip_condition_then_discard_energy(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        defender = ctx.defender
        if not (results and results[0]) or defender is None or \
                ctx.effects_blocked(defender):
            return
        await ctx.apply_special_condition(defender, condition)
        if ctx.attached_energies(defender):
            await ctx.discard_energy_from(defender, 1)
    return effect


def _t64_recover_named_cards(m, ability):
    wanted = normalize(m.group(1))

    def predicate(card) -> bool:
        return wanted in normalize(getattr(card, "display_name", "") or "")
    return recover_from_discard(predicate=predicate, count=99, minimum=0)


def _t64_optional_bonus_recoil(m, ability):
    bonus = int(m.group(1))
    recoil = int(m.group(2))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if await ctx.ask_yes_no(prompt=f"Do {bonus} more and take {recoil}?"):
            await ctx.deal_damage(printed + bonus)
            if ctx.attacker is not None:
                await ctx.deal_damage(recoil, target=ctx.attacker,
                                      ignore_weakness=True)
        else:
            await ctx.deal_damage()
    return effect


def _t64_mill_both_bonus_per_energy(m, ability):
    per = int(m.group(1))

    async def effect(ctx):
        energy = 0
        for player_id in (ctx.player_id, ctx.opponent_id):
            top = ctx.deck_top(1, player_id)
            if not top:
                continue
            if is_energy_card(top[0]):
                energy += 1
            await ctx.discard_cards(list(top))
        if energy:
            await ctx.deal_damage(per * energy, apply_modifiers=False)
    return effect


def _t64_mill_per_named_energy(m, ability):
    wanted = normalize(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        count = sum(1 for card in ctx.attached_energies(attacker)
                    if is_energy_card(card)
                    and wanted in normalize(getattr(card, "display_name", "") or ""))
        if count:
            top = ctx.deck_top(count, ctx.opponent_id)
            if top:
                await ctx.discard_cards(top)
    return effect


def _t64_heal_per_named_energy(m, ability):
    amount = int(m.group(1))
    wanted = normalize(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        count = sum(1 for card in ctx.attached_energies(attacker)
                    if is_energy_card(card)
                    and wanted in normalize(getattr(card, "display_name", "") or ""))
        if count:
            await ctx.heal(amount * count, attacker)
    return effect


def _t64_attach_energy_up_to_self(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)]
        if attacker is None or not pile:
            return
        picks = await ctx.choose_cards(pile, limit, minimum=0, prompt=(
            f"Choose up to {limit} Energy cards"))
        for card in picks:
            await ctx.attach_energy(card, attacker)
    return effect


def _t64_recover_energy_recoil(m, ability):
    limit = _count(m.group(1))
    recoil = int(m.group(2))

    async def effect(ctx):
        await ctx.deal_damage()
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)]
        if pile:
            picks = await ctx.choose_cards(pile, limit, minimum=0, prompt=(
                f"Choose up to {limit} Energy cards"))
            if picks:
                await ctx.put_in_hand(list(picks), reveal=False)
        if ctx.attacker is not None:
            await ctx.deal_damage(recoil, target=ctx.attacker,
                                  ignore_weakness=True)
    return effect


def _t64_damage_opponent_bench_chosen(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [pokemon for pokemon in ctx.opponent_bench()
                if not ctx.effects_blocked(pokemon)]
        if not pool:
            return
        target = pool[0] if len(pool) == 1 else \
            await ctx.choose_pokemon(pool, "Choose a Benched Pokémon")
        if target is not None:
            await ctx.deal_damage(amount, target=target, ignore_weakness=True)
    return effect


def _t64_confused_after_damage(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if results and not results[0] and ctx.attacker is not None:
            await ctx.apply_special_condition(ctx.attacker,
                                              SpecialConditions.CONFUSED)
    return effect


def _t65_bonus_if_used_last_turn(m, ability):
    wanted = m.group(1)
    bonus = int(m.group(2))

    def cond(ctx) -> bool:
        attacker = ctx.attacker
        return attacker is not None and ctx.attack_used_last_turn(
            title=wanted, entity=attacker, whose="own")
    return bonus_if(cond, bonus)


def _t65_base_swap_if_used_last_turn(m, ability):
    wanted = m.group(1)
    changed = int(m.group(2))

    async def effect(ctx):
        attacker = ctx.attacker
        used = attacker is not None and ctx.attack_used_last_turn(
            title=wanted, entity=attacker, whose="own")
        await ctx.deal_damage(changed if used else None)
    return effect


def _t65_gate_used_last_turn(m, ability):
    wanted = m.group(1)

    async def effect(ctx):
        attacker = ctx.attacker
        if attacker is None or not ctx.attack_used_last_turn(
                title=wanted, entity=attacker, whose="own"):
            return
        await ctx.deal_damage()
    return effect


def _t65_bonus_if_played_named(m, ability):
    wanted = m.group(1)
    bonus = int(m.group(2))

    def cond(ctx) -> bool:
        return ctx.played_trainer_this_turn(wanted) > 0
    return bonus_if(cond, bonus)


def _t65_bonus_if_damaged_last_turn(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        attacker = ctx.attacker
        return attacker is not None and \
            ctx.damaged_by_attack_last_turn(attacker) > 0
    return bonus_if(cond, bonus)


def _t65_bonus_if_own_ko_last_turn(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        return ctx.knocked_out_last_turn(ctx.player_id) > 0
    return bonus_if(cond, bonus)


def _t65_bonus_if_defender_moved(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        defender = ctx.defender
        return defender is not None and ctx.moved_to_active_last_turn(defender)
    return bonus_if(cond, bonus)


def _t65_next_turn_boost_named(m, ability):
    title = m.group(1)
    amount = int(m.group(2))
    return boost_own_next_turn(amount, attack_title=title)


def _t65_use_last_opponent_attack(m, ability):
    async def effect(ctx):
        records = getattr(ctx.session.turn_state, "attacks_used_last_turn", [])
        for entity_id, _archetype, title in reversed(records or []):
            entity = ctx.session.board_state.get_entity(entity_id) \
                if hasattr(ctx.session, "board_state") else None
            if entity is None:
                continue
            for attack in (ctx.attacks_of(entity) or []):
                if getattr(attack, "title", None) == title:
                    await ctx.use_attack(attack, source=entity)
                    return
    return effect


def _t65_bonus_if_self_damaged(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        attacker = ctx.attacker
        return attacker is not None and \
            ctx.max_hp(attacker) > attacker.get_attribute(AttrID.HP, 0)
    return bonus_if(cond, bonus)


def _t65_bonus_if_defender_damaged_last_turn(m, ability):
    bonus = int(m.group(1))

    def cond(ctx) -> bool:
        defender = ctx.defender
        return defender is not None and \
            ctx.damaged_by_attack_last_turn(defender) > 0
    return bonus_if(cond, bonus)


def _t66_recoil_per_typed_energy(m, ability):
    per = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        attacker = ctx.attacker
        await ctx.deal_damage()
        if attacker is None:
            return
        count = sum(1 for energy in ctx.attached_energies(attacker)
                    if energy_provides_type(energy, type_value))
        if count:
            await ctx.deal_damage(per * count, target=attacker,
                                  ignore_weakness=True)
    return effect


def _t66_optional_draw_both(m, ability):
    amount = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if await ctx.ask_yes_no(prompt="Let your opponent draw?"):
            await ctx.draw_cards(amount, ctx.opponent_id)
        if await ctx.ask_yes_no(prompt="Draw cards?"):
            await ctx.draw_cards(amount)
    return effect


def _t66_search_basic_energy_attach_many(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(is_basic_energy_card, count=limit,
                                      minimum=0, prompt="Choose Energy cards")
        candidates = ctx.my_pokemon_in_play()
        if picks and candidates:
            await distribute_energy(ctx, list(picks), candidates)
        await ctx.shuffle_deck()
    return effect


def _t66_discard_typed_heal(m, ability):
    count = _count(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value
    amount = int(m.group(3))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        energies = [energy for energy in ctx.attached_energies(attacker)
                    if energy_provides_type(energy, type_value)]
        if energies:
            await ctx.discard_cards(energies[:min(count, len(energies))])
            await ctx.heal(amount, attacker)
    return effect


def _t66_peek_then_choose(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(1, ctx.player_id)
        if not top:
            return
        if await ctx.ask_yes_no(prompt="Put that card into your hand?"):
            await ctx.put_in_hand(list(top), reveal=False)
            return
        await ctx.discard_cards(list(top))
        await ctx.draw_cards(1)
    return effect


def _t66_search_typed_energy_show_hand(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(
            lambda card: is_energy_card(card)
            and energy_provides_type(card, type_value),
            count=1, minimum=0, prompt="Choose an Energy card")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=True)
        await ctx.shuffle_deck()
    return effect


def _t66_recoil_then_opponent_switch(m, ability):
    from ptcgo.game.card_effects.support_common import opponent_switches
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.attacker is not None:
            await ctx.deal_damage(amount, target=ctx.attacker,
                                  ignore_weakness=True)
        if ctx.opponent_bench():
            await opponent_switches(ctx)
    return effect


def _t66_condition_if_defender_basic(m, ability):
    from ptcgo.game.session.effects import is_basic_pokemon
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        if is_basic_pokemon(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _t66_base_swap_if_defender_hp(m, ability):
    threshold, changed = int(m.group(1)), int(m.group(2))

    async def effect(ctx):
        defender = ctx.defender
        low = defender is not None and \
            defender.get_attribute(AttrID.HP, 0) <= threshold
        await ctx.deal_damage(changed if low else None)
    return effect


def _t66_pre_heal_defender_single(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        defender = ctx.defender
        if defender is not None:
            await ctx.heal(amount, defender)
        await ctx.deal_damage()
    return effect


def _t66_condition_unless_opponent_discards(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        hand = list(ctx.hand(ctx.opponent_id))
        discarded = False
        if hand:
            picks = await ctx.choose_cards(hand, 1, minimum=0, prompt=(
                "Discard a card to avoid the Special Condition"),
                player_id=ctx.opponent_id)
            if picks:
                await ctx.discard_cards(list(picks))
                discarded = True
        defender = ctx.defender
        if not discarded and defender is not None and \
                not ctx.effects_blocked(defender):
            await ctx.apply_special_condition(defender, condition)
    return effect


def _t66_heal_per_defender_energy(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        attacker, defender = ctx.attacker, ctx.defender
        if attacker is None or defender is None:
            return
        count = len(ctx.attached_energies(defender))
        if count:
            await ctx.heal(count * 10, attacker)
    return effect


def _t66_base_swap_if_defender_has_energy(m, ability):
    changed = int(m.group(1))

    async def effect(ctx):
        defender = ctx.defender
        has_energy = defender is not None and bool(
            ctx.attached_energies(defender))
        await ctx.deal_damage(changed if has_energy else None)
    return effect


def _t66_flip_nothing_or_discard(m, ability):
    async def effect(ctx):
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        if not (results and results[0]):
            return
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender) and \
                ctx.attached_energies(defender):
            await ctx.discard_energy_from(defender, 1)
        await ctx.deal_damage()
    return effect


def _t66_flip_base_swap_any_tails(m, ability):
    coins = _count(m.group(1))
    changed = int(m.group(2))

    async def effect(ctx):
        results = await ctx.flip_coins(coins, getattr(ability, "title", ""))
        tails = sum(1 for result in results or [] if not result)
        await ctx.deal_damage(changed if tails else None)
    return effect


def _t66_discard_typed_heal_all(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        energies = [energy for energy in ctx.attached_energies(attacker)
                    if energy_provides_type(energy, type_value)]
        if energies:
            await ctx.discard_cards(energies)
            await ctx.heal(9990, attacker)
    return effect


def _t66_draw_top_and_bottom(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        deck = ctx.session.board.find_player_area(ctx.player_id, "deck") \
            if hasattr(ctx.session, "board") else None
        await ctx.draw_cards(1)
        if deck is not None and getattr(deck, "children", None):
            bottom = deck.children[0]
            await ctx.put_in_hand([bottom], reveal=False)
    return effect


def _t66_condition_if_defender_not_evolved(m, ability):
    condition = CONDITIONS[m.group(1)]

    async def effect(ctx):
        await ctx.deal_damage()
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        if _stage_of(defender) == 0:
            await ctx.apply_special_condition(defender, condition)
    return effect


def _t66_switch_defender_plain(m, ability):
    from ptcgo.game.card_effects.support_common import opponent_switches

    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.opponent_bench():
            await opponent_switches(ctx)
    return effect


def _t66_heal_and_cure(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return
        await ctx.heal(amount, attacker)
        await ctx.cure_all_conditions(attacker)
    return effect


def _t66_flip_search_basic_energy(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        attacker = ctx.attacker
        if not (results and results[0]) or attacker is None:
            return
        picks = await ctx.search_deck(is_basic_energy_card, count=1, minimum=0,
                                      prompt="Choose an Energy card")
        for card in picks:
            await ctx.attach_energy(card, attacker)
        await ctx.shuffle_deck()
    return effect


def _t66_discard_to_top_of_deck(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        pile = ctx.discard_pile()
        if not pile:
            return
        picks = await ctx.choose_cards(pile, limit, prompt=(
            f"Choose up to {limit} cards"))
        for card in picks:
            await ctx.put_on_top_of_deck(card)
    return effect


def _t66_bounce_self_optional(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        if ctx.my_bench():
            await remove_self_from_play(destination="hand")(ctx)
    return effect


def _t66_counters_damaged_opponents(m, ability):
    counters = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.opponent_pokemon_in_play():
            if ctx.effects_blocked(pokemon):
                continue
            if ctx.max_hp(pokemon) > pokemon.get_attribute(AttrID.HP, 0):
                await ctx.deal_damage(counters * 10, target=pokemon,
                                      as_counters=True)
    return effect


def _t66_heal_each_bench(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        for pokemon in ctx.my_bench():
            await ctx.heal(amount, pokemon)
    return effect


def _t66_flip_recover_any(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, getattr(ability, "title", ""))
        pile = ctx.discard_pile()
        if not (results and results[0]) or not pile:
            return
        picks = await ctx.choose_cards(pile, 1, prompt="Choose a card")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=False)
    return effect


def _t66_bonus_per_named_energy(m, ability):
    per = int(m.group(1))
    wanted = normalize(m.group(2))

    def count(ctx) -> int:
        attacker = ctx.attacker
        if attacker is None:
            return 0
        return sum(1 for energy in ctx.attached_energies(attacker)
                   if is_energy_card(energy)
                   and wanted in normalize(getattr(energy, "display_name", "") or ""))
    return damage_per(count, per)


def _t66_prevent_effects_from_ex(m, ability):
    from ptcgo.game.card_effects.passives_common import (
        PredicatePreventionPassive)
    from ptcgo.game.data_utils import subtypes_for

    def is_ex(calc) -> bool:
        attacker = getattr(calc, "attacker", None)
        if attacker is None:
            return False
        return any(sub.lower() == "ex" for sub in subtypes_for(attacker.archetype_id))
    return PredicatePreventionPassive(lambda calc, c: is_ex(calc))


def _t66_prevent_effects_from_gx_ex(m, ability):
    from ptcgo.game.card_effects.passives_common import (
        PredicatePreventionPassive)
    from ptcgo.game.data_utils import subtypes_for

    def is_gx_or_ex(calc) -> bool:
        attacker = getattr(calc, "attacker", None)
        if attacker is None:
            return False
        subtypes = [sub.lower() for sub in subtypes_for(attacker.archetype_id)]
        return "gx" in subtypes or "ex" in subtypes
    return PredicatePreventionPassive(lambda calc, c: is_gx_or_ex(calc))


def _t68_bonus_per_self_counters_then_heal(m, ability):
    base, per, heal = int(m.group(1)), int(m.group(2)), int(m.group(3))

    async def effect(ctx):
        attacker = ctx.attacker
        counters = 0
        if attacker is not None:
            counters = (ctx.max_hp(attacker)
                        - attacker.get_attribute(AttrID.HP, 0)) // 10
        await ctx.deal_damage(base + per * counters)
        if attacker is not None and heal:
            await ctx.heal(heal, attacker)
    return effect


def _t68_optional_typed_all_base_swap(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value
    changed = int(m.group(2))

    async def effect(ctx):
        attacker = ctx.attacker
        pool = []
        if attacker is not None:
            pool = [energy for energy in ctx.attached_energies(attacker)
                    if energy_provides_type(energy, type_value)]
        if pool and await ctx.ask_yes_no(prompt="Discard that Energy?"):
            await ctx.discard_cards(pool)
            await ctx.deal_damage(changed)
            return
        await ctx.deal_damage()
    return effect


def _t68_optional_discard_hand_bonus(m, ability):
    limit = _count(m.group(1))
    per = int(m.group(2))

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        pool = list(ctx.hand())
        picks = []
        if pool:
            picks = await ctx.choose_cards(pool, limit, minimum=0, prompt=(
                f"Choose up to {limit} cards to discard"))
            if picks:
                await ctx.discard_cards(list(picks))
        await ctx.deal_damage(printed + per * len(picks))
    return effect


def _t68_scale_two_typed_energy_all_own(m, ability):
    per = int(m.group(1))
    first = TYPE_WORDS[m.group(2)].value
    second = TYPE_WORDS[m.group(3)].value

    def count(ctx) -> int:
        total = 0
        for pokemon in ctx.my_pokemon_in_play():
            for energy in ctx.attached_energies(pokemon):
                if energy_provides_type(energy, first) or \
                        energy_provides_type(energy, second):
                    total += 1
        return total
    return damage_per(count, per)


def _t68_damage_opponent_chosen_ignoring(m, ability):
    amount = int(m.group(1))
    targets = 1

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [pokemon for pokemon in ctx.opponent_pokemon_in_play()
                if not ctx.effects_blocked(pokemon)]
        if not pool:
            return
        picks = pool if len(pool) <= targets else await ctx.choose_cards(
            pool, targets, prompt=f"Choose {targets} Pokémon")
        for target in picks:
            await ctx.deal_damage(amount, target=target, ignore_weakness=True,
                                  ignore_resistance=True)
    return effect


def _t68_search_basic_energy_to_hand_many(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        picks = await ctx.search_deck(is_basic_energy_card, count=limit,
                                      minimum=0, prompt="Choose Energy cards")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=True)
        await ctx.shuffle_deck()
    return effect


def _t68_prevent_from_tag_team(m, ability):
    from ptcgo.game.card_effects.passives_common import (
        PredicatePreventionPassive)
    from ptcgo.game.data_utils import subtypes_for

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        if attacker is None:
            return

        def is_tag_team(calc) -> bool:
            source = getattr(calc, "attacker", None)
            if source is None:
                return False
            subtypes = [sub.lower() for sub in subtypes_for(source.archetype_id)]
            return "tag team" in subtypes or "tagteam" in subtypes
        ctx.add_passive_through_opponents_turn(
            attacker, PredicatePreventionPassive(lambda calc, c: is_tag_team(calc)))
    return effect


def _t68_bonus_bench_typed_ignoring(m, ability):
    per = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    async def effect(ctx):
        count = sum(1 for pokemon in ctx.my_bench()
                    if type_value in (pokemon.get_attribute(AttrID.POKEMON_TYPES)
                                      or []))
        await ctx.deal_damage(per * count, ignore_weakness=True)
    return effect


def _t68_bonus_bench_with_typed_energy(m, ability):
    per = int(m.group(1))
    type_value = TYPE_WORDS[m.group(2)].value

    def count(ctx) -> int:
        return sum(1 for pokemon in ctx.my_bench()
                   if any(energy_provides_type(energy, type_value)
                          for energy in ctx.attached_energies(pokemon)))
    return damage_per(count, per)


def _t68_attach_typed_hand_bench_heal_all(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_basic_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_bench()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, 1, prompt="Choose an Energy card")
        if not picks:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Benched Pokémon")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
            await ctx.heal(9990, target)
    return effect


def _t68_attach_typed_hand_any(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        pool = [card for card in ctx.hand() if is_basic_energy_card(card)
                and energy_provides_type(card, type_value)]
        candidates = ctx.my_pokemon_in_play()
        if not pool or not candidates:
            return
        picks = await ctx.choose_cards(pool, 1, prompt="Choose an Energy card")
        if not picks:
            return
        target = candidates[0] if len(candidates) == 1 else \
            await ctx.choose_pokemon(candidates, "Choose a Pokémon")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    return effect


def _t68_bench_own_name_from_discard(m, ability):
    limit = _count(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        source = ctx.source
        own = normalize(getattr(source, "display_name", "") or "")
        if not own:
            return
        pool = [card for card in ctx.discard_pile()
                if _is_pokemon_card(card)
                and normalize(getattr(card, "display_name", "") or "") == own]
        if not pool:
            return
        picks = await ctx.choose_cards(pool, limit, minimum=0, prompt=(
            f"Choose up to {limit} Pokémon"))
        for card in picks:
            await ctx.bench_pokemon(card)
    return effect


def _t69_spread_opponent_ex(m, ability):
    amount = int(m.group(1))

    async def effect(ctx):
        await ctx.deal_damage()
        from ptcgo.game.data_utils import subtypes_for
        for pokemon in ctx.opponent_pokemon_in_play():
            if ctx.effects_blocked(pokemon):
                continue
            subtypes = [sub.lower() for sub in subtypes_for(pokemon.archetype_id)]
            if "ex" in subtypes:
                await ctx.deal_damage(amount, target=pokemon,
                                      ignore_weakness=True,
                                      ignore_resistance=True)
    return effect


def _t69_attach_typed_from_discard_self(m, ability):
    type_value = TYPE_WORDS[m.group(1)].value

    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        pile = [card for card in ctx.discard_pile() if is_energy_card(card)
                and energy_provides_type(card, type_value)]
        if attacker is None or not pile:
            return
        picks = await ctx.choose_cards(pile, 1, prompt="Choose an Energy card")
        if picks:
            await ctx.attach_energy(picks[0], attacker)
    return effect


def _t69_search_self_name_to_hand(m, ability):
    async def effect(ctx):
        await ctx.deal_damage()
        own = normalize(getattr(ctx.source, "display_name", "") or "")
        if not own:
            return
        picks = await ctx.search_deck(
            lambda card: normalize(getattr(card, "display_name", "") or "") == own,
            count=1, minimum=0, prompt="Choose this Pokémon")
        if picks:
            await ctx.put_in_hand(list(picks), reveal=True)
        await ctx.shuffle_deck()
    return effect


def _t70_burn_counters_passive(m, ability):
    from ptcgo.game.card_effects.passives_common import BurnCountersPassive
    return BurnCountersPassive(int(m.group(1)))


def _scale_from_phrase(m, ability):
    phrase = m.group(2).strip()
    counter = COUNT_PHRASES.get(phrase)
    if counter is None:
        return None
    return _more(counter, ability, int(m.group(1)))


def _bonus_from_phrase(m, ability):
    phrase = m.group(1).strip()
    condition = CONDITION_PHRASES.get(phrase)
    if condition is None:
        return None
    return bonus_if(condition, _count(m.group(2)))


# ----------------------------------------------------------------------
# Pattern table: (name, compiled regex, builder). First full match wins.
# ----------------------------------------------------------------------

_PATTERNS: List[Tuple[str, "re.Pattern", Callable]] = [
    # -- coin flips ----------------------------------------------------
    ("flip.damage-times-heads",
     re.compile(r"flip (an?|\d+) coins?\. this attack does (\d+) damage "
                r"times the number of heads\."), _flip_damage_times_heads),
    ("flip.damage-per-heads",
     re.compile(r"flip (an?|\d+) coins?\. this attack does (\d+) damage "
                r"for each heads\."), _flip_damage_per_heads),
    ("flip.until-tails-times-heads",
     re.compile(r"flip a coin until you get tails\. this attack does (\d+) "
                r"damage (?:times the number of heads|for each heads)\."),
     _flip_until_tails_times),
    ("flip.until-tails-bonus-per-heads",
     re.compile(r"flip a coin until you get tails\. this attack does (\d+) "
                r"more damage (?:times the number of heads|for each heads)\."),
     _flip_until_tails_bonus),
    ("flip.bonus-per-heads",
     re.compile(r"flip (an?|\d+) coins?\. this attack does (\d+) more damage "
                r"for each heads\."), _flip_bonus_per_heads),
    ("flip.more-damage",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) more damage\."),
     _flip_heads_damage),
    ("flip.tails-nothing",
     re.compile(r"flip a coin\. if tails, this attack does nothing\."),
     _flip_tails_nothing),
    ("flip.any-tails-nothing",
     re.compile(r"flip (an?|\d+) coins?\. if either of them is tails, this "
                r"attack does nothing\."), _flip_all_heads_nothing),
    ("flip.damage-plus-bonus",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage plus "
                r"(\d+) more damage\."), _flip_plus_bonus),
    ("flip.damage-plus-bonus-else-damage",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage plus "
                r"(\d+) more damage; if tails, this attack does (\d+) damage\."),
     _flip_choice_damage),
    ("flip.base-plus-bonus-per-heads",
     re.compile(r"flip (an?|\d+) coins?\. this attack does (\d+) damage plus "
                r"(\d+) more damage for each heads\."),
     _flip_heads_plus_bonus_per_heads),

    # -- special conditions -------------------------------------------
    ("flip.defender-condition",
     re.compile(r"flip a coin\. if heads, (?:the defending|your opponent's "
                r"active) pokemon is now (" + _CONDITION_WORDS + r")\."),
     _flip_condition),
    ("defender-condition",
     re.compile(r"(?:the defending|your opponent's active) pokemon is now ("
                + _CONDITION_WORDS + r")\."), _condition),
    ("defender-two-conditions",
     re.compile(r"(?:the defending|your opponent's active) pokemon is now ("
                + _CONDITION_WORDS + r") and (" + _CONDITION_WORDS + r")\."),
     _two_conditions),
    ("self-condition",
     re.compile(r"this pokemon is now (" + _CONDITION_WORDS + r")\."),
     _self_condition),
    ("poison.counters",
     re.compile(r"your opponent's active pokemon is now poisoned\. put (\d+) "
                r"damage counters instead of 1 on that pokemon between turns\."),
     _poison_counters),

    # -- recoil / healing ---------------------------------------------
    ("self-damage",
     re.compile(r"this pokemon (?:also )?does (\d+) damage to itself\."),
     _recoil),
    ("flip.tails-self-damage",
     re.compile(r"flip a coin\. if tails, this pokemon does (\d+) damage to "
                r"itself\."), _flip_tails_recoil),
    ("heal.self",
     re.compile(r"heal (\d+) damage from this pokemon\."), _heal_self),
    ("heal.each-own-counters",
     re.compile(r"heal (\d+) damage from each of your pokemon\."),
     _heal_each_own_including_self),
    ("heal.choice",
     re.compile(r"heal (\d+) damage from (\d+) of your pokemon\."),
     _heal_choice),
    ("heal.dealt",
     re.compile(r"heal from this pokemon the same amount of damage you did to "
                r"your opponent's active pokemon\."), _heal_dealt),

    # -- draw / mill ---------------------------------------------------
    ("draw.one", re.compile(r"draw a card\."), _draw),
    ("draw.n", re.compile(r"draw (\d+) cards?\."), _draw),
    ("draw.until", re.compile(r"(?:you may )?draw cards until you have (\d+) "
                              r"cards in your hand\."), _draw_until),
    ("mill.opponent", re.compile(r"discard the top (?:(\d+) cards?|card) of "
                                 r"your opponent's deck\."), _mill_opponent),
    ("mill.own", re.compile(r"discard the top (?:(\d+) cards?|card) of your "
                            r"deck\."), _mill_own),

    # -- energy discard ------------------------------------------------
    ("discard.self-energy-all",
     re.compile(r"discard all energy (?:cards? )?(?:attached )?(?:from|to) "
                r"this pokemon\."), _self_energy_discard_all),
    ("discard.self-energy-type",
     re.compile(r"discard (an?|\d+) (" + _TYPE_WORDS + r") energy (?:cards? )?"
                r"(?:attached )?(?:from|to) this pokemon\."),
     _self_energy_discard_type),
    ("discard.self-energy",
     re.compile(r"discard (an?|\d+) energy (?:cards? )?(?:attached )?"
                r"(?:from|to) this pokemon\."), _self_energy_discard),
    ("discard.defender-special-energy-flip",
     re.compile(r"flip a coin\. if heads, discard (?:a|an) special energy "
                r"(?:card )?(?:attached to|from) (?:the defending|your "
                r"opponent's active) pokemon\."),
     _flip_defender_special_energy_discard),
    ("discard.defender-energy-flip",
     re.compile(r"flip a coin\. if heads, discard (an?|\d+) energy (?:cards? )?"
                r"(?:attached to|from) (?:the defending|your opponent's "
                r"active) pokemon\."), _flip_defender_energy_discard),
    ("discard.defender-special-energy",
     re.compile(r"discard (?:a|an) special energy (?:card )?(?:attached to|"
                r"from) (?:the defending|your opponent's active) pokemon\."),
     _defender_special_energy_discard),
    ("discard.defender-energy",
     re.compile(r"discard (an?|\d+) energy (?:cards? )?(?:attached to|from) "
                r"(?:the defending|your opponent's active) pokemon\."),
     _defender_energy_discard),

    # -- snipes and spreads --------------------------------------------
    ("snipe.any",
     re.compile(r"(?:this attack does|does) (\d+) damage to (an?|\d+) of your "
                r"opponent's pokemon" + _SNIPE_TAIL), _snipe),
    ("snipe.choose-any",
     re.compile(r"choose (an?|\d+) of your opponent's pokemon\. this attack does "
                r"(\d+) damage to that pokemon" + _SNIPE_TAIL),
     _snipe_choose),
    ("snipe.bench-also-base",
     re.compile(r"this attack also does (\d+) damage to (an?|\d+) of your "
                r"opponent's benched pokemon" + _SNIPE_TAIL),
     _snipe_bench_also_base),
    ("snipe.bench",
     re.compile(r"(?:this attack does|does) (\d+) damage to (an?|\d+) of your "
                r"opponent's benched pokemon" + _SNIPE_TAIL), _snipe_bench),
    ("spread.opponent-all",
     re.compile(r"this attack does (\d+) damage to each of your opponent's "
                r"pokemon" + _SNIPE_TAIL), _spread_opponent),
    ("spread.opponent-bench",
     re.compile(r"(?:this attack does|does) (\d+) damage to each of your "
                r"opponent's benched pokemon" + _BENCH_SPREAD_TAIL),
     _spread_opponent_bench),
    ("spread.own-bench",
     re.compile(r"(?:this attack does|does) (\d+) damage to each of your "
                r"benched pokemon" + _BENCH_SPREAD_TAIL), _spread_own_bench),
    ("spread.both-benches",
     re.compile(r"does (\d+) damage to each benched pokemon \(both yours and "
                r"your opponent's\)" + _BENCH_SPREAD_TAIL),
     _spread_both_benches),

    # -- locks ---------------------------------------------------------
    ("lock.self-next-turn-plain",
     re.compile(r"(?:during your next turn, this pokemon (?:can't attack|"
                r"can't use attacks)|this pokemon can't attack during your "
                r"next turn)\."), _lock_self),
    ("lock.defender-retreat",
     re.compile(r"(?:the defending pokemon can't retreat during your "
                r"opponent's next turn|during your opponent's next turn, the "
                r"defending pokemon can't retreat)\."), _no_retreat),
    ("lock.defender-attacks-flip",
     re.compile(r"flip a coin\. if heads, the defending pokemon can't attack "
                r"during your opponent's next turn\."), _flip_defender_lock),
    ("lock.smokescreen",
     re.compile(r"if the defending pokemon tries to attack during your "
                r"opponent's next turn, your opponent flips a coin\. if "
                r"tails, that attack does nothing\."), _smokescreen),

    # -- damage-pipeline modifiers -------------------------------------
    ("ignore.resistance",
     re.compile(r"this attack's damage isn't affected by resistance\."),
     _ignore_resistance),
    ("ignore.weakness-resistance",
     re.compile(r"this attack's damage isn't affected by weakness or "
                r"resistance\."), _ignore_weakness_and_resistance),
    ("ignore.target-effects",
     re.compile(r"this attack's damage isn't affected by any effects on your "
                r"opponent's active pokemon\."), _ignore_target_effects),
    ("ignore.all",
     re.compile(r"this attack's damage isn't affected by (?:weakness, "
                r"resistance, poke-powers, poke-bodies, or any other effects "
                r"on the defending pokemon|weakness or resistance, or by any "
                r"effects on your opponent's active pokemon)\."), _ignore_all),
    ("protect.reduce",
     re.compile(r"during your opponent's next turn, (?:this pokemon takes|any "
                r"damage done to this pokemon by attacks is reduced by) (\d+)"
                r"(?: less damage from attacks)? \(after applying weakness and "
                r"resistance\)\."), _take_less),
    ("protect.flip-damage",
     re.compile(r"flip a coin\. if heads, prevent all damage done to this "
                r"pokemon by attacks during your opponent's next turn\."),
     _flip_prevent),
    ("protect.flip-all",
     re.compile(r"flip a coin\. if heads, (?:prevent all effects of attacks, "
                r"including damage, done to this pokemon during your "
                r"opponent's next turn|during your opponent's next turn, "
                r"prevent all damage from and effects of attacks done to this "
                r"pokemon)\."), _flip_prevent_all),

    # -- scaling -------------------------------------------------------
    ("scale.type-energy-self",
     re.compile(r"this attack does (\d+) more damage for each (" + _TYPE_WORDS +
                r") energy attached to this pokemon\."),
     _more_per_energy_self_type),
    ("scale.energy-self",
     re.compile(r"this attack does (\d+) more damage for each energy attached "
                r"to this pokemon\."), _more_per_energy_self),
    ("scale.energy-defender",
     re.compile(r"this attack does (\d+) more damage for each energy attached "
                r"to your opponent's active pokemon\."),
     _more_per_energy_defender),
    ("scale.counter-self",
     re.compile(r"(?:this attack does|does) (\d+) more damage for each damage "
                r"counter on this pokemon\."), _more_per_counter_self),
    ("scale.counter-defender",
     re.compile(r"this attack does (\d+) more damage for each damage counter "
                r"on your opponent's active pokemon\."),
     _more_per_counter_defender),
    ("scale.bench",
     re.compile(r"this attack does (\d+) more damage for each of your "
                r"opponent's benched pokemon\."), _more_per_bench),
    ("scale.prizes-taken",
     re.compile(r"this attack does (\d+) more damage for each prize card your "
                r"opponent has taken\."), _more_per_prizes_taken),
    ("scale.damage-per-counter-self",
     re.compile(r"this attack does (\d+) damage for each damage counter on "
                r"this pokemon\."), _damage_per_counter_self),

    # -- conditional bonuses -------------------------------------------
    ("bonus.defender-has-damage",
     re.compile(r"if your opponent's active pokemon already has any damage "
                r"counters on it, this attack does (\d+) more damage\."),
     _bonus_defender_has_damage),
    ("bonus.self-has-damage",
     re.compile(r"if this pokemon has any damage counters on it, this attack "
                r"does (\d+) more damage\."), _bonus_self_has_damage),
    ("bonus.bench-has-damage",
     re.compile(r"if your benched pokemon have any damage counters on them, "
                r"this attack does (\d+) more damage\."),
     _bonus_own_bench_damaged),
    ("bonus.stadium",
     re.compile(r"if there is any stadium card in play, this attack does (\d+) "
                r"more damage\."), _bonus_stadium),
    ("bonus.defender-condition",
     re.compile(r"if your opponent's active pokemon is (" + _CONDITION_WORDS +
                r"), this attack does (\d+) more damage\."), _bonus_condition),
    ("bonus.defender-any-condition",
     re.compile(r"if your opponent's active pokemon is affected by a special "
                r"condition, this attack does (\d+) more damage\."),
     _bonus_any_condition),
    ("bonus.hand-equal",
     re.compile(r"if you have the same number of cards in your hand as your "
                r"opponent, this attack does (\d+) more damage\."),
     _bonus_hand_equal),
    ("bonus.own-energy-type",
     re.compile(r"if this pokemon has any (" + _TYPE_WORDS + r") energy "
                r"attached to it, this attack does (\d+) more damage\."),
     _bonus_own_energy),
    ("bonus.defender-is-ex",
     re.compile(r"if your opponent's active pokemon is a pokemon ex, this "
                r"attack does (\d+) more damage\."), _bonus_defender_is_ex),
    ("bonus.defender-is-ex-or-v",
     re.compile(r"if your opponent's active pokemon is a pokemon ex or pokemon "
                r"v, this attack does (\d+) more damage\."),
     _bonus_defender_is_ex_or_v),

    # -- switching / utility -------------------------------------------
    ("switch.self",
     re.compile(r"switch this pokemon with (an?|\d+) of your benched pokemon\."),
     _switch_self),
    ("switch.self-optional",
     re.compile(r"you may switch this pokemon with (an?|\d+) of your benched "
                r"pokemon\."), _switch_self_optional),
    ("switch.opponent-chooses",
     re.compile(r"(?:your opponent switches (?:the defending|their active) "
                r"pokemon with (an?|\d+) of (?:his or her|their) benched pokemon\.|"
                r"switch out your opponent's active pokemon to the bench\. "
                r"\(your opponent chooses the new active pokemon\.\))"),
     _gust_opponent_chooses),
    ("discard.random-opponent-hand",
     re.compile(r"discard (an?|\d+) random cards? from your opponent's hand\."),
     _discard_random_opponent),
    ("search.basic-to-bench",
     re.compile(r"search your deck for (?:a basic pokemon|up to (\d+) basic "
                r"pokemon) and put (?:it|them) onto your bench\. (?:then, )?"
                r"shuffle your deck(?: afterward)?\."), _search_basic_to_bench),
    ("counters.place-any",
     re.compile(r"put (\d+) damage counters on your opponent's pokemon in any "
                r"way you like\."), _place_counters_any),
    ("energy.move-to-bench",
     re.compile(r"move (an?|\d+) energy (?:card )?(?:attached )?from this "
                r"pokemon to (an?|\d+) of your benched pokemon\."),
     _energy_move),

    # -- deck search / evolution ---------------------------------------
    ("search.basic-energy-to-hand",
     re.compile(r"search your deck for up to (\d+) basic energy cards, reveal "
                r"them, and put them into your hand\. then, shuffle your "
                r"deck\."), _search_basic_energy_to_hand),
    ("search.pokemon-to-hand",
     re.compile(r"search your deck for up to (\d+) pokemon, reveal them, and "
                r"put them into your hand\. then, shuffle your deck\."),
     _search_pokemon_to_hand),
    ("search.any-to-hand",
     re.compile(r"(?:you may )?search your deck for up to (\d+) cards and put "
                r"them into your hand\. then, shuffle your deck\."),
     _search_any_to_hand),
    ("search.evolve-self",
     re.compile(r"search your deck for a card that evolves from this pokemon "
                r"and put it onto this pokemon to evolve it\. then, shuffle "
                r"your deck\."), _evolve_from_deck),
    ("attach.energy-from-discard",
     re.compile(r"attach (?:a|(\d+)) basic energy cards? from your discard "
                r"pile to (?:this pokemon|(?:a|\d+) of your benched pokemon)\."),
     _attach_energy_from_discard),

    # -- next-turn passives --------------------------------------------
    ("protect.no-weakness",
     re.compile(r"during your opponent's next turn, this pokemon has no "
                r"weakness\."), _no_weakness_next_turn),
    ("protect.no-resistance",
     re.compile(r"during your opponent's next turn, this pokemon has no "
                r"resistance\."), _no_resistance_next_turn),

    # -- damage shaping ------------------------------------------------
    ("scale.less-per-counter-self",
     re.compile(r"this attack does (\d+) less damage for each damage counter "
                r"on this pokemon\."), _less_per_counter_self),
    ("bonus.base-plus-per-counter-defender",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each damage "
                r"counter on the defending pokemon\."),
     _base_plus_per_counter_defender),
    ("bonus.base-plus-per-energy-defender",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each energy "
                r"cards? attached to the defending pokemon\."),
     _base_plus_per_energy_defender),
    ("scale.retreat-cost",
     re.compile(r"this attack does (\d+) (more damage|damage) for each "
                r"colorless in your opponent's active pokemon's retreat cost\."),
     _scale_retreat_cost),
    ("bonus.base-plus-if-evolved",
     re.compile(r"if the defending pokemon is an evolved pokemon, this attack "
                r"does (\d+) damage plus (\d+) more damage\."),
     _base_plus_if_defender_evolved),
    ("bonus.base-plus-if-ex",
     re.compile(r"if the defending pokemon is pokemon-ex, this attack does "
                r"(\d+) damage plus (\d+) more damage\."),
     _base_plus_if_defender_ex),

    # -- utility -------------------------------------------------------
    ("reveal.opponent-hand",
     re.compile(r"your opponent reveals their hand\."), _reveal_hand),
    ("discard.stadium",
     re.compile(r"discard a stadium in play\."), _discard_stadium),
    ("discard.stadium-bonus",
     re.compile(r"you may discard a stadium in play\. if you do, this attack "
                r"does (\d+) more damage\."), _discard_stadium_bonus),
    ("lock.defender-chosen-attack",
     re.compile(r"choose (?:1|a) of the defending pokemon's attacks\. that "
                r"pokemon can't use that attack during your opponent's next "
                r"turn\."), _lock_chosen_attack),

    # -- ability passives ----------------------------------------------
    ("ability.takes-less",
     re.compile(r"this pokemon takes (\d+) less damage from attacks \(after "
                r"applying weakness and resistance\)\."),
     _passive_takes_less),
    ("ability.flip-prevent-damage",
     re.compile(r"if any damage is done to this pokemon by attacks, flip a "
                r"coin\. if heads, prevent that damage\."),
     _passive_flip_prevent),

    # -- batch 3: energy costs, bench placement, conditions, self-locks ----
    ("scale.more-times-type-energy",
     re.compile(r"this attack does (\d+) more damage times the amount of ("
                + _TYPE_WORDS + r") energy attached to this pokemon\."),
     _more_times_type_energy),
    ("scale.damage-per-energy-self",
     re.compile(r"this attack does (\d+) damage for each energy attached to "
                r"this pokemon\."), _damage_per_energy_self),
    ("scale.damage-per-bench",
     re.compile(r"this attack does (\d+) damage for each of your opponent's "
                r"benched pokemon\."), _damage_per_bench_opponent),
    ("scale.both-benches",
     re.compile(r"this attack does (\d+) more damage for each benched pokemon "
                r"\(both yours and your opponent's\)\."),
     _more_per_both_benches),
    ("debuff.defender-attacks",
     re.compile(r"during your opponent's next turn, (?:any damage done by "
                r"attacks from the defending pokemon is reduced by|attacks "
                r"used by the defending pokemon do|the defending pokemon's "
                r"attacks do) (\d+) (?:less damage )?\(before applying "
                r"weakness and resistance\)\."), _debuff_defender_attacks),
    ("protect.from-basic",
     re.compile(r"during your opponent's next turn, prevent all damage done to "
                r"this pokemon by attacks from basic pokemon\."),
     _prevent_from_basic),
    ("snipe.choose-any-ignore-all",
     re.compile(r"choose (an?|\d+) of your opponent's pokemon\. this attack "
                r"does (\d+) damage to that pokemon\. this attack's damage "
                r"isn't affected by weakness, resistance, poke-powers, "
                r"poke-bodies, or any other effects on the defending "
                r"pokemon\."), _snipe_choose_ignore_all),
    ("snipe.choose-bench",
     re.compile(r"choose (an?|\d+) of your opponent's benched pokemon\. this "
                r"attack does (\d+) damage to that pokemon" + _SNIPE_TAIL),
     _snipe_bench_choose),
    ("snipe.bench-if-any",
     re.compile(r"if your opponent has any benched pokemon, choose (an?|\d+) "
                r"of them and this attack does (\d+) damage to it"
                + _SNIPE_TAIL), _bench_snipe_if_any),
    ("bonus.defender-evolved",
     re.compile(r"if your opponent's active pokemon is an evolution pokemon, "
                r"this attack does (\d+) more damage\."), _bonus_evolved),
    ("bonus.base-plus-if-damaged",
     re.compile(r"if the defending pokemon already has any damage counters on "
                r"it, this attack does (\d+) damage plus (\d+) more damage\."),
     _base_plus_if_defender_damaged),
    ("bonus.base-plus-per-energy-defender-short",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each energy "
                r"attached to the defending pokemon\."),
     _base_plus_per_energy_defender_short),
    ("scale.more-per-energy-defender-short",
     re.compile(r"does (\d+) more damage for each energy attached to the "
                r"defending pokemon\."), _more_per_energy_defender_short),
    ("spread.opponent-all-short",
     re.compile(r"does (\d+) damage to each of your opponent's pokemon"
                + _SNIPE_TAIL), _spread_opponent),
    ("ignore.all-short",
     re.compile(r"this attack's damage isn't affected by weakness, resistance, "
                r"or any other effects on your opponent's active pokemon\."),
     _ignore_all),
    ("discard.defender-tools",
     re.compile(r"before doing damage, discard all pokemon tools from your "
                r"opponent's active pokemon\."), _discard_defender_tools),
    ("optional.bonus-self-damage",
     re.compile(r"you may do (\d+) more damage\. if you do, this pokemon does "
                r"(\d+) damage to itself\."), _optional_bonus_self_damage),
    ("recover.from-discard",
     re.compile(r"put (an?|\d+) cards? from your discard pile into your "
                r"hand\."), _recover_from_discard),
    ("lock.defender-chosen-attack-active",
     re.compile(r"choose (an?|\d+) of your opponent's active pokemon's attacks"
                r"\. that pokemon can't use that attack during your opponent's "
                r"next turn\."), _lock_chosen_attack_opponent_active),
    ("search.pokemon-to-hand-one",
     re.compile(r"search your deck for a pokemon, reveal it, and put it into "
                r"your hand\. then, shuffle your deck\."), _search_one_pokemon),
    ("search.supporter-to-hand",
     re.compile(r"search your deck for a supporter card, reveal it, and put it "
                r"into your hand\. then, shuffle your deck\."), _search_supporter),
    ("shuffle-hand-draw",
     re.compile(r"shuffle your hand into your deck\. then, draw (\d+) "
                r"cards?\."), _shuffle_hand_draw),
    ("attach.search-energy-any",
     re.compile(r"search your deck for up to (\d+) basic energy cards and "
                r"attach them to your pokemon in any way you like\. then, "
                r"shuffle your deck\."), _search_energy_attach_any),
    ("reveal.opponent-hand-his-her",
     re.compile(r"your opponent reveals his or her hand\."), _reveal_hand),
    ("discard.random-hand-into-deck",
     re.compile(r"choose a random card from your opponent's hand\. your "
                r"opponent reveals that card and shuffles it into their "
                r"deck\."), _random_hand_card_into_deck),
    ("switch.opponent-chooses-his-her",
     re.compile(r"your opponent switches his or her active pokemon with (an?|"
                r"\d+) of his or her benched pokemon\."),
     _gust_opponent_chooses),

    # -- batch 4: wording variants of the same shapes --------------------
    ("scale.more-per-type-energy-short",
     re.compile(r"does (\d+) more damage for each (" + _TYPE_WORDS +
                r") energy attached to this pokemon\."),
     _more_per_type_energy_short),
    ("bonus.with-tool-attached",
     re.compile(r"if this pokemon has a pokemon tool card attached to it, this "
                r"attack does (\d+) more damage\."), _more_with_tool),
    ("spread.own-bench-also-base",
     re.compile(r"this attack also does (\d+) damage to each of your benched "
                r"pokemon" + _BENCH_SPREAD_TAIL), _spread_own_bench_also_base),
    ("protect.flip-damage-short",
     re.compile(r"flip a coin\. if heads, during your opponent's next turn, "
                r"prevent all damage done to this pokemon by attacks\."),
     _flip_prevent_damage_short),
    ("counters.place-opponent-bench",
     re.compile(r"put (\d+) damage counters on your opponent's benched pokemon "
                r"in any way you like\."), _counters_on_opponent_bench),
    ("lock.defender-retreat-long",
     re.compile(r"the defending pokemon can't retreat until the end of your "
                r"opponent's next turn\."), _no_retreat_next_turn_long),
    ("bonus.entered-active-this-turn",
     re.compile(r"if this pokemon (?:moved from your bench to the active spot|"
                r"was on the bench and became your active pokemon) this turn, "
                r"this attack does (\d+) more damage\."),
     _entered_active_bonus),
    ("scale.more-times-energy-defender",
     re.compile(r"this attack does (\d+) more damage times the amount of "
                r"energy attached to your opponent's active pokemon\."),
     _more_times_amount_energy_defender),
    ("scale.damage-per-prizes-taken",
     re.compile(r"this attack does (\d+) damage for each prize card you have "
                r"taken\."), _damage_per_prizes_self),
    ("scale.damage-per-energy-opponent",
     re.compile(r"this attack does (\d+) damage for each energy attached to "
                r"all of your opponent's pokemon\."),
     _damage_per_energy_opponent_all),
    ("poison.counters-defender",
     re.compile(r"the defending pokemon is now poisoned\. put (\d+) damage "
                r"counters instead of 1 on (?:the defending pokemon|that "
                r"pokemon) between turns\."), _poison_counters_on_defender),
    ("discard.any-stadium",
     re.compile(r"discard any stadium card in play\."), _discard_any_stadium),
    ("ignore.all-except-weakness",
     re.compile(r"this attack's damage isn't affected by resistance, "
                r"poke-powers, poke-bodies, or any other effects on the "
                r"defending pokemon\."), _ignore_all_except_weakness),
    ("ability.basic-no-retreat",
     re.compile(r"your basic pokemon in play have no retreat cost\."),
     _no_retreat_passive_team),

    # -- batch 5: remaining repeat wordings ------------------------------
    ("snipe.choose-any-ignore-two",
     re.compile(r"choose (an?|\d+) of your opponent's pokemon\. this attack "
                r"does (\d+) damage to that pokemon\. this attack's damage "
                r"isn't affected by (?:weakness and resistance|weakness, "
                r"resistance, or any other effects on the defending pokemon)\."),
     _snipe_choose_ignore_two),
    ("copy.defender-attack",
     re.compile(r"choose (an?|\d+) of your opponent's active pokemon's attacks "
                r"and use it as this attack\."), _copy_defender_attack),
    ("energy-discard-then-snipe",
     re.compile(r"discard (an?|\d+) energy from this pokemon\. this attack "
                r"does (\d+) damage to (an?|\d+) of your opponent's pokemon"
                + _SNIPE_TAIL), _energy_discard_then_snipe),
    ("heal.bench-choice",
     re.compile(r"heal (\d+) damage from (an?|\d+) of your benched pokemon\."),
     _heal_bench_choice),
    ("scale.both-actives-energy",
     re.compile(r"this attack does (\d+) more damage for each energy attached "
                r"to both active pokemon\."), _more_per_both_actives_energy),
    ("counters.place-active",
     re.compile(r"put (\d+) damage counters on your opponent's active "
                r"pokemon\."), _counters_active),
    ("flip.two-heads-bonus",
     re.compile(r"flip (\d+) coins\. if both of them are heads, this attack "
                r"does (\d+) more damage\."), _flip_two_heads_bonus),
    ("lock.defender-cannot-use-attacks",
     re.compile(r"during your opponent's next turn, the defending pokemon "
                r"can't use attacks\."), _lock_defender_attacks_plain),
    ("ignore.resistance-is-not",
     re.compile(r"this attack's damage is not affected by resistance\."),
     _ignore_resistance_is_not),
    ("defender-three-conditions",
     re.compile(r"your opponent's active pokemon is now (" + _CONDITION_WORDS +
                r"), (" + _CONDITION_WORDS + r"), and (" + _CONDITION_WORDS +
                r")\."), _three_conditions),
    ("switch.in-opponent-bench",
     re.compile(r"switch in (an?|\d+) of your opponent's benched pokemon to "
                r"the active spot\."), _switch_in_opponent_bench),
    ("lock.basic-defender-attacks",
     re.compile(r"if the defending pokemon is a basic pokemon, it can't attack "
                r"during your opponent's next turn\."), _lock_basic_defender),
    ("remove.self-to-hand",
     re.compile(r"put this pokemon and all (?:attached )?cards into your "
                r"hand\."), _return_self_to_hand),
    ("remove.self-to-deck",
     re.compile(r"you may shuffle this pokemon and all cards attached to it "
                r"into your deck\."), _shuffle_self_into_deck),
    ("bonus.stadium-then-discard-card",
     re.compile(r"if there is any stadium card in play, this attack does (\d+) "
                r"more damage\. then, discard that stadium card\."),
     _bonus_then_discard_stadium),
    ("ignore.weakness-resistance-plain",
     re.compile(r"don't apply weakness and resistance for this attack\."),
     _ignore_all_plain),
    ("mill.own-attach-energy",
     re.compile(r"discard the top (\d+) cards? of your deck\. if any of those "
                r"cards are energy cards, attach them to this pokemon\."),
     _discard_top_attach_energy),
    ("reveal.hand-per-trainer",
     re.compile(r"your opponent reveals their hand\. this attack does (\d+) "
                r"damage for each trainer card you find there\."),
     _reveal_hand_per_trainer),
    ("bonus.ko-last-turn",
     re.compile(r"if any of your pokemon were knocked out by damage from an "
                r"attack during (?:your opponent's|his or her) last turn, this "
                r"attack does (\d+) more damage\."), _bonus_kos_last_turn),
    ("bonus.healed-this-turn",
     re.compile(r"if this pokemon was healed during this turn, this attack does "
                r"(\d+) more damage\."), _bonus_healed_this_turn),

    # -- batch 6: generic phrase lookups (count + condition tails) --------
    ("scale.phrase", re.compile(r"(?:this attack does|does) (\d+) (?:more )?"
                                r"damage (?:times the amount of|for each) (.+)\."),
     _scale_from_phrase),
    ("bonus.phrase", re.compile(r"if (.+?), (?:this attack does|does) (\d+) "
                                r"(?:more |extra )?damage\."),
     _bonus_from_phrase),

    # -- batch 7: discard-for-damage composites --------------------------
    ("discard.all-for-damage",
     re.compile(r"discard all (?:basic )?(?:(?P<type>" + _TYPE_WORDS +
                r") )?energy from this pokemon\. this attack does (\d+) "
                r"(?:more )?damage for each card you discarded in this way\."),
     _discard_for_damage),
    ("discard.any-for-damage",
     re.compile(r"you may discard any (?:amount|number) of (?:(?P<type>"
                + _TYPE_WORDS + r") )?(?:basic )?energy from (?:this pokemon|"
                r"your pokemon|your benched pokemon)\. this attack does "
                r"(\d+) (?:more )?damage for each card you discarded in this "
                r"way\."), _discard_for_damage),
    ("discard.up-to-for-damage",
     re.compile(r"(?:you may )?discard up to (\d+) (?:(?P<type>"
                + _TYPE_WORDS + r") )?(?:basic )?(?:energy|energy cards?) from "
                r"(?:this pokemon|your pokemon|your benched pokemon|your hand)\."
                r" this attack does (\d+) (?:more )?damage for each card you "
                r"discarded in this way\."), _discard_for_damage),
    ("discard.hand-cards-for-damage",
     re.compile(r"discard any (?:amount|number) of (supporter cards|basic "
                r"energy cards|energy cards|cards) from your hand\. this "
                r"attack does (\d+) (?:more )?damage for each card you "
                r"discarded in this way\."), _discard_for_damage),
    ("discard.any-energy-among-for-damage",
     re.compile(r"discard any amount of (?:(?P<type>" + _TYPE_WORDS +
                r") )?(?:basic )?energy from among your pokemon,? and this "
                r"attack does (\d+) (?:more )?damage for each card you "
                r"discarded in this way\."), _discard_for_damage),
    ("bonus.counter-threshold",
     re.compile(r"if the defending pokemon already has (\d+) or more damage "
                r"counters on it, this attack does (\d+) more damage\."),
     _bonus_threshold_counters),
    ("bonus.extra-energy-attached",
     re.compile(r"if this pokemon has at least (\d+) extra (?:(?P<type>"
                + _TYPE_WORDS + r") )?energy attached(?: to it)?"
                r"(?: \(in addition to this attack's cost\))?, this attack "
                r"does (\d+) more damage\."),
     _bonus_extra_energy),
    ("bonus.prize-comparison",
     re.compile(r"if you have (more|fewer|the same number of) prize cards? "
                r"remaining than your opponent, this attack does (\d+) more "
                r"damage\."), _bonus_prize_comparison),
    # -- batch 8: remaining generic riders ---------------------------------
    ("copy.defender-attack-short",
     re.compile(r"choose (an?|\d+) of the defending pokemon's attacks and use "
                r"it as this attack\."), _copy_defender_attack),
    ("lock.defender-chosen-attack-short",
     re.compile(r"choose (an?|\d+) of the defending pokemon's attacks\. that "
                r"pokemon can't use that attack during your opponent's next "
                r"turn\."), _lock_chosen_attack_opponent_active),
    ("snipe.choose-any-ignore-effects",
     re.compile(r"choose (an?|\d+) of your opponent's pokemon\. this attack "
                r"does (\d+) damage to that pokemon\. this attack's damage "
                r"isn't affected by any effects on the defending pokemon\."),
     _snipe_choose_ignore_two),
    ("switch.opponent-chooses-annotated",
     re.compile(r"(?:if your opponent has any benched pokemon, he or she "
                r"chooses (?:an?|\d+) of them and switches it with the defending "
                r"pokemon|your opponent switches the defending pokemon with "
                r"(?:an?|\d+) of his or her benched pokemon, if any)\."
                r"(?: \(do the damage before switching the pokemon\.\))?"),
     _gust_opponent_chooses),
    ("switch.defender-with-opponent-bench",
     re.compile(r"switch the defending pokemon with (an?|\d+) of your "
                r"opponent's benched pokemon\."), _switch_in_opponent_bench),
    ("gust.damage-new-active",
     re.compile(r"switch in (an?|\d+) of your opponent's benched pokemon to the "
                r"active spot\. this attack does (\d+) damage to the new "
                r"active pokemon\."), _gust_damage_new_active),
    ("discard.peek-opponent-hand",
     re.compile(r"choose (an?|\d+) cards? from your opponent's hand without "
                r"looking\. look at the card you chose, then have your opponent "
                r"shuffle that card into (?:his or her|their) deck\."),
     _peek_opponent_hand_card),
    ("flip.bonus-else-self-damage",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) more damage\. "
                r"if tails, this pokemon does (\d+) damage to itself\."),
     _flip_bonus_or_self_damage),
    ("ignore.defending-effects",
     re.compile(r"this attack's damage isn't affected by any effects on the "
                r"defending pokemon\."), _ignore_target_effects),
    ("discard.stadium-optional",
     re.compile(r"you may discard any stadium card in play\."),
     _discard_stadium_optional),
    ("attach.discard-distributed",
     re.compile(r"attach up to (\d+) basic (?:(?P<type>" + _TYPE_WORDS +
                r") )?energy cards? from your discard pile to your benched "
                r"pokemon in any way you like\."),
     _attach_from_discard_distributed),
    ("discard.defender-chosen-energy",
     re.compile(r"if the defending pokemon has any energy cards attached to it, "
                r"choose (an?|\d+) of them and discard it(?: or them)?\."),
     _defender_energy_discard),
    ("flip.draw-one",
     re.compile(r"flip a coin\. if heads, draw a card\."), _flip_draw_one),
    ("heal.dealt-defending",
     re.compile(r"heal from this pokemon the same amount of damage you did to "
                r"the defending pokemon\."), _heal_dealt),
    ("heal.each-bench",
     re.compile(r"heal (\d+) damage from each of your benched pokemon\."),
     _heal_each_bench),
    ("attach.discard-to-self",
     re.compile(r"attach (an?|\d+) energy cards? from your discard pile to "
                r"this pokemon\."), _attach_energy_from_discard),
    ("counters.chosen-target",
     re.compile(r"put (\d+) damage counters? on (an?|\d+) of your opponent's "
                r"pokemon\."), _counters_on_chosen),
    ("spread.over-chosen",
     re.compile(r"choose (an?|\d+) of your opponent's pokemon\. this attack "
                r"does (\d+) damage to each of them" + _SNIPE_TAIL),
     _spread_over_chosen),
    ("spread.opponent-bench-damaged",
     re.compile(r"(?:this attack )?does (\d+) damage to each of your "
                r"opponent's benched pokemon that has any damage counters on it"
                + _SNIPE_TAIL),
     _spread_opponent_bench_damaged),
    ("heal.all-self",
     re.compile(r"heal all damage from this pokemon\."), _heal_all_self),
    ("cure.all-conditions-self",
     re.compile(r"this pokemon recovers from all special conditions\."),
     _cure_self_conditions),
    ("snipe.own-bench",
     re.compile(r"this attack does (\d+) damage to (an?|\d+) of your benched "
                r"pokemon" + _SNIPE_TAIL), _snipe_own_bench),
    ("scale.united-wings",
     re.compile(r"this attack does (\d+) damage for each pokemon in your "
                r"discard pile that has the united wings attack\."),
     _scale_united_wings),
    ("scale.round-attack",
     re.compile(r"does (\d+) damage times the number of your pokemon that "
                r"have the round attack\."), _scale_round_attack),
    ("shuffle-hand-draw-opponent-size",
     re.compile(r"shuffle your hand into your deck\. then, draw a number of "
                r"cards equal to the number of cards in your opponent's "
                r"hand\."), _shuffle_hand_draw_opponent_size),
    ("lock.this-attack-next-turn",
     re.compile(r"this pokemon can't use (.+) during your next turn\."),
     _lock_this_attack),

    # -- batch 9: remaining repeat wordings --------------------------------
    ("snipe.choose-any-ignore-that",
     re.compile(r"choose (an?|\d+) of your opponent's pokemon\. this attack "
                r"does (\d+) damage to that pokemon\. this attack's damage "
                r"isn't affected by weakness, resistance, poke-powers, "
                r"poke-bodies, or any other effects on that pokemon\."),
     _snipe_choose_ignore_all),
    ("ignore.dont-apply-both",
     re.compile(r"don't apply weakness and resistance for this attack\.(?: "
                r"\(any other effects that would happen after applying "
                r"weakness and resistance are still applied\.\))?"),
     _ignore_all_plain),
    ("ignore.dont-apply-resistance",
     re.compile(r"don't apply resistance\."), _ignore_resistance_is_not),
    ("spread.opponent-bench-also-base",
     re.compile(r"this attack also does (\d+) damage to each of your "
                r"opponent's benched pokemon" + _BENCH_SPREAD_TAIL),
     _spread_opponent_bench_also_base),
    ("mill.by-heads",
     re.compile(r"flip a coin until you get tails\. for each heads, discard "
                r"the top card of your opponent's deck\."), _mill_by_heads),
    ("discard.peek-opponent-hand-discard",
     re.compile(r"choose (an?|\d+) cards? from your opponent's hand without "
                r"looking and discard it\."), _peek_opponent_hand_discard),
    ("flip.heads-tails-conditions",
     re.compile(r"flip a coin\. if heads, the defending pokemon is now (" +
                _CONDITION_WORDS + r")\. if tails, the defending pokemon is now ("
                + _CONDITION_WORDS + r")\."), _flip_two_conditions),
    ("scale.round-in-play",
     re.compile(r"this attack does (\d+) damage for each of your pokemon in "
                r"play that has the round attack\."), _damage_per_round_in_play),
    ("lock.opponent-items",
     re.compile(r"during your opponent's next turn, they can't play any item "
                r"cards from their hand\."), _lock_opponent_items),
    ("bonus.extra-prize-on-ko",
     re.compile(r"if your opponent's pokemon is knocked out by damage from "
                r"this attack, take (\d+) more prize card(?:s)?\."),
     _extra_prize_on_ko),
    ("snipe.bench-damaged-also-base",
     re.compile(r"this attack also does (\d+) damage to (an?|\d+) of your "
                r"opponent's benched pokemon that has any damage counters on it"
                + _SNIPE_TAIL), _snipe_bench_damaged_also_base),
    ("discard.any-opponent-energy",
     re.compile(r"discard (an?|\d+) energy from your opponent's pokemon\."),
     _discard_any_opponent_energy),
    ("protect.from-basic-noncolorless",
     re.compile(r"during your opponent's next turn, prevent all damage done to "
                r"this pokemon by attacks from basic non-colorless pokemon\."),
     _prevent_from_basic_noncolorless),

    # -- batch 10: last of the repeated wordings ---------------------------
    ("ignore.dont-apply-annotated",
     re.compile(r"don't apply weakness and resistance for this attack\. "
                r"\(any other effects[^)]*\)"), _ignore_all_plain),
    ("lock.defender-chosen-attack-worded",
     re.compile(r"choose (an?|\d+) of your opponent's active pokemon's "
                r"attacks\. during your opponent's next turn, that pokemon "
                r"can't use that attack\."),
     _lock_chosen_attack_opponent_active),
    ("lock.self-flip-tails",
     re.compile(r"flip a coin\. if tails, during your next turn, this pokemon "
                r"can't attack\."), _flip_tails_self_lock),
    ("switch.self-then-opponent",
     re.compile(r"switch this pokemon with (an?|\d+) of your benched pokemon\."
                r" if you do, switch out your opponent's active pokemon to the "
                r"bench\. \(your opponent chooses the new active pokemon\.\)"),
     _switch_both_actives),
    ("attach.discard-plain",
     re.compile(r"attach up to (\d+) basic energy cards from your discard pile "
                r"to (?:an?|\d+) of your benched pokemon\."),
     _attach_discard_plain),
    ("search.energy-attach-self-old",
     re.compile(r"search your deck for (?:an? )?basic (?:(?P<type>"
                + _TYPE_WORDS + r") )?energy card,? and attach it to this "
                r"pokemon\. (?:then, )?shuffle your deck(?: afterward)?\."),
     _search_energy_attach_self),
    ("search.energy-attach-self-typed",
     re.compile(r"search your deck for (?:an? )?(?P<type>" + _TYPE_WORDS +
                r") energy card and attach it to this pokemon\. (?:then, )?"
                r"shuffle your deck(?: afterward)?\."),
     _search_energy_attach_self),
    ("flip.random-discard",
     re.compile(r"flip a coin\. if heads, discard a random card from your "
                r"opponent's hand\."), _flip_random_discard),
    ("search.basic-energy-show",
     re.compile(r"search your deck for a basic energy card, show it to your "
                r"opponent, and put it into your hand\. shuffle your deck "
                r"afterward\."), _search_basic_energy_show),
    ("search.item-to-hand",
     re.compile(r"search your deck for an item card, reveal it, and put it into "
                r"your hand\. then, shuffle your deck\."), _search_item_to_hand),
    ("search.any-card-old",
     re.compile(r"search your deck for a card and put it into your hand\. "
                r"shuffle your deck afterward\."), _search_any_card_old),
    ("search.basic-to-bench-old",
     re.compile(r"search your deck for (\d+) basic pokemon and put them onto "
                r"your bench\. shuffle your deck afterward\."),
     _search_basic_to_bench),
    ("heal.remove-counter-each",
     re.compile(r"remove (\d+) damage counters? from each of your pokemon\."),
     _remove_counter_each_own),
    ("condition.both-actives",
     re.compile(r"both active pokemon are now (" + _CONDITION_WORDS + r")\."),
     _both_actives_condition),
    ("flip.confused-and-poisoned",
     re.compile(r"flip a coin\. if heads, the defending pokemon is now confused "
                r"and poisoned\."), _flip_confused_poisoned),
    ("spread.own-bench-plain",
     re.compile(r"does (\d+) damage to each of your own benched pokemon"
                + _BENCH_SPREAD_TAIL), _spread_own_bench_plain),
    ("switch.opponent-bench-to-active",
     re.compile(r"switch (an?|\d+) of your opponent's benched pokemon with "
                r"their active pokemon\."), _switch_in_opponent_bench),
    ("discard.opponent-hand",
     re.compile(r"your opponent discards (an?|\d+) cards? from their hand\."),
     _opponent_discards),
    ("discard.hand-draw-n",
     re.compile(r"discard your hand and draw (\d+) cards\."),
     _discard_hand_draw_n),

    # -- batch 11: the four high-traffic shapes, remaining wordings --------
    ("lock.defender-cannot-attack",
     re.compile(r"the defending pokemon can't attack during your opponent's "
                r"next turn\."), _lock_defender_attacks_plain),
    ("lock.defender-flip-attack-retreat",
     re.compile(r"flip a coin\. if heads, the defending pokemon can't attack "
                r"or retreat during your opponent's next turn\."),
     _lock_defender_attacks_and_retreat),
    ("flip.spread-opponent-bench",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage to "
                r"each of your opponent's benched pokemon"
                + _BENCH_SPREAD_TAIL), _flip_spread_bench),
    ("discard.all-energy-optional-bonus",
     re.compile(r"you may discard all energy from this pokemon\. if you do, "
                r"this attack does (\d+) more damage\."),
     _optional_all_energy_bonus),
    ("discard.self-energy-flip-typed",
     re.compile(r"flip a coin\. if tails, discard a(?:n)? (?:(?P<type>"
                + _TYPE_WORDS + r") )?energy (?:card )?attached to this "
                r"pokemon\."), _flip_self_energy_discard),
    ("energy.move-basic-to-bench",
     re.compile(r"move a basic energy from this pokemon to (an?|\d+) of your "
                r"benched pokemon\."), _move_basic_energy),
    ("self-condition-then-heal",
     re.compile(r"this pokemon is now (" + _CONDITION_WORDS + r")\. heal "
                r"(\d+) damage from it\."), _self_condition_then_heal),
    ("flip.bonus-else-condition",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) more "
                r"damage\. if tails, (?:your opponent's active|the defending) "
                r"pokemon is now (" + _CONDITION_WORDS + r")\."),
     _flip_bonus_else_condition),
    ("flip.paralyze-else-nothing",
     re.compile(r"flip a coin\. if tails, this attack does nothing\. if "
                r"heads, (?:the defending|your opponent's active) pokemon is "
                r"now (" + _CONDITION_WORDS + r")\."),
     _flip_paralyze_else_nothing),
    ("snipe.damaged-only",
     re.compile(r"choose (an?|\d+) of your opponent's pokemon that has any "
                r"damage counters on it\. this attack does (\d+) damage to "
                r"that pokemon" + _SNIPE_TAIL), _snipe_damaged_only),
    ("condition.then-no-retreat",
     re.compile(r"your opponent's active pokemon is now (" + _CONDITION_WORDS +
                r")\. during your opponent's next turn, that pokemon can't "
                r"retreat\."), _condition_then_no_retreat),
    ("heal.all-bench-choice",
     re.compile(r"heal all damage from (an?|\d+) of your benched pokemon\."),
     _heal_all_bench_choice),

    # -- batch 12: condition wordings and their flips ----------------------
    ("poison.checkup-counters",
     re.compile(r"your opponent's active pokemon is now poisoned\. during "
                r"pokemon checkup, (?:put|place) (\d+) damage counters on that "
                r"pokemon instead of 1\."), _checkup_poison_counters),
    ("defender-two-conditions-flip",
     re.compile(r"flip a coin\. if heads, (?:the defending|your opponent's "
                r"active) pokemon is now (" + _CONDITION_WORDS + r") and ("
                + _CONDITION_WORDS + r")\."), _flip_two_target_conditions),
    ("flip.bonus-and-condition",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage plus "
                r"(\d+) more damage and (?:the defending|your opponent's "
                r"active) pokemon is now (" + _CONDITION_WORDS + r")\."),
     _flip_bonus_and_condition),
    ("energy-cost-then-condition",
     re.compile(r"discard (an?|\d+) (?:" + _TYPE_WORDS + r")? ?energy "
                r"(?:card )?attached to this pokemon\. (?:the defending|your "
                r"opponent's active) pokemon is now (" + _CONDITION_WORDS +
                r")\."), _energy_cost_then_condition),
    ("flip.damage-then-self-condition",
     re.compile(r"flip coins?\. this attack does (\d+) damage times the "
                r"number of heads\. this pokemon is now confused\."),
     _flip_damage_then_self_condition),

    # -- batch 13: utility riders from the tail ----------------------------
    ("energy.attached-to-hand",
     re.compile(r"put (an?|\d+) energy attached to this pokemon into your "
                r"hand\."), _energy_to_hand),
    ("boost.own-next-turn-titled",
     re.compile(r"during your next turn, this pokemon's (.+) attack does "
                r"(\d+) more damage(?: \(before applying weakness and "
                r"resistance\))?\."), _own_next_turn_title_boost),
    ("discard.each-opponent-energy",
     re.compile(r"discard (an?|\d+) energy from each of your opponent's "
                r"pokemon\."), _discard_energy_each_opponent),
    ("switch.opponent-optional",
     re.compile(r"you may have your opponent switch his or her active pokemon "
                r"with (?:an?|\d+) of his or her benched pokemon\."),
     _optional_gust_opponent),
    ("heal.counter-from-chosen",
     re.compile(r"remove (\d+) damage counters? from (?:an?|\d+) of your "
                r"pokemon\."), _heal_counter_from_chosen),
    ("reorder.either-deck-top",
     re.compile(r"look at the top (\d+) cards of either player's deck and put "
                r"them back on top of that player's deck in any order\."),
     _reorder_either_deck),
    ("energy.move-opponent-to-bench",
     re.compile(r"you may move an energy from your opponent's active pokemon to "
                r"(?:an?|\d+) of their benched pokemon\."),
     _move_opponent_energy_to_bench),
    ("counters.move-bench-to-defender",
     re.compile(r"move all damage counters from (?:an?|\d+) of your benched "
                r"pokemon to your opponent's active pokemon\."),
     _move_counters_to_opponent),
    ("protect.from-evolution",
     re.compile(r"during your opponent's next turn, prevent all damage done to "
                r"this pokemon by attacks from evolution pokemon\."),
     _prevent_from_evolution),
    ("attach.hand-energy-distributed",
     re.compile(r"you may attach any number of basic energy cards from your hand "
                r"to your pokemon in any way you like\."),
     _attach_hand_energy_distributed),
    ("attach.hand-energy-one",
     re.compile(r"attach (?:an?|\d+) energy card from your hand to (?:an?|\d+) "
                r"of your pokemon\."), _attach_hand_energy_one),
    ("search.energy-attach-one-target",
     re.compile(r"search your deck for up to (\d+) (?:(?P<type>"
                + _TYPE_WORDS + r") )?energy cards and attach them to (?:an?|"
                r"\d+) of your pokemon\. then, shuffle your deck\."),
     _search_energy_attach_one_target),
    ("protect.all-effects-no-flip",
     re.compile(r"prevent all effects of attacks, including damage, done to "
                r"this pokemon during your opponent's next turn\."),
     _prevent_all_no_flip),
    ("heal.block-defender",
     re.compile(r"the defending pokemon can't be healed during your opponent's "
                r"next turn\."), _heal_block_defender),
    ("search.stadium-to-hand",
     re.compile(r"search your deck for a stadium card, reveal it, and put it "
                r"into your hand\. then, shuffle your deck\."),
     _search_stadium_to_hand),
    ("extra-turn",
     re.compile(r"take another turn after this one\. \(skip the "
                r"between-turns step\.\)"), _take_extra_turn),
    ("energy.move-bench-to-self-batch59",
     re.compile(r"move any number of energy from your benched pokemon to this "
                r"pokemon\."), _move_bench_energy_to_self),
    ("attack.usable-first-turn",
     re.compile(r"if you go first, you can use this attack on your first "
                r"turn\."), _usable_first_turn),
    ("snipe.multi-ignore-all",
     re.compile(r"this attack does (\d+) damage to (an?|\d+) of your "
                r"opponent's pokemon\. this attack's damage isn't affected by "
                r"weakness or resistance, or by any effects on those "
                r"pokemon\."), _snipe_multi_ignore_all),
    ("remove.self-to-hand-short",
     re.compile(r"return this pokemon and all cards attached to it to your "
                r"hand\."), _return_self_to_hand),
    ("recover.any-one-card",
     re.compile(r"put any (an?|\d+) cards? from your discard pile into your "
                r"hand\."), _recover_from_discard),

    # -- batch 14: fills the gaps the tail still shows ---------------------
    ("snipe.ignore-weakness-or-resistance",
     re.compile(r"choose (an?|\d+) of your opponent's pokemon\. this attack "
                r"does (\d+) damage to that pokemon\. this attack's damage "
                r"isn't affected by weakness or resistance\."),
     _snipe_ignore_weakness_or_resistance),
    ("ignore.pokemon-powers",
     re.compile(r"this attack's damage isn't affected by weakness, resistance, "
                r"pokemon powers, or any other effects on the defending "
                r"pokemon\."), _ignore_all),
    ("discard.stadium-any-optional",
     re.compile(r"you may discard (?:a |any )?stadium(?: card)? in play\."),
     _discard_stadium_optional),
    ("flip.tails-nothing-heads-shield",
     re.compile(r"flip a coin\. if tails, this attack does nothing\. if "
                r"heads, prevent all effects of attacks, including damage, "
                r"done to this pokemon during your opponent's next turn\."),
     _flip_tails_nothing_heads_shield),
    ("discard.all-defender-energy",
     re.compile(r"discard all energy (?:cards? )?(?:attached )?from your "
                r"opponent's active pokemon\."), _discard_all_defender_energy),
    ("ko.defender-self-damage",
     re.compile(r"knock out your opponent's active pokemon\. if your "
                r"opponent's active pokemon is knocked out in this way, this "
                r"pokemon does (\d+) damage to itself\."),
     _ko_defender_self_damage),
    ("energy.shuffle-opponent-into-deck",
     re.compile(r"shuffle all energy from each of your opponent's pokemon into "
                r"their deck\."), _shuffle_opponent_energy_into_deck),
    ("flip.tails-named-self-damage",
     re.compile(r"flip a coin\. if tails, \w+ does (\d+) damage to itself\."),
     _flip_tails_named_self_damage),
    ("recover.item-card",
     re.compile(r"put an item card from your discard pile into your hand\."),
     _recover_item),
    ("lock.smokescreen-worded",
     re.compile(r"during your opponent's next turn, if the defending pokemon "
                r"tries to attack, your opponent flips a coin\. if tails, that "
                r"attack doesn't happen\."), _smokescreen_worded),
    ("lock.opponent-items-their-turn",
     re.compile(r"your opponent can't play any item cards from their hand "
                r"during their next turn\."), _lock_opponent_items_v2),
    ("discard.peek-opponent-hand-that-card",
     re.compile(r"choose (an?|\d+) card from your opponent's hand without "
                r"looking\. look at that card you chose, then have your "
                r"opponent shuffle that card into his or her deck\."),
     _peek_opponent_hand_card),

    # -- batch 15: final wording fills -------------------------------------
    ("ignore.defending-effects-long",
     re.compile(r"this attack's damage isn't affected by weakness, resistance, "
                r"or any other effects on the defending pokemon\."),
     _ignore_all),
    ("condition.gate-not-present",
     re.compile(r"if the defending pokemon is not (" + _CONDITION_WORDS +
                r"), this attack does nothing\."), _condition_gate),
    ("condition.both-this-and-defender",
     re.compile(r"both this pokemon and the defending pokemon are now (" +
                _CONDITION_WORDS + r")\."), _both_this_and_defender),
    ("discard.all-defender-energy-two-heads",
     re.compile(r"flip (\d+) coins\. if both of them are heads, discard all "
                r"energy attached to the defending pokemon\."),
     _flip_two_heads_discard_all),
    ("energy.move-own-around",
     re.compile(r"move as many (?:(?P<type>" + _TYPE_WORDS + r") )?energy "
                r"attached to your pokemon to your other pokemon in any way you "
                r"like\."), _move_own_energy_around),
    ("search.energy-attach-one-any",
     re.compile(r"search your deck for (?:an? )?(?:(?P<type>" + _TYPE_WORDS +
                r") )?energy card and attach it to (?:an?|\d+) of your "
                r"pokemon\. shuffle your deck afterward\."),
     _search_energy_attach_any_old),
    ("protect.prevent-incoming",
     re.compile(r"during your opponent's next turn, if this pokemon would be "
                r"damaged by an attack, prevent that attack's damage done to "
                r"this pokemon\."), _prevent_incoming_next_turn),
    ("search.energy-attach-self-count",
     re.compile(r"search your deck for up to (\d+) (?:(?P<type>"
                + _TYPE_WORDS + r") )?energy cards and attach them to this "
                r"pokemon\. then, shuffle your deck\."),
     _search_energy_attach_self_two),
    ("search.supporter-show",
     re.compile(r"search your deck for a supporter card, show it to your "
                r"opponent, and put it into your hand\. shuffle your deck "
                r"afterward\."), _search_supporter_show),
    ("discard.random-hand-into-deck-his-her",
     re.compile(r"choose a random card from your opponent's hand\. your "
                r"opponent reveals that card and shuffles it into his or her "
                r"deck\."), _random_hand_card_into_deck),

    # -- batch 16: reordered locks, hand reveals, pile movement ------------
    ("lock.this-attack-next-turn-reversed",
     re.compile(r"during your next turn, this pokemon can't use (.+?)\."),
     _lock_this_attack_reversed),
    ("reveal.opponent-hand-plain",
     re.compile(r"look at your opponent's hand\."), _reveal_hand),
    ("search.energy-show-any",
     re.compile(r"search your deck for an energy card, show it to your "
                r"opponent, and put it into your hand\. shuffle your deck "
                r"afterward\."), _search_energy_show_any),
    ("energy.move-between-opponents",
     re.compile(r"move an energy card attached to the defending pokemon to "
                r"another of your opponent's pokemon\."),
     _move_energy_between_opponents),
    ("flip.until-tails-draw",
     re.compile(r"flip a coin until you get tails\. for each heads, draw a "
                r"card\."), _flip_until_tails_draw),
    ("discard.defender-trainers",
     re.compile(r"before doing damage, discard all trainer cards attached to "
                r"the defending pokemon\."), _discard_defender_trainers),
    ("counters.move-between-opponents",
     re.compile(r"move as many damage counters on your opponent's pokemon as "
                r"you like to any of your opponent's other pokemon in any way "
                r"you like\."), _move_opponent_counters),
    ("search.energy-each-bench",
     re.compile(r"for each of your benched pokemon, search your deck for a "
                r"basic (?:(?P<type>" + _TYPE_WORDS + r") )?energy card and "
                r"attach it to that pokemon\. then, shuffle your deck\."),
     _search_energy_each_bench),
    ("copy.own-bench-attack",
     re.compile(r"choose (an?|\d+) of your benched (.+?)'s attacks and use it "
                r"as this attack\."), _copy_own_bench_attack),
    ("flip.condition-and-discard-energy",
     re.compile(r"flip a coin\. if heads, (?:the defending|your opponent's "
                r"active) pokemon is now (" + _CONDITION_WORDS + r") and "
                r"discard an energy (?:card )?attached to the defending "
                r"pokemon\."), _flip_condition_and_discard),
    ("search.energy-attach-distributed",
     re.compile(r"search your deck for up to (\d+) energy cards and attach "
                r"them to your pokemon in any way you like\. then, shuffle "
                r"your deck\."), _search_energy_attach_distributed),
    ("attach.hand-energy-capped-typed",
     re.compile(r"you may attach up to (\d+) (?:(?P<type>" + _TYPE_WORDS +
                r") )?energy cards from your hand to your pokemon in any way "
                r"you like\."), _attach_hand_energy_capped),
    ("lock.smokescreen-use-attack",
     re.compile(r"during your opponent's next turn, if the defending pokemon "
                r"tries to use an attack, your opponent flips a coin\. if "
                r"tails, that attack doesn't happen\."),
     _smokescreen_use_attack),

    # -- batch 17: typed switching, typed Energy costs, condition knock-outs
    ("switch.self-typed-bench",
     re.compile(r"switch this pokemon with (?:an?|\d+) of your benched ("
                r"(?P<type>" + _TYPE_WORDS + r") )pokemon\."),
     _switch_self_typed),
    ("scale.ultra-beast",
     re.compile(r"this attack does (\d+) (?:more )?damage for each of your "
                r"ultra beasts in play\."), _ultra_beast_count),
    ("heal.all-own-pokemon",
     re.compile(r"heal all damage from all of your pokemon\."), _heal_all_own),
    ("attach.discard-typed-self",
     re.compile(r"attach (\d+) (?:(?P<type>" + _TYPE_WORDS + r") )?energy "
                r"cards from your discard pile to this pokemon\."),
     _attach_discard_typed_self),
    ("discard.self-energy-all-typed",
     re.compile(r"discard all (?:(?P<type>" + _TYPE_WORDS + r") )?energy from "
                r"this pokemon\."), _discard_all_typed_self),
    ("energy.move-all-to-bench",
     re.compile(r"move all energy from this pokemon to (?:an?|\d+) of your "
                r"benched pokemon\."), _move_all_energy_to_bench),
    ("flip.tails-nothing-else-prevent",
     re.compile(r"flip a coin\. if tails, this attack does nothing\. if heads, "
                r"during your opponent's next turn, prevent all damage done to "
                r"this pokemon by attacks\."), _flip_tails_nothing_else_shield),
    ("lock.opponent-energy-stadium",
     re.compile(r"during your opponent's next turn, they can't play any special "
                r"energy or stadium cards from their hand\."),
     _lock_opponent_energy_stadium),
    ("recover.flip-up-to-heads",
     re.compile(r"flip (\d+) coins\. put a number of cards up to the number of "
                r"heads from your discard pile into your hand\."),
     _flip_recover_up_to_heads),
    ("ko.if-defender-has-any-condition",
     re.compile(r"if (?:your opponent's active|the defending) pokemon is "
                r"affected by a special condition, that pokemon is knocked "
                r"out\."), _ko_any_condition),
    ("gate.defender-undamaged",
     re.compile(r"if your opponent's active pokemon has no damage counters on "
                r"it before this attack does damage, this attack does "
                r"nothing\."), _gate_if_damaged),

    # -- batch 18: old-era wordings for bonuses and searches ----------------
    ("bonus.base-plus-any-condition",
     re.compile(r"if (?:the defending|your opponent's active) pokemon is "
                r"affected by a special condition, this attack does (\d+) "
                r"damage plus (\d+) more damage\."), _base_plus_if_any_condition),
    ("bonus.base-plus-condition",
     re.compile(r"if (?:the defending|your opponent's active) pokemon is ("
                + _CONDITION_WORDS + r"), this attack does (\d+) damage plus "
                r"(\d+) more damage\."), _base_plus_if_condition),
    ("flip.times-heads",
     re.compile(r"flip (an?|\d+) coins?\. this attack does (\d+) times the "
                r"number of heads\."), _flip_times_heads),
    ("bonus.base-plus-hand-equal",
     re.compile(r"if you have the same number of cards in your hand as your "
                r"opponent, this attack does (\d+) damage plus (\d+) more "
                r"damage\."), _base_plus_if_hand_equal),
    ("bonus.base-plus-stadium-discard",
     re.compile(r"if there is any stadium card in play, this attack does "
                r"(\d+) damage plus (\d+) more damage\. discard that stadium "
                r"card\."), _base_plus_stadium_then_discard),
    ("snipe.undamaged-only",
     re.compile(r"choose (an?|\d+) of your opponent's pokemon that doesn't "
                r"have any damage counters on it\. this attack does (\d+) "
                r"damage to that pokemon" + _SNIPE_TAIL), _snipe_undamaged),
    ("flip.heads-spread-all",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage to "
                r"each of your opponent's pokemon" + _SNIPE_TAIL),
     _flip_heads_spread_all),
    ("search.evolution-to-hand",
     re.compile(r"search your deck for an evolution card, show it to your "
                r"opponent, and put it into your hand\. shuffle your deck "
                r"afterward\."), _search_evolution_to_hand),
    ("heal.counters-each-bench",
     re.compile(r"remove (\d+) damage counters from each of your benched "
                r"pokemon\."), _remove_counters_each_bench),
    ("bonus.base-plus-per-energy-cards",
     re.compile(r"this attack does (\d+) damage plus (\d+) more damage for "
                r"each energy cards? attached to the defending pokemon\."),
     _base_plus_per_energy_cards_defender),
    ("bonus.base-plus-threshold-counters",
     re.compile(r"if (?:the defending|your opponent's active) pokemon already "
                r"has at least (\d+) damage counters on it, this attack does "
                r"(\d+) damage plus (\d+) more damage\."),
     _base_plus_threshold_counters),
    ("search.trainer-show",
     re.compile(r"search your deck for a trainer card, show it to your "
                r"opponent, and put it into your hand\. shuffle your deck "
                r"afterward\."), _search_trainer_show),

    # -- batch 19: counters on the bench, self-locks, evolution search -------
    ("counters.on-bench-chosen",
     re.compile(r"put (\d+) damage counters on (?:an?|(\d+)) of your "
                r"opponent's benched pokemon\."), _counters_on_bench_chosen),
    ("lock.this-attack-until-leaves",
     re.compile(r"this pokemon can't use (.+?) again until it leaves the active "
                r"spot\."), _lock_until_leaves),
    ("gate.must-have-entered-active",
     re.compile(r"if this pokemon didn't move from the bench to the active spot "
                r"this turn, this attack does nothing\."), _gate_entered_active),
    ("ko.chosen-basic-non-gx",
     re.compile(r"knock out (?:an?|\d+) of your opponent's basic pokemon that "
                r"isn't a pokemon-gx\."), _ko_chosen_basic_non_gx),
    ("switch.opponent-bench-to-hand",
     re.compile(r"put (\d+) of your opponent's benched pokemon and all cards "
                r"attached to them into your opponent's hand\."),
     _opponent_bench_to_hand),
    ("search.evolve-any-own",
     re.compile(r"search your deck for a card that evolves from (?:an?|\d+) of "
                r"your pokemon and put it onto that pokemon to evolve it\. "
                r"then, shuffle your deck\."), _evolve_from_deck_any),
    ("scale.times-both-actives-energy",
     re.compile(r"this attack does (\d+) damage times the amount of energy "
                r"attached to both active pokemon\. this damage isn't affected "
                r"by weakness or resistance\."), _damage_times_both_actives_energy),
    ("flip.tails-nothing-heads-shield-all",
     re.compile(r"flip a coin\. if tails, this attack does nothing\. if heads, "
                r"during your opponent's next turn, prevent all damage from and "
                r"effects of attacks done to this pokemon\."),
     _flip_tails_nothing_heads_shield_all),
    ("bonus.extra-energy-snipe",
     re.compile(r"if this pokemon has at least (\d+) extra (?:(?P<type>"
                + _TYPE_WORDS + r") )?energy attached(?: to it)?(?: \(in "
                r"addition to this attack's cost\))?, this attack does (\d+) "
                r"damage to (?:an?|\d+) of your opponent's benched pokemon"
                + _SNIPE_TAIL), _bonus_extra_energy_snipe),

    # -- batch 20: continuous ability protection ---------------------------
    ("ability.prevent-from-ex-v",
     re.compile(r"prevent all damage done to this pokemon by attacks from your "
                r"opponent's pokemon ex and pokemon v\."),
     _passive_prevent_from_ex_or_v),
    ("ability.prevent-from-type",
     re.compile(r"prevent all damage done to this pokemon by attacks from ("
                + _TYPE_WORDS + r") pokemon\."), _passive_prevent_from_type),
    ("ability.prevent-from-ability-holders",
     re.compile(r"prevent all damage from attacks done to this pokemon by your "
                r"opponent's pokemon that have an ability\."),
     _passive_prevent_from_ability_holders),
    ("ability.effect-shield",
     re.compile(r"prevent all effects of attacks used by your opponent's "
                r"pokemon done to this pokemon\. \(damage is not an "
                r"effect\.\)"), _passive_effect_shield),
    ("ability.effect-shield-except-damage",
     re.compile(r"prevent all effects of your opponent's attacks, except "
                r"damage, done to this pokemon\."),
     _passive_effect_shield_no_damage),

    # -- batch 22: abilities that react to being damaged -------------------
    ("trigger.counters-on-attacker",
     re.compile(r"put (\d+) damage counters? on the attacking "
                r"pokemon\."), _counters_on_attacker),
    ("trigger.condition-on-attacker",
     re.compile(r"the attacking pokemon is now (" + _CONDITION_WORDS + r")\."),
     _condition_on_attacker),
    ("trigger.knock-out-attacker",
     re.compile(r"the attacking pokemon is knocked out\."), _knock_out_attacker),

    # -- batch 23: flat damage reduction and free basic retreat ------------
    ("ability.takes-less-flat",
     re.compile(r"(?:this pokemon takes|any damage done to this pokemon by "
                r"attacks is reduced by) (\d+) (?:less damage from attacks|"
                r"\(after applying weakness and resistance\))"
                r"(?: \(after applying weakness and resistance\))?\."),
     _passive_takes_less_flat),
    ("ability.flip-prevent-all-damage",
     re.compile(r"if any damage is done to this pokemon by attacks, flip a "
                r"coin\. if heads, prevent that damage\."),
     _passive_flip_prevent_all),
    ("ability.basic-free-retreat",
     re.compile(r"your basic pokemon in play have no retreat cost\."),
     _passive_basic_free_retreat),

    # -- batch 24: ability-shaped search/attach and counter spreads --------
    ("ability.search-attach-energy-distributed",
     re.compile(r"search your deck for up to (\d+) basic (?:(?P<type>"
                + _TYPE_WORDS + r") )?energy cards? and attach them to your "
                r"pokemon in any way you like\. then,? shuffle your deck\."),
     _search_attach_basic_energy_distributed),
    ("ability.counters-chosen-opponents",
     re.compile(r"choose (?:an?|(\d+)) of your opponent's pokemon and put "
                r"(\d+) damage counters on each of them\."),
     _counters_on_chosen_opponents),

    # -- batch 25: deck-top order, retreat-cost taxes, prize gates ---------
    ("reorder.top-own",
     re.compile(r"look at the top (\d+) cards of your deck and put them back "
                r"(?:on top of your deck )?in any order\."), _reorder_own_top),
    ("debuff.defender-retreat-cost-up",
     re.compile(r"your opponent's active pokemon's retreat cost is colorless "
                r"more\."), _raise_defender_retreat),
    ("bonus.opponent-prizes-at-most",
     re.compile(r"if your opponent has (\d+) or fewer prize cards remaining, "
                r"this attack does (\d+) more damage\."),
     _bonus_if_opponent_prizes_at_most),
    ("scale.less-per-defender-retreat",
     re.compile(r"this attack does (\d+) less damage for each colorless in "
                r"your opponent's active pokemon's retreat cost\."),
     _less_per_defender_retreat_colorless),
    ("ability.switch-active-with-bench",
     re.compile(r"switch your active pokemon with (?:an?|\d+) of your benched "
                r"pokemon\."), _switch_active_with_bench),

    # -- batch 26: flip bonus with self-heal, next-turn team boost ---------
    ("flip.bonus-and-heal-self",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) more damage "
                r"and heal (\d+) damage from this pokemon\."),
     _flip_bonus_and_heal_self),
    ("boost.own-next-turn-all",
     re.compile(r"during your next turn, each of this pokemon's attacks does "
                r"(\d+) more damage(?: \(before applying weakness and "
                r"resistance\))?\."), _own_next_turn_all_boost),
    # -- batch 27: bench damage shield and opponent retreat tax ------------
    ("shield.prevent-damage-at-most",
     re.compile(r"during your opponent's next turn, if this pokemon would be "
                r"damaged by an attack, prevent that attack's damage done to "
                r"this pokemon if that damage is (\d+) or less\."),
     _prevent_damage_at_most_next_turn),
    ("shield.prevent-damage-at-most-named",
     re.compile(r"during your opponent's next turn, if .+? would be damaged by "
                r"an attack, prevent that attack's damage done to .+? if that "
                r"damage is (\d+) or less\."),
     _prevent_damage_at_most_next_turn),
    ("self.bench-spread",
     re.compile(r"this attack also does (\d+) damage to (?:an?|(\d+)) of your "
                r"benched pokemon\. \(don't apply weakness and resistance for "
                r"benched pokemon\.\)"), _self_bench_spread),






    ("delayed.counters-on-defender",
     re.compile(r"at the end of your opponent's next turn, put (\d+) damage "
                r"counters? on the defending pokemon\."),
     _schedule_counters_on_defender),
    ("delayed.condition-on-defender",
     re.compile(r"at the end of your opponent's next turn, the defending pokemon "
                r"is now (" + _CONDITION_WORDS + r")\."),
     _schedule_condition_on_defender),
    ("delayed.knock-out-defender",
     re.compile(r"(?:(?P<discard>discard all energy (?:attached to|from) this "
                r"pokemon)\. )?(?:at the end of your opponent's next turn, "
                r"discard the defending pokemon and all attached cards|the "
                r"defending pokemon is knocked out at the end of your opponent's "
                r"next turn|at the end of your opponent's next turn, the "
                r"defending pokemon will be knocked out)\."),
     _schedule_knock_out_defender),
    # -- batch 70: the Burn checkup override -------------------------------
    ("burn.counters-instead-of",
     re.compile(r"put (\d+) damage counters instead of \d+ on your opponent's "
                r"burned pokemon between turns\."), _t70_burn_counters_passive),
    # -- batch 69: typed prevention, self search and spreads ----------------
    ("spread.opponent-ex-ignoring-mods",
     re.compile(r"this attack does (\d+) damage to each of your opponent's "
                r"pokemon ex\. \(don't apply weakness and resistance for "
                r"benched pokemon\.\)"), _t69_spread_opponent_ex),
    ("attach.typed-energy-from-discard-self",
     re.compile(r"attach a (" + _TYPE_WORDS + r") energy card from your discard "
                r"pile to this pokemon\."), _t69_attach_typed_from_discard_self),
    ("search.self-name-to-hand",
     re.compile(r"search your deck for (?:m )?this pokemon, reveal it, and put it "
                r"into your hand\..*"), _t69_search_self_name_to_hand),
    ("bonus.per-self-counters-then-heal",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each damage "
                r"counter on this pokemon\. then, remove (\d+) damage counters "
                r"from this pokemon\."), _t68_bonus_per_self_counters_then_heal),
    ("damage.base-swap-optional-typed-all",
     re.compile(r"you may discard all (" + _TYPE_WORDS + r") energy attached to "
                r"this pokemon\. if you do, this attack's base damage is (\d+) "
                r"instead of (\d+)\."), _t68_optional_typed_all_base_swap),
    ("bonus.optional-hand-discard-per-card",
     re.compile(r"you may discard up to (\d+) energy cards from your hand, and "
                r"this attack does (\d+) more damage for each card you discarded "
                r"in this way\."), _t68_optional_discard_hand_bonus),
    ("scale.per-two-typed-energy-all-own",
     re.compile(r"this attack does (\d+) damage for each (" + _TYPE_WORDS +
                r") energy and each (" + _TYPE_WORDS + r") energy attached to all "
                r"of your pokemon\."), _t68_scale_two_typed_energy_all_own),
    ("damage.chosen-opponent-ignoring-mods",
     re.compile(r"this attack does (\d+) damage to (?:an?|\d+) of your "
                r"opponent's pokemon\. this damage isn't affected by weakness or "
                r"resistance\."), _t68_damage_opponent_chosen_ignoring),
    ("search.basic-energy-to-hand-many",
     re.compile(r"search your deck for up to (\d+) basic energy cards, reveal "
                r"them, and put them into your hand\. shuffle your deck "
                r"afterward\."), _t68_search_basic_energy_to_hand_many),
    ("prevent.damage-from-tag-team",
     re.compile(r"during your opponent's next turn, prevent all damage done to "
                r"this pokemon by attacks from tag team pokemon\."),
     _t68_prevent_from_tag_team),
    ("bonus.benched-typed-ignoring-weakness",
     re.compile(r"this attack does (\d+) more damage for each of your benched (" +
                _TYPE_WORDS + r") pokemon\. this attack's damage isn't affected by "
                r"weakness\."), _t68_bonus_bench_typed_ignoring),
    ("scale.benched-with-typed-energy",
     re.compile(r"this attack does (\d+) more damage for each of your benched "
                r"pokemon that has any (" + _TYPE_WORDS + r") energy attached\."),
     _t68_bonus_bench_with_typed_energy),
    ("attach.typed-hand-bench-then-heal-all",
     re.compile(r"attach a basic (" + _TYPE_WORDS + r") energy card from your hand "
                r"to (?:an?|\d+) of your benched pokemon\. if you do, heal all "
                r"damage from that pokemon\."), _t68_attach_typed_hand_bench_heal_all),
    ("attach.typed-hand-any-target",
     re.compile(r"attach a basic (" + _TYPE_WORDS + r") energy card from your hand "
                r"to (?:an?|\d+) of your pokemon\."), _t68_attach_typed_hand_any),
    ("bench.own-name-from-discard",
     re.compile(r"put up to (\d+) this pokemon from your discard pile onto your "
                r"bench\."), _t68_bench_own_name_from_discard),
    # -- batch 66: recoil, peeks, prevention and the tail ------------------
    ("recoil.per-typed-energy",
     re.compile(r"this pokemon does damage to itself equal to (\d+) times the "
                r"number of (" + _TYPE_WORDS + r") energy cards attached to "
                r"it\."), _t66_recoil_per_typed_energy),
    ("draw.optional-both-players",
     re.compile(r"your opponent may draw (an?|\d+) cards?\. either way, you may "
                r"draw (?:an?|\d+) cards?\."), _t66_optional_draw_both),
    ("attach.search-basic-energy-many",
     re.compile(r"search your deck for up to (\d+) basic energy cards and attach "
                r"them to (?:an?|\d+) of your pokemon\. shuffle your deck "
                r"afterward\."), _t66_search_basic_energy_attach_many),
    ("heal.discard-typed-heal-counters",
     re.compile(r"discard (\d+) (" + _TYPE_WORDS + r") energy attached to this "
                r"pokemon and remove (\d+) damage counters from this pokemon\."),
     _t66_discard_typed_heal),
    ("deck.peek-hand-or-discard",
     re.compile(r"look at the top card of your deck\. you may put it into your "
                r"hand\. if not, discard it and draw a card\."),
     _t66_peek_then_choose),
    ("search.typed-energy-show-opponent",
     re.compile(r"search your deck for a (" + _TYPE_WORDS + r") energy card, show "
                r"it to your opponent, and put it into your hand\. shuffle your "
                r"deck afterward\."), _t66_search_typed_energy_show_hand),
    ("recoil.then-opponent-switch",
     re.compile(r"this pokemon does (\d+) damage to itself\. your opponent "
                r"switches the defending pokemon with (?:an?|\d+) of (?:his or "
                r"her|their) benched pokemon, if any\."),
     _t66_recoil_then_opponent_switch),
    ("condition.if-defender-basic",
     re.compile(r"if the defending pokemon is a basic pokemon, that pokemon is "
                r"now (" + _CONDITION_WORDS + r")\."),
     _t66_condition_if_defender_basic),
    ("damage.base-swap-if-defender-low-hp",
     re.compile(r"as long as the defending pokemon's remaining hp is (\d+) or "
                r"less, this attack's base damage is (\d+) instead of (\d+)\."),
     _t66_base_swap_if_defender_hp),
    ("heal.pre-damage-one-counter",
     re.compile(r"before doing damage, remove (\d+) damage counter from the "
                r"defending pokemon\."), _t66_pre_heal_defender_single),
    ("condition.unless-opponent-discards",
     re.compile(r"if your opponent doesn't discard a card from (?:his or her|"
                r"their) hand, the defending pokemon is now (" +
                _CONDITION_WORDS + r")\."),
     _t66_condition_unless_opponent_discards),
    ("heal.per-defender-energy-cards",
     re.compile(r"remove from this pokemon a number of damage counters equal to "
                r"the amount of energy attached to the defending pokemon\."),
     _t66_heal_per_defender_energy),
    ("damage.base-swap-if-defender-energy",
     re.compile(r"if the defending pokemon has any energy cards attached to it, "
                r"this attack's base damage is (\d+) instead of (\d+)\."),
     _t66_base_swap_if_defender_has_energy),
    ("flip.nothing-or-discard-energy",
     re.compile(r"flip a coin\. if tails, this attack does nothing\. if heads, "
                r"discard an energy card attached to the defending pokemon\."),
     _t66_flip_nothing_or_discard),
    ("flip.base-swap-if-any-tails",
     re.compile(r"flip (an?|\d+) coins?\. if either of them is tails, this "
                r"attack's base damage is (\d+) instead of (\d+)\."),
     _t66_flip_base_swap_any_tails),
    ("heal.discard-typed-all-heal-all",
     re.compile(r"discard a (" + _TYPE_WORDS + r") energy attached to this pokemon "
                r"and remove all damage counters from this pokemon\."),
     _t66_discard_typed_heal_all),
    ("draw.top-and-bottom",
     re.compile(r"draw a card from the top and the bottom of your deck\."),
     _t66_draw_top_and_bottom),
    ("condition.if-defender-not-evolved",
     re.compile(r"if the defending pokemon isn't an evolved pokemon, that pokemon "
                r"is now (" + _CONDITION_WORDS + r")\."),
     _t66_condition_if_defender_not_evolved),
    ("switch.defender-plain",
     re.compile(r"switch (?:an?|\d+) of your opponent's benched pokemon with (?:"
                r"an?|\d+) of the defending pokemon\."), _t66_switch_defender_plain),
    ("heal.counters-and-conditions",
     re.compile(r"remove (\d+) damage counters? and all special conditions from "
                r"this pokemon\."), _t66_heal_and_cure),
    ("flip.search-basic-energy",
     re.compile(r"flip a coin\. if heads, search your deck for a basic energy "
                r"card and attach it to this pokemon\. shuffle your deck "
                r"afterward\."), _t66_flip_search_basic_energy),
    ("topdeck.from-discard-any",
     re.compile(r"search your discard pile for any (\d+) card, show it to your "
                r"opponent, and put it on top of your deck\."),
     _t66_discard_to_top_of_deck),
    ("bounce.self-if-bench",
     re.compile(r"return this pokemon and all cards attached to it to your hand\. "
                r"\(if you don't have any benched pokemon, this attack does "
                r"nothing\.\)"), _t66_bounce_self_optional),
    ("counters.on-damaged-opponents",
     re.compile(r"put (\d+) damage counter on each of your opponent's pokemon "
                r"that already has damage counters on it\."),
     _t66_counters_damaged_opponents),
    ("heal.each-benched",
     re.compile(r"remove (\d+) damage counter from each of your benched "
                r"pokemon\."), _t66_heal_each_bench),
    ("recover.flip-any-card",
     re.compile(r"flip a coin\. if heads, put any (\d+) card from your discard "
                r"pile into your hand\."), _t66_flip_recover_any),
    ("bonus.per-named-energy-attached",
     re.compile(r"this attack does (\d+) more damage for each ([a-z][\w' -]*) "
                r"energy attached to this pokemon\."), _t66_bonus_per_named_energy),
    ("prevent.effects-from-ex",
     re.compile(r"prevent all effects of attacks, including damage, done to this "
                r"pokemon by (?:your opponent's )?pokemon-ex\..*"),
     _t66_prevent_effects_from_ex),
    ("prevent.effects-from-gx-ex",
     re.compile(r"prevent all effects of attacks, including damage, done to this "
                r"pokemon by (?:your opponent's )?pokemon-gx or pokemon-ex\..*"),
     _t66_prevent_effects_from_gx_ex),
    # -- batch 65: previous-turn memory ------------------------------------
    ("bonus.used-attack-last-turn",
     re.compile(r"if this pokemon used ([a-z][\w' -]*) during your last turn, "
                r"this attack does (\d+) more damage\."),
     _t65_bonus_if_used_last_turn),
    ("damage.base-swap-used-last-turn",
     re.compile(r"if this pokemon used ([a-z][\w' -]*) during your last turn, "
                r"this attack's base damage is (\d+) instead of (\d+)\."),
     _t65_base_swap_if_used_last_turn),
    ("gate.used-attack-last-turn",
     re.compile(r"this attack can't be used unless this pokemon used (?:its )?([a-z][\w' "
                r"-]*) attack last turn\."), _t65_gate_used_last_turn),
    ("bonus.played-named-this-turn",
     re.compile(r"if you played ([a-z][\w' -]*) from your hand during this turn, "
                r"this attack does (\d+) more damage\."),
     _t65_bonus_if_played_named),
    ("bonus.damaged-last-turn",
     re.compile(r"if this pokemon was damaged by an attack during your "
                r"opponent's last turn, this attack does (\d+) more damage\."),
     _t65_bonus_if_damaged_last_turn),
    ("bonus.own-ko-last-turn",
     re.compile(r"if any of your pokemon were knocked out during your opponent's "
                r"last turn, this attack does (\d+) more damage\."),
     _t65_bonus_if_own_ko_last_turn),
    ("bonus.defender-moved-last-turn",
     re.compile(r"if your opponent's active pokemon moved from the bench to the "
                r"active spot during your opponent's last turn, this attack does "
                r"(\d+) more damage\."), _t65_bonus_if_defender_moved),
    ("boost.next-turn-named",
     re.compile(r"during your next turn, this pokemon's ([a-z][\w' -]*) "
                r"attack's base damage is (\d+)\."), _t65_next_turn_boost_named),
    ("attack.use-last-opponent-attack",
     re.compile(r"if your opponent's pokemon used an attack during (?:his or her|"
                r"their) last turn, use it as this attack\."),
     _t65_use_last_opponent_attack),
    ("bonus.self-has-counters",
     re.compile(r"if this pokemon has any damage counters on it, this attack does "
                r"(\d+) more damage\."), _t65_bonus_if_self_damaged),
    ("bonus.defender-damaged-last-turn",
     re.compile(r"if the defending pokemon was damaged by an attack during your "
                r"last turn, this attack does (\d+) more damage\."),
     _t65_bonus_if_defender_damaged_last_turn),
    # -- batch 64: spreads, snipes and the survey tail ----------------------
    ("counters.distribute-opponent-any",
     re.compile(r"put (\d+) damage counters on your opponent's pokemon in any "
                r"way you like\."), _t64_distribute_counters_opponent),
    ("spread.damaged-opponent-bench",
     re.compile(r"this attack does (\d+) damage to each of your opponent's "
                r"benched pokemon that has any damage counters on it\."),
     _t64_spread_damaged_bench),
    ("snipe.scaled-by-target-energy",
     re.compile(r"this attack does (\d+) damage times the number of energy "
                r"attached to that pokemon\."), _t64_snipe_scaled_by_energy),
    ("bench.search-self",
     re.compile(r"search your deck for this pokemon and put it onto your bench\. "
                r"(?:then, )?shuffle your deck(?: afterward)?\."),
     _t64_search_self_to_bench),
    ("gate.named-energy-discard",
     re.compile(r"discard a ([a-z][\w' -]*) energy attached to this pokemon\. "
                r"if you can't discard a \1 energy, this attack does "
                r"nothing\."), _t64_gate_named_energy),
    ("scale.per-two-typed-energy-own",
     re.compile(r"this attack does (\d+) damage times the amount of basic (" +
                _TYPE_WORDS + r") and basic (" + _TYPE_WORDS + r") energy attached "
                r"to your pokemon\."), _t64_scale_two_typed_energy_own),
    ("energy.move-defender-to-bench-plain",
     re.compile(r"move an energy attached to the defending pokemon to (?:an?|"
                r"\d+) of your opponent's benched pokemon\."),
     _t64_move_defender_energy_to_bench),
    ("damage.own-chosen",
     re.compile(r"does (\d+) damage to (?:an?|\d+) of your pokemon\. \(don't "
                r"apply weakness and resistance for benched pokemon\.\)"),
     _t64_damage_own_chosen),
    ("mill.opponent-top-card",
     re.compile(r"discard the top card from your opponent's deck\."),
     _t64_mill_opponent_top),
    ("condition.flip-choose-condition",
     re.compile(r"flip a coin\. if heads, choose (?:an?|\d+) special "
                r"condition\. the defending pokemon is now affected by that "
                r"special condition\."), _t64_flip_choice_condition),
    ("bonus.stadium-then-discard-that",
     re.compile(r"if a stadium is in play, this attack does (\d+) more damage\. "
                r"then, discard that stadium\."), _t64_stadium_bonus_then_discard),
    ("deck.optional-shuffle-self",
     re.compile(r"you may shuffle this pokemon and all attached cards into your "
                r"deck\."), _t64_optional_shuffle_self),
    ("scale.per-active-energy",
     re.compile(r"does (\d+) damage times the amount of energy attached to all "
                r"of your active pokemon\."), _t64_scale_per_active_energy),
    ("bonus.last-prize",
     re.compile(r"if you have only (\d+) prize card remaining, this attack does "
                r"(\d+) more damage\."), _t64_bonus_one_prize_left),
    ("bonus.optional-typed-all-energy",
     re.compile(r"you may discard all (" + _TYPE_WORDS + r") energy from this "
                r"pokemon\. if you do, this attack does (\d+) more damage\."),
     _t64_optional_typed_all_bonus),
    ("lock.discard-energy-defender-no-attack",
     re.compile(r"discard an energy from this pokemon\. during your opponent's "
                r"next turn, the defending pokemon can't attack\."),
     _t64_discard_energy_then_lock_defender),
    ("switch.discard-energy-then-self",
     re.compile(r"discard an energy from this pokemon\. if you do, switch it "
                r"with (?:an?|\d+) of your benched pokemon\."),
     _t64_discard_energy_then_switch),
    ("retreat.condition-defender-plain",
     re.compile(r"your opponent's active pokemon is now (" + _CONDITION_WORDS +
                r")\. that pokemon can't retreat during your opponent's next "
                r"turn\."), _t64_condition_then_defender_no_retreat_word),
    ("scale.night-march-discard",
     re.compile(r"this attack does (\d+) damage times the number of pokemon in "
                r"your discard pile that have the night march attack\."),
     _t64_scale_night_march_discard),
    ("flip.times-heads-then-confused-b64",
     re.compile(r"flip (an?|\d+) coins?\. this attack does (\d+) damage for "
                r"each heads\. this pokemon is now confused\."),
     _t64_flip_times_heads_then_confused),
    ("condition.flip-then-discard-energy",
     re.compile(r"flip a coin\. if heads, your opponent's active pokemon is now ("
                + _CONDITION_WORDS + r"), and discard an energy from that "
                r"pokemon\."), _t64_flip_condition_then_discard_energy),
    ("recover.named-cards-all",
     re.compile(r"put all ([a-z][\w' -]*) cards from your discard pile into your "
                r"hand\."), _t64_recover_named_cards),
    ("bonus.optional-recoil",
     re.compile(r"you may do (\d+) more damage\. if you do, this pokemon also "
                r"does (\d+) damage to itself\."), _t64_optional_bonus_recoil),
    ("bonus.mill-both-per-energy",
     re.compile(r"discard the top card of each player's deck\. this attack does ("
                r"\d+) more damage for each energy card discarded in this "
                r"way\."), _t64_mill_both_bonus_per_energy),
    ("mill.per-named-energy",
     re.compile(r"for each ([a-z][\w' -]*) energy attached to this pokemon, "
                r"discard the top card of your opponent's deck\."),
     _t64_mill_per_named_energy),
    ("heal.per-named-energy",
     re.compile(r"heal from this pokemon (\d+) damage for each ([a-z][\w' -]*) "
                r"energy attached to this pokemon\."), _t64_heal_per_named_energy),
    ("attach.energy-up-to-self-discard",
     re.compile(r"choose up to (\d+) energy cards from your discard pile and "
                r"attach them to this pokemon\."), _t64_attach_energy_up_to_self),
    ("recover.energy-then-recoil",
     re.compile(r"put up to (\d+) energy cards from your discard pile into your "
                r"hand\. this pokemon does (\d+) damage to itself\."),
     _t64_recover_energy_recoil),
    ("damage.opponent-bench-chosen",
     re.compile(r"does (\d+) damage to (?:an?|\d+) of your opponent's benched "
                r"pokemon\. \(don't apply weakness or resistance for benched "
                r"pokemon\.\)"), _t64_damage_opponent_bench_chosen),
    ("condition.confused-on-tails",
     re.compile(r"flip a coin\. if tails, this pokemon is now confused \(after "
                r"doing damage\)\."), _t64_confused_after_damage),
    # -- batch 63: granted attacks and free attack costs -------------------
    ("grant.attacks-any-in-play",
     re.compile(r"this pokemon can use the attacks of any pokemon in play "
                r"\(both yours and your opponent's\)\..*"), _grant_attacks_any_in_play),
    ("grant.attacks-own-bench",
     re.compile(r"this pokemon can use the attacks of any of your benched "
                r"pokemon\..*"), _grant_attacks_bench),
    ("grant.attacks-discard-basics",
     re.compile(r"this pokemon can use the attacks of (?:any )?basic pokemon in "
                r"your discard pile\..*"), _grant_attacks_discard_basics),
    ("grant.attacks-gx-ex-bench-discard",
     re.compile(r"this pokemon can use the attacks of any pokemon-gx or "
                r"pokemon-ex on your bench or in your discard pile\..*"),
     _grant_attacks_bench_discard_gx_ex),
    ("grant.previous-evolutions",
     re.compile(r"this pokemon can use (?:any attack from|the attacks of) its "
                r"previous evolutions\..*"), _grant_previous_evolutions),
    ("cost.free-if-tools-in-discard",
     re.compile(r"if you have (\d+) or more pokemon tool cards in your discard "
                r"pile, ignore all energy in the attack cost of each of this "
                r"pokemon's attacks\."), _free_cost_if_tools_in_discard),
    ("cost.free-if-stadiums-in-discard",
     re.compile(r"if you have (\d+) or more stadium cards in your discard pile, "
                r"ignore all energy in this pokemon's attack costs\."),
     _free_cost_if_stadiums_in_discard),
    ("cost.free-if-named-in-play",
     re.compile(r"if you have ([a-z][\w' -]*) in play, ignore all energy in the "
                r"costs of attacks used by this pokemon\."),
     _free_cost_if_named_in_play),
    ("cost.free-plain",
     re.compile(r"ignore all energy in this pokemon's attack costs?\."),
     _free_cost_plain),
    ("cost.free-team-with-attack",
     re.compile(r"ignore all energy in the attack costs of each of your pokemon "
                r"in play that has the ([a-z][\w' -]*) attack\."),
     _free_cost_team_with_attack),
    ("cost.free-next-attack",
     re.compile(r"you may use this attack without paying its energy cost\."),
     _t63_free_next_attack),
    ("attack.use-opponent-attack",
     re.compile(r"choose (?:an?|\d+) of your opponent's pokemon's attacks and "
                r"use it as this attack\."), _t63_use_opponent_attack),
    # -- batch 62: the one-card tail, seventh pass -------------------------
    ("scale.per-opponent-ability-b62",
     re.compile(r"this attack does (\d+) damage for each of your opponent's "
                r"pokemon in play that has an ability\."),
     _t62_scale_per_opponent_ability),
    ("bonus.defender-v-or-gx",
     re.compile(r"if your opponent's active pokemon is a pokemon v or "
                r"pokemon-gx, this attack does (\d+) more damage\."),
     _t62_bonus_defender_v_or_gx),
    ("attach.typed-discard-single-any",
     re.compile(r"attach a (" + _TYPE_WORDS + r") energy card from your discard "
                r"pile to (?:an?|\d+) of your pokemon\."),
     _t62_attach_typed_discard_single_any),
    ("counters.per-discard-pokemon",
     re.compile(r"put (\d+) damage counter on your opponent's active pokemon for "
                r"each pokemon in your discard pile\."),
     _t62_counters_per_discard_pokemon),
    ("attach.typed-hand-then-switch",
     re.compile(r"attach a (" + _TYPE_WORDS + r") energy card from your hand to "
                r"this pokemon\. if you do, switch it with (?:an?|\d+) of your "
                r"benched pokemon\."), _t62_attach_hand_then_switch),
    ("bonus.optional-hand-discard",
     re.compile(r"you may discard a card from your hand\. if you do, this attack "
                r"does (\d+) more damage\."), _t62_optional_hand_bonus),
    ("hand.reveal-chosen-to-bottom",
     re.compile(r"your opponent reveals their hand\. choose a card you find "
                r"there and put it on the bottom of their deck\."),
     _t62_reveal_hand_bottom_card),
    ("scale.per-distinct-basic-type-all-own",
     re.compile(r"this attack does (\d+) more damage for each type of basic "
                r"energy attached to all of your pokemon\."),
     _t62_bonus_per_distinct_basic_type_all),
    ("counters.per-prizes-opponent-taken",
     re.compile(r"put (\d+) damage counters on your opponent's active pokemon for "
                r"each prize card your opponent has taken\."),
     _t62_counters_per_prizes_taken),
    ("attach.hand-bench-then-heal",
     re.compile(r"attach an energy card from your hand to (?:an?|\d+) of your "
                r"benched pokemon\. if you do, heal (\d+) damage from that "
                r"pokemon\."), _t62_attach_hand_bench_then_heal),
    ("recoil.then-condition-plain",
     re.compile(r"this pokemon also does (\d+) damage to itself\. your "
                r"opponent's active pokemon is now (" + _CONDITION_WORDS + r")\."),
     _t62_recoil_then_condition),
    ("gate.typed-hand-discard-many",
     re.compile(r"discard (\d+) (" + _TYPE_WORDS + r") energy cards from your "
                r"hand\. if you don't, this attack does nothing\."),
     _t62_gate_typed_hand_discard),
    ("heal.chosen-many-damaged",
     re.compile(r"remove (\d+) damage counters? from (?:an?|(\d+)) of your "
                r"pokemon\s*$"), _t62_heal_chosen_many),
    ("energy.flip-tails-discard-typed",
     re.compile(r"flip a coin\. if tails, discard (\d+) (" + _TYPE_WORDS +
                r") energy attached to this pokemon\."),
     _t62_flip_tails_discard_typed),
    ("bonus.optional-then-asleep",
     re.compile(r"you may do (\d+) more damage\. if you do, this pokemon is now "
                r"asleep\."), _t62_optional_bonus_then_asleep),
    ("counters.each-opponent-variant",
     re.compile(r"put (\d+) damage counters each of your opponent's pokemon\."),
     _t62_counters_each_opponent_all),
    ("counters.both-active-to-hp",
     re.compile(r"put damage counters on both active pokemon until the remaining "
                r"hp of each pokemon is (\d+)\."),
     _t62_counters_both_active_to_hp),
    ("bonus.optional-mill-typed",
     re.compile(r"you may discard the top card of your deck\. if that card is a ("
                + _TYPE_WORDS + r") energy card, this attack does (\d+) more "
                r"damage\."), _t62_optional_mill_bonus_typed),
    ("hand.opponent-flips-discard",
     re.compile(r"your opponent flips (\d+) coins?\. for each tails, he or she "
                r"discards a card from his or her hand\."),
     _t62_opponent_flips_discard_hand),
    ("attach.mill-typed-attach-nocard",
     re.compile(r"discard the top card of your deck\. if that card is a (" +
                _TYPE_WORDS + r") energy, attach it to this pokemon\."),
     _t62_mill_typed_attach_nocard),
    ("heal.discard-energy-heal-all-it",
     re.compile(r"discard an energy attached to this pokemon and heal all damage "
                r"from it\."), _t62_discard_energy_heal_all_it),
    ("condition.choose-asleep-poisoned",
     re.compile(r"choose either asleep or poisoned\. your opponent's active "
                r"pokemon is now affected by that special condition\."),
     _t62_choose_asleep_or_poisoned),
    ("attach.discard-typed-target-many",
     re.compile(r"attach (an?|\d+) energy cards from your discard pile to (?:an?|"
                r"\d+) of your (" + _TYPE_WORDS + r") pokemon\."),
     _t62_attach_energy_discard_typed_target),
    ("scale.per-energy-all-in-play",
     re.compile(r"this attack does (\d+) damage times the amount of energy "
                r"attached to all pokemon in play\."),
     _t62_scale_per_energy_all_in_play),
    ("delayed.discard-defender-next-turn",
     re.compile(r"at the end of your opponent's next turn, discard the defending "
                r"pokemon and all cards attached to it\."),
     _t62_delayed_discard_defender),
    ("switch.flip-opponent-benched",
     re.compile(r"flip a coin\. if heads, switch (?:an?|\d+) of your opponent's "
                r"benched pokemon with (?:his or her|their) active pokemon\."),
     _t62_flip_opponent_switch_plain),
    ("discard.tool-attached-any-opponent",
     re.compile(r"discard a pokemon tool card attached to (?:an?|\d+) of your "
                r"opponent's pokemon\."), _t62_discard_tool_attached_any),
    ("draw.then-bottom-a-card",
     re.compile(r"draw (\d+) cards?\. then, put a card from your hand on the "
                r"bottom of your deck\."), _t62_draw_then_bottom_card),
    ("scale.per-special-energy-opponent-discard",
     re.compile(r"this attack does (\d+) damage times the number of special "
                r"energy cards in your opponent's discard pile\."),
     _t62_scale_per_special_energy_opponent_discard),
    ("search.trainer-afterward",
     re.compile(r"search your deck for a trainer card, reveal it, and put it into "
                r"your hand\. shuffle your deck afterward\."),
     _t62_search_trainer_afterward),
    # -- batch 61: the one-card tail, sixth pass ---------------------------
    ("bonus.asleep-usable",
     re.compile(r"this attack can be used even if this pokemon is asleep\. if "
                r"it is, this attack does (\d+) more damage\."),
     _t61_asleep_usable_bonus),
    ("mill.flip-per-heads-many",
     re.compile(r"flip (an?|\d+) coins?\. for each heads, discard (\d+) cards? "
                r"from the top of your opponent's deck\."),
     _t61_flip_mill_per_heads),
    ("condition.both-active-two",
     re.compile(r"both active pokemon are now (" + _CONDITION_WORDS + r") and ("
                + _CONDITION_WORDS + r")\."), _t61_both_active_conditions),
    ("lock.defender-if-typed-pair",
     re.compile(r"if the defending pokemon is a (" + _TYPE_WORDS + r") or (" +
                _TYPE_WORDS + r") pokemon, it can't attack during your "
                r"opponent's next turn\."), _t61_lock_defender_if_typed_pair),
    ("lock.heal-then-attack",
     re.compile(r"heal (\d+) damage from this pokemon\. this pokemon can't "
                r"attack during your next turn\."), _t61_heal_then_lock),
    ("attach.all-basic-hand-distributed",
     re.compile(r"attach as many basic energy cards as you like from your hand "
                r"to your pokemon in any way you like\."),
     _t61_attach_all_basic_hand),
    ("gate.opponent-ex-required",
     re.compile(r"if your opponent's active pokemon isn't a pokemon-ex, this "
                r"attack does nothing\."), _t61_gate_opponent_ex_present),
    ("bonus.optional-item-trade",
     re.compile(r"you may discard an item card from your hand\. if you do, this "
                r"attack does (\d+) more damage\."), _t61_optional_item_bonus),
    ("energy.move-defender-to-bench-any",
     re.compile(r"move an energy attached to your opponent's active pokemon to ("
                r"an?|\d+) of (?:his or her|their) benched pokemon\."),
     _t61_move_defender_energy_bench),
    ("heal.discard-typed-first",
     re.compile(r"discard a (" + _TYPE_WORDS + r") energy attached to this "
                r"pokemon and heal (\d+) damage from it\."),
     _t61_discard_typed_heal),
    ("attach.opponent-discard-energy",
     re.compile(r"attach (\d+) energy cards from your opponent's discard pile "
                r"to (?:his or her|their) pokemon in any way you like\."),
     _t61_attach_opponent_discard_energy),
    ("search.pokemon-to-hand-many",
     re.compile(r"search your deck for up to (\d+) pokemon, reveal them, and put "
                r"them into your hand\. shuffle your deck afterward\."),
     _t61_search_pokemon_to_hand),
    ("attach.typed-discard-distributed-many",
     re.compile(r"attach (\d+) (" + _TYPE_WORDS + r") energy cards from your "
                r"discard pile to your pokemon in any way you like\."),
     _t61_attach_typed_discard_distributed),
    ("attach.search-energy-to-self",
     re.compile(r"search your deck for (\d+) energy cards and attach them to "
                r"this pokemon\. shuffle your deck afterward\."),
     _t61_search_energy_attach_self),
    ("recover.typed-pokemon-many",
     re.compile(r"put (\d+) (" + _TYPE_WORDS + r") pokemon from your discard "
                r"pile into your hand\."), _t61_recover_typed_pokemon_many),
    ("condition.discard-typed-all-first",
     re.compile(r"discard all (" + _TYPE_WORDS + r") energy attached to this "
                r"pokemon\. your opponent's active pokemon is now (" +
                _CONDITION_WORDS + r")\."),
     _t61_discard_typed_all_then_condition),
    ("recoil.no-weakness-plain",
     re.compile(r"this pokemon does (\d+) damage to itself\. don't apply "
                r"weakness to this damage\."), _t61_recoil_no_weakness_plain),
    ("attach.up-to-basic-hand-self",
     re.compile(r"attach up to (\d+) basic energy cards from your hand to this "
                r"pokemon\."), _t61_attach_up_to_basic_hand_self),
    ("energy.move-all-self-to-bench",
     re.compile(r"you may move all energy from this pokemon to your benched "
                r"pokemon in any way you like\."), _t61_move_all_energy_to_bench),
    ("scale.per-opponent-typed",
     re.compile(r"this attack does (\d+) damage times the number of (" +
                _TYPE_WORDS + r") pokemon your opponent has in play\."),
     _t61_scale_per_opponent_typed),
    ("deck.peek-then-shuffle",
     re.compile(r"look at the top card of your deck\. then, you may shuffle your "
                r"deck\."), _t61_peek_then_optional_shuffle),
    ("counters.each-opponent-then-switch",
     re.compile(r"put (\d+) damage counters? on each of your opponent's "
                r"pokemon\. switch this pokemon with (?:an?|\d+) of your "
                r"benched pokemon\."), _t61_counters_then_switch),
    ("discard.special-chosen-many",
     re.compile(r"discard a special energy attached to (?:an?|\d+) of your "
                r"opponent's pokemon\."), _t61_discard_special_chosen),
    ("draw.then-optional-switch",
     re.compile(r"draw (\d+) cards?\. you may switch this pokemon with (?:an?|"
                r"\d+) of your benched pokemon\."), _t61_draw_then_optional_switch),
    ("deck.shuffle-basic-energy-back-many",
     re.compile(r"shuffle (\d+) basic energy cards from your discard pile into "
                r"your deck\."), _t61_shuffle_basic_energy_back_many),
    ("hand.reveal-discard-trainer",
     re.compile(r"your opponent reveals (?:his or her|their) hand\. discard a "
                r"trainer card you find there\."), _t61_reveal_hand_discard_trainer),
    ("attach.mill-typed-card",
     re.compile(r"discard the top card of your deck\. if that card is a (" +
                _TYPE_WORDS + r") energy card, attach it to this pokemon\."),
     _t61_mill_typed_attach_single),
    ("bonus.optional-typed-energy-all",
     re.compile(r"you may discard all (" + _TYPE_WORDS + r") energy attached to "
                r"this pokemon\. if you do, this attack does (\d+) more "
                r"damage\."), _t61_optional_typed_energy_bonus),
    ("discard.all-special-each-opponent",
     re.compile(r"discard all special energy attached to each of your opponent's "
                r"pokemon\."), _t61_discard_all_special_each_opponent),
    ("deck.look-through-shuffle",
     re.compile(r"look through your deck\. shuffle your deck afterward\."),
     _t61_look_through_deck),
    ("discard.defender-energy-if-ex",
     re.compile(r"if your opponent's active pokemon is a pokemon-ex, discard an "
                r"energy attached to that pokemon\."),
     _t61_discard_defender_energy_if_ex),
    ("recover.pokemon-many",
     re.compile(r"put (\d+) pokemon from your discard pile into your hand\."),
     _t61_recover_pokemon_many),
    ("bonus.more-prizes-left",
     re.compile(r"if you have more prize cards left than your opponent, this "
                r"attack does (\d+) more damage\."), _t61_bonus_more_prizes_left),
    ("search.typed-energy-to-hand-afterward",
     re.compile(r"search your deck for a (" + _TYPE_WORDS + r") energy card, "
                r"reveal it, and put it into your hand\. shuffle your deck "
                r"afterward\."), _t61_search_typed_energy_to_hand),
    ("switch.self-if-defender-ex",
     re.compile(r"if your opponent's active pokemon is a pokemon-ex, switch this "
                r"pokemon with (?:an?|\d+) of your benched pokemon\."),
     _t61_switch_if_defender_ex),
    ("scale.revealed-items",
     re.compile(r"each player reveals (?:his or her|their) hand\. this attack "
                r"does (\d+) damage times the number of item cards revealed\."),
     _t61_scale_revealed_items),
    ("bonus.mill-energy-self",
     re.compile(r"discard the top card of your deck\. if that card is an energy "
                r"card, this attack does (\d+) more damage\."),
     _t61_bonus_mill_energy),
    ("recover.typed-energy-many",
     re.compile(r"put (\d+) (" + _TYPE_WORDS + r") energy from your discard pile "
                r"into your hand\."), _t61_recover_typed_energy_many),
    ("pre.switch-opponent-forced",
     re.compile(r"before doing damage, have your opponent switch (?:his or her|"
                r"their) active pokemon with (?:an?|\d+) of (?:his or her|their) "
                r"benched pokemon\."), _t61_pre_switch_opponent_imperative),
    ("bounce.self-on-tails",
     re.compile(r"flip a coin\. if tails, return this pokemon and all cards "
                r"attached to it to your hand\."), _t61_flip_tails_return_self),
    ("scale.mill-per-energy-discarded",
     re.compile(r"discard the top (\d+) cards of your deck\. this attack does ("
                r"\d+) damage times the number of energy cards you "
                r"discarded\."), _t61_mill_scale_per_energy),
    ("mill.opponent-if-damaged",
     re.compile(r"if this pokemon has any damage counters on it, discard the top ("
                r"\d+) cards of your opponent's deck\."),
     _t61_mill_opponent_if_damaged),
    ("attach.discard-energy-any-pokemon",
     re.compile(r"attach an energy card from your discard pile to (?:an?|\d+) of "
                r"your pokemon\."), _t61_attach_discard_energy_any_pokemon),
    ("hand.opponent-bottom-card",
     re.compile(r"your opponent puts a card from (?:his or her|their) hand on the "
                r"bottom of (?:his or her|their) deck\."),
     _t61_opponent_hand_to_bottom),
    ("bonus.optional-typed-energy-return",
     re.compile(r"you may return a (" + _TYPE_WORDS + r") energy from this "
                r"pokemon to your hand\. if you do, this attack does (\d+) more "
                r"damage\."), _t61_optional_typed_energy_return_bonus),
    ("attach.hand-energy-bench-up-to",
     re.compile(r"attach up to (\d+) energy cards from your hand to (?:an?|\d+) "
                r"of your benched pokemon\."),
     _t61_attach_hand_energy_bench_up_to),
    ("condition.defender-then-strip-tools",
     re.compile(r"your opponent's active pokemon is now (" + _CONDITION_WORDS +
                r")\. discard all pokemon tool cards attached to that "
                r"pokemon\."), _t61_condition_then_strip_tools),
    ("draw.card-then-switch",
     re.compile(r"draw a card\. switch this pokemon with (?:an?|\d+) of your "
                r"benched pokemon\."), _t61_draw_then_switch),
    ("condition.flip-or-nothing",
     re.compile(r"flip a coin\. if heads, your opponent's active pokemon is now ("
                + _CONDITION_WORDS + r")\. if tails, this attack does "
                r"nothing\."), _t61_flip_condition_or_nothing),
    ("attach.optional-hand-energy-bench",
     re.compile(r"you may attach an energy card from your hand to (?:an?|\d+) of "
                r"your benched pokemon\."), _t61_optional_attach_hand_bench),
    ("bonus.per-evolution-in-play",
     re.compile(r"this attack does (\d+) more damage for each of your evolution "
                r"pokemon in play\."), _t61_bonus_per_evolution_in_play),
    ("bonus.mega-on-bench",
     re.compile(r"if you have any mega evolution pokemon on your bench, this "
                r"attack does (\d+) more damage\."), _t61_bonus_if_mega_on_bench),
    # -- batch 60: the one-card tail, fifth pass ---------------------------
    ("bonus.named-stadium",
     re.compile(r"if ([a-z][\w' -]*) is in play, this attack does (\d+) more "
                r"damage\."), _t60_bonus_named_stadium),
    ("delayed.ko-defender-after-asleep",
     re.compile(r"this pokemon is now asleep\. at the end of your opponent's "
                r"next turn, the defending pokemon will be knocked out\."),
     _t60_asleep_then_delayed_ko),
    ("attach.basic-each-typed-bench",
     re.compile(r"attach a basic energy card from your discard pile to each of "
                r"your basic benched (" + _TYPE_WORDS + r") pokemon\."),
     _t60_attach_basic_each_typed_bench),
    ("bonus.per-other-in-play",
     re.compile(r"this attack does (\d+) more damage for each other pokemon in "
                r"play \(both yours and your opponent's\)\."),
     _t60_bonus_per_other_in_play),
    ("bonus.self-low-hp",
     re.compile(r"if this pokemon's remaining hp is (\d+) or less, this attack "
                r"does (\d+) more damage\."), _t60_bonus_low_hp),
    ("lock.discard-energy-then",
     re.compile(r"discard an energy from this pokemon\. it can't attack during "
                r"your next turn\."), _t60_discard_energy_then_lock),
    ("lock.heal-all-then",
     re.compile(r"heal all damage from this pokemon\. it can't attack during "
                r"your next turn\."), _t60_heal_all_then_lock_plain),
    ("scale.flip-per-own-in-play-any",
     re.compile(r"flip a coin for each pokemon you have in play\. this attack "
                r"does (\d+) damage for each heads\."),
     _t60_flip_per_own_in_play_any),
    ("heal.flip-until-tails-self",
     re.compile(r"flip a coin until you get tails\. for each heads, heal (\d+) "
                r"damage from this pokemon\."), _t60_flip_until_heal_self),
    ("energy.move-typed-self-to-bench",
     re.compile(r"move (an?|\d+) (" + _TYPE_WORDS + r") energy from this pokemon "
                r"to (?:an?|\d+) of your benched pokemon\."),
     _t60_move_typed_self_to_bench),
    ("scale.per-tools-all-pokemon",
     re.compile(r"this attack does (\d+) damage for each pokemon tool card "
                r"attached to all pokemon\."), _t60_scale_per_tools_all),
    ("deck.shuffle-typed-pokemon-back",
     re.compile(r"shuffle (an?|\d+) (" + _TYPE_WORDS + r") pokemon from your "
                r"discard pile into your deck\."),
     _t60_shuffle_typed_pokemon_back),
    ("bounce.opponent-active",
     re.compile(r"your opponent puts their active pokemon and all cards attached "
                r"to it into their hand\."), _t60_opponent_bounce_active),
    ("lock.flip-trainers-their",
     re.compile(r"flip a coin\. if heads, your opponent can't play any trainer "
                r"cards from their hand during their next turn\."),
     _t60_flip_trainer_lock_their),
    ("scale.per-basic-energy-all-own",
     re.compile(r"this attack does (\d+) damage times the amount of basic energy "
                r"attached to all of your pokemon\."),
     _t60_per_basic_energy_all_own),
    ("search.discard-cards",
     re.compile(r"search your deck for up to (\d+) pokemon and discard them\. "
                r"then, shuffle your deck\."), _t60_search_and_discard),
    ("bonus.evolved-this-turn",
     re.compile(r"if this pokemon evolved from ([a-z][\w' -]*) during this "
                r"turn, this attack does (\d+) more damage\."),
     _t60_bonus_evolved_this_turn),
    ("scale.capped-per-pokemon-discard",
     re.compile(r"this attack does (\d+) damage for each pokemon in your discard "
                r"pile\. you can't do more than (\d+) damage in this way\."),
     _t60_capped_per_pokemon_in_discard),
    ("deck.reveal-supporter-to-bottom",
     re.compile(r"your opponent reveals their hand\. choose a supporter card you "
                r"find there and put it on the bottom of their deck\."),
     _t60_reveal_supporter_to_bottom),
    ("lock.flip-items",
     re.compile(r"flip a coin\. if heads, during your opponent's next turn, they "
                r"can't play any item cards from their hand\."),
     _t60_flip_lock_items),
    ("scale.flip-per-typed-energy-self",
     re.compile(r"flip a coin for each (" + _TYPE_WORDS + r") energy attached to "
                r"this pokemon\. this attack does (\d+) damage for each "
                r"heads\."), _t60_flip_per_typed_energy_self),
    ("mill.flip-opponent-top",
     re.compile(r"flip a coin\. if heads, discard the top card of your "
                r"opponent's deck\."), _t60_flip_mill_opponent_card),
    ("bonus.typed-energy-threshold",
     re.compile(r"if this pokemon has (\d+) or more (" + _TYPE_WORDS + r") energy "
                r"attached, this attack does (\d+) more damage\."),
     _t60_bonus_typed_energy_threshold),
    ("search.basic-typed-energy-attach",
     re.compile(r"search your deck for a basic (" + _TYPE_WORDS + r") energy card "
                r"and attach it to (?:an?|\d+) of your pokemon\. then, shuffle "
                r"your deck\."), _t60_search_basic_energy_attach_typed),
    ("energy.move-typed-any",
     re.compile(r"you may move any amount of (" + _TYPE_WORDS + r") energy from "
                r"your pokemon to your other pokemon in any way you like\."),
     _t60_move_typed_energy_any),
    ("hand.discard-both-players",
     re.compile(r"discard a card from your hand\. if you do, your opponent "
                r"discards a card from their hand\."),
     _t60_discard_hand_opponent_discards),
    ("gate.discard-a-card",
     re.compile(r"discard a card from your hand\. if you can't, this attack does "
                r"nothing\."), _t60_gate_discard_hand),
    ("search.supporters",
     re.compile(r"search your deck for up to (\d+) supporter cards, reveal them, "
                r"and put them into your hand\. then, shuffle your deck\."),
     _t60_search_supporters),
    ("attach.typed-bench-up-to",
     re.compile(r"attach up to (\d+) basic (" + _TYPE_WORDS + r") energy cards "
                r"from your discard pile to (?:an?|\d+) of your benched "
                r"pokemon\."), _t60_attach_typed_bench_up_to),
    ("bonus.prize-count",
     re.compile(r"if your opponent has exactly (\d+) or (\d+) prize cards? "
                r"remaining, this attack does (\d+) more damage\."),
     _t60_bonus_prize_count),
    ("hand.flip-until-random-discard",
     re.compile(r"flip a coin until you get tails\. for each heads, discard a "
                r"random card from your opponent's hand\."),
     _t60_flip_until_random_discard),
    ("recoil.flip-tails-plain",
     re.compile(r"flip a coin\. if tails, this pokemon also does (\d+) damage "
                r"to itself\."), _t60_flip_tails_recoil_plain),
    ("recover.items-and-tools",
     re.compile(r"put up to (\d+) in any combination of item cards and pokemon "
                r"tool cards from your discard pile into your hand\."),
     _t60_recover_items_and_tools),
    ("attach.typed-basic-from-discard",
     re.compile(r"attach a basic (" + _TYPE_WORDS + r") energy card from your "
                r"discard pile to this pokemon\."), _t60_attach_typed_basic_self),
    ("gate.condition-absent",
     re.compile(r"if this pokemon isn't (" + _CONDITION_WORDS + r"), this attack "
                r"does nothing\."), _t60_gate_condition_absent),
    ("gate.evolved-this-turn-nothing",
     re.compile(r"if this pokemon evolved during this turn, this attack does "
                r"nothing\."), _t60_gate_evolved_this_turn),
    ("scale.per-energy-opponent-discard",
     re.compile(r"this attack does (\d+) damage for each energy card in your "
                r"opponent's discard pile\."),
     _t60_scale_per_energy_opponent_discard),
    ("energy.flip-move-defender",
     re.compile(r"flip a coin\. if heads, move an energy from your opponent's "
                r"active pokemon to (?:an?|\d+) of their benched pokemon\."),
     _t60_flip_move_defender_energy),
    ("gate.damaged-threshold-nothing",
     re.compile(r"if this pokemon has (\d+) or more damage counters on it, this "
                r"attack does nothing\."), _t60_gate_damaged_only),
    ("attach.typed-hand-bench-many",
     re.compile(r"attach a basic (" + _TYPE_WORDS + r") energy card from your "
                r"hand to (?:an?|(\d+)) of your benched pokemon\."),
     _t60_attach_typed_hand_bench_many),
    ("switch.asleep-new-active",
     re.compile(r"switch in (?:an?|\d+) of your opponent's benched pokemon to the "
                r"active spot\. the new active pokemon is now asleep\."),
     _t60_switch_then_asleep),
    ("deck.peek-optional-bottom",
     re.compile(r"look at the top card of your deck\. you may put that card on "
                r"the bottom of your deck\."), _t60_optional_bottom_of_deck),
    ("attach.typed-hand-any-distributed",
     re.compile(r"you may attach any number of basic (" + _TYPE_WORDS + r") "
                r"energy cards from your hand to your pokemon in any way you "
                r"like\."), _t60_attach_typed_hand_any_distributed),
    ("energy.move-any-own-distributed",
     re.compile(r"you may move any amount of energy from your pokemon to your "
                r"other pokemon in any way you like\."),
     _t60_move_energy_any_own),
    ("bonus.opponent-typed-in-play",
     re.compile(r"if your opponent has any (" + _TYPE_WORDS + r") pokemon in "
                r"play, this attack does (\d+) more damage\."),
     _t60_bonus_opponent_typed),
    ("energy.flip-tails-discard-each",
     re.compile(r"flip (an?|\d+) coins?\. for each tails, discard an energy "
                r"from this pokemon\."), _t60_flip_tails_discard_energy_self),
    ("recoil.per-counter",
     re.compile(r"this pokemon also does (\d+) damage to itself for each damage "
                r"counter on it\."), _t60_recoil_per_counter),
    ("recover.typed-basic-energy-one",
     re.compile(r"put a basic (" + _TYPE_WORDS + r") energy card from your "
                r"discard pile into your hand\."), _t60_recover_basic_energy_one),
    ("attach.hand-energy-then-heal",
     re.compile(r"attach an energy card from your hand to this pokemon\. if you "
                r"do, heal (\d+) damage from this pokemon\."),
     _t60_attach_hand_energy_heal),
    ("bonus.optional-self-lock",
     re.compile(r"you may do (\d+) more damage\. if you do, during your next "
                r"turn, this pokemon can't attack\."),
     _t60_optional_bonus_self_lock),
    ("gate.typed-discard-hand",
     re.compile(r"discard a basic (" + _TYPE_WORDS + r") energy card from your "
                r"hand\. if you can't, this attack does nothing\."),
     _t60_gate_typed_discard),
    ("ko.defender-if-special-energy",
     re.compile(r"if your opponent's active pokemon has any special energy "
                r"attached, it is knocked out\."),
     _t60_ko_if_defender_special_energy),
    ("peek.opponent-then-shuffle",
     re.compile(r"look at the top card of your opponent's deck\. you may have "
                r"your opponent shuffle their deck\."), _t60_peek_optional_shuffle),
    ("scale.per-ex-and-v",
     re.compile(r"this attack does (\d+) damage for each of your opponent's "
                r"pokemon ex and pokemon v in play\."), _t60_scale_per_ex_and_v),
    ("scale.per-special-energy-opponent-all",
     re.compile(r"this attack does (\d+) damage for each special energy attached "
                r"to all of your opponent's pokemon\."),
     _t60_scale_per_special_energy_opponent),
    ("bonus.more-energy-than-defender",
     re.compile(r"if this pokemon has more energy attached than your opponent's "
                r"active pokemon, this attack does (\d+) more damage\."),
     _t60_bonus_more_energy_than_defender),
    ("condition.prize-gated",
     re.compile(r"if you have exactly (\d+) prize cards? remaining, your "
                r"opponent's active pokemon is now (" + _CONDITION_WORDS +
                r")\."), _t60_prize_gate_condition),
    ("ko.both-active",
     re.compile(r"both active pokemon are knocked out\."), _t60_ko_both_active),
    ("counters.each-with-ability",
     re.compile(r"put (\d+) damage counters on each pokemon that has an ability "
                r"\(both yours and your opponent's\)\."),
     _t60_counters_each_with_ability),
    ("discard.tools-and-special-first",
     re.compile(r"before doing damage, discard all pokemon tools and special "
                r"energy from your opponent's active pokemon\."),
     _t60_strip_tools_and_special),
    # -- batch 59: the one-card tail, fourth pass -------------------------
    ("switch.gust-then-condition",
     re.compile(r"switch the defending pokemon with (?:an?|\d+) of your "
                r"opponent's benched pokemon\. the new defending pokemon is now ("
                + _CONDITION_WORDS + r")\."), _t59_gust_then_condition),
    ("retreat.tax-defender",
     re.compile(r"the retreat cost for the defending pokemon is (\d+) until the "
                r"end of your next turn\."), _t59_retreat_tax_defender),
    ("condition.choose-burned-poisoned",
     re.compile(r"choose either burned or poisoned\. the defending pokemon is "
                r"now affected by that special condition\."),
     _t59_choose_condition),
    ("counters.distribute-any",
     re.compile(r"put (\d+) damage counters on any pokemon \(both yours and "
                r"your opponent's\) in any way you like\."),
     _t59_distribute_counters),
    ("counters.on-own-bench",
     re.compile(r"put (\d+) damage counters? on (?:an?|(\d+)) of your benched "
                r"pokemon\."), _t59_counters_on_own_bench),
    ("draw.per-basic-opponent",
     re.compile(r"draw a card for each of your opponent's pokemon that isn't an "
                r"evolved pokemon\."), _t59_draw_per_basic_opponent),
    ("damage.minus-per-defender-energy",
     re.compile(r"does (\d+) damage minus (\d+) damage for each energy "
                r"attached to the defending pokemon\."),
     _t59_minus_per_defender_energy),
    ("heal.discard-hand-for-heal",
     re.compile(r"you may discard (\d+) cards from your hand\. if you do, "
                r"remove (\d+) damage counters from (?:an?|\d+) of your "
                r"pokemon\."), _t59_discard_cards_heal),
    ("damage.minus-per-hand",
     re.compile(r"does (\d+) damage minus (\d+) damage for each card in your "
                r"hand\."), _t59_minus_per_hand),
    ("bench.search-typed-basic",
     re.compile(r"search your deck for up to (\d+) (" + _TYPE_WORDS + r") basic "
                r"pokemon and put them onto your bench\. shuffle your deck "
                r"afterward\."), _t59_search_typed_basic_bench),
    ("attach.typed-discard-to-many-any",
     re.compile(r"search your discard pile for a (" + _TYPE_WORDS + r") energy "
                r"card and attach it to (?:an?|\d+) of your pokemon\."),
     _t59_attach_typed_from_discard),
    ("bonus.self-damaged-threshold",
     re.compile(r"if this pokemon already has (\d+) or more damage counters on "
                r"it, this attack does (\d+) damage plus (\d+) more damage\."),
     _t59_bonus_if_damaged_self),
    ("attach.typed-energy-up-to-self-any",
     re.compile(r"search your discard pile for up to (\d+) (" + _TYPE_WORDS +
                r") energy cards and attach them to this pokemon\."),
     _t59_typed_energy_from_discard_self),
    ("bonus.defender-stage-plain",
     re.compile(r"if the defending pokemon is a stage (\d+) pokemon, this "
                r"attack does (\d+) damage plus (\d+) more damage\."),
     _t59_bonus_defender_stage_plain),
    ("flip.bonus-comma",
     re.compile(r"flip a coin, if heads this attack does (\d+) damage plus (\d+) "
                r"more damage\."), _t59_flip_bonus_comma),
    ("pre.switch-opponent-optional",
     re.compile(r"before doing damage, you may switch your opponent's active "
                r"pokemon with (?:an?|\d+) of (?:his or her|their) benched "
                r"pokemon\."), _t59_pre_switch_opponent),
    ("gate.stadium-present-nothing-else",
     re.compile(r"if there is any stadium card in play, this attack does "
                r"nothing\."), _t59_gate_stadium_present),
    ("attach.flip-discard-energy-any",
     re.compile(r"flip a coin\. if heads, search your discard pile for an energy "
                r"card and attach it to this pokemon\."),
     _t59_flip_attach_discard_energy),
    ("draw.named-in-play-instead",
     re.compile(r"draw a card\. if you have ([a-z][\w' -]*) in play, draw (\d+) "
                r"cards instead\."), _t59_draw_named_in_play),
    ("discard.two-typed-plain",
     re.compile(r"discard a (" + _TYPE_WORDS + r") and a (" + _TYPE_WORDS +
                r") energy attached to this pokemon\."),
     _t59_discard_two_typed_plain),
    ("gate.cannot-discard-basics",
     re.compile(r"discard (an?|\d+) basic energy cards? attached to this "
                r"pokemon\. \(if you can't discard cards, this attack does "
                r"nothing\.?\)?"), _t59_gate_cant_discard),
    ("heal.pre-damage-defender-plain",
     re.compile(r"before doing damage, remove (\d+) damage counters from the "
                r"defending pokemon\."), _t59_pre_heal_defender),
    ("heal.evolved-this-turn-all",
     re.compile(r"if this pokemon evolved from ([a-z][\w' -]*) during this "
                r"turn, remove all damage counters from this pokemon\."),
     _t59_evolved_this_turn_heal_all),
    ("condition.evolved-this-turn",
     re.compile(r"if this pokemon evolved from ([a-z][\w' -]*) during this "
                r"turn, the defending pokemon is now (" + _CONDITION_WORDS +
                r")\."), _t59_evolved_this_turn_condition),
    ("heal.self-recover",
     re.compile(r"recover (\d+) damage from this pokemon\."),
     _t59_heal_self_amount),
    ("recover.supporter",
     re.compile(r"search your discard pile for a supporter card, show it to your "
                r"opponent, and put it into your hand\."), _t59_recover_supporter),
    ("attach.mill-typed-energy",
     re.compile(r"discard the top (\d+) cards of your deck\. if any of those "
                r"cards are (" + _TYPE_WORDS + r") energy cards, attach them to "
                r"this pokemon\."), _t59_mill_attach_typed),
    ("bench.basic-from-each-discard",
     re.compile(r"put a basic pokemon from each player's discard pile onto its "
                r"owner's bench\."), _t59_bench_basic_each_side),
    ("bonus.lost-zone-typed",
     re.compile(r"if you have any (" + _TYPE_WORDS + r") energy cards in the "
                r"lost zone, this attack does (\d+) more damage\."),
     _t59_bonus_lost_zone_typed),
    ("gate.no-stadium-nothing",
     re.compile(r"if you don't have a stadium card in play, this attack does "
                r"nothing\."), _t59_gate_no_stadium),
    ("switch.bench-then-confuse",
     re.compile(r"switch (?:an?|\d+) of your opponent's benched pokemon with "
                r"their active pokemon\. the new active pokemon is now "
                r"confused\."), _t59_switch_then_confuse),
    ("energy.move-bench-to-self-any",
     re.compile(r"move as many energy as you like from your benched pokemon to "
                r"this pokemon\."), _t59_move_bench_energy_self),
    ("discard.opponent-tools-up-to-any",
     re.compile(r"discard up to (an?|\d+) pokemon tool cards? attached to your "
                r"opponent's pokemon\."), _t59_discard_opponent_tools),
    ("recoil.flip-self-damage",
     re.compile(r"flip a coin\. if heads, this pokemon does (\d+) damage to "
                r"itself\."), _t59_flip_recoil),
    ("heal.bench-then-discard-energy",
     re.compile(r"heal (\d+) damage from each of your benched pokemon\. then, "
                r"discard (\d+) energy attached to this pokemon\."),
     _t59_heal_bench_then_discard),
    ("scale.per-opponent-in-play",
     re.compile(r"this attack does (\d+) damage times the number of pokemon your "
                r"opponent has in play\."), _t59_per_opponent_in_play),
    ("bonus.defender-no-energy",
     re.compile(r"if your opponent's active pokemon has no energy attached to "
                r"it, this attack does (\d+) more damage\."),
     _t59_bonus_defender_no_energy),
    ("search.items-to-hand",
     re.compile(r"search your deck for up to (\d+) item cards, reveal them, and "
                r"put them into your hand\. shuffle your deck afterward\."),
     _t59_search_items),
    ("draw.bench-named-more",
     re.compile(r"draw a card\. if ([a-z][\w' -]*) is on your bench, draw (\d+) "
                r"more cards?\."), _t59_draw_bench_named_more),
    ("bonus.mill-trainer-opponent",
     re.compile(r"discard the top card of your opponent's deck\. if that card is "
                r"a trainer card, this attack does (\d+) more damage\."),
     _t59_mill_opponent_bonus_if_trainer),
    ("bonus.optional-mill-both",
     re.compile(r"you may do (\d+) more damage\. if you do, discard the top ("
                r"\d+) cards of each player's deck\."),
     _t59_optional_bonus_mill_both),
    ("heal.both-active",
     re.compile(r"heal (\d+) damage from both active pokemon\."),
     _t59_heal_both_active),
    ("recover.stadiums-many",
     re.compile(r"put (\d+) stadium cards from your discard pile into your "
                r"hand\."), _t59_recover_stadiums),
    ("bonus.per-opponent-ex",
     re.compile(r"this attack does (\d+) more damage for each of your "
                r"opponent's pokemon-ex\."), _t59_bonus_per_opponent_ex),
    ("scale.per-defender-typed-energy",
     re.compile(r"this attack does (\d+) more damage for each (" + _TYPE_WORDS +
                r") energy attached to your opponent's active pokemon\."),
     _t59_bonus_per_defender_typed_energy),
    ("attach.typed-discard-each-bench-chosen",
     re.compile(r"choose (?:an?|\d+) of your benched pokemon\. attach a (" +
                _TYPE_WORDS + r") energy card from your discard pile to each of "
                r"those pokemon\."), _t59_attach_typed_bench_chosen),
    ("attach.hand-basic-self-simple",
     re.compile(r"attach a basic energy card from your hand to this pokemon\."),
     _t59_attach_hand_basic_self),
    ("bonus.defender-type-plus",
     re.compile(r"if the defending pokemon is a (" + _TYPE_WORDS + r") pokemon, "
                r"this attack does (\d+) damage plus (\d+) more damage\."),
     _t59_bonus_defender_type_plus),
    ("recover.typed-pokemon",
     re.compile(r"put a (" + _TYPE_WORDS + r") pokemon from your discard pile "
                r"into your hand\."), _t59_recover_typed_pokemon),
    ("discard.defender-tools-all",
     re.compile(r"discard all pokemon tool cards from your opponent's active "
                r"pokemon\."), _t59_strip_defender_tools),
    ("energy.move-defender-to-bench",
     re.compile(r"move an energy from your opponent's active pokemon to (?:an?|"
                r"\d+) of their benched pokemon\."),
     _t59_move_defender_energy_to_bench),
    ("hand.return-bench-pokemon",
     re.compile(r"put (\d+) of your benched pokemon and all cards attached to it "
                r"into your hand\."), _t59_return_bench_to_hand),
    ("heal.self-no-retreat-simple",
     re.compile(r"heal (\d+) damage from this pokemon\. it can't retreat during "
                r"your next turn\."), _t59_heal_self_no_retreat_simple),
    ("attach.typed-discard-bench-many",
     re.compile(r"attach (\d+) (" + _TYPE_WORDS + r") energy cards from your "
                r"discard pile to (?:an?|\d+) of your benched pokemon\."),
     _t59_attach_typed_discard_bench),
    ("scale.per-own-typed-holder",
     re.compile(r"this attack does (\d+) more damage for each of your pokemon "
                r"that has any (" + _TYPE_WORDS + r") energy attached to it\."),
     _t59_bonus_per_own_typed_energy),
    ("attach.hand-energy-bench",
     re.compile(r"attach an energy card from your hand to (?:an?|\d+) of your "
                r"benched pokemon\."), _t59_attach_hand_energy_bench),
    ("recover.energy-cards",
     re.compile(r"put (an?|\d+) energy cards from your discard pile into your "
                r"hand\."), _t59_recover_energy_cards),
    ("condition.defender-typed-energy",
     re.compile(r"if your opponent's active pokemon has any (" + _TYPE_WORDS +
                r") energy attached to it, it is now (" + _CONDITION_WORDS +
                r")\."), _t59_condition_if_defender_typed_energy),
    ("hand.discard-all",
     re.compile(r"discard your hand\."), _t59_discard_hand),
    ("bonus.optional-energy-trade",
     re.compile(r"you may discard an energy from this pokemon\. if you do, this "
                r"attack does (\d+) more damage\."), _t59_optional_energy_bonus),
    ("scale.per-basic-energy-self",
     re.compile(r"this attack does (\d+) more damage times the amount of basic "
                r"energy attached to this pokemon\."),
     _t59_bonus_per_basic_energy_self),
    ("scale.per-opponent-ability",
     re.compile(r"this attack does (\d+) more damage for each of your "
                r"opponent's pokemon that has an ability\."),
     _t59_bonus_per_opponent_ability),
    ("draw.per-retreat-cost",
     re.compile(r"draw a card for each of your pokemon in play that has a retreat "
                r"cost of exactly (\d+)\."), _t59_draw_per_retreat_cost),
    ("search.trainer-to-hand",
     re.compile(r"search your deck for a trainer card, reveal it, and put it into "
                r"your hand\. then, shuffle your deck\."), _t59_search_trainer),
    ("switch.self-if-defender-evolved",
     re.compile(r"if your opponent's active pokemon is an evolution pokemon, "
                r"switch this pokemon with (?:an?|\d+) of your benched "
                r"pokemon\."), _t59_switch_if_evolved),
    ("bonus.prizes-equal",
     re.compile(r"if each player has exactly (\d+) prize cards? remaining, this "
                r"attack does (\d+) more damage\."), _t59_bonus_if_prizes_equal),
    ("discard.tool-chosen-opponent",
     re.compile(r"discard a pokemon tool card from (?:an?|\d+) of your "
                r"opponent's pokemon\."), _t59_discard_tool_chosen),
    # -- batch 58: the one-card tail, third pass --------------------------
    ("gate.all-tails-nothing",
     re.compile(r"flip (an?|\d+) coins?\. if (?:\d+ or )?both of them are "
                r"tails, this attack does nothing\."), _gate_all_tails_nothing),
    ("condition.flip-choice",
     re.compile(r"flip a coin\. if heads, the defending pokemon is now asleep, "
                r"confused, paralyzed, or poisoned \(your choice\)\."),
     _flip_defender_condition_choice),
    ("heal.flip-if-damaged",
     re.compile(r"if this pokemon has any damage counters on it, flip a coin\. "
                r"if heads, remove (\d+) of those damage counters\."),
     _flip_heal_if_damaged),
    ("attach.typed-energy-discard-self-any",
     re.compile(r"take (an?|\d+) (" + _TYPE_WORDS + r") energy card from your "
                r"discard pile and attach it to this pokemon\."),
     _typed_energy_discard_to_self),
    ("condition.flip-any-heads",
     re.compile(r"flip (an?|\d+) coins?\. if (?:\d+ or )?both of them are "
                r"heads, the defending pokemon is now (" + _CONDITION_WORDS +
                r")\."), _flip_condition_heads_any),
    ("topdeck.opponent-discard-on-flip",
     re.compile(r"flip a coin\. if heads, choose a card from your opponent's "
                r"discard pile and put it on top of (?:his or her|their) "
                r"deck\."), _flip_topdeck_opponent_discard),
    ("switch.flip-self-with-bench",
     re.compile(r"if you have any benched pokemon, flip a coin\. if heads, "
                r"switch this pokemon with (?:an?|\d+) of your benched "
                r"pokemon\."), _flip_switch_self_b58),
    ("recover.flip-typed-energy-per-heads",
     re.compile(r"flip (an?|\d+) coins?\. for each heads, if you have a (" +
                _TYPE_WORDS + r") energy card in your discard pile, put it into "
                r"your hand\."), _flip_recover_energy_per_heads),
    ("recoil.then-discard-stadium",
     re.compile(r"this pokemon does (\d+) damage to itself\. if there is a "
                r"stadium card in play, discard it\."),
     _recoil_then_discard_stadium),
    ("heal.both-sides-damaged",
     re.compile(r"you and your opponent remove (\d+) damage counter from each "
                r"of your pokemon with damage counters on them\."),
     _heal_both_sides_damaged),
    ("condition.flip-heads-or-tails",
     re.compile(r"flip a coin\. if heads, the defending pokemon is now (" +
                _CONDITION_WORDS + r"); if tails, the defending pokemon is now ("
                + _CONDITION_WORDS + r")\."), _flip_defender_or_condition),
    ("recoil.then-flip-condition",
     re.compile(r"this pokemon does (\d+) damage to itself\. flip a coin\. if "
                r"heads, the defending pokemon is now (" + _CONDITION_WORDS +
                r")\."), _recoil_then_flip_condition),
    ("condition.flip-two",
     re.compile(r"flip (an?|\d+) coins?\. if both are heads, the defending "
                r"pokemon is now (" + _CONDITION_WORDS + r") and (" +
                _CONDITION_WORDS + r")\."), _flip_two_conditions_b58),
    ("deck.flip-shuffle-self",
     re.compile(r"flip a coin\. if heads, shuffle this pokemon and all cards "
                r"attached to it into your deck \(after doing damage\)\."),
     _flip_shuffle_self_into_deck),
    ("draw.flip-plain",
     re.compile(r"flip a coin\. if heads, draw (\d+) cards?\."),
     _flip_draw_plain),
    ("damage.base-doubled-if-defender-type",
     re.compile(r"if the defending pokemon is (" + _TYPE_WORDS + r"), this "
                r"attack's base damage is doubled\."),
     _base_doubled_if_defender_type),
    ("energy.flip-tails-discard-all-cards",
     re.compile(r"flip a coin\. if tails, discard all energy cards attached to "
                r"this pokemon\."), _flip_tails_discard_all_energy_cards),
    ("lock.flip-tails-self-next",
     re.compile(r"flip a coin\. if tails, you can't use this attack during your "
                r"next turn\."), _flip_tails_self_lock_b58),
    ("retreat.flip-defender-cannot",
     re.compile(r"flip a coin\. if heads, the defending pokemon can't retreat "
                r"during your opponent's next turn\."),
     _flip_defender_no_retreat),
    ("counters.flip-until-target-hp-and",
     re.compile(r"flip a coin\. if heads, put a number of damage counters on the "
                r"defending pokemon so that its remaining hp are (\d+)\."),
     _flip_counters_until_hp_b58),
    ("draw.each-player-both",
     re.compile(r"each player draws (an?|\d+) cards?\."), _each_player_draws_b58),
    ("flip.all-heads-base-plus",
     re.compile(r"flip (an?|\d+) coins?\. if both of them are heads, this "
                r"attack does (\d+) damage plus (\d+) more damage\."),
     _flip_all_heads_base_plus),
    ("draw.per-typed-energy-all",
     re.compile(r"draw a card for each (" + _TYPE_WORDS + r") energy attached to "
                r"all of your pokemon\."), _draw_per_typed_energy_all),
    ("flip.bonus-or-recoil",
     re.compile(r"if heads, this attack does (\d+) damage plus (\d+) more "
                r"damage\. if tails, this pokemon does (\d+) damage to "
                r"itself\."), _flip_bonus_or_recoil),
    ("draw.per-typed-in-play",
     re.compile(r"draw a card for each of your (" + _TYPE_WORDS + r") pokemon in "
                r"play\."), _draw_per_typed_in_play),
    ("condition.then-heal-self",
     re.compile(r"the defending pokemon is now (" + _CONDITION_WORDS +
                r")\. remove (\d+) damage counters from this pokemon\."),
     _condition_then_heal_self),
    ("hand.flip-random-discard-opponent",
     re.compile(r"flip (an?|\d+) coins?\. for each heads, discard a card from "
                r"your opponent's hand without looking\."),
     _discard_random_opponent_hand),
    ("condition.then-flip-second",
     re.compile(r"the defending pokemon is now (" + _CONDITION_WORDS +
                r")\. flip a coin\. if heads, the defending pokemon is also (" +
                _CONDITION_WORDS + r")\."), _condition_then_flip_second),
    ("damage.base-swap-if-opponent-typed",
     re.compile(r"if your opponent has any (" + _TYPE_WORDS + r") pokemon in "
                r"play, this attack's base damage is (\d+) instead of (\d+)\."),
     _base_swap_if_opponent_typed),
    ("mill.opponent-then-heal-amount",
     re.compile(r"discard the top card of your opponent's deck\. then, remove ("
                r"\d+) damage counters from this pokemon\."),
     _mill_opponent_then_heal_self),
    ("recover.typed-energy-distributed",
     re.compile(r"search your discard pile for up to (\d+) (" + _TYPE_WORDS +
                r") energy cards and attach them to your pokemon in any way you "
                r"like\."), _recover_typed_energy_distributed),
    ("recover.typed-energy-to-many",
     re.compile(r"search your discard pile for up to (\d+) (" + _TYPE_WORDS +
                r") energy cards and attach them to (?:an?|\d+) of your "
                r"pokemon\."), _recover_typed_energy_to_many),
    ("draw.discard-typed-hand-then",
     re.compile(r"discard a (" + _TYPE_WORDS + r") energy card from your hand\. "
                r"then, draw (\d+) cards?\."), _discard_typed_hand_then_draw),
    ("scale.flip-per-typed-in-play",
     re.compile(r"flip a coin for each (" + _TYPE_WORDS + r") pokemon you have "
                r"in play\. this attack does (\d+) damage times the number of "
                r"heads\."), _flip_per_typed_in_play),
    ("heal.each-own-with-energy",
     re.compile(r"remove (\d+) damage counters from each of your pokemon that "
                r"has any energy attached to it\."), _heal_each_with_energy),
    ("switch.flip-defender-with-bench",
     re.compile(r"flip a coin\. if heads, switch the defending pokemon with ("
                r"an?|\d+) of your opponent's benched pokemon\."),
     _flip_switch_defender),
    ("heal.all-conditions-and-damage",
     re.compile(r"remove all special conditions and (\d+) damage counters from "
                r"this pokemon\."), _cure_all_and_heal),
    ("scale.flip-per-own-in-play",
     re.compile(r"flip a coin for each of your pokemon in play\. this attack "
                r"does (\d+) damage times the number of heads\."),
     _flip_per_own_in_play),
    ("flip.bonus-plain",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage plus ("
                r"\d+) damage\."), _flip_bonus_plain),
    ("bonus.per-evolved-from",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each of your "
                r"pokemon in play that evolves from ([a-z][\w' -]*)\."),
     _bonus_per_evolved_from),
    ("hand.discard-gate",
     re.compile(r"discard (an?|\d+) cards? from your hand\. \(if you can't "
                r"discard (?:an?|\d+) cards? from your hand, this attack does "
                r"nothing\.\)"), _discard_hand_gate),
    ("mill.self-then-heal",
     re.compile(r"discard the top card of your deck\. then, remove (\d+) "
                r"damage counters from this pokemon\."), _mill_self_then_heal),
    ("condition.defender-no-retreat-simple",
     re.compile(r"the defending pokemon is now (" + _CONDITION_WORDS + r")(?:,)? "
                r"and can't retreat during your opponent's next turn\."),
     _condition_and_defender_no_retreat),
    ("hand.flip-opponent-discards-all",
     re.compile(r"flip (an?|\d+) coins?\. if both of them are heads, your "
                r"opponent discards all cards? from (?:his or her|their) "
                r"hand\."), _flip_opponent_discards_hand),
    ("condition.then-switch-self",
     re.compile(r"the defending pokemon is now (" + _CONDITION_WORDS + r")\. "
                r"switch this pokemon with (?:an?|\d+) of your benched "
                r"pokemon\."), _condition_then_switch_self),
    ("condition.two-then-heal-self",
     re.compile(r"the defending pokemon is now (" + _CONDITION_WORDS + r") and ("
                + _CONDITION_WORDS + r")\. remove (\d+) damage counters from "
                r"this pokemon\."), _two_conditions_then_heal_self),
    ("heal.flip-self-per-heads-any",
     re.compile(r"flip (an?|\d+) coins?\. for each heads, remove (\d+) damage "
                r"counters from this pokemon\."), _flip_heal_self_per_heads),
    ("hand.flip-look-discard",
     re.compile(r"flip a coin\. if heads, look at your opponent's hand, choose ("
                r"an?|\d+) card,? and discard it\."), _flip_look_discard_hand),
    ("counters.per-hand-card",
     re.compile(r"place (\d+) damage counters on your opponent's active pokemon "
                r"for each card in your hand\."), _counters_per_hand_card),
    ("heal.flip-all-heads-all",
     re.compile(r"flip (an?|\d+) coins?\. if both of them are heads, heal all "
                r"damage from (?:an?|\d+) of your pokemon\."),
     _flip_all_heads_heal_all),
    ("bonus.typed-energy-in-play",
     re.compile(r"if you have at least (\d+) (" + _TYPE_WORDS + r") energy in "
                r"play, this attack does (\d+) more damage\."),
     _bonus_if_typed_energy_in_play),
    ("damage.less-per-defender-energy",
     re.compile(r"this attack does (\d+) less damage for each energy attached to "
                r"your opponent's active pokemon\."), _less_per_defender_energy),
    ("counters.chosen-opponents",
     re.compile(r"place (\d+) damage counters? on (?:an?|(\d+)) of your "
                r"opponent's pokemon\."), _counters_chosen_opponents),
    ("heal.benched-typed",
     re.compile(r"heal (\d+) damage from (?:an?|\d+) of your benched (" +
                _TYPE_WORDS + r") pokemon\."), _heal_benched_typed),
    ("condition.self-asleep-then-draw",
     re.compile(r"this pokemon is now asleep\. draw (\d+) cards?\."),
     _self_asleep_draw),
    ("condition.discard-energy-then",
     re.compile(r"discard (an?|\d+) energy from this pokemon, and your "
                r"opponent's active pokemon is now (" + _CONDITION_WORDS +
                r")\."), _discard_self_energy_then_condition),
    ("counters.on-active-opponent",
     re.compile(r"place (\d+) damage counters? on your opponent's active "
                r"pokemon\."), _counters_on_defender_active),
    ("bonus.defender-no-retreat-cost",
     re.compile(r"if your opponent's active pokemon has no retreat cost, this "
                r"attack does (\d+) more damage\."),
     _bonus_if_defender_no_retreat),
    ("bench.basics-from-discard",
     re.compile(r"put up to (\d+) basic pokemon from your discard pile onto your "
                r"bench\."), _bench_basics_from_discard),
    ("counters.chosen-bench",
     re.compile(r"place (\d+) damage counters? on (?:an?|(\d+)) of your "
                r"opponent's benched pokemon\."), _counters_chosen_bench),
    ("counters.until-hp",
     re.compile(r"place damage counters on your opponent's active pokemon until "
                r"its remaining hp is (\d+)\."), _counters_until_hp_b58),
    ("heal.discard-all-energy-bench",
     re.compile(r"discard all energy from this pokemon\. heal all damage from ("
                r"an?|\d+) of your benched pokemon\."),
     _discard_all_energy_heal_bench),
    ("retreat.flip-defender-no-retreat-simple",
     re.compile(r"flip a coin\. if heads, during your opponent's next turn, the "
                r"defending pokemon can't retreat\."),
     _flip_defender_cannot_retreat),
    ("scale.per-energy-all-pokemon",
     re.compile(r"this attack does (\d+) damage for each energy attached to all "
                r"pokemon\."), _per_energy_all_pokemon),
    ("discard.three-typed",
     re.compile(r"discard a (" + _TYPE_WORDS + r") energy, a (" + _TYPE_WORDS +
                r") energy, and a (" + _TYPE_WORDS + r") energy from this "
                r"pokemon\."), _discard_three_typed),
    ("deck.reveal-item-to-bottom",
     re.compile(r"your opponent reveals their hand, and you put an item card you "
                r"find there on the bottom of your opponent's deck\."),
     _reveal_item_to_bottom),
    ("deck.shuffle-discard-types",
     re.compile(r"shuffle up to (\d+) in any combination of pokemon and basic "
                r"energy cards from your discard pile into your deck\."),
     _shuffle_discard_types_back),
    ("scale.per-bench-max-hp",
     re.compile(r"this attack does (\d+) damage for each of your benched pokemon "
                r"that has a maximum hp of (\d+)\."), _per_bench_max_hp),
    # -- batch 57: the one-card tail, second pass -------------------------
    ("mill.flip-until-tails-opponent",
     re.compile(r"flip a coin until you get tails\. for each heads, discard "
                r"the top card from your opponent's deck\."),
     _flip_until_mill_opponent),
    ("discard.flip-energy-each-opponent",
     re.compile(r"flip a coin\. if heads, discard an energy card from each of "
                r"your opponent's pokemon\."),
     _flip_discard_energy_each_opponent),
    ("heal.flip-until-chosen",
     re.compile(r"flip a coin until you get tails\. for each heads, remove "
                r"(\d+) damage counters from (?:an?|(\d+)) of your pokemon\."),
     _flip_until_heal_chosen),
    ("discard.energy-any-own",
     re.compile(r"discard (\d+) energy attached to any of your pokemon in any "
                r"way you like\."), _discard_energy_any_own),
    ("damage.base-swap-if-lower-hp",
     re.compile(r"if the defending pokemon has fewer remaining hp than this "
                r"pokemon, this attack's base damage is (\d+)\."),
     _base_swap_if_lower_hp),
    ("condition.flip-multi",
     re.compile(r"flip (\d+) coins?\. if both are heads, the defending pokemon "
                r"is now burned, paralyzed, and poisoned\."),
     _flip_multi_condition),
    ("counters.move-to-opponent-bench",
     re.compile(r"move up to (\d+) damage counters from this pokemon to "
                r"(?:an?|\d+) of your opponent's benched pokemon\."),
     _move_counters_to_opponent_bench),
    ("energy.flip-tails-discard-self",
     re.compile(r"flip (\d+) coins?\. for each tails, discard (\d+) energy "
                r"card attached to this pokemon\."),
     _flip_tails_discard_self_energy_many),
    ("mill.opponent-then-heal-self",
     re.compile(r"your opponent discards the top card from (?:his or her|their) "
                r"deck\. then,? you remove a damage counter from this "
                r"pokemon\."), _mill_opponent_heal_self),
    ("switch.defender-with-bench",
     re.compile(r"choose (?:an?|\d+) of your opponent's benched pokemon and "
                r"switch the defending pokemon with it\."),
     _switch_defender_with_bench),
    ("peek.opponent-top-cards",
     re.compile(r"look at the top (\d+) cards of your opponent's deck\. put "
                r"them back in the same order\."), _peek_opponent_top_cards),
    ("flip.nothing-on-tails",
     re.compile(r"flip a coin\. if tails this attack does nothing\."),
     _nothing_on_tails),
    ("heal.flip-self-per-heads",
     re.compile(r"flip (\d+) coins?\. for each heads, remove (\d+) damage "
                r"counters? on this pokemon\."), _flip_heal_self_each_heads),
    ("deck.shuffle-basic-energy-back",
     re.compile(r"shuffle a basic energy card from your discard pile into your "
                r"deck\."), _shuffle_basic_energy_back),
    ("counters.on-defender-single",
     re.compile(r"put a damage counter on the defending pokemon\."),
     _counter_on_defender_single),
    ("hand.refresh-up-to",
     re.compile(r"you may discard up to (\d+) cards from your hand\. if you do, "
                r"draw that many cards\."), _refresh_up_to),
    ("damage.base-swap-if-damaged",
     re.compile(r"if there are (\d+) or more damage counters on this pokemon, "
                r"this attack's base damage is (\d+) instead of (\d+)\."),
     _base_swap_if_damaged),
    ("heal.chosen-with-energy",
     re.compile(r"choose (?:an?|\d+) of your pokemon with an energy card "
                r"attached to it\. remove (\d+) damage counter from that "
                r"pokemon\."), _heal_chosen_with_energy),
    ("heal.self-one-counter",
     re.compile(r"remove a damage counter from this pokemon\."),
     _heal_self_single_counter),
    ("flip.times-heads-plain",
     re.compile(r"flip (\d+) coins?\. this attack does (\d+) damage times the "
                r"number of heads\s*$"), _flip_times_heads_optional_period),
    ("counters.on-chosen-opponent",
     re.compile(r"choose (?:an?|\d+) of your opponent's pokemon\. put a damage "
                r"counter on that pokemon\."), _counter_on_chosen_opponent),
    ("flip.scaled-in-play",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage times "
                r"the number of pokemon you have in play\."),
     _flip_scaled_in_play),
    ("heal.each-own-plain",
     re.compile(r"remove (\d+) damage counter from each of your pokemon, "
                r"including this pokemon\."), _heal_each_own_plain),
    ("attach.discard-energy-active",
     re.compile(r"attach (an?|\d+) energy card from your discard pile to your "
                r"active pokemon\."), _attach_discard_energy_active),
    ("attach.up-to-discard-self",
     re.compile(r"attach up to (\d+) energy cards from your discard pile to this "
                r"pokemon\."), _attach_up_to_discard_self),
    ("gate.no-opponent-ex",
     re.compile(r"if your opponent has no pokemon-ex in play, this attack does "
                r"nothing\."), _gate_no_opponent_ex),
    ("damage.base-swap-if-defender-type-plain",
     re.compile(r"if the defending pokemon is (" + _TYPE_WORDS + r") pokemon, "
                r"this attack's base damage is (\d+)\."),
     _base_swap_if_defender_type_plain),
    ("energy.self-to-hand",
     re.compile(r"return (an?|\d+) energy cards? attached to this pokemon to "
                r"your hand\."), _energy_from_self_to_hand),
    ("damage.base-plus-per-named-energy",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each ([a-z][\w' "
                r"-]*) card attached to this pokemon\."),
     _bonus_named_energy_attached),
    ("condition.then-optional-switch",
     re.compile(r"the defending pokemon is now (" + _CONDITION_WORDS + r")\. you "
                r"may switch this pokemon with (?:an?|\d+) of your benched "
                r"pokemon\."), _condition_then_optional_switch),
    ("bonus.per-own-bench",
     re.compile(r"does (\d+) damage plus (\d+) more for each of your benched "
                r"pokemon\."), _bonus_per_own_bench),
    ("condition.if-defender-special-energy",
     re.compile(r"if the defending pokemon has any special energy cards? "
                r"attached to it, the defending pokemon is now (" +
                _CONDITION_WORDS + r")\."),
     _condition_if_defender_special_energy),
    ("condition.named-stadium",
     re.compile(r"if ([a-z][\w' -]*) is in play, the defending pokemon is now ("
                + _CONDITION_WORDS + r")\."), _condition_if_named_stadium),
    ("draw.flip-until-tails",
     re.compile(r"flip a coin until you get tails\. for each heads, draw (\d+) "
                r"cards?\."), _flip_until_draw),
    ("lock.defender-if-basic",
     re.compile(r"if the defending pokemon is a basic pokemon, that pokemon "
                r"can't attack during your opponent's next turn\."),
     _lock_defender_if_basic),
    ("scale.per-benched-stage",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each of your "
                r"benched stage (\d+) evolved pokemon\."),
     _per_benched_stage),
    ("counters.opponent-chooses-target",
     re.compile(r"your opponent chooses (?:an?|\d+) of (?:his or her|their) "
                r"pokemon\. put (\d+) damage counters on that pokemon\."),
     _opponent_chooses_counter_target),
    ("discard.two-typed-energy",
     re.compile(r"discard a (" + _TYPE_WORDS + r") energy card and a (" +
                _TYPE_WORDS + r") energy card attached to this pokemon\."),
     _discard_two_typed_energy),
    ("counters.each-defender",
     re.compile(r"put (\d+) damage counters on each defending pokemon\."),
     _counters_each_defender),
    ("scale.per-counters-on-active",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each damage "
                r"counter on all of your active pokemon\."),
     _per_counters_on_active),
    ("damage.each-active",
     re.compile(r"does (\d+) damage to each active pokemon \(both yours and "
                r"your opponent's\)\."), _damage_each_active),
    ("attach.mill-basic-energy",
     re.compile(r"discard the top card from your deck\. if that card is a basic "
                r"energy card, attach it to this pokemon\."),
     _mill_attach_basic_energy),
    ("discard.condition-gated-energy",
     re.compile(r"if the defending pokemon is (" + _CONDITION_WORDS + r"), "
                r"discard an energy card attached to the defending pokemon\."),
     _condition_discard_defender_energy),
    ("bonus.special-energy-opponent-discard",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each special "
                r"energy card in your opponent's discard pile\."),
     _bonus_special_energy_in_opponent_discard),
    ("bonus.per-defender-distinct-type",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each type of "
                r"basic energy attached to the defending pokemon\."),
     _bonus_per_defender_distinct_type),
    ("recover.stadium",
     re.compile(r"search your discard pile for a stadium card, show it to your "
                r"opponent, and put it into your hand\."), _recover_stadium),
    ("heal.pre-damage-defender",
     re.compile(r"before doing damage, remove (\d+) damage counters from the "
                r"defending pokemon \(all if there are less than \d+\)\."),
     _pre_damage_heal_defender),
    ("attach.flip-typed-energy",
     re.compile(r"flip a coin\. if heads, attach a (" + _TYPE_WORDS + r") energy "
                r"card from your hand to any of your pokemon\."),
     _flip_attach_typed),
    ("scale.per-typed-energy-in-play",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each (" +
                _TYPE_WORDS + r") energy in play\."),
     _per_typed_energy_in_play),
    ("draw.to-match-opponent-plain",
     re.compile(r"draw cards until you have the same number of cards in your "
                r"hand as your opponent has in (?:his or her|their) hand\."),
     _draw_to_match_opponent),
    # -- batch 56: the one-card tail, first pass --------------------------
    ("bonus.self-special-energy",
     re.compile(r"if this pokemon has a special energy attached to it, this "
                r"attack does (\d+) more damage\."),
     _bonus_if_self_special_energy),
    ("scale.per-hand-size",
     re.compile(r"does (\d+) damage times the number of cards in your "
                r"hand\."), _per_hand_size),
    ("scale.per-opponent-hand-size",
     re.compile(r"does (\d+) damage times the number of cards in your "
                r"opponent's hand\."), _per_opponent_hand_size),
    ("cure.defender",
     re.compile(r"remove all special conditions from the defending pokemon\."),
     _cure_defender),
    ("flip.draw-per-heads",
     re.compile(r"flip (\d+) coins?\. for each heads, draw a card\."),
     _flip_draw_per_heads),
    ("bonus.defender-resistance",
     re.compile(r"if the defending pokemon has any resistance, this attack does "
                r"(\d+) more damage\."), _bonus_if_defender_resistance),
    ("search.any-cards",
     re.compile(r"search your deck for any (\d+) cards and put them into your "
                r"hand\. shuffle your deck afterward\."), _search_any_cards),
    ("scale.per-defender-retreat-cost",
     re.compile(r"does (\d+) damage times the number of colorless in the "
                r"defending pokemon's retreat cost\."),
     _per_defender_retreat_cost),
    ("flip.heal-each-own",
     re.compile(r"flip a coin\. if heads, heal (\d+) damage from each of your "
                r"pokemon\."), _flip_heal_each_own),
    ("shield.no-damage-from-ex",
     re.compile(r"during your opponent's next turn, prevent all damage done to "
                r"this pokemon by attacks from pokemon-ex\."),
     _prevent_damage_from_ex),
    ("bonus.stadium-discard-optional",
     re.compile(r"you may discard any stadium card in play\. if you do, this "
                r"attack does (\d+) more damage\."), _stadium_discard_bonus),
    ("mill.per-typed-energy-self",
     re.compile(r"for each (" + _TYPE_WORDS + r") energy attached to this "
                r"pokemon, discard the top card of your opponent's deck\."),
     _mill_per_typed_energy_self),
    ("bonus.stadium-then-discard",
     re.compile(r"if there is any stadium card in play, this attack does "
                r"(\d+) more damage\. discard the stadium card\."),
     _stadium_bonus_and_discard),
    ("hand.reveal-discard-items",
     re.compile(r"your opponent reveals (?:his or her|their) hand\. discard all "
                r"item cards you find there\."), _reveal_hand_discard_items),
    ("condition.optional-energy-trade",
     re.compile(r"you may discard an energy attached to this pokemon\. if you "
                r"do, the defending pokemon is now (" + _CONDITION_WORDS +
                r")\."), _discard_energy_trade_condition),
    ("attach.discard-basic-to-many",
     re.compile(r"attach (\d+) basic energy cards from your discard pile to "
                r"(?:an?|1) of your pokemon\."), _attach_discard_basic_to_many),
    ("draw.discard-typed-hand",
     re.compile(r"discard an? (" + _TYPE_WORDS + r") energy card from your "
                r"hand\. if you do, draw (\d+) cards?\."),
     _discard_typed_hand_draw),
    ("draw.discard-named-hand",
     re.compile(r"discard an? ([a-z][\w' -]*) card from your hand\. if you do, "
                r"draw (\d+) cards?\."), _discard_named_hand_draw),
    ("scale.per-tools-in-play",
     re.compile(r"does (\d+) damage for each pokemon tool card attached to "
                r"pokemon in play \(both yours and your opponent's\)\."),
     _per_tools_in_play),
    ("attach.hand-basic-to-many",
     re.compile(r"attach (\d+) basic energy cards from your hand to (?:an?|1) "
                r"of your pokemon\."), _attach_hand_basic_to_many),
    ("lock.all-supporters",
     re.compile(r"your opponent can't play any supporter cards from (?:his or "
                r"her|their) hand during (?:his or her|their) next turn\."),
     _lock_supporters),
    ("discard.defender-tools-first",
     re.compile(r"before doing damage, discard all pokemon tool cards attached "
                r"to the defending pokemon\."), _discard_defender_tools),
    ("lock.defender-if-ex",
     re.compile(r"if the defending pokemon is a pokemon-ex, that pokemon can't "
                r"attack during your opponent's next turn\."),
     _lock_defender_if_ex),
    ("heal.all-chosen-discard-energy",
     re.compile(r"heal all damage from (?:an?|1) of your pokemon\. then, "
                r"discard all energy attached to this pokemon\."),
     _heal_all_chosen_then_discard_energy),
    ("gate.undamaged-only",
     re.compile(r"if this pokemon has no damage counters on it, this attack does "
                r"nothing\."), _gate_undamaged_only),
    ("scale.per-defender-conditions",
     re.compile(r"does (\d+) damage times the number of special conditions "
                r"affecting the defending pokemon\."),
     _per_defender_conditions),
    ("scale.per-lost-zone-own",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each of your "
                r"pokemon in the lost zone\."), _per_lost_zone_own),
    ("mill.opponent-lost-zone-then-asleep",
     re.compile(r"put the top card of your opponent's deck in the lost zone\. "
                r"this pokemon is now asleep\."),
     _mill_opponent_lost_zone_then_asleep),
    ("condition.defender-then-no-retreat",
     re.compile(r"your opponent's active pokemon is now (" + _CONDITION_WORDS +
                r")\. it can't retreat during your opponent's next turn\."),
     _condition_then_defender_no_retreat),
    ("recover.trainer",
     re.compile(r"search your discard pile for a trainer card, show it to your "
                r"opponent, and put it into your hand\."), _recover_trainer),
    ("bonus.evolved-from-named",
     re.compile(r"if this pokemon is evolved from ([a-z][\w' -]*), this attack "
                r"does (\d+) damage plus (\d+) more damage\."),
     _bonus_if_evolved_from),
    ("condition.then-heal-chosen",
     re.compile(r"the defending pokemon is now (" + _CONDITION_WORDS +
                r")\. remove (\d+) damage counters from (?:an?|1) of your "
                r"pokemon\."), _condition_then_heal_chosen),
    ("heal.typed-own",
     re.compile(r"remove (\d+) damage counters from each of your (" +
                _TYPE_WORDS + r") pokemon\."), _heal_typed_own),
    ("scale.per-typed-all-in-play",
     re.compile(r"does (\d+) damage times the number of (" + _TYPE_WORDS +
                r") pokemon in play \(both yours and your opponent's\)\."),
     _per_typed_all_in_play),
    ("counters.flip-move-all-to-defender",
     re.compile(r"flip a coin\. if heads, move all damage counters from this "
                r"pokemon to the defending pokemon\."),
     _move_all_counters_to_defender),
    ("counters.both-benches",
     re.compile(r"put (\d+) damage counters? on each benched pokemon \(both "
                r"yours and your opponent's\)\."), _counters_on_both_benches),
    ("scale.per-distinct-basic-type",
     re.compile(r"this attack does (\d+) damage times the number of different "
                r"types of basic energy cards attached to this pokemon\."),
     _scale_per_distinct_basic_type_self),
    ("draw.gate-self-condition",
     re.compile(r"if this pokemon is (" + _CONDITION_WORDS + r"), draw (\d+) "
                r"cards?\."), _gate_self_condition_draw),
    ("condition.if-defender-lower-hp",
     re.compile(r"if the defending pokemon has fewer remaining hp than this "
                r"pokemon, the defending pokemon is now (" + _CONDITION_WORDS +
                r")\."), _condition_if_defender_lower_hp),
    ("damage.base-plus-per-typed-energy",
     re.compile(r"does (\d+) damage plus (\d+) damage for each (" +
                _TYPE_WORDS + r") energy attached to this pokemon\."),
     _base_plus_typed_energy_self),
    ("prize.extra-on-ko",
     re.compile(r"if the defending pokemon is knocked out by this attack, take "
                r"(\d+) more prize cards?\."), _extra_prize_on_ko),
    ("heal.stadium-gated-self",
     re.compile(r"if there is any stadium card in play, remove (\d+) damage "
                r"counters from this pokemon\."), _stadium_heal_self),
    ("draw.reveal-top-conditional",
     re.compile(r"reveal the top card of your deck and put it into your hand\. "
                r"if that card is a pokemon, draw (\d+) cards?\."),
     _reveal_top_conditional_draw),
    ("condition.mill-then-condition",
     re.compile(r"you may discard the top card of your deck\. if you do, the "
                r"defending pokemon is now (" + _CONDITION_WORDS + r")\."),
     _mill_then_condition),
    ("condition.confused-and-no-retreat",
     re.compile(r"the defending pokemon is now confused and can't retreat during "
                r"your opponent's next turn\."), _confused_and_no_retreat),
    # -- batch 55: the two-card tier, fifth pass ---------------------------
    ("deck.shuffle-one-discard-back",
     re.compile(r"shuffle a card from your discard pile into your deck\."),
     _shuffle_one_discard_into_deck),
    ("bonus.defender-special-energy",
     re.compile(r"if your opponent's active pokemon has any special energy "
                r"attached to it, this attack does (\d+) more damage\."),
     _bonus_if_defender_special_energy),
    ("bonus.defender-tool",
     re.compile(r"if your opponent's active pokemon has a pokemon tool "
                r"attached, this attack does (\d+) more damage\."),
     _bonus_if_defender_tool),
    ("switch.opponent-self-switches",
     re.compile(r"you may have your opponent switch (?:their|his or her) active "
                r"pokemon with (?:an?|\d+) of (?:their|his or her) benched "
                r"pokemon\."), _opponent_switches_self),
    ("recover.one-pokemon",
     re.compile(r"put a pokemon from your discard pile into your hand\."),
     _recover_one_pokemon),
    ("peek.opponent-top-card",
     re.compile(r"look at the top card of your opponent's deck\."),
     _reveal_opponent_top_card),
    ("recover.basic-energy",
     re.compile(r"put (an?|\d+) basic energy cards? from your discard pile into "
                r"your hand\."), _recover_basic_energy),
    ("recover.typed-basic-energy",
     re.compile(r"put up to (\d+) basic (" + _TYPE_WORDS + r") energy cards? "
                r"from your discard pile into your hand\."),
     _recover_typed_basic_energy),
    ("scale.per-benched-both",
     re.compile(r"this attack does (\d+) damage for each benched pokemon "
                r"\(both yours and your opponent's\)\."), _per_benched_both),
    ("mill.prize-gated",
     re.compile(r"if you have exactly (\d+), (\d+), or (\d+) prize cards "
                r"remaining, discard the top (\d+) cards of your deck\."),
     _prize_gated_self_mill),
    ("hand.discard-any-draw-to",
     re.compile(r"you may discard any number of cards from your hand\. then, "
                r"draw cards until you have (\d+) cards? in your hand\."),
     _discard_any_then_draw_to),
    ("hand.shuffle-draw-per-bench",
     re.compile(r"shuffle your hand into your deck\. then, draw a card for each "
                r"benched pokemon \(both yours and your opponent's\)\."),
     _shuffle_hand_draw_per_bench),
    ("flip.bonus-and-heal",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) more damage, "
                r"and heal (\d+) damage from this pokemon\."),
     _flip_bonus_and_heal_self),
    ("search.typed-basic-energy-self",
     re.compile(r"search your deck for up to (\d+) basic (" + _TYPE_WORDS +
                r") energy cards? and attach them to this pokemon\. then, "
                r"shuffle your deck\."), _search_typed_basic_energy_self),
    ("discard.flip-until-tails-energy",
     re.compile(r"flip a coin until you get tails\. for each heads, discard an "
                r"energy from your opponent's active pokemon\."),
     _flip_until_tails_discard_energy),
    ("energy.defender-energy-to-hand",
     re.compile(r"(?:you may )?put (?:an?|\d+) energy attached to your "
                r"opponent's active pokemon into (?:their|his or her) hand\."),
     _return_defender_energy_to_hand),
    ("bonus.self-typed-energy",
     re.compile(r"if this pokemon has any (" + _TYPE_WORDS + r") energy "
                r"attached, this attack does (\d+) more damage\."),
     _bonus_if_self_typed_energy),
    ("attach.up-to-basic-distributed",
     re.compile(r"attach up to (\d+) basic energy cards? from your discard pile "
                r"to your pokemon in any way you like\."),
     _attach_up_to_basic_distributed),
    ("attach.typed-hand-distributed",
     re.compile(r"attach up to (\d+) basic (" + _TYPE_WORDS + r") energy cards? "
                r"from your hand to your pokemon in any way you like\."),
     _attach_typed_hand_distributed),
    ("switch.flip-opponent-switch",
     re.compile(r"flip a coin\. if heads, switch in (?:an?|\d+) of your "
                r"opponent's benched pokemon to the active spot\."),
     _flip_opponent_switch),
    ("recoil.flip-all-tails",
     re.compile(r"flip (\d+) coins\. if both of them are tails, this pokemon "
                r"also does (\d+) damage to itself\."), _flip_all_tails_recoil),
    ("energy.flip-tails-discard-all",
     re.compile(r"flip a coin\. if tails, discard all energy from this "
                r"pokemon\."), _flip_tails_discard_all_energy),
    ("counters.chosen-then-self-lock",
     re.compile(r"put (\d+) damage counters? on (?:an?|(\d+)) of your "
                r"opponent's pokemon\. during your next turn, this pokemon "
                r"can't attack\."), _counters_chosen_then_self_lock),
    ("counters.damaged-opponent-bench",
     re.compile(r"put (\d+) damage counters? on each of your opponent's benched "
                r"pokemon that has any damage counters on it\."),
     _counters_damaged_opponent_bench),
    ("ko.defender-if-condition",
     re.compile(r"if your opponent's active pokemon is (" + _CONDITION_WORDS +
                r"), it is knocked out\."), _ko_defender_if_condition),
    ("recover.items-up-to",
     re.compile(r"put up to (\d+) item cards? from your discard pile into your "
                r"hand\."), _recover_items_up_to),
    ("attach.typed-discard-to-many",
     re.compile(r"attach up to (\d+) basic (" + _TYPE_WORDS + r") energy cards? "
                r"from your discard pile to (?:an?|1|(\d+)) of your "
                r"pokemon\."), _attach_typed_discard_to_many),
    ("attach.typed-discard-each-bench",
     re.compile(r"attach a basic (" + _TYPE_WORDS + r") energy card from your "
                r"discard pile to each of your benched pokemon\."),
     _attach_typed_discard_each_bench),
    ("discard.typed-energy-own",
     re.compile(r"discard (\d+) (" + _TYPE_WORDS + r") energy from your "
                r"pokemon\."), _discard_typed_energy_own),
    ("scale.per-special-energy-self",
     re.compile(r"this attack does (\d+) damage for each special energy card "
                r"attached to this pokemon\."), _per_special_energy_self),
    ("bonus.typed-on-bench",
     re.compile(r"if you have any (" + _TYPE_WORDS + r") pokemon on your bench, "
                r"this attack does (\d+) more damage\."), _bonus_if_typed_on_bench),
    ("deck.shuffle-bench-into-deck",
     re.compile(r"shuffle (an?|\d+) of your benched pokemon and all attached "
                r"cards into your deck\."), _shuffle_bench_into_deck),
    ("hand.reveal-discard-card",
     re.compile(r"your opponent reveals (?:their|his or her) hand\. discard a "
                r"card you find there\."), _reveal_hand_discard_card),
    ("scale.per-typed-energy-opponent-all",
     re.compile(r"this attack does (\d+) damage for each (" + _TYPE_WORDS +
                r") energy attached to all of your opponent's pokemon\."),
     _per_typed_energy_opponent_all),
    ("discard.self-and-cards",
     re.compile(r"discard this pokemon and all attached cards\."),
     _discard_self_and_cards),
    ("gate.hand-equal-else-nothing",
     re.compile(r"if you don't have the same number of cards in your hand as "
                r"your opponent, this attack does nothing\."),
     _gate_hand_equal),
    ("discard.all-special-opponent",
     re.compile(r"discard all special energy from all of your opponent's "
                r"pokemon\."), _discard_all_special_opponent),
    ("counters.each-opponent-plain",
     re.compile(r"put (\d+) damage counters? on each of your opponent's "
                r"pokemon\."), _counters_each_opponent),
    ("search.basic-energy-attach-distributed",
     re.compile(r"search your deck for up to (\d+) basic energy cards and "
                r"attach them to (?:an?|\d+) of your pokemon\. then, shuffle "
                r"your deck\."), _search_basic_energy_attach_distributed),
    ("ko.opponent-with-counters",
     re.compile(r"knock out (?:an?|(\d+)) of your opponent's pokemon that has "
                r"exactly (\d+) damage counters on it\."),
     _ko_opponent_with_counters),
    ("energy.discard-all-take-prize",
     re.compile(r"discard all energy from this pokemon, and take a prize "
                r"card\."), _discard_all_energy_take_prize),
    ("scale.per-stage-on-bench",
     re.compile(r"this attack does (\d+) more damage for each stage (\d+) "
                r"pokemon on your bench\."), _per_stage_on_bench),
    ("attach.typed-hand-to-bench",
     re.compile(r"you may attach a (" + _TYPE_WORDS + r") energy card from your "
                r"hand to (?:an?|1) of your benched pokemon\."),
     _attach_typed_hand_to_bench),
    ("flip.per-counters-on-self",
     re.compile(r"flip a coin for each damage counter on this pokemon\. this "
                r"attack does (\d+) damage times the number of heads\."),
     _per_counters_flip),
    ("hand.refresh-same-count",
     re.compile(r"discard as many cards as you like from your hand\. then, draw "
                r"that many cards\."), _refresh_hand),
    # -- batch 54: the two-card tier, fourth pass -------------------------
    ("flip.base-plus-per-heads",
     re.compile(r"flip (\d+) coins\. this attack does (\d+) damage plus "
                r"(\d+) more damage for each heads"),
     _flip_base_plus_per_heads),
    ("attach.hand-basic-self",
     re.compile(r"attach any number of basic energy cards from your hand to "
                r"this pokemon\."), _attach_hand_basic_self),
    ("attach.hand-basic-distributed",
     re.compile(r"attach any number of basic energy cards from your hand to "
                r"your pokemon in any way you like\."),
     _attach_hand_basic_distributed),
    ("heal.if-damaged",
     re.compile(r"if there are any damage counters on this pokemon, remove "
                r"(\d+) of them\."), _heal_if_damaged),
    ("topdeck.from-discard-on-flip",
     re.compile(r"flip a coin\. if heads, choose a card from your discard pile "
                r"and put it on top of your deck\."), _flip_topdeck_from_discard),
    ("heal.all-then-self-lock",
     re.compile(r"remove all damage counters from this pokemon\. this pokemon "
                r"can't attack during your next turn\."),
     _heal_all_then_self_lock),
    ("condition.flip-all-defenders",
     re.compile(r"flip a coin\. if heads, each defending pokemon is now (" +
                _CONDITION_WORDS + r")\."), _flip_all_defenders_condition),
    ("lock.flip-all-defenders",
     re.compile(r"flip a coin\. if heads, each defending pokemon can't attack "
                r"during your opponent's next turn\."),
     _flip_all_defenders_lock),
    ("damage.base-swap-if-resistance",
     re.compile(r"if the defending pokemon has any resistance, this attack's "
                r"base damage is (\d+) instead of (\d+)\."),
     _base_damage_if_resistance),
    ("attach.basic-from-discard-self",
     re.compile(r"search your discard pile for a basic energy card and attach "
                r"it to this pokemon\."), _attach_basic_from_discard_self),
    ("discard.special-energy-defender",
     re.compile(r"discard a special energy card, if any, attached to the "
                r"defending pokemon\."), _discard_special_energy_defender),
    ("damage.base-swap-if-defender-type",
     re.compile(r"if the defending pokemon is a (" + _TYPE_WORDS + r") pokemon, "
                r"this attack's base damage is (\d+) instead of (\d+)\."),
     _base_damage_if_defender_type),
    ("delayed.counters-after-opponent-turn",
     re.compile(r"put (\d+) damage counters on the defending pokemon at the end "
                r"of your opponent's next turn\."),
     _delayed_counters_after_opponent_turn),
    ("bonus.defender-stage",
     re.compile(r"if the defending pokemon is a stage (\d+) evolved pokemon, "
                r"this attack does (\d+) damage plus (\d+) more damage\."),
     _bonus_if_defender_stage),
    ("bonus.defender-typed-resistance",
     re.compile(r"if the defending pokemon has (" + _TYPE_WORDS + r") "
                r"resistance, this attack does (\d+) damage plus (\d+) more "
                r"damage\."), _bonus_if_defender_typed_resistance),
    ("scale.per-all-in-play-minus-self",
     re.compile(r"does (\d+) damage times the number of pokemon in play "
                r"\(both yours and your opponent's\), excluding this "
                r"pokemon\."), _per_all_in_play_minus_self),
    ("condition.typed-energy-threshold",
     re.compile(r"if this pokemon has at least (\d+) (" + _TYPE_WORDS +
                r") energy attached to it, the defending pokemon is now (" +
                _CONDITION_WORDS + r")\."), _typed_energy_threshold_condition),
    ("scale.per-all-own-energy",
     re.compile(r"does (\d+) damage times the amount of energy attached to all "
                r"of your pokemon \(including this pokemon\)\."),
     _per_energy_all_own),
    ("mill.self-top",
     re.compile(r"discard the top (\d+) cards from your deck\."), _self_mill),
    ("damage.base-plus-per-distinct-basic-type",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each type of "
                r"basic energy card attached to this pokemon\."),
     _per_distinct_basic_type),
    ("attach.flip-basic-from-discard",
     re.compile(r"flip a coin\. if heads, search your discard pile for a basic "
                r"energy card and attach it to this pokemon\."),
     _flip_attach_basic_from_discard),
    ("heal.each-own-counters-self",
     re.compile(r"remove (\d+) damage counters from each of your pokemon "
                r"\(including this pokemon\)\."), _heal_each_own_including_self),
    ("condition.if-defender-damaged",
     re.compile(r"if the defending pokemon (?:already )?has any damage counters "
                r"on it, the defending pokemon is now (" + _CONDITION_WORDS +
                r")\."), _condition_if_defender_damaged),
    ("bonus.more-hand-than-opponent-attack",
     re.compile(r"if you have more cards in your hand than your opponent, this "
                r"attack does (\d+) damage plus (\d+) more damage\."),
     _bonus_if_more_hand_than_opponent),
    ("counters.on-defender",
     re.compile(r"put (\d+) damage counters? on the defending pokemon\."),
     _counters_on_defender_plain),
    ("hand.shuffle-draw-up-to",
     re.compile(r"shuffle your hand into your deck\. draw up to (\d+) "
                r"cards?\."), _shuffle_hand_draw_up_to),
    ("bonus.stadium-plain",
     re.compile(r"if (?:there is any|a) stadium (?:card )?(?:is )?in play, this "
                r"attack does (\d+) damage plus (\d+) more damage\."),
     _bonus_if_stadium_plain),
    ("attach.typed-energy-discard-self",
     re.compile(r"take up to (an?|\d+) (" + _TYPE_WORDS + r") energy cards? "
                r"from your discard pile and attach them? to this pokemon\."),
     _typed_energy_from_discard_to_self),
    ("condition.self-asleep-after",
     re.compile(r"this pokemon is now asleep \(after doing damage\)\."),
     _self_asleep_after_damage),
    ("lock.self-next-turn",
     re.compile(r"you can't use this attack during your next turn\."),
     _self_attack_lock_plain),
    ("lock.flip-all-trainers",
     re.compile(r"flip a coin\. if heads, your opponent can't play trainer "
                r"cards during (?:his or her|their) next turn\."),
     _flip_trainer_lock),
    ("recoil.no-weakness",
     re.compile(r"this pokemon does (\d+) damage to itself and don't apply "
                r"weakness to this damage\."), _recoil_no_weakness),
    ("heal.self-then-no-retreat",
     re.compile(r"remove (\d+) damage counters from this pokemon\. this "
                r"pokemon can't retreat during your next turn\."),
     _heal_self_then_no_retreat),
    ("draw.to-match-opponent",
     re.compile(r"draw cards until you have the same number of cards in your "
                r"hand as your opponent\."), _draw_to_match_opponent),
    ("search.tool-to-hand",
     re.compile(r"search your deck for a pokemon tool card, reveal it, and put "
                r"it into your hand\. then, shuffle your deck\."),
     _search_tool_to_hand),
    ("counters.double-opponent",
     re.compile(r"double the number of damage counters on each of your "
                r"opponent's pokemon\."), _double_opponent_counters),
    ("scale.reveal-hand-per-energy",
     re.compile(r"your opponent reveals (?:his or her|their) hand, and this "
                r"attack does (\d+) damage for each energy card you find "
                r"there\."), _reveal_hand_per_energy),
    ("mill.then-recover",
     re.compile(r"discard the top (\d+) cards of your deck and put (\d+) of "
                r"them into your hand\."), _mill_then_recover),
    ("search.energy-to-hand",
     re.compile(r"search your deck for an energy card, reveal it, and put it "
                r"into your hand\. then, shuffle your deck\."),
     _search_energy_to_hand_plain),
    ("search.basic-bench-any",
     re.compile(r"search your deck for any number of basic pokemon and put them "
                r"onto your bench\. then, shuffle your deck\."),
     _search_basic_bench_any),
    ("damage.half-remaining-hp",
     re.compile(r"does damage equal to half the defending pokemon's remaining hp "
                r"\(rounded down to the nearest (\d+)\)\."),
     _half_remaining_hp),
    ("attach.hand-basic-one",
     re.compile(r"you may attach a basic energy card from your hand to (?:an?|1) "
                r"of your pokemon\."), _attach_hand_basic_one),
    # -- batch 53: the two-card tier, third pass ---------------------------
    ("energy.typed-return-to-hand",
     re.compile(r"return (an?|\d+) (" + _TYPE_WORDS + r") energy attached to "
                r"this pokemon to your hand\."), _typed_energy_return_to_hand),
    ("lock.flip-tails-self-attack",
     re.compile(r"flip a coin\. if tails, this pokemon can't attack during your "
                r"next turn\."), _flip_tails_self_attack_lock),
    ("discard.typed-defender-energy",
     re.compile(r"discard an? (" + _TYPE_WORDS + r") energy from your opponent's "
                r"active pokemon\."), _discard_typed_defender_energy),
    ("search.typed-pokemon-many",
     re.compile(r"search your deck for up to (\d+) (" + _TYPE_WORDS +
                r") pokemon, reveal them, and put them into your hand\."),
     _search_typed_pokemon_many),
    ("search.typed-energy-attach-any",
     re.compile(r"search your deck for an? (" + _TYPE_WORDS + r") energy card and "
                r"attach it to (?:an?|1) of your pokemon\. then, shuffle your "
                r"deck\."), _search_typed_energy_attach_any),
    ("attach.discard-basic-distributed",
     re.compile(r"attach (an?|\d+) basic energy cards? from your discard pile to "
                r"your pokemon in any way you like\."),
     _attach_discard_basic_distributed),
    ("draw.card-then-asleep",
     re.compile(r"draw a card\. if you do, this pokemon is now asleep\."),
     _draw_then_asleep),
    ("condition.then-bench-counters",
     re.compile(r"your opponent's active pokemon is now (" + _CONDITION_WORDS +
                r")\. put (\d+) damage counters? on each of your opponent's "
                r"benched pokemon\."), _condition_then_bench_counters),
    ("counters.flip-until-hp",
     re.compile(r"flip a coin\. if heads, put damage counters on your opponent's "
                r"active pokemon until its remaining hp is (\d+)\."),
     _flip_counters_until_hp),
    ("bonus.capped-per-discard",
     re.compile(r"this attack does (\d+) more damage for each pokemon in your "
                r"discard pile\. you can't add more than (\d+) damage in this "
                r"way\."), _bonus_capped_per_discard),
    ("scale.per-damaged-own",
     re.compile(r"this attack does (\d+) damage for each of your pokemon that "
                r"has any damage counters on it\."), _per_damaged_own),
    ("recover.typed-energy",
     re.compile(r"put (an?|\d+) (" + _TYPE_WORDS + r") energy cards? from your "
                r"discard pile into your hand\."), _recover_typed_energy),
    ("discard.energy-trade-plain",
     re.compile(r"discard an energy (?:card )?(?:attached )?from this pokemon"
                r"(?:,? then,?|\. if you do,) discard an energy (?:card )?"
                r"(?:attached )?from your opponent's active pokemon\."),
     _discard_energy_trade_plain),
    ("ko.defender-if-basic",
     re.compile(r"if your opponent's active pokemon is a basic pokemon, it is "
                r"knocked out\."), _ko_defender_if_basic),
    ("ko.defender-if-all-heads",
     re.compile(r"flip (\d+) coins\. if both of them are heads, your opponent's "
                r"active pokemon is knocked out\."), _ko_defender_if_all_heads),
    ("scale.per-named-in-discard",
     re.compile(r"this attack does (\d+) damage for each ([a-z][\w' -]*) in your "
                r"discard pile\."), _per_named_in_discard),
    ("mill.flip-per-heads",
     re.compile(r"flip (\d+) coins\. for each heads, discard the top (\d+) "
                r"cards? of your opponent's deck\."), _flip_mill_per_heads),
    ("heal.then-self-no-retreat",
     re.compile(r"heal (\d+) damage from this pokemon\. during your next turn, "
                r"this pokemon can't retreat\."), _heal_then_self_no_retreat),
    ("bench.pokemon-from-discard",
     re.compile(r"put a pokemon from your discard pile onto your bench\."),
     _bench_from_discard),
    ("recover.pokemon",
     re.compile(r"put up to (\d+) pokemon from your discard pile into your "
                r"hand\."), _recover_pokemon),
    ("heal.and-cure-self",
     re.compile(r"heal (\d+) damage from this pokemon, and it recovers from all "
                r"special conditions\."), _heal_and_cure_self),
    ("lock.defender-attacks-if-evolved",
     re.compile(r"if the defending pokemon is an evolution pokemon, it can't "
                r"attack during your opponent's next turn\."),
     _lock_defender_if_evolved),
    ("discard.opponent-tools-up-to",
     re.compile(r"discard up to (an?|\d+) pokemon tools? from your opponent's "
                r"pokemon\."), _discard_opponent_tools),
    ("bonus.self-has-condition",
     re.compile(r"if this pokemon is (" + _CONDITION_WORDS + r"), this attack "
                r"does (\d+) more damage\."), _bonus_if_self_condition),
    ("condition.if-defender-type",
     re.compile(r"if your opponent's active pokemon is a (" + _TYPE_WORDS +
                r") pokemon, it is now (" + _CONDITION_WORDS + r")\."),
     _condition_if_defender_type),
    ("switch.opponent-chooses-new",
     re.compile(r"switch (\d+) of your opponent's benched pokemon with your "
                r"opponent's active pokemon\."), _opponent_switches_chosen),
    ("counters.each-opponent-with-energy",
     re.compile(r"put (\d+) damage counters? on each of your opponent's pokemon "
                r"that has any energy attached to it\."),
     _counters_each_opponent_with_energy),
    ("gate.defender-must-be-condition",
     re.compile(r"you can't use this attack unless the defending pokemon is (" +
                _CONDITION_WORDS + r")\."), _gate_defender_condition),
    ("lock.all-trainers",
     re.compile(r"your opponent can't play trainer cards during (?:his or her|"
                r"their) next turn\."), _lock_all_trainers),
    ("scale.times-defender-energy-cards",
     re.compile(r"does (\d+) damage times the number of energy cards attached to "
                r"the defending pokemon\."), _times_defender_energy_cards),
    ("discard.energy-heal-all",
     re.compile(r"discard an energy attached to this pokemon and heal all damage "
                r"from this pokemon\."), _discard_energy_heal_all),
    ("recover.flip-per-heads",
     re.compile(r"flip (\d+) coins\. for each heads, put a card from your "
                r"discard pile into your hand\."), _flip_recover_per_heads),
    ("bonus.lower-hp-than-defender",
     re.compile(r"if this pokemon has fewer remaining hp than the defending "
                r"pokemon, this attack does (\d+) more damage\."),
     _bonus_if_lower_hp),
    ("scale.times-typed-in-play",
     re.compile(r"does (\d+) damage times the number of (" + _TYPE_WORDS +
                r") pokemon you have in play\."), _times_typed_in_play),
    ("discard.flip-energy-chosen",
     re.compile(r"flip a coin\. if heads, discard an energy attached to "
                r"(?:an?|(\d+)) of your opponent's pokemon\."),
     _flip_discard_energy_chosen),
    ("flip.times-heads-then-self-lock",
     re.compile(r"flip (\d+) coins\. this attack does (\d+) damage times the "
                r"number of heads\. this pokemon can't attack during your next "
                r"turn\."), _flip_times_heads_then_self_lock),
    # -- batch 52: two-card tier, second pass ------------------------------
    ("energy.move-typed-to-bench",
     re.compile(r"move an? (" + _TYPE_WORDS + r") energy (?:card )?from this "
                r"pokemon to (?:an?|1) of your benched pokemon\."),
     _move_typed_energy_to_bench),
    ("draw.then-self-condition",
     re.compile(r"draw (\d+) cards?\. this pokemon is now (" +
                _CONDITION_WORDS + r")\."), _draw_then_self_condition),
    ("heal.then-self-condition",
     re.compile(r"heal (\d+) damage from this pokemon\. this pokemon is now ("
                + _CONDITION_WORDS + r")\."), _heal_then_self_condition),
    ("heal.then-switch",
     re.compile(r"heal (\d+) damage from this pokemon\. switch this pokemon "
                r"with (?:an?|1) of your benched pokemon\."), _heal_then_switch),
    ("heal.then-defender-no-retreat",
     re.compile(r"heal (\d+) damage from this pokemon\. the defending pokemon "
                r"can't retreat during your opponent's next turn\."),
     _heal_then_defender_no_retreat),
    ("condition.then-defender-no-retreat",
     re.compile(r"the defending pokemon is now (" + _CONDITION_WORDS +
                r")\. the defending pokemon can't retreat during your "
                r"opponent's next turn\."), _condition_then_defender_no_retreat),
    ("discard.self-energy-then-defender-locked",
     re.compile(r"discard an energy attached to this pokemon\. the defending "
                r"pokemon can't attack during your opponent's next turn\."),
     _discard_energy_then_defender_locked),
    ("search.basic-energy-attach-any-one",
     re.compile(r"search your deck for a basic energy card and attach it to "
                r"(?:an?|1) of your pokemon\. shuffle your deck afterward\."),
     _search_energy_attach_any_one),
    ("draw.shuffle-hand-then-draw",
     re.compile(r"shuffle your hand into your deck, then draw (\d+) cards?(?P<"
                r"sleep>\. this pokemon is now asleep)?\."),
     _shuffle_hand_then_draw),
    ("self.damage-own-ignore-mods",
     re.compile(r"does (\d+) damage to (?:an?|(\d+)) of your pokemon, and don't "
                r"apply weakness and resistance to this damage\."),
     _damage_own_any_ignore_mods),
    ("mill.flip-opponent-or-self",
     re.compile(r"flip a coin\. if heads, discard the top (\d+) cards? of your "
                r"opponent's deck\. if tails, discard the top \1 cards? of your "
                r"deck\."), _flip_mill_opponent_or_self),
    ("gate.defender-not-condition",
     re.compile(r"if your opponent's active pokemon isn't (" + _CONDITION_WORDS +
                r"), this attack does nothing\."), _gate_defender_not_condition),
    ("bonus.counters-at-least",
     re.compile(r"if this pokemon has (\d+) or more damage counters on it, this "
                r"attack does (\d+) more damage\."), _bonus_if_counters_at_least),
    ("protect.flip-damage-plain",
     re.compile(r"flip a coin\. if heads, prevent all damage done to this "
                r"pokemon during your opponent's next turn\."),
     _flip_prevent_damage_plain),
    ("condition-and-no-retreat",
     re.compile(r"flip a coin\. if heads, the defending pokemon is now (" +
                _CONDITION_WORDS + r") and can't retreat during your opponent's "
                r"next turn\."), _condition_and_no_retreat),
    ("flip.defender-or-self-condition",
     re.compile(r"flip a coin\. if heads, the defending pokemon is now (" +
                _CONDITION_WORDS + r")\. if tails, this pokemon is now (" +
                _CONDITION_WORDS + r")\."), _flip_defender_or_self_condition),
    ("flip.condition-else-self-damage",
     re.compile(r"flip a coin\. if heads, the defending pokemon is now (" +
                _CONDITION_WORDS + r")\. if tails, this pokemon does (\d+) "
                r"damage to itself\."), _flip_condition_else_self_damage),
    ("scale.times-same-name-in-play",
     re.compile(r"does (\d+) damage times the number of this pokemon you have "
                r"in play\."), _times_named_self_in_play),
    ("scale.times-pokemon-in-play",
     re.compile(r"does (\d+) damage times the number of pokemon in play \(both "
                r"yours and your opponent's\)\."), _times_both_in_play),
    ("flip.times-heads-then-confused",
     re.compile(r"flip (\d+) coins\. this attack does (\d+) damage times the "
                r"number of heads\. this pokemon is now confused \(after doing "
                r"damage\)\."), _flip_times_heads_then_confused),
    ("scale.base-on-tails",
     re.compile(r"flip a coin\. if tails, this attack's base damage is (\d+) "
                r"instead of \d+\."), _base_on_tails),
    ("discard.return-defender-flip",
     re.compile(r"flip a coin\. if heads, your opponent returns the defending "
                r"pokemon and all cards attached to it to (?:his or her|their) "
                r"hand\."), _return_defender_to_hand_flip),
    ("protect.reduce-next-turn-plain",
     re.compile(r"during your opponent's next turn, any damage done to this "
                r"pokemon by attacks is reduced by (\d+)\."),
     _reduce_damage_next_turn_plain),
    ("ignore.weakness-resistance-then-self-lock",
     re.compile(r"this attack's damage isn't affected by weakness or "
                r"resistance\. this pokemon can't attack during your next "
                r"turn\."), _ignore_wr_then_self_lock),
    ("lock.this-attack-named-short",
     re.compile(r"this pokemon can't use (.+)\."), _lock_this_attack_short),
    # -- batch 51: the two-card tier, plain mechanics ----------------------
    ("search.basic-energy-to-bench-one",
     re.compile(r"search your deck for a basic energy card and attach it to "
                r"(?:an?|1) of your benched pokemon\. shuffle your deck "
                r"afterward\."), _search_basic_energy_to_bench_one),
    ("flip.bonus-plus-condition",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) more damage "
                r"and the defending pokemon is now (" + _CONDITION_WORDS +
                r")\."), _flip_heads_bonus_and_condition),
    ("bonus.stadium-and-heal",
     re.compile(r"if there is any stadium card in play, this attack does (\d+) "
                r"more damage and heal (\d+) damage from this pokemon\."),
     _stadium_bonus_and_heal),
    ("scale.times-own-prizes-taken",
     re.compile(r"does (\d+) damage times the number of prize cards you have "
                r"taken\."), _times_prizes_taken_mine),
    ("recover.items",
     re.compile(r"put (an?|\d+) item cards? from your discard pile into your "
                r"hand\."), _recover_items),
    ("bonus.more-hand-than-opponent",
     re.compile(r"if you have more cards in your hand than your opponent, this "
                r"attack does (\d+) more damage\."), _bonus_if_more_hand),
    ("scale.times-special-energy-opponent-discard",
     re.compile(r"does (\d+) damage times the number of special energy cards in "
                r"your opponent's discard pile\."),
     _times_special_energy_in_opponent_discard),
    ("bonus.per-opponent-bench",
     re.compile(r"does (\d+) more damage for each of your opponent's benched "
                r"pokemon\."), _bonus_per_opponent_bench),
    ("bonus.per-distinct-energy-type",
     re.compile(r"does (\d+) more damage for each different type of basic "
                r"energy attached to this pokemon\."),
     _bonus_per_distinct_energy_type),
    ("flip.heal-per-heads",
     re.compile(r"flip (\d+) coins\. for each heads, heal (\d+) damage from "
                r"this pokemon\."), _flip_heal_per_heads),
    ("discard.defender-tool",
     re.compile(r"(?:before doing damage, )?discard a pokemon tool card attached "
                r"to the defending pokemon\."), _discard_defender_tool),
    ("scale.times-defender-counters",
     re.compile(r"does (\d+) damage times the number of damage counters on the "
                r"defending pokemon\."), _times_defender_counters),
    ("counters.move-to-opponent",
     re.compile(r"move up to (\d+) damage counters? from any of your pokemon to "
                r"any of your opponent's pokemon in any way you like\."),
     _move_counters_any_direction),
    ("self.damage-then-switch",
     re.compile(r"this pokemon does (\d+) damage to itself\. switch this "
                r"pokemon with (?:an?|1) of your benched pokemon\."),
     _self_damage_then_switch),
    ("condition.defender-and-self-asleep",
     re.compile(r"the defending pokemon is now (" + _CONDITION_WORDS +
                r")\. this pokemon is now asleep\."),
     _defender_condition_self_asleep),
    ("heal.team-with-energy",
     re.compile(r"heal (\d+) damage from each of your pokemon that has any "
                r"energy attached to it\."), _heal_team_with_energy),
    ("bonus.base-plus-opponent-has-type",
     re.compile(r"if your opponent has any (" + _TYPE_WORDS + r") pokemon in "
                r"play, this attack does (\d+) damage plus (\d+) more "
                r"damage\."), _bonus_if_opponent_has_typed),
    ("counters.equal-self-counters",
     re.compile(r"count the number of damage counters on this pokemon\. put that "
                r"many damage counters on (?:an?|(\d+)) of your opponent's "
                r"pokemon\."), _counters_equal_self_counters),
    ("counters.flip-each-bench",
     re.compile(r"flip a coin\. if heads, put (\d+) damage counters? on each of "
                r"your opponent's benched pokemon\."), _flip_counters_each_bench),
    ("search.any-one-card",
     re.compile(r"search your deck for any (?:1 )?card and put it into your "
                r"hand\. shuffle your deck afterward\."), _search_any_one_card),
    ("draw.shuffle-hand-only",
     re.compile(r"shuffle your hand into your deck\."), _shuffle_hand_only),
    ("ignore.weakness-resistance-then-asleep",
     re.compile(r"this attack's damage isn't affected by weakness or "
                r"resistance\. this pokemon is now asleep\."),
     _ignore_wr_then_self_asleep),
    ("discard.flip-tails-all-typed",
     re.compile(r"flip a coin\. if tails, discard all (" + _TYPE_WORDS +
                r") energy attached to this pokemon\."),
     _flip_tails_discard_all_typed),
    # -- batch 50: last-turn memory and its conditional tails --------------
    ("lastturn.damage-taken-bonus",
     re.compile(r"if this pokemon was damaged by an attack during your "
                r"opponent's last turn, this attack does that much more "
                r"damage\."), _bonus_last_turn_damage),
    ("lastturn.condition-on-defender",
     re.compile(r"if this pokemon was damaged by an attack during your "
                r"opponent's last turn, the defending pokemon is now ("
                + _CONDITION_WORDS + r")\."), _condition_if_damaged_last_turn),
    ("lastturn.repeat-damage",
     re.compile(r"if this pokemon was attacked last turn, do the final result of "
                r"that attack on this pokemon to the defending pokemon\."),
     _repeat_last_turn_damage),
    ("ko.flip-active-or-bench-basic",
     re.compile(r"flip a coin\. if heads, knock out your opponent's active basic "
                r"pokemon\. if tails, knock out (?:an?|1) of your opponent's "
                r"benched basic pokemon\."), _ko_flip_active_or_bench_basic),
    ("gate.must-be-asleep",
     re.compile(r"this attack can be used if this pokemon is asleep\. if it is "
                r"not asleep, this attack does nothing\."), _gate_must_be_asleep),
    ("protect.flip-prevent-damage-next-turn",
     re.compile(r"flip a coin\. if heads, prevent all damage done by attacks to "
                r"this pokemon during your opponent's next turn\. \(any other "
                r"effects of attacks still happen\.\)"),
     _flip_prevent_all_damage_next_turn),
    ("spread.opponent-ex-only",
     re.compile(r"this attack does (\d+) damage to each of your opponent's "
                r"pokemon ex\."), _spread_ex_only),
    ("counters.place-chosen-any",
     re.compile(r"place (\d+) damage counters on (?:an?|(\d+)) of your "
                r"opponent's pokemon\."), _place_counters_chosen_any),
    ("discard.return-defender-unless-ko",
     re.compile(r"unless this attack knocks out the defending pokemon, return the "
                r"defending pokemon and all cards attached to it to your "
                r"opponent's hand\."), _return_defender_unless_ko),
    # -- batch 48: discard-pile attaches with their conditional tails ------
    ("attach.flip-discard-energy-self",
     re.compile(r"flip a coin\. if heads, attach (?P<count>an?|\d+) (?:(?P<type>"
                + _TYPE_WORDS + r") )?energy cards? from your discard pile to "
                r"this pokemon\."), _attach_discard_energy_self),
    ("attach.discard-of-them-self",
     re.compile(r"if there are any (?P<type>" + _TYPE_WORDS + r") energy cards "
                r"in your discard pile, (?:flip a coin\. if heads, )?attach "
                r"(?P<count>an?|\d+) of them to this pokemon\."),
     _attach_discard_energy_self),
    ("recover.flip-one-card",
     re.compile(r"flip a coin\. if heads, put a card from your discard pile "
                r"into your hand\."), _flip_recover_one),
    ("attach.discard-energy-one-target",
     re.compile(r"attach (?:an?|\d+) (?:(?P<type>" + _TYPE_WORDS + r") )?basic "
                r"energy card from your discard pile to (?:an?|1) of your "
                r"pokemon\."), _discard_energy_to_one_target),
    ("search.typed-pokemon-reveal",
     re.compile(r"search your deck for an? (" + _TYPE_WORDS + r") pokemon, "
                r"reveal it, and put it into your hand\. shuffle your deck "
                r"afterward\."), _search_typed_pokemon_to_hand),
    ("search.stadium-then-discard-any",
     re.compile(r"search your deck for a stadium card, show it to your "
                r"opponent, and put it into your hand\. shuffle your deck "
                r"afterward\. if there is any stadium card in play, discard "
                r"it\."), _search_stadium_then_discard_any),
    ("bonus.optional-typed-energy-to-hand",
     re.compile(r"you may put an? (" + _TYPE_WORDS + r") energy attached to this "
                r"pokemon into your hand and have this attack do (\d+) more "
                r"damage\."), _optional_typed_energy_to_hand_for_bonus),
    ("search.flip-any-card",
     re.compile(r"flip a coin\. if heads, search your deck for any (?:1 )?card "
                r"and put it into your hand\. shuffle your deck afterward\."),
     _flip_search_any_card),
    ("recover.one-card-unconditional",
     re.compile(r"put a card from your discard pile into your hand\."),
     _recover_one_unconditional),
    ("attach.discard-typed-energy-self",
     re.compile(r"attach up to (\d+) basic (" + _TYPE_WORDS + r") energy cards? "
                r"from your discard pile to this pokemon\."),
     _attach_many_typed_discard_self),
    ("shuffle.own-typed-energy-for-damage",
     re.compile(r"shuffle any amount of (" + _TYPE_WORDS + r") energy from your "
                r"pokemon into your deck\. this attack does (\d+) damage for "
                r"each card you shuffled into your deck in this way\."),
     _shuffle_own_energy_for_damage),
    # -- batch 47: ability utilities from the mid tail ----------------------
    ("search.basic-typed-energy-to-hand",
     re.compile(r"search your deck for up to (\d+) basic (?:(?P<type>"
                + _TYPE_WORDS + r") )?energy cards?, reveal (?:them|it), and "
                r"put (?:them|it) into your hand\. then, shuffle your deck\."),
     _search_basic_typed_energy_to_hand),
    ("heal.own-with-energy",
     re.compile(r"heal (\d+) damage from (?:an?|1) of your pokemon that has any "
                r"energy attached to it\."), _heal_own_with_energy),
    ("energy.move-typed-between-own",
     re.compile(r"move an? (" + _TYPE_WORDS + r") energy (?:card )?from (?:an?|1) "
                r"of your pokemon to another of your pokemon\."),
     _move_typed_energy_between_own),
    ("ability.attacks-boost-at-low-hp",
     re.compile(r"if this pokemon's remaining hp is (\d+) or less, its attacks "
                r"do (\d+) more damage to your opponent's active pokemon "
                r"\(before applying weakness and resistance\)\."),
     _passive_attacks_boost_at_low_hp),
    ("draw.one-card",
     re.compile(r"draw a card\."), _draw_one),
    # -- batch 46: conditions, typed scaling and shop-style riders ---------
    ("bonus.base-plus-defender-damaged",
     re.compile(r"if the defending pokemon has any damage counters on it, this "
                r"attack does (\d+) damage plus (\d+) more damage\."),
     _base_plus_if_defender_damaged),
    ("scale.times-energy-both-actives",
     re.compile(r"does (\d+) damage times the total amount of energy attached "
                r"to this pokemon and the defending pokemon\."),
     _times_energy_both_actives),
    ("lock.opponent-non-supporters",
     re.compile(r"your opponent can't play any trainer cards \(except for "
                r"supporter cards\) from (?:his or her|their) hand during your "
                r"opponent's next turn\."), _lock_opponent_non_supporters),
    ("bonus.optional-discard-energy-base",
     re.compile(r"you may discard an energy card attached to this pokemon\. if "
                r"you do, this attack does (\d+) damage plus (\d+) more "
                r"damage\."), _optional_discard_energy_then_base_plus),
    ("bonus.base-plus-self-has-tool",
     re.compile(r"if this pokemon has a pokemon tool card attached to it, this "
                r"attack does (\d+) damage plus (\d+) more damage\."),
     _base_plus_if_self_has_tool),
    ("counters.equal-opponent-hand",
     re.compile(r"count the number of cards in your opponent's hand\. put that "
                r"many damage counters on the defending pokemon\."),
     _counters_equal_opponent_hand),
    ("search.typed-energy-to-hand",
     re.compile(r"search your deck for up to (\d+) (?:(\w+) )?energy cards?\, "
                r"reveal (?:them|it)\, and put (?:them|it) into your hand\. "
                r"then, shuffle your deck\."), _search_typed_energy_to_hand),
    ("peek.opponent-prizes",
     re.compile(r"look at (\d+) of your opponent's face-down prize cards\."),
     _peek_opponent_prizes),
    ("discard.flips-heads-defender-energy",
     re.compile(r"flip (\d+) coins\. for each heads, discard an energy from "
                r"your opponent's active pokemon\."),
     _flip_heads_discard_defender_energy_each),
    ("disrupt.reveal-hand-discard-chosen",
     re.compile(r"your opponent reveals (?:their|his or her) hand, and you "
                r"discard a card you find there\."), _reveal_hand_discard_chosen),
    ("bonus.own-prizes-exactly",
     re.compile(r"if you have exactly (\d+) prize cards? remaining, this attack "
                r"does (\d+) more damage\."), _bonus_if_own_prizes_exactly),
    ("disrupt.opponent-shuffles-hand-cards",
     re.compile(r"your opponent chooses (\d+) cards? from their hand and "
                r"shuffles those cards into their deck\."),
     _opponent_shuffles_hand_cards),
    ("scale.per-basic-energy-opponent-discard",
     re.compile(r"this attack does (\d+) damage for each basic energy card in "
                r"your opponent's discard pile\."),
     _per_basic_energy_in_opponent_discard),
    ("discard.all-self-then-condition",
     re.compile(r"discard all energy from this pokemon\. your opponent's active "
                r"pokemon is now (" + _CONDITION_WORDS + r")\."),
     _discard_all_self_then_condition),
    ("scale.per-named-team-in-play",
     re.compile(r"this attack does (\d+) damage for each of your ([a-z]"
                r"[\w' -]*) pokemon in play\."), _per_named_team_in_play),
    ("discard.opponent-tools-and-special",
     re.compile(r"discard all pokemon tools and special energy from all of your "
                r"opponent's pokemon\."),
     _discard_all_opponent_tools_and_special),
    ("bonus.empty-hand-printed",
     re.compile(r"if you have no cards in your hand, this attack does (\d+) "
                r"more damage\."), _bonus_if_empty_hand_printed),
    ("self.damage-per-counters",
     re.compile(r"this pokemon does (\d+) damage to itself for each damage "
                r"counter on it\."), _self_damage_per_counters),
    ("bonus.times-opponent-energy",
     re.compile(r"this attack does (\d+) more damage times the number of energy "
                r"attached to your opponent's active pokemon\."),
     _more_times_opponent_energy),
    ("bonus.defender-gx-or-ex",
     re.compile(r"if your opponent's active pokemon is a pokemon-gx or a "
                r"pokemon-ex, this attack does (\d+) more damage(?: \(before "
                r"applying weakness and resistance\))?\."),
     _bonus_if_defender_gx_or_ex),
    ("bonus.per-bench-typed",
     re.compile(r"this attack does (\d+) more damage for each of your benched ("
                + _TYPE_WORDS + r") pokemon\."), _more_per_bench_typed),
    ("disrupt.shuffle-hand-draw-their-hand",
     re.compile(r"shuffle your hand into your deck\. then, draw a card for each "
                r"card in your opponent's hand\."),
     _shuffle_hand_draw_opponent_hand),
    ("bonus.per-team-typed-energy",
     re.compile(r"this attack does (\d+) more damage times the amount of ("
                + _TYPE_WORDS + r") energy attached to your pokemon\."),
     _more_per_team_typed_energy),
    ("flip.base-plus-else-base",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage plus "
                r"(\d+) more damage\. if tails, this attack does \1 "
                r"damage\."), _flip_base_plus_else_base),
    ("snipe.flip-heads-chosen-no-tail",
     re.compile(r"flip a coin\. if heads, choose (?:an?|(\d+)) of your "
                r"opponent's pokemon\. this attack does (\d+) damage to that "
                r"pokemon\. don't apply weakness and resistance\."),
     _flip_snipe_chosen_no_tail),
    ("peek.top-pick-shuffle-rest",
     re.compile(r"look at the top (\d+) cards of your deck and put (\d+) of "
                r"them into your hand\. shuffle the other cards back into your "
                r"deck\."), _top_pick_then_shuffle),
    # -- batch 45: own-name searches, flipped spreads, stadium riders ------
    ("search.same-name-to-bench",
     re.compile(r"search your deck for up to (\d+) this pokemon and put them "
                r"onto your bench\. then, shuffle your deck\."),
     _search_name_onto_bench),
    ("search.same-name-one-to-bench",
     re.compile(r"search your deck for this pokemon and put it onto your bench"
                r"(?: then,| )? shuffle your deck(?: afterward)?\."),
     _search_name_onto_bench),
    ("search.same-name-to-bench-full",
     re.compile(r"search your deck for a basic pokemon named this pokemon and "
                r"put it onto your bench\. shuffle your deck afterward\. \(you "
                r"can't use this attack if your bench is full\.\)"),
     _search_name_onto_bench_one),
    ("switch.self-then-opponent-swaps",
     re.compile(r"switch this pokemon with (?:an?|1) of your benched pokemon\. "
                r"then, your opponent switches (?:the defending pokemon|his or "
                r"her active pokemon) with (?:an?|1) of his or her benched "
                r"pokemon\."), _switch_self_then_opponent_switches),
    ("heal.self-if-damage-landed",
     re.compile(r"unless all damage from this attack is prevented, you may "
                r"remove (\d+) damage counters? from this pokemon\."),
     _heal_if_damage_landed),
    ("reorder.either-top-any-order",
     re.compile(r"look at the top (\d+) cards of either player's deck and put "
                r"them back in any order\."), _reorder_either_top_plain),
    ("bonus.per-opponent-with-ability",
     re.compile(r"this attack does (\d+) more damage for each of your "
                r"opponent's pokemon in play that has an ability\."),
     _more_per_opponent_with_ability),
    ("spread.flip-per-opponent",
     re.compile(r"for each of your opponent's pokemon, flip a coin\. if heads, "
                r"this attack does (\d+) damage to that pokemon" + _SNIPE_TAIL),
     _flip_per_opponent_spread),
    ("spread.flips-times-heads-all",
     re.compile(r"flip (\d+) coins\. this attack does (\d+) damage times the "
                r"number of heads to each of your opponent's pokemon" +
                _SNIPE_TAIL), _flip_times_heads_spread_all),
    ("peek.self-top-pokemon-bench",
     re.compile(r"look at the top (\d+) cards of your deck\. you may put any "
                r"number of pokemon you find there onto your bench\. shuffle "
                r"the other cards back into your deck\."),
     _top_pokemon_to_bench),
    ("bonus.stadium-then-discard-plain",
     re.compile(r"if there is any stadium card in play, this attack does (\d+) "
                r"more damage\. discard that stadium card\."),
     _bonus_stadium_then_discard_plain),
    ("bonus.per-prizes-taken-recoil",
     re.compile(r"this attack does (\d+) more damage for each prize card your "
                r"opponent has taken\. this pokemon also does (\d+) damage to "
                r"itself\."), _more_per_prizes_taken_recoil),
    # -- batch 44: the 3-card tail, second pass ----------------------------
    ("attach.flip-typed-discard-self",
     re.compile(r"flip a coin\. if heads, search your discard pile for an? ("
                + _TYPE_WORDS + r") energy card and attach it to this "
                r"pokemon\."), _flip_attach_typed_discard_self),
    ("draw.opponent-may-draw",
     re.compile(r"your opponent may draw (an?|\d+) cards?\."),
     _opponent_may_draw),
    ("bonus.base-plus-self-damaged",
     re.compile(r"if this pokemon has any damage counters on it, this attack "
                r"does (\d+) damage plus (\d+) more damage\."),
     _base_plus_if_self_damaged),
    ("bonus.base-plus-self-typed-energy",
     re.compile(r"if this pokemon has any (" + _TYPE_WORDS + r") energy "
                r"attached to it, this attack does (\d+) damage plus (\d+) "
                r"more damage\."), _base_plus_if_self_has_typed_energy),
    ("scale.base-becomes-if-defender-damaged",
     re.compile(r"if the defending pokemon (?:already )?has any damage "
                r"counters? on it, this attack's base damage is (\d+) instead "
                r"of \d+\."), _base_becomes_if_defender_damaged),
    ("heal.self-then-defender-no-retreat",
     re.compile(r"remove (\d+) damage counters? from this pokemon\. the "
                r"defending pokemon can't retreat during your opponent's next "
                r"turn\."), _heal_self_then_lock_retreat),
    ("attach.discard-energy-up-to-self",
     re.compile(r"search your discard pile for up to (\d+) energy cards and "
                r"attach them to this pokemon\."), _attach_many_discard_energy_self),
    ("bonus.base-plus-opponent-one-prize",
     re.compile(r"if your opponent has only 1 prize card left, this attack does "
                r"(\d+) damage plus (\d+) more damage\."),
     _base_plus_if_opponent_one_prize),
    ("snipe.flip-heads-chosen-spread",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage to "
                r"(?:an?|(\d+)) of your opponent's pokemon" + _SNIPE_TAIL),
     _flip_heads_chosen_spread),
    ("energy.take-from-own-other",
     re.compile(r"take a basic energy card attached to (?:an?|1) of your "
                r"pokemon and attach it to another of your pokemon\."),
     _take_energy_from_own_other),
    ("switch.self-if-any",
     re.compile(r"switch this pokemon with (?:an?|1) of your benched pokemon, "
                r"if any\."), _switch_self_if_any),
    ("scale.base-plus-per-defender-retreat",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each colorless "
                r"energy in the defending pokemon's retreat cost \(after "
                r"applying effects to the retreat cost\)\."),
     _base_plus_per_defender_retreat_colorless),
    ("condition.if-defender-evolved",
     re.compile(r"if (?:the defending pokemon|your opponent's active pokemon) "
                r"is an evolved pokemon, (?:the defending pokemon|your "
                r"opponent's active pokemon) is now (" + _CONDITION_WORDS +
                r")\."), _condition_if_defender_evolved),
    ("recover.energy-reveal",
     re.compile(r"search your discard pile for an energy card, show it to your "
                r"opponent, and put it into your hand\."), _recover_energy_reveal),
    ("draw.from-bottom",
     re.compile(r"draw (\d+) cards? from the bottom of your deck\."),
     _draw_from_bottom),
    ("self.bench-damage-chosen",
     re.compile(r"does (\d+) damage to (?:an?|(\d+)) of your benched pokemon"
                + _SNIPE_TAIL), _damage_own_bench),
    ("disrupt.hand-down-to",
     re.compile(r"discard random cards from your opponent's hand until they "
                r"have (\d+) cards? in their hand\."),
     _discard_opponent_hand_down_to),
    ("bonus.base-plus-empty-hand",
     re.compile(r"if you have no cards in your hand, this attack does (\d+) "
                r"damage plus (\d+) more damage\."), _base_plus_if_empty_hand),
    ("bonus.per-damaged-bench",
     re.compile(r"this attack does (\d+) more damage for each of your benched "
                r"pokemon that has any damage counters on it\."),
     _more_per_damaged_bench),
    ("bonus.per-all-opponent-counters",
     re.compile(r"this attack does (\d+) more damage for each damage counter on "
                r"all of your opponent's pokemon\."),
     _more_per_all_opponent_counters),
    ("heal.self-no-period",
     re.compile(r"heal (\d+) damage from this pokemon"), _heal_self_no_period),
    ("search.any-cards-up-to",
     re.compile(r"search your deck for up to (\d+) cards and put them into your "
                r"hand\. shuffle your deck afterward\."), _search_any_cards_up_to),
    ("gate.no-stadium",
     re.compile(r"if there is no stadium in play, this attack does nothing\."),
     _gate_no_stadium),
    ("reorder.opponent-top",
     re.compile(r"look at the top (\d+) cards of your opponent's deck and put "
                r"them back in any order\."), _reorder_opponent_top),
    ("peek.self-top-discard",
     re.compile(r"look at the top card of your deck\. you may discard that "
                r"card\."), _peek_and_optional_discard),
    # -- batch 43: target-side boosts, hand mills, capped bonuses ----------
    ("self.to-hand-discard-attached",
     re.compile(r"you may put this pokemon into your hand\. \(discard all "
                r"cards attached to this pokemon\.\)"), _self_to_hand),
    ("discard.hand-energy-then-damage",
     re.compile(r"discard up to (\d+) basic (?:(?P<type>" + _TYPE_WORDS +
                r") )?energy cards? from your hand\. this attack does (\d+) "
                r"damage for each card you discarded in this way\."),
     _discard_hand_energy_then_damage_swap),
    ("scale.per-named-in-play",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each ([a-z]"
                r"[\w' -]*) you have in play\."), _per_named_in_play),
    ("bonus.defender-takes-more-next-turn",
     re.compile(r"during your next turn, the defending pokemon takes (\d+) "
                r"more damage from attacks \(after applying weakness and "
                r"resistance\)\."), _defender_takes_more_next_turn),
    ("energy.move-any-between-own",
     re.compile(r"move any number of energy from your pokemon to your other "
                r"pokemon in any way you like\."), _move_any_energy_between_own),
    ("energy.move-all-to-bench-any",
     re.compile(r"move all energy from this pokemon to your benched pokemon in "
                r"any way you like\."), _move_all_energy_to_bench_any),
    ("counters.until-remaining-hp",
     re.compile(r"put damage counters on your opponent's active pokemon until "
                r"its remaining hp is (\d+)\."), _counters_until_hp),
    ("counters.per-opponent-hand",
     re.compile(r"for each card in your opponent's hand, put (\d+) damage "
                r"counters? on their active pokemon\."),
     _counters_per_opponent_hand),
    ("scale.per-attack-in-discard",
     re.compile(r"this attack does (\d+) damage for each pokemon in your "
                r"discard pile that has the ([a-z][\w' -]*) attack\."),
     _per_cards_with_attack_in_discard),
    ("scale.times-hand-size",
     re.compile(r"this attack does (\d+) damage times the number of cards in "
                r"your hand\."), _times_hand_size),
    ("bonus.capped-per-supporter-discard",
     re.compile(r"this attack does (\d+) more damage for each supporter card "
                r"in your discard pile\. you can't add more than (\d+) damage "
                r"in this way\."), _bonus_capped_per_supporter_discard),
    ("bonus.capped-per-energy-type",
     re.compile(r"this attack does (\d+) more damage for each type of basic "
                r"energy card in your discard pile\. you can't add more than "
                r"(\d+) damage in this way\."), _bonus_capped_per_energy_type),
    ("bonus.per-opponent-gx-ex",
     re.compile(r"this attack does (\d+) more damage for each of your "
                r"opponent's pokemon-gx and pokemon-ex in play\."),
     _bonus_per_opponent_gx_ex),
    ("search.energy-attach-bench-any",
     re.compile(r"search your deck for up to (\d+) (?:(?P<type>"
                + _TYPE_WORDS + r") )?energy cards and attach them to your "
                r"benched pokemon in any way you like\. then, shuffle your "
                r"deck\."), _search_energy_attach_bench),
    # -- batch 42: team boosts, energy-gated retreat, first-turn evolution --
    ("ability.retreat-free-with-any-energy",
     re.compile(r"if this pokemon has any energy attached(?: to it)?, it has no "
                r"retreat cost\."), _free_retreat_with_energy),
    ("ability.typed-energy-retreat-cost",
     re.compile(r"if this pokemon has any (" + _TYPE_WORDS + r") energy "
                r"attached to it, the retreat cost for this pokemon is (\d+)\."),
     _passive_typed_energy_retreat_cost),
    ("ability.team-typed-damage-boost",
     re.compile(r"your (" + _TYPE_WORDS + r") pokemon's attacks do (\d+) more "
                r"damage to (?:the active|your opponent's active) pokemon "
                r"\(before applying weakness and resistance\)\."),
     _passive_team_typed_boost),
    ("ability.effects-only-shield",
     re.compile(r"prevent all effects of attacks, (?:excluding|except) damage, "
                r"done to this pokemon(?: by the attacking pokemon)?\."),
     _passive_effects_shield),
    ("ability.reduce-damage-from-types",
     re.compile(r"any damage done to this pokemon by attacks from (" +
                _TYPE_WORDS + r")(?: pokemon)? and (" + _TYPE_WORDS +
                r") pokemon is reduced by (\d+) \(after applying weakness and "
                r"resistance\)\."), _passive_reduce_from_types_joined),
    ("ability.hp-per-typed-energy",
     re.compile(r"this pokemon gets \+(\d+) hp for each (" + _TYPE_WORDS +
                r") energy attached to it\."), _passive_hp_per_typed_energy),
    ("ability.recover-basics-and-evolutions",
     re.compile(r"choose up to (\d+) basic pokemon and/or evolution cards from "
                r"your discard pile and put them into your hand\."),
     _recover_basics_and_evolutions),
    ("ability.condition-immunity-list",
     re.compile(r"this pokemon can't become (" + _CONDITION_WORDS +
                r"(?:, " + _CONDITION_WORDS + r")*(?:,? (?:or|and) "
                + _CONDITION_WORDS + r"))\."), _passive_condition_immunity_list),
    ("ability.evolve-early",
     re.compile(r"this pokemon can evolve during (?:your first turn or the turn "
                r"you play it|the turn you play it)\."), _passive_evolve_early),
    ("ability.team-free-retreat-no-gx-ex",
     re.compile(r"your pokemon in play have no retreat cost, except pokemon-gx "
                r"and pokemon-ex\."), _passive_team_free_retreat_no_gx_ex),
    # -- batch 41: bench scaling, mills, swaps and resistance gates --------
    ("heal.equal-to-damage-dealt",
     re.compile(r"remove from this pokemon the number of damage counters equal "
                r"to the damage you did to the defending pokemon\."),
     _heal_equal_to_damage),
    ("bonus.self-on-bench",
     re.compile(r"if this pokemon is on your bench, this attack does (\d+) "
                r"more damage\."), _more_if_self_on_bench),
    ("bonus.all-bench-damaged",
     re.compile(r"if all of your benched pokemon have at least (?:an?|1) damage "
                r"counters? on them, this attack does (\d+) more damage\."),
     _more_if_all_bench_damaged),
    ("scale.base-becomes-if-energy-differs",
     re.compile(r"if this pokemon and the defending pokemon have a different "
                r"amount of energy attached to them, this attack's base damage "
                r"is (\d+) instead of \d+\."), _base_becomes_if_energy_differs),
    ("counters.place-then-damage-each",
     re.compile(r"put up to (\d+) damage counters on this pokemon\. this "
                r"attack does (\d+) damage for each damage counter you placed "
                r"in this way\."), _counters_then_damage_per_placed),
    ("scale.half-defender-hp",
     re.compile(r"does damage to the defending pokemon equal to half the "
                r"defending pokemon's remaining hp \(rounded up to the nearest "
                r"10\)\."), _half_defender_hp),
    ("mill.own-then-damage-per-energy",
     re.compile(r"discard the top (\d+) cards? from your deck\. this attack "
                r"does (\d+) damage times the number of energy cards you "
                r"discarded\."), _mill_own_then_damage_per_energy),
    ("flip.both-tails-else-discard-energy",
     re.compile(r"flip (\d+) coins\. if both are tails, this attack does "
                r"nothing\. for each heads, discard an energy attached to the "
                r"defending pokemon\."), _flip_both_tails_else_discard_energy),
    ("search.named-energy-attach-self",
     re.compile(r"search your deck for an? ([a-z][\w' -]*) energy card and "
                r"attach it to this pokemon\. (?:then, )?shuffle your deck(?: "
                r"afterward)?\."), _search_named_energy_attach_self),
    ("bonus.per-prizes-taken-discard-energy",
     re.compile(r"this attack does (\d+) more damage for each prize card your "
                r"opponent has taken\. discard an energy from this pokemon\."),
     _more_per_prizes_taken_discard_energy),
    ("counters.swap-both-actives",
     re.compile(r"switch all damage counters on this pokemon with those on your "
                r"opponent's active pokemon\."), _swap_all_damage_counters),
    ("bonus.defender-resistance-type",
     re.compile(r"if your opponent's active pokemon has (" + _TYPE_WORDS +
                r") resistance, this attack does (\d+) more damage\."),
     _more_if_defender_resistance),
    ("shuffle.opponent-deck",
     re.compile(r"shuffle your opponent's deck\."), _shuffle_opponent_deck),
    ("lock.flip-defender-retreat",
     re.compile(r"flip a coin\. if heads, the defending pokemon can't retreat "
                r"during your next turn\."), _flip_lock_defender_retreat),
    ("reorder.either-top-up-to",
     re.compile(r"look at up to (\d+) cards from the top of either player's "
                r"deck and rearrange them as you like\."), _rearrange_either_top),
    ("condition.both-confused",
     re.compile(r"both the defending pokemon and this pokemon are now "
                r"\(?(?:confused)\)?(?: \(after doing damage\))?\.") if False
     else re.compile(r"both the defending pokemon and this pokemon are now ("
                     + _CONDITION_WORDS + r")(?: \(after doing damage\))?\."),
     _flip_both_confused),
    # -- batch 40: condition gates, immunity, team shields, play triggers ---
    ("ability.asleep-damage-shield",
     re.compile(r"as long as this pokemon is asleep, prevent all damage done to "
                r"this pokemon by attacks\."), _passive_asleep_shield),
    ("ability.condition-immune-all",
     re.compile(r"this pokemon can't be affected by any special conditions\."),
     _passive_condition_immune_all),
    ("ability.all-attack-damage-reduced",
     re.compile(r"all damage done by attacks to this pokemon is reduced by "
                r"(\d+) \(after applying weakness and resistance\)\."),
     _passive_takes_less_flat),
    ("ability.ultra-beast-takes-less",
     re.compile(r"your ultra beasts take (\d+) less damage from your "
                r"opponent's attacks \(after applying weakness and "
                r"resistance\)\."), _passive_ultra_beast_takes_less),
    ("ability.basic-attack-tax-active",
     re.compile(r"as long as this pokemon is your active pokemon, your "
                r"opponent's basic pokemon's attacks cost ((?:colorless)+) "
                r"more\."), _passive_basic_attack_tax_active),
    ("discard.opponent-special-energy-chosen",
     re.compile(r"discard (?:an?|(\d+)) special energy from (?:an?|1) of your "
                r"opponent's pokemon\."), _discard_special_energy_chosen),
    ("condition.leave-both-actives",
     re.compile(r"leave both active pokemon (" + _CONDITION_WORDS + r")\."),
     _both_actives_conditions),
    # -- batch 39: discard-pile attaches, flip riders, play locks -----------
    ("spread.both-benches-recoil",
     re.compile(r"does (\d+) damage to each pokemon on each player's bench"
                + _SNIPE_TAIL + r" this pokemon does (\d+) damage to "
                r"itself\."), _both_benches_and_recoil),
    ("bonus.base-plus-less-energy",
     re.compile(r"if this pokemon has less energy attached to it than the "
                r"defending pokemon, this attack does (\d+) damage plus (\d+) "
                r"more damage\."), _base_plus_if_less_energy),
    ("discard.flip-tails-self-energy",
     re.compile(r"flip a coin\. if tails, discard (an?|\d+) energy attached to "
                r"this pokemon\."), _flip_tails_discard_self_energy),
    ("scale.per-self-counter-flip-confuse",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each damage "
                r"counter on this pokemon\. flip a coin\. if tails, this "
                r"pokemon is now confused \(after doing damage\)\."),
     _per_self_counter_then_flip_confuse),
    ("recover.card-to-deck-top",
     re.compile(r"put a card from your discard pile on top of your deck\."),
     _discard_card_to_deck_top),
    ("energy.move-bench-to-self-one",
     re.compile(r"move an energy from (?:an?|1) of your benched pokemon to this "
                r"pokemon\."), _move_bench_energy_to_self_one),
    ("attach.flip-basic-discard-self",
     re.compile(r"flip a coin\. if heads, attach a basic energy card from your "
                r"discard pile to this pokemon\."),
     _flip_attach_basic_from_discard_self),
    ("gate.bench-at-most",
     re.compile(r"if you have (\d+) or fewer benched pokemon, this attack does "
                r"nothing\."), _gate_bench_at_most),
    ("snipe.flip-heads-bench",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage to "
                r"(?:an?|1) of your opponent's benched pokemon" + _SNIPE_TAIL),
     _flip_heads_bench_snipe),
    ("attach.discard-energy-to-bench",
     re.compile(r"(?:search your discard pile for|attach) an? (?P<basic>basic "
                r")?(?:(?P<type>" + _TYPE_WORDS + r") )?energy card (?:from your "
                r"discard pile to|and attach it to) (?:an?|1) of your benched "
                r"pokemon\."), _attach_discard_energy_to_bench),
    ("energy.optional-typed-move-to-bench",
     re.compile(r"you may move an? (" + _TYPE_WORDS + r") energy card attached "
                r"to this pokemon to (?:an?|1) of your benched pokemon\."),
     _optional_typed_energy_move),
    ("flip.per-typed-energy-base-plus",
     re.compile(r"flip a coin for each (" + _TYPE_WORDS + r") energy attached "
                r"to this pokemon\. this attack does (\d+) damage plus (\d+) "
                r"more damage for each heads\."),
     _flip_per_typed_energy_base_plus),
    ("discard.optional-trade-energy",
     re.compile(r"you may discard an energy from this pokemon\. if you do, "
                r"discard an energy from your opponent's active pokemon\."),
     _optional_trade_energy_discard),
    ("flip.base-plus-heal-counters",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage plus "
                r"(\d+) more damage and remove (\d+) damage counters? from this "
                r"pokemon\."), _flip_base_plus_heal_counters),
    ("lock.flip-opponent-supporters",
     re.compile(r"flip a coin\. if heads, your opponent can't play any "
                r"supporter cards from (?:his or her|their) hand during (?:his "
                r"or her|their) next turn\."), _flip_lock_supporters),
    ("lock.opponent-special-energy",
     re.compile(r"your opponent can't play any special energy cards from their "
                r"hand during their next turn\."), _lock_opponent_special_energy),
    ("discard.flip-random-opponent-hand",
     re.compile(r"flip a coin\. if heads, choose (an?|\d+) cards? from your "
                r"opponent's hand without looking and discard (?:it|them)\."),
     _flip_discard_random_opponent),
    ("discard.flip-defender-energy-card",
     re.compile(r"if the defending pokemon has any energy cards attached to it, "
                r"flip a coin\. if heads, choose (?:an?|1) of those energy cards "
                r"and discard it\."), _flip_discard_defender_energy),
    ("attach.basic-hand-energy-one",
     re.compile(r"attach a basic energy card from your hand to (?:an?|1) of "
                r"your pokemon\."), _attach_hand_energy_one),
    ("self.damage-no-modifiers",
     re.compile(r"this pokemon does (\d+) damage to itself, and don't apply "
                r"weakness and resistance to this damage\."), _named_self_damage),
    ("flip.tails-nothing-heads-shield-an-attack",
     re.compile(r"flip a coin\. if tails, this attack does nothing\. if heads, "
                r"prevent all effects of an attack, including damage, done to "
                r"this pokemon during your opponent's next turn\."),
     _flip_tails_nothing_heads_shield_all),
    ("counters.on-own-chosen",
     re.compile(r"put (\d+) damage counters? on (an?|\d+) of your pokemon\."),
     _counters_on_own_chosen),
    ("heal.each-typed",
     re.compile(r"heal (\d+) damage from each of your (" + _TYPE_WORDS +
                r") pokemon\."), _heal_each_typed),
    ("recover.supporter-card",
     re.compile(r"put a supporter card from your discard pile into your "
                r"hand\."), _recover_supporter),
    ("ko.if-counters-at-least",
     re.compile(r"if your opponent's active pokemon has (\d+) or more damage "
                r"counters on it, that pokemon is knocked out\."),
     _ko_if_counters_at_least),
    ("protect.effects-shield-damage-not-effect",
     re.compile(r"during your opponent's next turn, prevent all effects of "
                r"attacks used by your opponent's pokemon done to this "
                r"pokemon\. \(damage is not an effect\.\)"),
     _shield_effects_only),
    ("lock.defender-cannot-attack-reordered",
     re.compile(r"during your opponent's next turn, the defending pokemon "
                r"can't attack\."), _lock_defender_attacks_plain),
    ("flip.per-self-energy-coins-equal",
     re.compile(r"flip a number of coins equal to the number of energy "
                r"attached to this pokemon\. this attack does (\d+) damage "
                r"times the number of heads\."), _flip_per_self_energy),
    # -- batch 38: old-era self riders, energy costs, flip shields ----------
    ("scale.base-plus-phrase",
     re.compile(r"(?:this attack )?does (\d+) damage plus (\d+) more damage "
                r"for each (.+)\."), _base_plus_from_phrase),
    ("scale.times-number-phrase",
     re.compile(r"(?:this attack )?does (\d+) damage times the number of "
                r"(.+)\."), _times_number_from_phrase),
    ("protect.flip-all-effects",
     re.compile(r"flip a coin\. if heads, (?:during your opponent's next turn, "
                r"prevent all effects of attacks, including damage, done to "
                r"this pokemon|prevent all effects of an attack, including "
                r"damage, done to this pokemon during your opponent's next "
                r"turn)\."), _flip_protect_all),
    ("protect.flip-damage-only",
     re.compile(r"flip a coin\. if heads, prevent all damage done to this "
                r"pokemon during your opponent's next turn\. \(any other "
                r"effects of attacks still happen\.\)"), _flip_protect_damage),
    ("heal.remove-self-counters",
     re.compile(r"remove (\d+) damage counters? from this pokemon\."),
     _remove_self_counters),
    ("heal.flip-remove-self-counters",
     re.compile(r"flip a coin\. if heads, remove (\d+) damage counters? from "
                r"this pokemon\."), _flip_remove_self_counters),
    ("cure.self",
     re.compile(r"remove all special conditions from this pokemon\."),
     _cure_self),
    ("cure.self-heal-sleep",
     re.compile(r"remove all special conditions and (\d+) damage counters? "
                r"from this pokemon\. this pokemon is now asleep\."),
     _cure_heal_sleep_self),
    ("cost.discard-self-energy",
     re.compile(r"discard (?:(?P<all>all)|(?P<count>an?|\d+)) "
                r"(?P<basic>basic )?(?:(?P<type>" + _TYPE_WORDS + r") )?energy "
                r"(?:cards? )?attached to this pokemon (?:in order to use this "
                r"attack|or this attack does nothing)\."),
     _energy_cost_then_damage),
    ("flip.times-heads-self-condition",
     re.compile(r"flip (\d+) coins\. this attack does (\d+) damage times the "
                r"number of heads\. this pokemon is now (" + _CONDITION_WORDS +
                r")\."), _flip_times_heads_self_condition),
    ("flip.plus-else-self-damage",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage plus "
                r"(\d+) more damage(?:\.|;) if tails, this (?:attack does \1 "
                r"damage and this )?pokemon does (\d+) damage to itself\."),
     _flip_plus_else_self_damage),
    ("optional.base-plus-self-damage",
     re.compile(r"you may do (\d+) damage plus (\d+) more damage\. if you "
                r"do, this pokemon does (\d+) damage to itself\."),
     _optional_base_plus_self_damage),
    ("protect.reduce-all-damage-next-turn",
     re.compile(r"all damage done by attacks to this pokemon during your "
                r"opponent's next turn is reduced by (\d+) \(after applying "
                r"weakness and resistance\)\."), _reduce_next_turn),
    ("debuff.self-vulnerable-next-turn",
     re.compile(r"during your opponent's next turn, any damage done to this "
                r"pokemon by attacks is increased by (\d+) \(after applying "
                r"weakness and resistance\)\."), _vulnerable_next_turn),
    ("attach.discard-energy-to-self",
     re.compile(r"search your discard pile for an? (?:(" + _TYPE_WORDS +
                r") )?energy card and attach it to this pokemon\."),
     _attach_discard_energy_to_self),
    ("flip.tails-counters-self",
     re.compile(r"flip a coin\. if tails, put (\d+) damage counters? on this "
                r"pokemon\."), _flip_tails_counters_self),
    ("counters.on-self",
     re.compile(r"put (\d+) damage counters? on this pokemon\."),
     _counters_on_self),
    ("draw.each-player",
     re.compile(r"each player draws (\d+) cards?\."), _each_player_draws),
    ("flip.times-self-counters",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage times "
                r"the number of damage counters on this pokemon\."),
     _flip_times_self_counters),
    ("attach.typed-hand-energy-self",
     re.compile(r"attach an? (" + _TYPE_WORDS + r") energy card from your hand "
                r"to this pokemon\."), _attach_typed_hand_energy_to_self),
    ("switch.flip-self",
     re.compile(r"flip a coin\. if heads, switch this pokemon with (?:an?|1) "
                r"of your benched pokemon\."), _flip_switch_self),
    ("search.evolve-self-counts-as",
     re.compile(r"search your deck for a card that evolves from this pokemon "
                r"and put it on(?:to)? this pokemon\. \(this counts as evolving "
                r"this pokemon\.\) shuffle your deck(?: afterward)?\."),
     _evolve_from_deck),
    # -- batch 37: continuous ability shields, retreat rules, utilities ----
    ("ability.bench-team-shield",
     re.compile(r"prevent all damage done to your benched pokemon by your "
                r"opponent's attacks\."), _passive_bench_team_shield),
    ("ability.flip-survive",
     re.compile(r"if this pokemon would be knocked out by damage from an "
                r"attack, flip a coin\. if heads, this pokemon is not knocked "
                r"out, and its remaining hp becomes (\d+)\."),
     _passive_flip_survive),
    ("ability.special-energy-hp",
     re.compile(r"if this pokemon has any special energy attached(?: to it)?, "
                r"it gets \+(\d+) hp\."), _passive_special_energy_hp),
    ("ability.active-team-takes-less",
     re.compile(r"as long as this pokemon is your active pokemon, all of your "
                r"pokemon take (\d+) less damage from your opponent's attacks "
                r"\(after applying weakness and resistance\)\."),
     _passive_active_team_takes_less),
    ("ability.active-vs-active-debuff",
     re.compile(r"as long as this pokemon is in the active spot, attacks used "
                r"by your opponent's active pokemon do (\d+) less damage "
                r"\(before applying weakness and resistance\)\."),
     _passive_active_vs_active_debuff),
    ("ability.condition-immunity",
     re.compile(r"this pokemon can't be (" + _CONDITION_WORDS + r")\."),
     _passive_condition_immunity),
    ("ability.typed-energy-free-retreat",
     re.compile(r"if this pokemon has any (" + _TYPE_WORDS + r") energy "
                r"attached(?: to it)?, it has no retreat cost\."),
     _passive_typed_energy_free_retreat),
    ("ability.team-typed-energy-free-retreat",
     re.compile(r"each of your pokemon that has any (" + _TYPE_WORDS +
                r") energy attached to it has no retreat cost\."),
     _passive_team_typed_energy_free_retreat),
    ("ability.bench-active-retreat-discount",
     re.compile(r"as long as this pokemon is on your bench, your active "
                r"pokemon's retreat cost is ((?:colorless)+) less\."),
     _passive_bench_active_retreat_discount),
    ("ability.benched-full-shield",
     re.compile(r"as long as this pokemon is on your bench, prevent all damage "
                r"from and effects of attacks from your opponent's pokemon "
                r"done to this pokemon\."), _passive_benched_full_shield),
    ("ability.discard-pokemon-heal-self",
     re.compile(r"discard a pokemon from your hand\. if you do, heal (\d+) "
                r"damage from this pokemon\."), _discard_pokemon_heal_self),
    ("ability.attach-typed-hand-energy",
     re.compile(r"attach an? (" + _TYPE_WORDS + r") energy card from your hand "
                r"to (?:an?|1) of your pokemon\."),
     _attach_typed_hand_energy_to_one),
    ("ability.top-pick-rest-bottom",
     re.compile(r"look at the top (\d+) cards of your deck and put (\d+) of "
                r"them into your hand\. put the other cards? on the bottom of "
                r"your deck(?: in any order)?\."), _top_pick_rest_bottom),
    # -- batch 36: next-turn shields, recoveries, old-era riders -----------
    ("flip.both-tails-nothing",
     re.compile(r"flip (\d+) coins\. if both (?:of them )?are tails, this "
                r"attack does nothing\."), _flip_two_both_tails_nothing),
    ("flip.heads-heal-self",
     re.compile(r"flip a coin\. if heads, heal (\d+) damage from this "
                r"pokemon\."), _flip_heal_self),
    ("search.any-pokemon-reveal",
     re.compile(r"search your deck for a pokemon, reveal it, and put it into "
                r"your hand\. shuffle your deck afterward\."),
     _search_any_pokemon_reveal),
    ("draw.opponent-draws",
     re.compile(r"your opponent draws (an?|\d+) cards?\."), _opponent_draws),
    ("lock.opponent-items-his-or-her",
     re.compile(r"your opponent can't play any item cards from his or her hand "
                r"during his or her next turn\."), _lock_opponent_items_v2),
    ("ko.if-defender-condition-it",
     re.compile(r"if your opponent's active pokemon is affected by a special "
                r"condition, it is knocked out\."), _ko_any_condition),
    ("recover.basic-energy-up-to",
     re.compile(r"put up to (\d+) basic energy cards from your discard pile "
                r"into your hand\."), _recover_basic_energy_up_to),
    ("search.supporter-reveal-afterward",
     re.compile(r"search your deck for a supporter card, reveal it, and put it "
                r"into your hand\. shuffle your deck afterward\."),
     _search_supporter),
    ("recover.trainer-card",
     re.compile(r"put a trainer card from your discard pile into your "
                r"hand\."), _recover_trainer),
    ("heal.if-defender-condition",
     re.compile(r"if your opponent's active pokemon is (" + _CONDITION_WORDS +
                r"), heal (\d+) damage from this pokemon\."),
     _heal_if_defender_condition),
    ("condition.each-defending",
     re.compile(r"each defending pokemon is now (" + _CONDITION_WORDS + r")\."),
     _condition_each_defending),
    ("bonus.base-plus-more-prizes",
     re.compile(r"if you have more prize cards left than your opponent, this "
                r"attack does (\d+) damage plus (\d+) more damage\."),
     _base_plus_if_more_prizes),
    ("energy.typed-to-hand",
     re.compile(r"put (an?|\d+) (" + _TYPE_WORDS + r") energy attached to this "
                r"pokemon into your hand\."), _typed_energy_to_hand),
    ("remove.self-to-deck-forced",
     re.compile(r"shuffle this pokemon and all (?:attached cards|cards attached "
                r"to it) into your deck\."), _shuffle_self_into_deck_forced),
    ("bonus.extra-prize-vs-gx-ex",
     re.compile(r"if your opponent's pokemon-gx or pokemon-ex is knocked out by "
                r"damage from this attack, take (\d+) more prize cards?\."),
     _extra_prize_vs_gx_ex),
    ("protect.effects-only-next-turn",
     re.compile(r"prevent all effects of your opponent's attacks, except "
                r"damage, done to this pokemon during your opponent's next "
                r"turn\."), _shield_effects_only),
    ("protect.from-gx-ex-next-turn",
     re.compile(r"during your opponent's next turn, prevent all damage done to "
                r"this pokemon by attacks from pokemon-gx and pokemon-ex\."),
     _shield_from_gx_ex_next_turn),
    ("protect.flip-prevent-next-turn",
     re.compile(r"if any damage is done to this pokemon by attacks during your "
                r"opponent's next turn, flip a coin\. if heads, prevent that "
                r"damage\."), _flip_prevent_next_turn),
    ("protect.damage-at-most-plain",
     re.compile(r"during your opponent's next turn, prevent all damage done to "
                r"this pokemon by attacks if that damage is (\d+) or less\."),
     _prevent_damage_at_most_next_turn),
    ("lock.flip-tails-self",
     re.compile(r"flip a coin\. if tails, during your next turn, this pokemon "
                r"can't (?:use )?attacks?\."), _flip_tails_lock_self),
    ("lock.self-named",
     re.compile(r"(?!this pokemon)" + _SELF_NAME + r" can't attack during your "
                r"next turn\."), _lock_self),
    ("ko.if-exact-counters",
     re.compile(r"if your opponent's active pokemon has exactly (\d+) damage "
                r"counters on it, that pokemon is knocked out\."),
     _ko_if_exact_counters),
    ("heal.everyone",
     re.compile(r"heal (\d+) damage from each pokemon \(both yours and your "
                r"opponent's\)\."), _heal_everyone),
    ("disrupt.opponent-shuffle-hand-draw",
     re.compile(r"your opponent shuffles their hand into their deck and draws "
                r"(\d+) cards\."), _opponent_shuffles_hand_draws),
    ("search.any-card-optional",
     re.compile(r"you may search your deck for a card and put it into your "
                r"hand\. then, shuffle your deck\."), _search_any_card_optional),
    ("counters.each-damaged-opponent",
     re.compile(r"put (\d+) damage counters on each of your opponent's pokemon "
                r"that has any damage counters on it\."),
     _counters_each_damaged_opponent),
    ("spread.every-bench",
     re.compile(r"this attack does (\d+) damage to each benched pokemon \(both "
                r"yours and your opponent's\)" + _SNIPE_TAIL),
     _spread_every_bench),
    ("bonus.entered-active-and-condition",
     re.compile(r"if this pokemon was on the bench and became your active "
                r"pokemon this turn, this attack does (\d+) more damage, and "
                r"your opponent's active pokemon is now (" + _CONDITION_WORDS +
                r")\."), _entered_active_bonus_condition),
    ("gust.switch-then-damage-new",
     re.compile(r"switch (?:an?|\d+) of your opponent's benched pokemon with "
                r"their active pokemon\. this attack does (\d+) damage to the "
                r"new active pokemon\."),
     _gust_switch_then_damage_new),
    # -- batch 35: hand gates, discard-to-draw, self-counter scaling --------
    ("gate.hand-exactly",
     re.compile(r"if you don't have exactly (\d+) cards in your hand, this "
                r"attack does nothing\."), _gate_hand_exactly),
    ("draw.discard-hand-card-if-do",
     re.compile(r"discard a card from your hand\. if you do, draw (\d+) "
                r"cards?\."), _discard_hand_card_if_do_draw),
    ("discard.all-self-energy-then-spread",
     re.compile(r"discard all energy from this pokemon\. this attack does "
                r"(\d+) damage to (?:an?|(\d+)) of your opponent's pokemon"
                + _SNIPE_TAIL), _discard_all_self_then_spread),
    ("bonus.vs-evolved-discard-all",
     re.compile(r"if your opponent's active pokemon is an evolution pokemon, "
                r"this attack does (\d+) more damage, and discard all energy "
                r"from this pokemon\."), _bonus_vs_evolved_discard_all),
    ("scale.minus-per-self-counter",
     re.compile(r"(?:this attack )?does (\d+) damage minus (\d+) damage for "
                r"each damage counter on " + _SELF_NAME + r"\."),
     _minus_per_self_counter),
    ("bonus.optional-discard-energy",
     re.compile(r"you may discard an energy attached to this pokemon\. if you "
                r"do, this attack does (\d+) more damage\."),
     _optional_discard_energy_bonus),
    ("flip.until-tails-base-plus",
     re.compile(r"flip a coin until you get tails\. this attack does (\d+) "
                r"damage plus (\d+) more damage for each heads\."),
     _flip_until_tails_base_plus),
    ("flip.condition-else-nothing",
     re.compile(r"flip a coin\. if heads, the defending pokemon is now ("
                + _CONDITION_WORDS + r")\. if tails, this attack does nothing "
                r"\(not even damage\)\."), _flip_condition_else_nothing),
    ("switch.gust-if-bench",
     re.compile(r"if your opponent has any benched pokemon, choose (?:an?|1) "
                r"of them and switch it with (?:his or her active pokemon|the "
                r"defending pokemon)\."), _gust_you_choose),
    ("smokescreen.defender-next-turn",
     re.compile(r"if the defending pokemon tries to attack during your "
                r"opponent's next turn, your opponent flips a coin\. if tails, "
                r"that attack doesn't happen\."), _smokescreen_worded),
    # -- batch 34: ability utilities, heal-and-cure, tails conditions ------
    ("ability.search-typed-basic-to-bench",
     re.compile(r"search your deck for (?:an?|up to (\d+)) basic ("
                + _TYPE_WORDS + r") pokemon and put (?:it|them) onto your "
                r"bench\. then, shuffle your deck\."),
     _search_typed_basic_to_bench),
    ("ability.counters-then-self-ko",
     re.compile(r"put (\d+) damage counters on (?:an?|(\d+)) of your "
                r"opponent's pokemon\. if you use this ability, this pokemon "
                r"is knocked out\."), _counters_then_self_knock_out),
    ("ability.bench-self-switch-in",
     re.compile(r"if this pokemon is on your bench, you may switch (?:this "
                r"pokemon|it) with your active pokemon\."), _bench_self_switch_in),
    ("ability.no-energy-free-retreat",
     re.compile(r"if this pokemon has no energy attached(?: to it)?, it has no "
                r"retreat cost\."), _passive_no_energy_free_retreat),
    ("ability.opponent-active-retreat-tax",
     re.compile(r"your opponent's active pokemon's retreat cost is colorless "
                r"more\."), _passive_opponent_active_retreat_tax),
    ("flip.plus-bonus-else-condition",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage plus "
                r"(\d+) more damage\. if tails, this attack does (\d+) damage "
                r"and the defending pokemon is now (" + _CONDITION_WORDS +
                r")\."), _flip_plus_bonus_else_condition),
    ("heal.self-and-cure",
     re.compile(r"heal (\d+) damage and remove all special conditions from "
                r"this pokemon\."), _heal_and_cure_self),
    ("damage.each-defending",
     re.compile(r"does (\d+) damage to each defending pokemon\."),
     _damage_each_defending),
    ("ability.discard-card-draw",
     re.compile(r"you must discard a card from your hand in order to use this "
                r"ability\. once during your turn, you may draw (\d+) cards?\."),
     _discard_hand_card_then_draw),
    ("bonus.opponent-prizes-exactly",
     re.compile(r"if your opponent has exactly (\d+) prize cards? remaining, "
                r"this attack does (\d+) more damage\."),
     _bonus_if_opponent_prizes_exactly),
    ("bonus.deck-at-most",
     re.compile(r"if there are (\d+) or fewer cards in your deck, this attack "
                r"does (\d+) more damage\."), _bonus_if_deck_at_most),
    ("snipe.bench-chosen-spread",
     re.compile(r"choose (an?|\d+) of your opponent's benched pokemon\. this "
                r"attack does (\d+) damage to each of them" + _SNIPE_TAIL),
     _bench_chosen_spread),
    ("boost.next-turn-opposing-active",
     re.compile(r"during your next turn, (?:attacks used by this pokemon do|this "
                r"pokemon's attacks do) "
                r"(\d+) more damage to your opponent's active pokemon(?: "
                r"\(before applying weakness and resistance\))?\."),
     _next_turn_boost_opposing_active),
    ("self.named-damage-to-itself",
     re.compile(r"[a-z][\w' -]* does (\d+) damage to itself\."),
     _named_self_damage),
    ("snipe.spread-ignoring-weakness-resistance",
     re.compile(r"this attack does (\d+) damage to (?:an?|(\d+)) of your "
                r"opponent's pokemon\. this attack's damage isn't affected by "
                r"weakness or resistance\."), _spread_ignore_weakness_resistance),
    ("snipe.chosen-plain",
     re.compile(r"choose (an?|\d+) of your opponent's pokemon\. this attack "
                r"does (\d+) damage to that pokemon" + _SNIPE_TAIL),
     _snipe_chosen_plain),
    ("discard.self-energy-then-spread",
     re.compile(r"discard (\d+) energy attached to this pokemon\. this attack "
                r"does (\d+) damage to (?:an?|(\d+)) of your opponent's "
                r"pokemon" + _SNIPE_TAIL), _discard_self_energy_then_spread),
    ("flip.per-typed-energy-bonus",
     re.compile(r"flip a coin for each (?:(?P<type>" + _TYPE_WORDS +
                r") )?(?:\w+ )?energy attached to this pokemon\. this attack "
                r"does (\d+) more damage for each heads\."), _flip_per_typed_energy),
    ("scale.times-self-damage-counters",
     re.compile(r"(?:this attack )?does (\d+) damage times the number of damage "
                r"counters on " + _SELF_NAME + r"\."), _times_self_damage_counters),
    ("bonus.base-plus-per-bench",
     re.compile(r"does (\d+) damage plus (\d+) more damage for each of your "
                r"benched pokemon\."), _base_plus_per_bench),
    ("shield.retaliate-counters-next-turn",
     re.compile(r"during your opponent's next turn, if this pokemon is damaged "
                r"by an attack \(even if (?:this pokemon|it) is knocked out\), "
                r"put (\d+) damage counters on the attacking pokemon\."),
     _retaliate_counters_rider),
    ("shield.prevent-attack-damage-next-turn",
     re.compile(r"during your opponent's next turn, if this pokemon would be "
                r"damaged by an attack, prevent that attack's damage done to "
                r"this pokemon\."),
     _prevent_attack_damage_next_turn),
    ("flip.per-self-energy-per-heads",
     re.compile(r"flip a coin for each energy attached to this pokemon\. this "
                r"attack does (\d+) damage (?:times the number of heads|for "
                r"each heads)\."), _flip_per_self_energy),
    ("ability.bench-damage-shield",
     re.compile(r"as long as this pokemon is on your bench, prevent all damage "
                r"done to this pokemon by attacks \(both yours and your "
                r"opponent's\)\."), _passive_bench_damage_shield),
    ("ability.opponent-retreat-tax",
     re.compile(r"the retreat cost of each of your opponent's pokemon in play "
                r"is colorless more\."), _passive_opponent_retreat_tax),
    ("ability.survive-at-full-hp",
     re.compile(r"if this pokemon has full hp and would be knocked out by "
                r"damage from an attack, it is not knocked out, and its "
                r"remaining hp becomes (\d+)\."),
     _passive_survive_full_hp),
]







# "Once during your turn (before your attack), you may <effect>": the text
# itself proves the ability is activated, so binding it also sets the
# activation the engine needs to offer it at all.
_ABILITY_PREFIXES = (
    ("once during your turn (before your attack), you may ",
     "activation", Activations.ONCE_PER_TURN),
    ("once during your turn, you may ", "activation", Activations.ONCE_PER_TURN),
    ("once during your turn (before your attack), ", "activation",
     Activations.ONCE_PER_TURN),
    ("as often as you like during your turn (before your attack), you may ",
     "activation", Activations.UNLIMITED),
    ("as often as you like during your turn, you may ", "activation",
     Activations.UNLIMITED),
    ("during your turn (before your attack), you may ", "activation",
     Activations.UNLIMITED),
    # "When you play this Pokemon from your hand ..." fires on an event.
    ("when you play this pokemon from your hand to evolve 1 of your pokemon "
     "during your turn, you may ", "trigger", Triggers.ON_EVOLVE),
    ("when you play this pokemon from your hand onto your bench during your "
     "turn, you may ", "trigger", Triggers.ON_PLAY),
    ("once during your turn, if this pokemon is in the active spot, you may ",
     "activation_active", Activations.ONCE_PER_TURN),
    ("if this pokemon is your active pokemon, once during your turn (before "
     "your attack), you may ", "activation_active", Activations.ONCE_PER_TURN),
    ("if this pokemon is your active pokemon and is damaged by an opponent's "
     "attack (even if this pokemon is knocked out), ", "trigger",
     Triggers.ON_DAMAGED_BY_ATTACK),
    ("if this pokemon is in the active spot and is damaged by an attack from "
     "your opponent's pokemon (even if this pokemon is knocked out), ",
     "trigger", Triggers.ON_DAMAGED_BY_ATTACK),
)

# name -> bind count, for the coverage report.
BIND_COUNTS = {}
# name -> builder failures (a pattern must never fail silently unnoticed).
BIND_ERRORS = {}


# A trailing clause that switches an activated ability off; stripped before
# matching and enforced as a gate on the bound effect.
_ABILITY_SUFFIXES = (
    "this power can't be used if this pokemon is affected by a special "
    "condition.",
)

# Wordings that changed between eras but mean the same thing in a one-Active
# game; an unmatched text is retried with each side read as the other.
_SYNONYMS = (
    ("his or her", "their"),
    ("him or her", "them"),
    ("the defending pokemon", "your opponent's active pokemon"),
    ("your opponent's active pokemon", "the defending pokemon"),
    (" afterward.", "."),
    ("energy attached to this pokemon to ", "energy from this pokemon to "),
    ("energy card attached to this pokemon to ",
     "energy card from this pokemon to "),
    ("after your attack, you may switch", "you may switch"),
    (" energy attached to this pokemon.", " energy from this pokemon."),
)


def bind(ability, own_name: Optional[str] = None) -> Optional[str]:
    """Bind a wording pattern to `ability`; returns the pattern name or None.

    Only an `unimplemented` effect is ever replaced, so a card with a real
    script keeps it. Older cards name themselves where newer ones say "this
    Pokemon" ("Arcanine does 30 damage to itself"), so when the text as
    printed matches nothing, it is retried with the card's own name read as
    "this Pokemon".
    """
    if ability is None or getattr(ability, "effect", None) is not unimplemented:
        return None
    text = normalize(getattr(ability, "game_text", ""))
    # "(You can't use more than 1 GX attack in a game.)" is a rule marker on
    # the attack, not part of its effect text.
    text = text.replace(
        "(you can't use more than 1 gx attack in a game.)", "").strip()
    # Rule markers that gate the attack, not part of what it does.
    for marker in ("if you go second, you can't use this attack during your "
                   "first turn. ",):
        if text.startswith(marker):
            text = text[len(marker):].strip()
            ability.usable_first_turn = False
    if not text:
        return None

    binder = None
    if not isinstance(ability, Attack) and ability.activation is None \
            and ability.trigger is None:
        # An ability the engine never offers would be a dead bind. The wording
        # itself proves how it is offered ("once during your turn" = activated,
        # "when you play this Pokemon" = triggered), so strip the prefix here
        # and set that on the bind below; continuous passives match as written.
        for prefix, kind, value in _ABILITY_PREFIXES:
            if text.startswith(prefix):
                text = text[len(prefix):].strip()
                binder = (kind, value)
                break
    for suffix in _ABILITY_SUFFIXES:
        if text.endswith(suffix):
            text = text[:-len(suffix)].strip()
            gated = True
            break
    else:
        gated = False
    candidates = [text]
    if own_name:
        named = re.sub(r"(?<![\w'])" + re.escape(normalize(own_name))
                       + r"(?![\w'])", "this pokemon", text)
        if named != text:
            candidates.append(named)
    for text in list(candidates):
        for old, new in _SYNONYMS:
            if old in text:
                variant = text.replace(old, new)
                if variant not in candidates:
                    candidates.append(variant)
    for text in candidates:
        bound = _bind_text(ability, text, binder)
        if bound is not None:
            if gated:
                ability.effect = _gate_on_healthy(ability.effect)
            return bound
    return None


def _bind_text(ability, text: str, binder) -> Optional[str]:
    for name, pattern, build in _PATTERNS:
        match = pattern.fullmatch(text)
        if match is None:
            continue
        try:
            effect = build(match, ability)
        except Exception:
            # A malformed match must never turn a loadable card into a load
            # failure: leave it unimplemented and record why.
            BIND_ERRORS[name] = BIND_ERRORS.get(name, 0) + 1
            return None
        if effect is None:
            # The builder declined (an unknown phrase in a generic pattern):
            # keep looking, a later, more specific pattern may still apply.
            continue
        if isinstance(effect, Passive):
            pass
        elif binder is not None:
            kind, value = binder
            if kind == "trigger":
                ability.trigger = value
            else:
                ability.activation = value
            if kind == "activation_active":
                effect = _only_while_active(effect)
        elif not isinstance(ability, Attack) and ability.activation is None \
                and ability.trigger is None:
            # An ordinary coroutine on an ability the engine cannot offer.
            continue
        if isinstance(effect, Passive):
            # Continuous abilities ("this Pokemon takes 20 less damage"):
            # the passive rides the Ability, there is no coroutine to run.
            ability.passive = effect
        else:
            ability.effect = effect
        ability.effect_source = f"pattern:{name}"
        BIND_COUNTS[name] = BIND_COUNTS.get(name, 0) + 1
        return name
    return None


_register_counts()
_register_conditions()


def bind_definition(definition) -> int:
    """Bind every unimplemented ability on a resolved card definition."""
    bound = 0
    own_name = getattr(definition, "display_name", None)
    for ability in getattr(definition, "abilities", None) or []:
        if bind(ability, own_name) is not None:
            bound += 1
    return bound
