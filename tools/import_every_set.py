#!/usr/bin/env python3
"""Import every set in the pokemontcg.io catalogue that we do not already have.

Codes follow the API set id uppercased, which matches the client's own set
codes for most eras (XY6, SM10, HGSS1 ...). Existing folders are skipped, so
this is safe to re-run.

    ./venv/bin/python tools/import_every_set.py            # everything missing
    ./venv/bin/python tools/import_every_set.py --dry-run
"""

import argparse
import glob
import json
import os
import subprocess
import sys
import time
import urllib.request

SETS_API = "https://api.pokemontcg.io/v2/sets?pageSize=250"
CARDS_DIR = os.path.join("ptcgo", "game", "scripts", "cards")
CODE_OVERRIDES = {  # api id -> our code, where they differ
    "dv1": "DV",
    "bwp": "Promo_BW",
    "swshp": "Promo_SWSH",
    "swsh12pt5": "CZ",
    "cel25": "CEL25",
    "pgo": "PGO",
}


def fetch_sets(tries=6):
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(SETS_API, headers={"User-Agent": "spirit-import/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)["data"]
        except Exception as e:
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise SystemExit(f"could not fetch the set list: {last}")


def existing_codes():
    return {
        os.path.basename(p).upper()
        for p in glob.glob(os.path.join(CARDS_DIR, "*"))
        if os.path.isdir(p) and glob.glob(os.path.join(p, "*.py"))
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    have = existing_codes()
    todo = []
    for s in fetch_sets():
        code = CODE_OVERRIDES.get(s["id"], s["id"]).upper()
        if code in have:
            continue
        todo.append((s, code))

    print(f"sets missing: {len(todo)}")
    total = sum(s.get("total") or 0 for s, _ in todo)
    print(f"cards to import: {total}")
    for s, code in todo[:8]:
        print(f"  {code:<12} {s['name']}")
    if args.dry_run:
        return

    for index, (s, code) in enumerate(todo, 1):
        print(f"[{index}/{len(todo)}] {code} ({s['name']})", flush=True)
        try:
            subprocess.run([sys.executable, "tools/fetch_set.py", s["id"], code], check=True)
            subprocess.run(
                [sys.executable, "ptcgo/tools/import_set.py",
                 f"ptcgo/game/scripts/cards/{code}/{s['id']}.json", "--set-code", code],
                check=True, stdout=subprocess.DEVNULL)
            subprocess.run([sys.executable, "tools/fix_collector_numbers.py", code], check=True)
        except subprocess.CalledProcessError as e:
            print(f"  FAILED: {e}", flush=True)
            continue
        scripts = len(glob.glob(f"ptcgo/game/scripts/cards/{code}/*.py"))
        images = len(glob.glob(f"ptcgo/assets/cards/{code}/*.png"))
        print(f"  scripts={scripts} images={images}", flush=True)


if __name__ == "__main__":
    main()
