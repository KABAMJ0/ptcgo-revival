#!/usr/bin/env python3
"""Verify every card script has a usable texture, and re-fetch what it can.

Checks each script's PNG for existence and integrity with PIL, then retries the
download for anything missing or corrupt. Cards whose API image is genuinely
gone are reported so they can be given a rendered placeholder.

    ./venv/bin/python tools/audit_artwork.py [--fix]
"""

import glob
import json
import os
import sys
import time
import urllib.request

from PIL import Image

CARDS_DIR = "spirit/game/scripts/cards"
ASSETS_DIR = "spirit/assets/cards"


def api_cards(code):
    for candidate in glob.glob(os.path.join(CARDS_DIR, code, "*.json")):
        try:
            return json.load(open(candidate))
        except Exception:
            continue
    return []


def download(url, path, tries=3):
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "spirit-import/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            if len(data) < 2000:
                return False
            with open(path, "wb") as f:
                f.write(data)
            return True
        except Exception:
            time.sleep(1.5 * (attempt + 1))
    return False


def main():
    fix = "--fix" in sys.argv
    broken, fixed, unfixable = [], 0, []
    checked = 0

    for script in glob.glob(os.path.join(CARDS_DIR, "*", "*.py")):
        code = script.split(os.sep)[-2]
        stem = os.path.splitext(os.path.basename(script))[0]
        png = os.path.join(ASSETS_DIR, code, f"{stem}.png")
        checked += 1
        state = "ok"
        if not os.path.exists(png):
            state = "missing"
        else:
            try:
                with Image.open(png) as im:
                    im.verify()
                if os.path.getsize(png) < 2000:
                    state = "tiny"
            except Exception:
                state = "invalid"
        if state == "ok":
            continue
        broken.append((code, stem, state, png))

    print(f"checked {checked} scripts | broken {len(broken)}")
    if not fix or not broken:
        for row in broken[:20]:
            print("  ", row[0], row[1], row[2])
        return

    # Group by set so we only parse each set JSON once.
    by_set = {}
    for code, stem, state, png in broken:
        by_set.setdefault(code, []).append((stem, state, png))

    for code, entries in by_set.items():
        index = {}
        for card in api_cards(code):
            name = card.get("name", "")
            number = str(card.get("number", ""))
            index[f"{name}_{number}"] = card
        for stem, state, png in entries:
            card = index.get(stem)
            url = ((card or {}).get("images") or {}).get("large")
            if not url:
                url = ((card or {}).get("images") or {}).get("small")
            if not url:
                unfixable.append((code, stem, "no image url"))
                continue
            if os.path.exists(png):
                os.remove(png)
            if download(url, png):
                fixed += 1
            else:
                unfixable.append((code, stem, "download failed"))

    print(f"re-fetched {fixed} | still broken {len(unfixable)}")
    for row in unfixable[:30]:
        print("  ", row[0], row[1], row[2])
    json.dump(unfixable, open("/tmp/unfixable_art.json", "w"))


if __name__ == "__main__":
    main()
