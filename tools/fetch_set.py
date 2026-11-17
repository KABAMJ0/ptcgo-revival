#!/usr/bin/env python3
"""Download one set's card data from pokemontcg.io into the importer's JSON format.

    python3 tools/fetch_set.py bw2 BW2

Writes spirit/game/scripts/cards/<CODE>/<set_id>.json as a plain list of cards,
which is what spirit/tools/import_set.py expects (the API wraps them in "data").
The query needs a URL-encoded colon and retries, or the API answers 500.
"""

import json
import os
import sys
import time
import urllib.parse
import urllib.request


def get(url, tries=6):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "spirit-import/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:  # 500/502 are common on the free tier
            last = e
            time.sleep(1.5 * (i + 1))
    raise SystemExit(f"failed {url}: {last}")


def main():
    if len(sys.argv) < 3:
        raise SystemExit("usage: fetch_set.py <set_id> <SET_CODE>")
    set_id = sys.argv[1].lower()
    code = sys.argv[2].upper()

    out_dir = f"spirit/game/scripts/cards/{code}"
    os.makedirs(out_dir, exist_ok=True)

    cards, page = [], 1
    while True:
        q = urllib.parse.quote(f"set.id:{set_id}")
        d = get(f"https://api.pokemontcg.io/v2/cards?q={q}&pageSize=250&page={page}&orderBy=number")
        cards.extend(d.get("data", []))
        if not d.get("data") or len(cards) >= d.get("totalCount", 0):
            break
        page += 1

    path = os.path.join(out_dir, f"{set_id}.json")
    with open(path, "w") as f:
        json.dump(cards, f, indent=1)
    print(f"{code}: {len(cards)} cards -> {path}")


if __name__ == "__main__":
    main()
