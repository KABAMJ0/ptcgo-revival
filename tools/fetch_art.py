#!/usr/bin/env python3
"""Download the card art the repository does not ship.

Card PNGs (~14 GB) are gitignored, so a fresh checkout has scripts but no art.
For every card script without a texture this tries, in order:

  1. the official scan from pokemontcg.io, matched by name and number
  2. the upstream SpiritPTCGO repository, for Spirit's own SWSH-era scripts
     whose file names do not follow the API's naming
  3. tools/render_missing_art.py, which draws a face from the card's data

Safe to re-run: existing images are never downloaded again.

    ./venv/bin/python tools/fetch_art.py              # every set
    ./venv/bin/python tools/fetch_art.py SWSH1 BW2    # only these sets
"""

import glob
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

CARDS = os.path.join("spirit", "game", "scripts", "cards")
ASSETS = os.path.join("spirit", "assets", "cards")
API = "https://api.pokemontcg.io/v2/cards?q={q}&pageSize=250&page={page}"
UPSTREAM = "https://raw.githubusercontent.com/Bratah123/Spirit-PTCGO/main/spirit/assets/cards/{code}/{stem}.png"

# our set folder -> pokemontcg.io set id, where it is not simply the lowercase code
API_IDS = {
    "CZ": "swsh12pt5", "PROMO_SWSH": "swshp", "PROMO_BW": "bwp", "DV": "dv1",
    "COL": "col1", "TATM": "dc1", "TWENTIETHANN": "g1", "SL": "sm35", "DM": "sm75",
    "GUM": "det1", "HF": "sm115", "SVAULT": "sma", "PROMO_HGSS": "hsp",
    "PROMO_XY": "xyp", "PROMO_SM": "smp", "SWSH35": "swsh35", "SWSH45": "swsh45",
}
SKIP = {"CUSTOM", "FREE_ENERGY", "__PYCACHE__"}


def clean_name(name):
    return re.sub(r"[^a-zA-Z0-9]", "", name or "")


def get(url, tries=6, as_json=False):
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "spirit-fetch-art/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            return json.loads(data) if as_json else data
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
        except Exception:
            pass
        time.sleep(1.5 * (attempt + 1))
    return None


def api_cards(code):
    """Card records for a set: the committed set JSON if present, else the API."""
    for path in glob.glob(os.path.join(CARDS, code, "*.json")):
        try:
            return json.load(open(path, encoding="utf-8"))
        except Exception:
            continue
    set_id = API_IDS.get(code.upper(), code.lower())
    cards, page = [], 1
    while True:
        q = urllib.parse.quote(f"set.id:{set_id}")
        d = get(API.format(q=q, page=page), as_json=True)
        if not d or not d.get("data"):
            break
        cards.extend(d["data"])
        if len(cards) >= d.get("totalCount", 0):
            break
        page += 1
    return cards


def save(blob, path):
    if blob and len(blob) > 2000:
        with open(path, "wb") as f:
            f.write(blob)
        return True
    return False


def fetch_set(code):
    missing = []
    for script in glob.glob(os.path.join(CARDS, code, "*.py")):
        stem = os.path.splitext(os.path.basename(script))[0]
        if stem == "__init__":
            continue
        png = os.path.join(ASSETS, code, f"{stem}.png")
        if not os.path.exists(png):
            missing.append((stem, png))
    if not missing:
        return 0, 0
    os.makedirs(os.path.join(ASSETS, code), exist_ok=True)
    index = {}
    for card in api_cards(code):
        imgs = card.get("images") or {}
        url = imgs.get("large") or imgs.get("small")
        if url:
            index[f"{clean_name(card.get('name'))}_{card.get('number')}"] = url

    def one(item):
        stem, png = item
        url = index.get(stem)
        if url and save(get(url), png):
            return 1
        return 1 if save(get(UPSTREAM.format(code=code, stem=urllib.parse.quote(stem))), png) else 0

    with ThreadPoolExecutor(max_workers=8) as pool:
        got = sum(pool.map(one, missing))
    return got, len(missing)


def main():
    wanted = {a.upper() for a in sys.argv[1:]}
    codes = sorted(os.path.basename(p) for p in glob.glob(os.path.join(CARDS, "*")) if os.path.isdir(p))
    total_got = total_missing = 0
    for code in codes:
        if code.upper() in SKIP or (wanted and code.upper() not in wanted):
            continue
        got, missing = fetch_set(code)
        if missing:
            print(f"{code}: fetched {got}/{missing}", flush=True)
        total_got += got
        total_missing += missing
    print(f"downloaded {total_got} of {total_missing} missing images")
    # anything still without a scan gets a readable face drawn from its data
    subprocess.run([sys.executable, "tools/render_missing_art.py"], check=False)


if __name__ == "__main__":
    main()
