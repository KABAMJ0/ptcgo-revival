#!/usr/bin/env python3
"""Make set blocks and format legality match the real game.

Two things were wrong after the bulk import:

* every set older than Black & White carried era "OTHER", so the client's set
  filter had no block to group it under
* legality was derived from an era guess, which put XY and Sun & Moon sets in
  Unlimited only and left some Sword & Shield sets out of Standard

This maps each set's pokemontcg.io series to the client's block code and to the
formats the era is actually legal in, then rewrites sets.json.

    ./venv/bin/python tools/fix_set_filters.py [--dry-run]
"""

import glob
import json
import os
import sys

SETS_JSON = os.path.join("spirit", "database", "json_data", "sets.json")
META_PATH = os.path.join("spirit", "database", "json_data", "set_meta.json")
FORMATS_JSON = os.path.join("spirit", "database", "json_data", "formats.json")
CARDS = os.path.join("spirit", "game", "scripts", "cards")

# pokemontcg.io series -> (client block code, era key used by formats)
SERIES_BLOCK = {
    "base": ("BASE", "CLASSIC"),
    "neo": ("NEO", "CLASSIC"),
    "e-card": ("ECARD", "CLASSIC"),
    "gym": ("GYM", "CLASSIC"),
    "ex": ("EX", "CLASSIC"),
    "diamond & pearl": ("DP", "CLASSIC"),
    "platinum": ("PL", "CLASSIC"),
    "heartgold & soulsilver": ("HGSS", "CLASSIC"),
    "pop": ("POP", "CLASSIC"),
    "np": ("PROMO", "CLASSIC"),
    "other": ("OTHER", "CLASSIC"),
    "black & white": ("BW", "BW"),
    "xy": ("XY", "XY"),
    "sun & moon": ("SM", "SM"),
    "sword & shield": ("SWSH", "SWSH"),
    "scarlet & violet": ("SV", "SV"),
    "mega evolution": ("ME", "SV"),
}

# era key -> formats it is legal in
ERA_FORMATS = {
    "CLASSIC": [],                     # Unlimited only
    "BW": ["Expanded", "Legacy"],
    "XY": ["Expanded"],
    "SM": ["Expanded"],
    "SWSH": ["Standard", "Expanded"],
    "SV": ["Standard", "Expanded"],
}

AGNOSTIC = {"FREE_ENERGY", "CUSTOM"}


def main():
    dry = "--dry-run" in sys.argv
    meta = json.load(open(META_PATH))
    formats = {f["key"]: f["guid"] for f in json.load(open(FORMATS_JSON))["formats"]}
    entries = json.load(open(SETS_JSON))

    blocks = {}
    for code, record in meta.items():
        series = (record.get("series") or "").lower().strip()
        block, era = SERIES_BLOCK.get(series, ("OTHER", "CLASSIC"))
        blocks[code.upper()] = (block, era)

    changed = 0
    for entry in entries:
        name = entry.get("name", "")
        block, era = blocks.get(name.upper(), (None, None))
        if block is None:
            # not one of our folders: fall back to what is already there
            continue
        legal = []
        if name.upper() in AGNOSTIC:
            legal = [formats["Standard"], formats["Expanded"], formats["Legacy"]]
        else:
            for fmt in ERA_FORMATS.get(era, []):
                if fmt in formats:
                    legal.append(formats[fmt])
        count = len(glob.glob(os.path.join(CARDS, name, "*.py")))
        new = {"block": block, "legalFormats": legal}
        if count:
            new["count"] = count
        if any(entry.get(k) != v for k, v in new.items()):
            entry.update(new)
            changed += 1

    if dry:
        for entry in entries[:8]:
            print(entry["name"], entry.get("block"), len(entry.get("legalFormats") or []))
        print(f"dry run: {changed} entries would change")
        return

    json.dump(entries, open(SETS_JSON, "w"), indent=2)
    from collections import Counter
    print(f"entries updated: {changed}")
    print("blocks:", Counter(e.get("block") for e in entries))
    print("legal-in-count:", Counter(len(e.get("legalFormats") or []) for e in entries))


if __name__ == "__main__":
    main()
