#!/usr/bin/env python3
"""Give every set one clean series name and a stable order.

After the bulk import the client's set filter was a mess: sixteen sets sat under
"OTHER", one each under "NONE" and "RSP", and promos were scattered across four
different labels. Anything the filter cannot name is effectively ungroupable.

This assigns each set the series name players expect -- Base, Neo, E-Card, Gym,
EX, Diamond & Pearl, Platinum, HeartGold & SoulSilver, Black & White, XY,
Sun & Moon, Sword & Shield, Scarlet & Violet, Mega Evolution, POP Series,
Promos, Custom -- and sorts the list in release order inside each series.

    ./venv/bin/python tools/tidy_series.py [--dry-run]
"""

import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETS_JSON = os.path.join(ROOT, "ptcgo", "database", "json_data", "sets.json")
META_PATH = os.path.join(ROOT, "ptcgo", "database", "json_data", "set_meta.json")

# series as pokemontcg.io reports it -> the label the client's filter shows
SERIES_LABEL = {
    "base": "Base",
    "neo": "Neo",
    "e-card": "E-Card",
    "gym": "Gym",
    "ex": "EX",
    "diamond & pearl": "Diamond & Pearl",
    "platinum": "Platinum",
    "heartgold & soulsilver": "HeartGold & SoulSilver",
    "black & white": "Black & White",
    "xy": "XY",
    "sun & moon": "Sun & Moon",
    "sword & shield": "Sword & Shield",
    "scarlet & violet": "Scarlet & Violet",
    "mega evolution": "Mega Evolution",
    "pop": "POP Series",
    "np": "Promos",
    "other": "Promos",
}

# promotions and oddities that the API files under "other"
PROMO_PREFIXES = ("MCD", "PROMO", "PR-", "NP", "RSP", "FUT", "SVP", "SVE")
PROMO_NAMES = {"BP", "SI1", "RU1", "NPC", "DPP"}
CUSTOM_NAMES = {"CUSTOM", "FREE_ENERGY"}

# Series the 2020 client's collection filter was never built for. The sets stay
# owned and playable -- they simply do not appear in a picker whose vocabulary is
# Black & White through Sword & Shield.
# Every era is listed in the collection filter. The old eras were hidden on the
# person's earlier instruction; they asked for Base and the rest back.
HIDDEN_FROM_FILTER = set()

# The client builds the filter's label key from the block string itself:
# block "SM" looks up "collection.filter.series.sm". That is why the shipped set
# table uses short codes, and why a block called "Mega Evolution" rendered as a
# raw key -- its key became "collection.filter.series.mega evolution".
SLUG_FOR_LABEL = {
    "Base": "base", "Neo": "neo", "E-Card": "ecard", "Gym": "gym", "EX": "ex",
    "Diamond & Pearl": "dp", "Platinum": "pl", "HeartGold & SoulSilver": "hgss",
    "Black & White": "bw", "XY": "xy", "Sun & Moon": "sm",
    "Sword & Shield": "swsh", "Scarlet & Violet": "sv", "Mega Evolution": "me",
    "POP Series": "pop", "Promos": "promos", "Custom": "custom",
}

# the filter's own order, oldest era to newest, promos next to last
BLOCK_ORDER = [
    "Base", "Neo", "E-Card", "Gym", "EX", "Diamond & Pearl", "Platinum",
    "HeartGold & SoulSilver", "Black & White", "XY", "Sun & Moon",
    "Sword & Shield", "Scarlet & Violet", "Mega Evolution", "POP Series",
    "Promos", "Custom",
]


def label_for(entry, meta):
    name = (entry.get("name") or "").upper()
    if name in CUSTOM_NAMES:
        return "Custom"
    if name.startswith(PROMO_PREFIXES) or name in PROMO_NAMES:
        return "Promos"
    record = meta.get(entry.get("name"), {})
    series = (record.get("series") or "").strip().lower()
    if series in SERIES_LABEL:
        return SERIES_LABEL[series]
    # fall back to the existing block, capitalised the same way
    block = (entry.get("block") or "").strip()
    for label in BLOCK_ORDER:
        if block.upper() == label.upper().replace(" ", ""):
            return label
    return "Promos"


def main():
    dry = "--dry-run" in sys.argv
    meta = json.load(open(META_PATH)) if os.path.exists(META_PATH) else {}
    entries = json.load(open(SETS_JSON))

    changed = 0
    for entry in entries:
        label = label_for(entry, meta)
        if entry.get("block") != label:
            changed += 1
        entry["block"] = SLUG_FOR_LABEL.get(label, label.lower())
        entry["filter"] = label not in HIDDEN_FROM_FILTER
        # a set with no cards at all should not advertise itself in the picker
        code = entry.get("name", "")
        has_cards = bool(glob.glob(os.path.join(ROOT, "ptcgo", "game", "scripts", "cards", code, "*.py")))
        if not has_cards and not entry.get("count"):
            entry["count"] = 0

    entries.sort(key=lambda e: (
        BLOCK_ORDER.index(e["block"]) if e["block"] in BLOCK_ORDER else len(BLOCK_ORDER),
        (meta.get(e.get("name"), {}).get("releaseDate") or "9999"),
        e.get("name", ""),
    ))

    if dry:
        for e in entries[:12]:
            print(f"  {e['block']:<24} {e['name']:<14} {e.get('count')}")
        print(f"dry run: {changed} sets would change series")
        return

    json.dump(entries, open(SETS_JSON, "w"), indent=2)
    from collections import Counter
    counts = Counter(e["block"] for e in entries)
    print(f"sets re-grouped: {changed}")
    for label in BLOCK_ORDER:
        if counts.get(label):
            print(f"  {label:<24} {counts[label]}")


if __name__ == "__main__":
    main()
