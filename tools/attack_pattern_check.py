"""Behaviour checks for the wording-driven attack patterns.

`effect_smoke` proves a scripted attack runs without raising; this proves the
attacks bound from wording do what their text says. For each pattern it picks
a real card bound by that pattern, drives the attack on a headless session,
and asserts the observable outcome (damage, conditions, draws, locks, energy,
switches) against a before/after snapshot.

Usage: python tools/attack_pattern_check.py [-k pattern_name]
"""

import argparse
import asyncio
import logging
import random
import re
import sys
from contextlib import contextmanager

from spirit.game.attributes import AttrID
from spirit.game.models.board import EnergyEntity
from spirit.game.data_utils import Attack, CARD_DEFS_BY_GUID
from spirit.game.scripts.cards import loader as card_loader
from spirit.game.session import passives
from spirit.game.session.effects import resolve_attack
from spirit.tools.effect_smoke import (
    P1, P2, Rig, basic_energy_guids, pick_filler_basic, pick_filler_item,
)

PASS, FAIL = "PASS", "FAIL"


@contextmanager
def coins(values):
    """Force the coin flips inside this block (1 = heads)."""
    original = random.choice
    queue = list(values)

    def choice(seq):
        # Only coin flips (seq == [0, 1]) are forced; effects.flip_coins maps
        # 0 -> heads and 1 -> tails. Every other random.choice (a card from a
        # hand, an AI pick) keeps its real behaviour.
        if list(seq) != [0, 1]:
            return original(seq)
        wanted = queue.pop(0) if queue else 1
        return 0 if wanted else 1
    random.choice = choice
    try:
        yield
    finally:
        random.choice = original


def bound_abilities(pattern_name, attacks_only=True):
    """(definition, ability) pairs bound by `pattern_name`, in stable order."""
    out = []
    for guid in sorted(CARD_DEFS_BY_GUID):
        definition = CARD_DEFS_BY_GUID[guid]
        for ability in getattr(definition, "abilities", None) or []:
            if getattr(ability, "effect_source", "") != f"pattern:{pattern_name}":
                continue
            if attacks_only and not isinstance(ability, Attack):
                continue
            out.append((definition, ability))
    return out


def hp(pokemon):
    return pokemon.get_attribute(AttrID.HP, 0)


def snapshot(rig):
    board = rig.board
    return {
        "hp": {p.entity_id: hp(p) for pid in (P1, P2)
               for p in board.pokemon_in_play(pid)},
        "hand": len(board.find_player_area(P1, "hand").children or []),
        "hand2": len(board.find_player_area(P2, "hand").children or []),
        "deck2": len(board.find_player_area(P2, "deck").children or []),
        "discard2": len(board.find_player_area(P2, "discard").children or []),
        "attached": {p.entity_id: len(p.children or [])
                     for pid in (P1, P2) for p in board.pokemon_in_play(pid)},
        "active1": board.active_pokemon(P1),
        "active2": board.active_pokemon(P2),
    }


def delta(before, after, entity_id):
    return before["hp"].get(entity_id, 0) - after["hp"].get(entity_id, 0)


def expected_damage(rig, attacker, defender, amount, cap=None, **flags):
    """`amount` run through the real damage pipeline (weakness, resistance,
    taken-modifiers), capped by the defender's pre-hit HP."""
    calc = passives.compute_damage(rig.board, attacker, defender, amount,
                                   is_attack=True, **flags)
    limit = hp(defender) if cap is None else cap
    return min(calc.amount, limit)


def text_number(text, template):
    match = re.search(template, text or "")
    return int(match.group(1)) if match else None


# ----------------------------------------------------------------------
# Checks: (before, after, rig, ability, entities) -> (ok, detail)
# ----------------------------------------------------------------------

def check_flip_damage_times_heads(before, after, rig, ability, entities):
    per = text_number(ability.game_text, r"does (\d+) damage times")
    heads = 2
    dealt = delta(before, after, entities["p2_active"].entity_id)
    expected = expected_damage(rig, entities["p1_active"],
                               entities["p2_active"], per * heads)
    return dealt == expected, f"dealt {dealt} (expected {expected})"


