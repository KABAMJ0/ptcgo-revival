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
from spirit.game.data_utils import Attack, CARD_DEFS_BY_GUID
from spirit.game.scripts.cards import loader as card_loader
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
        # effects.flip_coins maps 0 -> heads, 1 -> tails.
        wanted = queue.pop(0) if queue else 1
        return 0 if wanted else 1
    random.choice = choice
    try:
        yield
    finally:
        random.choice = original


def bound_attacks(pattern_name):
    """(definition, attack) pairs bound by `pattern_name`, in stable order."""
    out = []
    for guid in sorted(CARD_DEFS_BY_GUID):
        definition = CARD_DEFS_BY_GUID[guid]
        for ability in getattr(definition, "abilities", None) or []:
            if isinstance(ability, Attack) and \
                    getattr(ability, "effect_source", "") == f"pattern:{pattern_name}":
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
    }


def delta(before, after, entity_id):
    return before["hp"].get(entity_id, 0) - after["hp"].get(entity_id, 0)


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
    expected = per * heads
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
    return dealt >= (ability.damage or 0) + 10, \
        f"dealt {dealt} with 2 counters on attacker (printed {ability.damage})"


def check_ignore_resistance(before, after, rig, ability, entities):
    dealt = delta(before, after, entities["p2_active"].entity_id)
    return dealt == (ability.damage or 0), \
        f"dealt {dealt} (printed {ability.damage}, resistance skipped)"


def check_bonus_condition(before, after, rig, ability, entities):
    dealt = delta(before, after, entities["p2_active"].entity_id)
    return dealt > 0, f"dealt {dealt}"


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
]


async def run_case(pattern, check, coin_values, seed_damage, fillers):
    candidates = bound_attacks(pattern)
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
    if pattern == "scale.counter-self":
        attacker.set_attribute(AttrID.HP, hp(attacker) - 20)

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
            status, detail = await run_case(pattern, check, coin_values,
                                            seed_damage, fillers)
        except Exception as exc:  # a raise is a failed check, not a crash
            status, detail = FAIL, f"{pattern:<30} raised {type(exc).__name__}: {exc}"
        if status == FAIL:
            failures += 1
        print(f"{status:<5}{detail}")
    print(f"\n{ran - failures}/{ran} pattern behaviours verified")
    return 1 if failures else 0


def main():
    logging.disable(logging.CRITICAL)
    parser = argparse.ArgumentParser(description="Verify bound attack patterns.")
    parser.add_argument("-k", dest="pattern", help="only cases matching this name")
    args = parser.parse_args()
    sys.exit(asyncio.run(main_async(args)))


if __name__ == "__main__":
    main()
