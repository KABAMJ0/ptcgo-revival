#!/usr/bin/env python3
"""Fill the gaps in the client's filter vocabulary.

The 2020 client renders a filter label by looking up a key it derives from the
value the server sends -- `collection.filter.series.<slug>` for a series,
`deckbuilder.cardfilters.rarity.<slug>` for a rarity, and so on. Anything we send
that it has no key for shows up as the raw key, which is what a screen full of
"collection.filter.series.mega evolution" was.

This compares the labels that client ships with the values our card data can
actually produce, and writes the missing ones to
`ptcgo/database/json_data/custom_labels.json`. The localization handler merges
that file at startup, so the labels travel with the repository instead of being
hard-coded in the handler.

    ./venv/bin/python tools/build_labels.py [--db PATH] [--dry-run]
"""

import argparse
import glob
import json
import os
import re
import sqlite3
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DB = os.path.join(ROOT, "ptcgo", "database", "game_data", "LocalizationDB-UTF16.db")
OUT_PATH = os.path.join(ROOT, "ptcgo", "database", "json_data", "custom_labels.json")
CARDS = os.path.join(ROOT, "ptcgo", "game", "scripts", "cards")

# series slug -> the name the filter should show
SERIES = {
    "base": "Base", "neo": "Neo", "ecard": "E-Card", "gym": "Gym", "ex": "EX",
    "dp": "Diamond & Pearl", "pl": "Platinum", "hgss": "HeartGold & SoulSilver",
    "bw": "Black & White", "xy": "XY", "sm": "Sun & Moon",
    "swsh": "Sword & Shield", "sv": "Scarlet & Violet", "me": "Mega Evolution",
    "pop": "POP Series", "promos": "Promos", "custom": "Custom",
}

# rarities our scripts use (Rarities.X) -> the phrase the filter shows
RARITY = {
    "common": "Common", "uncommon": "Uncommon", "rare": "Rare",
    "rareholo": "Rare Holo", "rareultra": "Ultra Rare", "raresecret": "Secret Rare",
    "rarerainbow": "Rainbow Rare", "rarepromo": "Promo",
    "rareholov": "Rare Holo V", "rareholovmax": "Rare Holo VMAX",
    "rareholovstar": "Rare Holo VSTAR", "rareradiant": "Radiant Rare",
    "amazing": "Amazing Rare",
}

# mechanics our cards carry that the client may need an attribute label for
ATTRIBUTES = {
    "v": "Pokémon V", "vmax": "Pokémon VMAX", "vstar": "Pokémon VSTAR",
    "vunion": "Pokémon V-UNION", "ex": "Pokémon ex", "tera": "Tera",
    "radiant": "Radiant", "prism": "Prism Star", "ace": "ACE SPEC",
    "break": "BREAK", "restored": "Restored", "legend": "Legend",
    "ultrabeast": "Ultra Beast",
}


def client_keys(db_path):
    if not os.path.exists(db_path):
        return set()
    con = sqlite3.connect(db_path)
    try:
        return {row[0] for row in con.execute("select key from Lookup")}
    finally:
        con.close()


def rarities_in_data():
    seen = set()
    for path in glob.glob(os.path.join(CARDS, "*", "*.py")):
        try:
            body = open(path, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        for token in re.findall(r"Rarities\.([A-Za-z]+)", body):
            seen.add(token.lower())
    return seen


def mechanics_in_data():
    seen = set()
    for path in glob.glob(os.path.join(CARDS, "*", "*.py")):
        try:
            body = open(path, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        for token in re.findall(r'"subtypes":\s*\[([^\]]*)\]', body):
            for word in re.findall(r'"([^"]+)"', token):
                seen.add(word.lower().replace(" ", "").replace("-", ""))
    return seen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    have = client_keys(args.db)
    if not have:
        print(f"warning: no localization db at {args.db}; assuming nothing exists")

    labels = {}

    def want(key, value):
        if key not in have:
            labels[key] = value

    for slug, name in SERIES.items():
        want(f"collection.filter.series.{slug}", f"<i>{name}</i> Series")
    for slug, name in RARITY.items():
        if slug not in rarities_in_data():
            continue
        want(f"deckbuilder.cardfilters.rarity.{slug}", name)
        want(f"deckbuilder.cardfilters.tooltips.rarity{slug}", name)
    for slug, name in ATTRIBUTES.items():
        if slug not in mechanics_in_data() and slug not in ("v", "vmax", "vstar", "ex"):
            continue
        want(f"deckbuilder.cardfilters.attributes.{slug}", name)

    if args.dry_run:
        for key, value in sorted(labels.items()):
            print(f"  {key} = {value}")
        print(f"{len(labels)} labels missing")
        return

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    json.dump(labels, open(OUT_PATH, "w"), indent=2, sort_keys=True)
    print(f"wrote {len(labels)} labels to {OUT_PATH}")


if __name__ == "__main__":
    main()