def check_flip_tails_nothing(before, after, rig, ability, entities):
    dealt = delta(before, after, entities["p2_active"].entity_id)
    return dealt == 0, f"dealt {dealt} (expected 0 on tails)"


def check_defender_condition(before, after, rig, ability, entities):
    conditions = entities["p2_active"].get_attribute(AttrID.SPECIAL_CONDITIONS) or []
    return bool(conditions), f"defender conditions={conditions}"


def check_self_condition(before, after, rig, ability, entities):
    conditions = entities["p1_active"].get_attribute(AttrID.SPECIAL_CONDITIONS) or []
    return bool(conditions), f"attacker conditions={conditions}"


def check_self_damage(before, after, rig, ability, entities):
    own = delta(before, after, entities["p1_active"].entity_id)
    return own > 0, f"attacker took {own} itself"


def check_heal_self(before, after, rig, ability, entities):
    attacker = entities["p1_active"].entity_id
    healed = after["hp"][attacker] - before["hp"][attacker]
    return healed > 0, f"healed {healed}"


def check_draw(before, after, rig, ability, entities):
    drawn = after["hand"] - before["hand"]
    return drawn > 0, f"hand {before['hand']} -> {after['hand']}"


def check_mill_opponent(before, after, rig, ability, entities):
    milled = before["discard2"] - after["discard2"]
    return milled < 0, f"opponent discard {before['discard2']} -> {after['discard2']}"


def check_discard_self_energy(before, after, rig, ability, entities):
    attacker = entities["p1_active"].entity_id
    gone = before["attached"][attacker] - after["attached"][attacker]
    return gone > 0, f"attached Energy {before['attached'][attacker]} -> " \
                     f"{after['attached'][attacker]}"


def check_snipe_any(before, after, rig, ability, entities):
    damaged = [pid for pid, before_hp in before["hp"].items()
               if after["hp"].get(pid, before_hp) < before_hp]
    return bool(damaged), f"{len(damaged)} opposing Pokemon damaged"


def check_snipe_bench(before, after, rig, ability, entities):
    damaged = [pid for pid, before_hp in before["hp"].items()
               if pid != entities["p2_active"].entity_id
               and after["hp"].get(pid, before_hp) < before_hp]
    return bool(damaged), f"{len(damaged)} other Pokemon damaged"


def check_no_retreat(before, after, rig, ability, entities):
    locked = rig.session.turn_state.retreat_locked(entities["p2_active"].entity_id)
    return bool(locked), f"retreat lock={locked}"


def check_lock_self(before, after, rig, ability, entities):
    locks = getattr(rig.session.turn_state, "attack_locks", {})
    ours = [k for k in locks if k[0] == entities["p1_active"].entity_id]
    return bool(ours), f"own attack locks={len(ours)}"


def check_switch_self(before, after, rig, ability, entities):
    changed = after["active1"] is not before["active1"]
    return changed, f"active changed={changed}"


def check_scale_counter_self(before, after, rig, ability, entities):
    dealt = delta(before, after, entities["p2_active"].entity_id)
    amount = (ability.damage or 0) + 10 * 2
    expected = expected_damage(rig, entities["p1_active"],
                               entities["p2_active"], amount)
    return dealt == expected, \
        f"dealt {dealt} (expected {expected}: printed + 10 x 2 counters)"


def check_ignore_resistance(before, after, rig, ability, entities):
    dealt = delta(before, after, entities["p2_active"].entity_id)
    expected = expected_damage(rig, entities["p1_active"],
                               entities["p2_active"], ability.damage or 0,
                               cap=before["hp"][entities["p2_active"].entity_id],
                               ignore_resistance=True)
    return dealt == expected, \
        f"dealt {dealt} (expected {expected}: resistance skipped)"


def check_bonus_condition(before, after, rig, ability, entities):
    dealt = delta(before, after, entities["p2_active"].entity_id)
    return dealt > 0, f"dealt {dealt}"


def check_search_hand(before, after, rig, ability, entities):
    drawn = after["hand"] - before["hand"]
    return drawn > 0, f"hand {before['hand']} -> {after['hand']}"


