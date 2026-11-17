#!/usr/bin/env python3
"""Assign every loaded set to the right play formats.

Spirit's shipped formats.json only knew the Sword & Shield block, so after
importing Black & White or Scarlet & Violet those sets were legal in Expanded
(which is "every loaded set") and nowhere else -- no Standard badge on SV cards,
no Legacy badge on BW cards.

The rules here follow the real era split:

    Standard  = SV block + SWSH block + basic energies + custom cards
    Expanded  = BW block and later + basic energies + custom cards
    Legacy    = BW block + basic energies + custom cards
    Unlimited = everything (allSets)

    python3 tools/classify_formats.py           # rewrite formats.json
    python3 tools/classify_formats.py --print   # show the mapping only
"""

import glob
import json
import os
import sys

FORMATS_PATH = os.path.join("spirit", "database", "json_data", "formats.json")
CARDS_DIR = os.path.join("spirit", "game", "scripts", "cards")

# Sets that carry no era marker but belong to one.
SV_ONLY = {"ZSV10PT5", "RSV10PT5", "SVP", "SVE"}
SWSH_ONLY = {"CEL25", "PGO", "CZ", "PROMO_SWSH"}
BW_ONLY = {"DV", "PROMO_BW"}
ERA_AGNOSTIC = {"FREE_ENERGY", "CUSTOM"}


def era_of(code: str) -> str:
    c = code.upper()
    if c in ERA_AGNOSTIC:
        return "AGNOSTIC"
    if c.startswith("SV") or c in SV_ONLY:
        return "SV"
    if c.startswith("SWSH") or c in SWSH_ONLY:
        return "SWSH"
    if c.startswith("BW") or c in BW_ONLY:
        return "BW"
    return "OTHER"


def loaded_sets():
    """Set folders that actually contain card scripts (skips __pycache__ and friends)."""
    found = []
    for path in glob.glob(os.path.join(CARDS_DIR, "*")):
        if not os.path.isdir(path) or os.path.basename(path).startswith("__"):
            continue
        if glob.glob(os.path.join(path, "*.py")):
            found.append(os.path.basename(path))
    return sorted(found)


def main():
    sets = loaded_sets()
    if not sets:
        raise SystemExit("no card sets found -- run the importer first")

    sv = [s for s in sets if era_of(s) == "SV"]
    swsh = [s for s in sets if era_of(s) == "SWSH"]
    bw = [s for s in sets if era_of(s) == "BW"]
    agnostic = [s for s in sets if era_of(s) == "AGNOSTIC"]
    other = [s for s in sets if era_of(s) == "OTHER"]
    if other:
        print(f"unclassified sets (left in Expanded only): {other}")

    mapping = {
        "Standard": sorted(sv + swsh + agnostic),
        "Expanded": sorted(bw + swsh + sv + agnostic + other),
        "Legacy": sorted(bw + agnostic + other),
    }

    if "--print" in sys.argv:
        for key, val in mapping.items():
            print(f"{key} ({len(val)}): {', '.join(val)}")
        return

    data = json.load(open(FORMATS_PATH))
    for fmt in data["formats"]:
        key = fmt.get("key")
        if key in mapping:
            fmt["sets"] = mapping[key]
            fmt["allSets"] = False
    json.dump(data, open(FORMATS_PATH, "w"), indent=2)
    print("formats.json updated: " + ", ".join(f"{k}={len(v)}" for k, v in mapping.items()))


if __name__ == "__main__":
    main()
