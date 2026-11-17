"""Rank the still-unimplemented attack effects by how often decks use the card.

Reads the server's deck table read-only (never writes), weights each card by
the deck's play count, and prints the unimplemented attacks on the cards that
real decks actually bring to the table.

Usage:
    python tools/attack_priority.py [--db PATH] [--top 30]
"""

import argparse
import json
import os
import sqlite3
import sys
from collections import Counter, defaultdict
from typing import Dict, List, Optional

DEFAULT_DB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(
    __file__))), "ptcgo_server.db")


def deck_weights(db_path: str) -> Dict[str, int]:
    """card GUID -> summed play weight across every stored deck."""
    weights: Dict[str, int] = defaultdict(int)
    if not os.path.exists(db_path):
        raise SystemExit(f"no database at {db_path}")
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        rows = conn.execute(
            "select deck_data, coalesce(overall_played, 0), "
            "coalesce(overall_wins, 0) from decks").fetchall()
    finally:
        conn.close()
    for deck_data, played, wins in rows:
        try:
            payload = json.loads(deck_data)
        except (TypeError, ValueError):
            continue
        cards = (payload.get("piles") or {}).get("deck") or []
        weight = max(1, int(played or 0)) + 1
        for guid in cards:
            weights[str(guid).lower()] += weight
    return weights


def report(db_path: str, top: int):
    from spirit.game.card_effects import patterns
    from spirit.game.data_utils import CARD_DEFS_BY_GUID, Attack, unimplemented
    from spirit.game.scripts.cards import loader

    loader.load_all()
    weights = deck_weights(db_path)
    print(f"decks read: {len(weights)} distinct cards across the deck table")

    ranked: List[tuple] = []
    for guid, weight in weights.items():
        definition = CARD_DEFS_BY_GUID.get(guid)
        if definition is None or not hasattr(definition, "abilities"):
            continue
        for ability in definition.abilities:
            if not isinstance(ability, Attack):
                continue
            if ability.effect is not unimplemented:
                continue
            ranked.append((weight, definition.display_name, definition.set_code,
                           ability.title, patterns.normalize(ability.game_text)))
    ranked.sort(key=lambda row: -row[0])

    print(f"unimplemented attacks on cards in real decks: {len(ranked)}")
    print()
    print(f"{'WEIGHT':>7}  {'CARD':<28}{'SET':<10}ATTACK / TEXT")
    seen = set()
    shown = 0
    for weight, name, set_code, title, text in ranked:
        key = (name, set_code, title)
        if key in seen:
            continue
        seen.add(key)
        shown += 1
        if shown > top:
            break
        print(f"{weight:>7}  {name[:27]:<28}{set_code:<10}{title}")
        print(f"{'':>48}{text[:110]}")
    return ranked


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", default=DEFAULT_DB)
    parser.add_argument("--top", type=int, default=25)
    args = parser.parse_args()
    report(args.db, args.top)


if __name__ == "__main__":
    main()