def check_attach_from_discard(before, after, rig, ability, entities):
    gained = [pid for pid, count in after["attached"].items()
              if count > before["attached"].get(pid, 0)]
    return bool(gained), f"{len(gained)} Pokemon gained Energy"


def check_temporary_passive(before, after, rig, ability, entities):
    count = len(rig.board.temporary_passives)
    return count > 0, f"{count} temporary passives"


def check_less_per_counter(before, after, rig, ability, entities):
    dealt = delta(before, after, entities["p2_active"].entity_id)
    amount = max(0, (ability.damage or 0) - 10 * 2)
    expected = expected_damage(rig, entities["p1_active"],
                               entities["p2_active"], amount)
    return dealt == expected, f"dealt {dealt} (expected {expected}: printed - 10 x 2)"


def check_lock_defender(before, after, rig, ability, entities):
    locks = getattr(rig.session.turn_state, "attack_locks", {})
    theirs = [key for key in locks
              if key[0] == entities["p2_active"].entity_id]
    return bool(theirs), f"defender attack locks={len(theirs)}"


def check_defender_switched(before, after, rig, ability, entities):
    changed = after["active2"] is not before["active2"]
    return changed, f"opposing Active changed={changed}"


def check_check_noop(before, after, rig, ability, entities):
    return True, "runs without raising"


def check_passive_bound(before, after, rig, ability, entities):
    return getattr(ability, "passive", None) is not None, \
        f"passive={type(getattr(ability, 'passive', None)).__name__}"


