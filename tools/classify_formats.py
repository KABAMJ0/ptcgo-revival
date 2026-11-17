#!/usr/bin/env python3
"""Assign every loaded set to the right play formats.

Real-era rules:
    Standard  = Scarlet & Violet + Sword & Shield + basic energies + custom
    Expanded  = Black & White and later (the real Expanded cutoff)
    Legacy    = the Black & White block
    Unlimited = everything, which is where pre-BW sets are legal

Era comes from the set's series in set_meta.json (written by
tools/build_set_catalog.py), falling back to the set code.

    ./venv/bin/python tools/classify_formats.py [--print]
"""

import glob
import json
import os
import sys

FORMATS_PATH = os.path.join("spirit", "database", "json_data", "formats.json")
META_PATH = os.path.join("spirit", "database", "json_data", "set_meta.json")
CARDS_DIR = os.path.join("spirit", "game", "scripts", "cards")

ERA_AGNOSTIC = {"FREE_ENERGY", "CUSTOM"}
SV_SERIES = {"scarlet & violet"}
SWSH_SERIES = {"sword & shield"}
BW_SERIES = {"black & white"}


def era_of(code, meta):
    c = code.upper()
    if c in ERA_AGNOSTIC:
        return "AGNOSTIC"
    series = (meta.get(code, {}).get("series") or "").lower()
    if series in SV_SERIES or c.startswith("SV") or c in {"ZSV10PT5", "RSV10PT5", "SVP", "SVE"}:
        return "SV"
    if series in SWSH_SERIES or c.startswith("SWSH") or c in {"CEL25", "PGO", "CZ", "PROMO_SWSH"}:
        return "SWSH"
    if series in BW_SERIES or c.startswith("BW") or c in {"DV", "PROMO_BW"}:
        return "BW"
    return "CLASSIC"  # Base, Neo, E-Card, EX, DP, Platinum, HGSS, POP, McDonald's


def loaded_sets():
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
    meta = json.load(open(META_PATH)) if os.path.exists(META_PATH) else {}

    sv = [s for s in sets if era_of(s, meta) == "SV"]
    swsh = [s for s in sets if era_of(s, meta) == "SWSH"]
    bw = [s for s in sets if era_of(s, meta) == "BW"]
    agnostic = [s for s in sets if era_of(s, meta) == "AGNOSTIC"]
    classic = [s for s in sets if era_of(s, meta) == "CLASSIC"]

    mapping = {
        "Standard": sorted(sv + swsh + agnostic),
        "Expanded": sorted(bw + swsh + sv + agnostic),
        "Legacy": sorted(bw + agnostic),
    }

    if "--print" in sys.argv:
        for key, val in mapping.items():
            print(f"{key} ({len(val)}): {', '.join(val[:12])} ...")
        print(f"Unlimited only ({len(classic)}): {', '.join(classic[:12])} ...")
        return

    data = json.load(open(FORMATS_PATH))
    for fmt in data["formats"]:
        key = fmt.get("key")
        if key in mapping:
            fmt["sets"] = mapping[key]
            fmt["allSets"] = False
    json.dump(data, open(FORMATS_PATH, "w"), indent=2)
    print("formats.json updated: " + ", ".join(f"{k}={len(v)}" for k, v in mapping.items())
          + f" | unlimited-only={len(classic)}")


if __name__ == "__main__":
    main()
