#!/usr/bin/env python3
"""Fold sets we imported under API ids into the client's own set codes.

Our importer names sets after pokemontcg.io ids (COL1, SM35, XYP ...), but the
2020 client already knows those sets under its own codes (COL, SL, Promo_XY).
Left alone that shows the same set twice in the collection and the shop, and
the client rejects duplicate abbreviations outright.

    ./venv/bin/python tools/merge_duplicate_sets.py [--dry-run]
"""

import glob
import json
import os
import shutil
import sys

CARDS = "ptcgo/game/scripts/cards"
ASSETS = "ptcgo/assets/cards"
PRODUCTS = "ptcgo/game/scripts/products"
SETS_JSON = "ptcgo/database/json_data/sets.json"

# our folder -> the client's code for the same set
MERGES = {
    "COL1": "COL",             # Call of Legends
    "DC1": "TATM",             # Dragon Vault / Trainer kits era
    "G1": "TwentiethAnn",      # Generations
    "SM35": "SL",              # Shining Legends
    "SM75": "DM",              # Dragon Majesty
    "DET1": "GUM",             # Detective Pikachu
    "SM115": "HF",             # Hidden Fates
    "SMA": "SVault",           # Hidden Fates Shiny Vault (client has no code for it)
    "HSP": "Promo_HGSS",       # HGSS promos
    "XYP": "Promo_XY",         # XY promos
    "SMP": "Promo_SM",         # SM promos
}


def move_set(old, new, dry):
    src_scripts, dst_scripts = os.path.join(CARDS, old), os.path.join(CARDS, new)
    src_assets, dst_assets = os.path.join(ASSETS, old), os.path.join(ASSETS, new)
    if not os.path.isdir(src_scripts):
        return 0
    moved = skipped = 0
    os.makedirs(dst_scripts, exist_ok=True)
    os.makedirs(dst_assets, exist_ok=True)
    for path in glob.glob(os.path.join(src_scripts, "*.py")):
        stem = os.path.splitext(os.path.basename(path))[0]
        target = os.path.join(dst_scripts, os.path.basename(path))
        if os.path.exists(target):
            skipped += 1
            continue
        if not dry:
            with open(path) as f:
                body = f.read()
            body = body.replace(f'key="{old}"', f'key="{new}"').replace(f'set_code="{old}"', f'set_code="{new}"')
            with open(target, "w") as f:
                f.write(body)
            os.remove(path)
            png_src = os.path.join(src_assets, f"{stem}.png")
            png_dst = os.path.join(dst_assets, f"{stem}.png")
            if os.path.exists(png_src) and not os.path.exists(png_dst):
                shutil.move(png_src, png_dst)
        moved += 1
    if not dry:
        shutil.rmtree(src_scripts, ignore_errors=True)
        shutil.rmtree(src_assets, ignore_errors=True)
        shutil.rmtree(os.path.join(PRODUCTS, old.lower()), ignore_errors=True)
    return moved, skipped


def main():
    dry = "--dry-run" in sys.argv
    total = 0
    for old, new in MERGES.items():
        result = move_set(old, new, dry)
        if result:
            moved, skipped = result
            total += moved
            print(f"{old} -> {new}: moved {moved}, skipped {skipped} duplicates")

    if dry:
        print(f"dry run: {total} scripts would move")
        return

    entries = json.load(open(SETS_JSON))
    by_name = {e["name"]: e for e in entries}
    for old, new in MERGES.items():
        dropped = by_name.pop(old, None)
        keep = by_name.get(new)
        if keep is None:
            if dropped:
                dropped["name"] = new
                by_name[new] = dropped
            continue
        count = len(glob.glob(os.path.join(CARDS, new, "*.py")))
        if dropped and dropped.get("count", 0) > count:
            count = dropped["count"]
        keep["count"] = count
    json.dump(sorted(by_name.values(), key=lambda e: e.get("number", 0)), open(SETS_JSON, "w"), indent=2)
    print(f"sets.json entries after merge: {len(by_name)}")


if __name__ == "__main__":
    main()