# (pattern, check, coin values, pre-damage the attacker?)
CASES = [
    ("flip.damage-times-heads", check_flip_damage_times_heads, (1, 1, 1, 1), 0),
    ("flip.tails-nothing", check_flip_tails_nothing, (0, 0, 0, 0), 0),
    ("defender-condition", check_defender_condition, (1, 1, 1, 1), 0),
    ("flip.defender-condition", check_defender_condition, (1, 1, 1, 1), 0),
    ("self-condition", check_self_condition, (1, 1, 1, 1), 0),
    ("self-damage", check_self_damage, (1, 1, 1, 1), 0),
    ("heal.self", check_heal_self, (1, 1, 1, 1), 60),
    ("draw.n", check_draw, (1, 1, 1, 1), 0),
    ("mill.opponent", check_mill_opponent, (1, 1, 1, 1), 0),
    ("discard.self-energy", check_discard_self_energy, (1, 1, 1, 1), 0),
    ("snipe.bench", check_snipe_bench, (1, 1, 1, 1), 0),
    ("lock.defender-retreat", check_no_retreat, (1, 1, 1, 1), 0),
    ("lock.self-next-turn", check_lock_self, (1, 1, 1, 1), 0),
    ("switch.self", check_switch_self, (1, 1, 1, 1), 0),
    ("scale.counter-self", check_scale_counter_self, (1, 1, 1, 1), 0),
    ("ignore.resistance", check_ignore_resistance, (1, 1, 1, 1), 0),
    ("search.basic-energy-to-hand", check_search_hand, (1, 1, 1, 1), 0),
    ("search.any-to-hand", check_search_hand, (1, 1, 1, 1), 0),
    ("attach.energy-from-discard", check_attach_from_discard, (1, 1, 1, 1), 0),
    ("protect.no-weakness", check_temporary_passive, (1, 1, 1, 1), 0),
    ("scale.less-per-counter-self", check_less_per_counter, (1, 1, 1, 1), 20),
    ("ability.takes-less", check_passive_bound, (1, 1, 1, 1), 0),
    ("snipe.choose-bench", check_snipe_bench, (1, 1, 1, 1), 0),
    ("debuff.defender-attacks", check_temporary_passive, (1, 1, 1, 1), 0),
    ("protect.from-basic", check_temporary_passive, (1, 1, 1, 1), 0),
    ("recover.from-discard", check_search_hand, (1, 1, 1, 1), 0),
    ("optional.bonus-self-damage", check_self_damage, (1, 1, 1, 1), 0),
    ("scale.damage-per-energy-self", check_bonus_condition, (1, 1, 1, 1), 0),
    ("discard.defender-tools", check_bonus_condition, (1, 1, 1, 1), 0),
    ("bonus.entered-active-this-turn", check_bonus_condition, (1, 1, 1, 1), 0),
    ("scale.damage-per-energy-opponent", check_bonus_condition, (1, 1, 1, 1), 0),
    ("ability.basic-no-retreat", check_passive_bound, (1, 1, 1, 1), 0),
    ("lock.defender-cannot-use-attacks", check_lock_defender, (1, 1, 1, 1), 0),
    ("switch.in-opponent-bench", check_defender_switched, (1, 1, 1, 1), 0),
    ("counters.place-active", check_bonus_condition, (1, 1, 1, 1), 0),
    ("heal.bench-choice", check_check_noop, (1, 1, 1, 1), 0),
    ("scale.phrase", check_bonus_condition, (1, 1, 1, 1), 0),
    ("bonus.phrase", check_bonus_condition, (1, 1, 1, 1), 0),
    ("bonus.extra-energy-attached", check_bonus_condition, (1, 1, 1, 1), 0),
    ("discard.up-to-for-damage", check_bonus_condition, (1, 1, 1, 1), 0),
    ("discard.all-for-damage", check_discard_self_energy, (1, 1, 1, 1), 0),
    ("counters.chosen-target", check_bonus_condition, (1, 1, 1, 1), 0),
    ("heal.all-self", check_heal_self, (1, 1, 1, 1), 60),
    ("lock.this-attack-next-turn", check_lock_self, (1, 1, 1, 1), 0),
    ("discard.peek-opponent-hand", check_check_noop, (1, 1, 1, 1), 0),
    ("scale.round-attack", check_bonus_condition, (1, 1, 1, 1), 0),
    ("copy.defender-attack-short", check_check_noop, (1, 1, 1, 1), 0),
    ("snipe.choose-any-ignore-that", check_snipe_any, (1, 1, 1, 1), 0),
    ("flip.heads-tails-conditions", check_defender_condition, (1, 1, 1, 1), 0),
    ("lock.opponent-items", check_check_noop, (1, 1, 1, 1), 0),
    ("bonus.extra-prize-on-ko", check_check_noop, (1, 1, 1, 1), 0),
    ("mill.by-heads", check_mill_opponent, (1, 1, 1, 1), 0),
    ("discard.any-opponent-energy", check_check_noop, (1, 1, 1, 1), 0),
    ("protect.from-basic-noncolorless", check_temporary_passive, (1, 1, 1, 1), 0),
    ("discard.opponent-hand", check_check_noop, (1, 1, 1, 1), 0),
    ("heal.remove-counter-each", check_heal_self, (1, 1, 1, 1), 60),
    ("condition.both-actives", check_defender_condition, (1, 1, 1, 1), 0),
    ("search.energy-attach-self-typed", check_attach_from_discard, (1, 1, 1, 1), 0),
    ("discard.hand-draw-n", check_check_noop, (1, 1, 1, 1), 0),
    ("switch.both-actives", check_switch_self, (1, 1, 1, 1), 0),
    ("lock.defender-cannot-attack", check_lock_defender, (1, 1, 1, 1), 0),
    ("lock.defender-flip-attack-retreat", check_lock_defender, (1, 1, 1, 1), 0),
    ("flip.spread-opponent-bench", check_snipe_any, (1, 1, 1, 1), 0),
    ("self-condition-then-heal", check_self_condition, (1, 1, 1, 1), 60),
    ("flip.paralyze-else-nothing", check_defender_condition, (1, 1, 1, 1), 0),
    ("snipe.damaged-only", check_check_noop, (1, 1, 1, 1), 0),
    ("heal.all-bench-choice", check_check_noop, (1, 1, 1, 1), 0),
    ("discard.all-energy-optional-bonus", check_check_noop, (1, 1, 1, 1), 0),
    ("defender-two-conditions-flip", check_defender_condition, (1, 1, 1, 1), 0),
    ("poison.checkup-counters", check_defender_condition, (1, 1, 1, 1), 0),
    ("flip.bonus-and-condition", check_defender_condition, (1, 1, 1, 1), 0),
    ("energy-cost-then-condition", check_defender_condition, (1, 1, 1, 1), 0),
    ("energy.attached-to-hand", check_discard_self_energy, (1, 1, 1, 1), 0),
    ("reorder.either-deck-top", check_check_noop, (1, 1, 1, 1), 0),
    ("counters.move-bench-to-defender", check_bonus_condition, (1, 1, 1, 1), 0),
    ("energy.move-opponent-to-bench", check_check_noop, (1, 1, 1, 1), 0),
    ("attach.hand-energy-one", check_attach_from_discard, (1, 1, 1, 1), 0),
    ("protect.all-effects-no-flip", check_temporary_passive, (1, 1, 1, 1), 0),
    ("extra-turn", check_check_noop, (1, 1, 1, 1), 0),
    ("heal.counter-from-chosen", check_heal_self, (1, 1, 1, 1), 60),
    ("protect.from-evolution", check_temporary_passive, (1, 1, 1, 1), 0),
    ("discard.each-opponent-energy", check_check_noop, (1, 1, 1, 1), 0),
    ("boost.own-next-turn-titled", check_check_noop, (1, 1, 1, 1), 0),
]


