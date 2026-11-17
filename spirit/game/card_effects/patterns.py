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

import re
import unicodedata
from typing import Callable, List, Optional, Tuple

from spirit.game.attributes import PokemonTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import (
    bonus_if,
    condition_attack,
    count_bench,
    count_energy,
    count_prizes_taken,
    damage_all_opponents,
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
from spirit.game.card_effects.passives_common import (
    flip_protection,
    protect_next_turn,
)
from spirit.game.card_effects.support_common import (
    draw_attack,
    draw_until_effect,
    gust_attack,
    heal_attack,
    heal_targets,
    search_to_bench,
    switch_self_attack,
)
from spirit.game.data_utils import unimplemented
from spirit.game.session.effects import is_special_energy

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
    return draw_attack(_count(m.group(1)))


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
    return discard_opponent_energy_attack(count=_count(m.group(1)),
                                          special_only=True)


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
    from spirit.game.card_effects.attacks_common import stadium_in_play_cond
    return bonus_if(stadium_in_play_cond, int(m.group(1)))


def _bonus_hand_equal(m, ability):
    from spirit.game.card_effects.attacks_common import hand_sizes_equal
    return bonus_if(hand_sizes_equal, int(m.group(1)))


def _bonus_any_condition(m, ability):
    from spirit.game.card_effects.attacks_common import defender_has_any_condition
    return bonus_if(defender_has_any_condition, int(m.group(1)))


def _bonus_own_energy(m, ability):
    from spirit.game.card_effects.attacks_common import self_has_energy_of_type
    return bonus_if(self_has_energy_of_type(TYPE_WORDS[m.group(1)]),
                    int(m.group(2)))


def _bonus_defender_is_ex(m, ability):
    from spirit.game.card_effects.attacks_common import defender_is_ex
    return bonus_if(defender_is_ex, int(m.group(1)))


def _bonus_defender_is_ex_or_v(m, ability):
    from spirit.game.card_effects.attacks_common import defender_is_ex_or_v
    return bonus_if(defender_is_ex_or_v, int(m.group(1)))


def _bonus_defender_has_damage(m, ability):
    from spirit.game.card_effects.attacks_common import has_damage
    return bonus_if(has_damage("defender"), int(m.group(1)))


def _bonus_self_has_damage(m, ability):
    from spirit.game.card_effects.attacks_common import has_damage
    return bonus_if(has_damage("self"), int(m.group(1)))


def _bonus_own_bench_damaged(m, ability):
    from spirit.game.card_effects.attacks_common import bench_has_damage_counters
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


# ----------------------------------------------------------------------
# Pattern table: (name, compiled regex, builder). First full match wins.
# ----------------------------------------------------------------------

_PATTERNS: List[Tuple[str, "re.Pattern", Callable]] = [
    # -- coin flips ----------------------------------------------------
    ("flip.damage-times-heads",
     re.compile(r"flip (a|\d+) coins?\. this attack does (\d+) damage "
                r"times the number of heads\."), _flip_damage_times_heads),
    ("flip.damage-per-heads",
     re.compile(r"flip (a|\d+) coins?\. this attack does (\d+) damage "
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
     re.compile(r"flip (a|\d+) coins?\. this attack does (\d+) more damage "
                r"for each heads\."), _flip_bonus_per_heads),
    ("flip.more-damage",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) more damage\."),
     _flip_heads_damage),
    ("flip.tails-nothing",
     re.compile(r"flip a coin\. if tails, this attack does nothing\."),
     _flip_tails_nothing),
    ("flip.any-tails-nothing",
     re.compile(r"flip (a|\d+) coins?\. if either of them is tails, this "
                r"attack does nothing\."), _flip_all_heads_nothing),
    ("flip.damage-plus-bonus",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage plus "
                r"(\d+) more damage\."), _flip_plus_bonus),
    ("flip.damage-plus-bonus-else-damage",
     re.compile(r"flip a coin\. if heads, this attack does (\d+) damage plus "
                r"(\d+) more damage; if tails, this attack does (\d+) damage\."),
     _flip_choice_damage),
    ("flip.base-plus-bonus-per-heads",
     re.compile(r"flip (a|\d+) coins?\. this attack does (\d+) damage plus "
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
     re.compile(r"discard (a|\d+) (" + _TYPE_WORDS + r") energy (?:cards? )?"
                r"(?:attached )?(?:from|to) this pokemon\."),
     _self_energy_discard_type),
    ("discard.self-energy",
     re.compile(r"discard (a|\d+) energy (?:cards? )?(?:attached )?"
                r"(?:from|to) this pokemon\."), _self_energy_discard),
    ("discard.defender-special-energy-flip",
     re.compile(r"flip a coin\. if heads, discard (?:a|an) special energy "
                r"(?:card )?(?:attached to|from) (?:the defending|your "
                r"opponent's active) pokemon\."),
     _flip_defender_special_energy_discard),
    ("discard.defender-energy-flip",
     re.compile(r"flip a coin\. if heads, discard (a|\d+) energy (?:cards? )?"
                r"(?:attached to|from) (?:the defending|your opponent's "
                r"active) pokemon\."), _flip_defender_energy_discard),
    ("discard.defender-special-energy",
     re.compile(r"discard (?:a|an) special energy (?:card )?(?:attached to|"
                r"from) (?:the defending|your opponent's active) pokemon\."),
     _defender_special_energy_discard),
    ("discard.defender-energy",
     re.compile(r"discard (a|\d+) energy (?:cards? )?(?:attached to|from) "
                r"(?:the defending|your opponent's active) pokemon\."),
     _defender_energy_discard),

    # -- snipes and spreads --------------------------------------------
    ("snipe.any",
     re.compile(r"(?:this attack does|does) (\d+) damage to (a|\d+) of your "
                r"opponent's pokemon" + _SNIPE_TAIL), _snipe),
    ("snipe.choose-any",
     re.compile(r"choose (a|\d+) of your opponent's pokemon\. this attack does "
                r"(\d+) damage to that pokemon" + _SNIPE_TAIL),
     _snipe_choose),
    ("snipe.bench-also-base",
     re.compile(r"this attack also does (\d+) damage to (a|\d+) of your "
                r"opponent's benched pokemon" + _SNIPE_TAIL),
     _snipe_bench_also_base),
    ("snipe.bench",
     re.compile(r"(?:this attack does|does) (\d+) damage to (a|\d+) of your "
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
     re.compile(r"switch this pokemon with (a|\d+) of your benched pokemon\."),
     _switch_self),
    ("switch.self-optional",
     re.compile(r"you may switch this pokemon with (a|\d+) of your benched "
                r"pokemon\."), _switch_self_optional),
    ("switch.opponent-chooses",
     re.compile(r"(?:your opponent switches (?:the defending|their active) "
                r"pokemon with (a|\d+) of (?:his or her|their) benched pokemon\.|"
                r"switch out your opponent's active pokemon to the bench\. "
                r"\(your opponent chooses the new active pokemon\.\))"),
     _gust_opponent_chooses),
    ("discard.random-opponent-hand",
     re.compile(r"discard (a|\d+) random cards? from your opponent's hand\."),
     _discard_random_opponent),
    ("search.basic-to-bench",
     re.compile(r"search your deck for (?:a basic pokemon|up to (\d+) basic "
                r"pokemon) and put (?:it|them) onto your bench\. (?:then, )?"
                r"shuffle your deck(?: afterward)?\."), _search_basic_to_bench),
    ("counters.place-any",
     re.compile(r"put (\d+) damage counters on your opponent's pokemon in any "
                r"way you like\."), _place_counters_any),
    ("energy.move-to-bench",
     re.compile(r"move (a|\d+) energy (?:card )?(?:attached )?from this "
                r"pokemon to (a|\d+) of your benched pokemon\."),
     _energy_move),
]

# name -> bind count, for the coverage report.
BIND_COUNTS = {}


def bind(ability) -> Optional[str]:
    """Bind a wording pattern to `ability`; returns the pattern name or None.

    Only an `unimplemented` effect is ever replaced, so a card with a real
    script keeps it.
    """
    if ability is None or getattr(ability, "effect", None) is not unimplemented:
        return None
    text = normalize(getattr(ability, "game_text", ""))
    if not text:
        return None
    for name, pattern, build in _PATTERNS:
        match = pattern.fullmatch(text)
        if match is None:
            continue
        try:
            effect = build(match, ability)
        except (ValueError, IndexError, KeyError, TypeError):
            # A malformed match must never turn a loadable card into a
            # load failure: leave it unimplemented and keep going.
            return None
        if effect is None:
            return None
        ability.effect = effect
        ability.effect_source = f"pattern:{name}"
        BIND_COUNTS[name] = BIND_COUNTS.get(name, 0) + 1
        return name
    return None


def bind_definition(definition) -> int:
    """Bind every unimplemented ability on a resolved card definition."""
    bound = 0
    for ability in getattr(definition, "abilities", None) or []:
        if bind(ability) is not None:
            bound += 1
    return bound
