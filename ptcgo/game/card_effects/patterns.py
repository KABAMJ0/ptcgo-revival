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

from ptcgo.game.attributes import AttrID, PokemonTypes, SpecialConditions
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
    debuff_defender_attacks,
    carrier_pokemon,
    opponent_retreat_tax_passive,
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
from ptcgo.game.card_effects.trainers import is_basic_energy_card, is_energy_card
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
        "the defending pokemon is a pokemon-ex": defender_is_ex,
    })
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
    cost)": attached minus what the attack itself costs."""
    type_value = TYPE_WORDS[type_word].value if type_word else None

    def cond(ctx) -> bool:
        attacker = ctx.attacker
        if attacker is None:
            return False
        attached = 0
        for energy in ctx.attached_energies(attacker):
            if type_value is None or energy_provides_type(energy, type_value):
                attached += 1
        cost = 0
        for cost_type, count in (getattr(ctx.ability, "cost", None) or {}).items():
            value = getattr(cost_type, "value", cost_type)
            if value in (PokemonTypes.COLORLESS.value,
                         PokemonTypes.UNSET.value) or value == type_value:
                cost += count
        return attached - cost >= required
    return cond


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
    if normalize(getattr(ability, "title", "")) == normalize(named):
        return None

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
        await ctx.reorder_deck_top(count, ctx.opponent_id,
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
            if not ctx.effects_blocked(target):
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
            if not ctx.effects_blocked(target):
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
    ("heal.each-own",
     re.compile(r"heal (\d+) damage from each of your pokemon\."),
     _heal_each_own),
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
    ("lock.self-next-turn",
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
    ("bonus.stadium-then-discard",
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
     re.compile(r"does (\d+) damage to each of your opponent's benched pokemon "
                r"that has any damage counters on it" + _SNIPE_TAIL),
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
    ("energy.move-bench-to-self",
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
     re.compile(r"(?:put|place) (\d+) damage counters on the attacking "
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
                r"on top of your deck in any order\."), _reorder_own_top),
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
     re.compile(r"during your next turn, attacks used by this pokemon do "
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
     re.compile(r"does (\d+) damage times the number of damage counters on "
                r"this pokemon\."), _times_self_damage_counters),
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


def bind(ability) -> Optional[str]:
    """Bind a wording pattern to `ability`; returns the pattern name or None.

    Only an `unimplemented` effect is ever replaced, so a card with a real
    script keeps it.
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
    for ability in getattr(definition, "abilities", None) or []:
        if bind(ability) is not None:
            bound += 1
    return bound