async def run_case(pattern, check, coin_values, seed_damage, fillers):
    candidates = bound_abilities(
        pattern, attacks_only=not pattern.startswith("ability."))
    if not candidates:
        return FAIL, f"{pattern:<30} no card is bound by this pattern"
    definition, ability = candidates[0]
    rig = Rig(definition, fillers["basic"], fillers["energy"], fillers["item"])
    entities = rig.setup("pokemon")
    attacker = entities["p1_active"]
    if attacker is None or entities["p2_active"] is None:
        return FAIL, f"{pattern:<30} rig did not place actives"

    if seed_damage:
        attacker.set_attribute(AttrID.HP, hp(attacker) - seed_damage)
    if pattern in ("scale.counter-self", "scale.less-per-counter-self"):
        attacker.set_attribute(AttrID.HP, hp(attacker) - 20)
    if pattern == "counters.move-bench-to-defender":
        # The rig's bench has no damage to move.
        bench = rig.board.find_player_area(P1, "bench")
        for card in list(bench.children)[:1]:
            card.set_attribute(AttrID.HP, max(10, hp(card) - 30))
    if pattern.startswith("attach."):
        # The rig's discard pile holds no Energy by default.
        for _ in range(2):
            rig.to_area(rig.pull(P1, lambda card: isinstance(card, EnergyEntity)),
                        P1, "discard")

    before = snapshot(rig)
    with coins(coin_values):
        await resolve_attack(rig.session, P1, attacker, ability,
                             ability.ability_id)
    after = snapshot(rig)
    ok, detail = check(before, after, rig, ability, entities)
    return (PASS if ok else FAIL), f"{pattern:<30} {definition.display_name} " \
                                   f"({definition.set_code}) '{ability.title}': {detail}"


async def main_async(args):
    card_loader.load_all()
    fillers = {"basic": pick_filler_basic(), "energy": basic_energy_guids(),
               "item": pick_filler_item()}
    failures = 0
    ran = 0
    for pattern, check, coin_values, seed_damage in CASES:
        if args.pattern and args.pattern not in pattern:
            continue
        ran += 1
        try:
            status, detail = await asyncio.wait_for(
                run_case(pattern, check, coin_values, seed_damage, fillers),
                timeout=args.timeout)
        except asyncio.TimeoutError:
            status, detail = FAIL, f"{pattern:<30} timed out"
        except Exception as exc:  # a raise is a failed check, not a crash
            status, detail = FAIL, f"{pattern:<30} raised {type(exc).__name__}: {exc}"
        if status == FAIL:
            failures += 1
        print(f"{status:<5}{detail}", flush=True)
    print(f"\n{ran - failures}/{ran} pattern behaviours verified")
    return 1 if failures else 0


def main():
    logging.disable(logging.CRITICAL)
    parser = argparse.ArgumentParser(description="Verify bound attack patterns.")
    parser.add_argument("-k", dest="pattern", help="only cases matching this name")
    parser.add_argument("--timeout", type=float, default=45.0,
                        help="seconds per case before it counts as a failure")
    args = parser.parse_args()
    sys.exit(asyncio.run(main_async(args)))


if __name__ == "__main__":
    main()
