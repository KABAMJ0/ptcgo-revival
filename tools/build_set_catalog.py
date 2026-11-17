#!/usr/bin/env python3
"""Give every imported set its real name, and catalogue it chronologically.

What this fixes:

* sets.json only described the Sword & Shield block, so BW and SV sets had no
  display name, no block and no chronological position in the client's set list.
* auto-generated booster packs are named `product.bw2.booster`, a localisation
  key the 2.94 client has never seen, so the shop showed blank pack names.

It derives everything from pokemontcg.io's set list:

    ./venv/bin/python tools/build_set_catalog.py

Writes spirit/database/json_data/set_meta.json (code -> name, abbreviation,
release date, series, order), rewrites sets.json, and generates a
BoosterPackDef product script for every set that lacks one.
"""

import glob
import json
import os
import time
import urllib.request
import uuid

SETS_API = "https://api.pokemontcg.io/v2/sets?pageSize=250"
META_PATH = os.path.join("spirit", "database", "json_data", "set_meta.json")
SETS_JSON = os.path.join("spirit", "database", "json_data", "sets.json")
FORMATS_JSON = os.path.join("spirit", "database", "json_data", "formats.json")
CARDS_DIR = os.path.join("spirit", "game", "scripts", "cards")
PRODUCTS_DIR = os.path.join("spirit", "game", "scripts", "products")
PACKS_DIR = os.path.join("spirit", "assets", "products", "custom_packs")

# Our set code -> pokemontcg.io set id, where they differ.
API_ID_OVERRIDES = {
    "CZ": "swsh12pt5",
    "PROMO_SWSH": "swshp",
    "PROMO_BW": "bwp",
    "SVP": "svp",
    "SVE": "sve",
    "DV": "dv1",
}

# Sets we built ourselves; they have no upstream record.
MANUAL_META = {
    "CUSTOM": {"name": "Custom Cards", "ptcgoCode": "CUSTOM", "releaseDate": "2026/01/01", "series": "Custom"},
    "FREE_ENERGY": {"name": "Basic Energy", "ptcgoCode": "ENERGY", "releaseDate": "2011/04/25", "series": "Black & White"},
}

PRODUCT_NAMESPACE = uuid.uuid5(uuid.NAMESPACE_DNS, "spiritptcgo.catalog.products")


def fetch_sets(tries=6):
    """pokemontcg.io answers 500 intermittently on the free tier, so retry."""
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(SETS_API, headers={"User-Agent": "spirit-catalog/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return {s["id"]: s for s in json.load(r)["data"]}
        except Exception as e:
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise SystemExit(f"could not fetch the set list: {last}")


def loaded_sets():
    out = []
    for path in glob.glob(os.path.join(CARDS_DIR, "*")):
        if not os.path.isdir(path) or os.path.basename(path).startswith("__"):
            continue
        if glob.glob(os.path.join(path, "*.py")):
            out.append(os.path.basename(path))
    return sorted(out)


def card_count(code):
    return len([f for f in os.listdir(os.path.join(CARDS_DIR, code)) if f.endswith(".py")])


def era_of(code):
    c = code.upper()
    if c in ("FREE_ENERGY", "CUSTOM"):
        return "UNLIMITED"
    if c.startswith("SV") or c in ("ZSV10PT5", "RSV10PT5", "SVP", "SVE"):
        return "SV"
    if c.startswith("SWSH") or c in ("CEL25", "PGO", "CZ", "PROMO_SWSH"):
        return "SWSH"
    if c.startswith("BW") or c in ("DV", "PROMO_BW"):
        return "BW"
    return "OTHER"


def pack_image(code):
    base = f"{code.lower()}_booster"
    try:
        pngs = [f.lower() for f in os.listdir(PACKS_DIR) if f.lower().endswith(".png")]
    except OSError:
        pngs = []
    if f"{base}.png" in pngs:
        return base
    for name in sorted(pngs):
        if name.startswith(base):
            return os.path.splitext(name)[0]
    return "booster_generic"


def main():
    upstream = fetch_sets()
    codes = loaded_sets()
    formats = {f["key"]: f["guid"] for f in json.load(open(FORMATS_JSON))["formats"]}

    meta = {}
    for code in codes:
        api_id = API_ID_OVERRIDES.get(code.upper(), code.lower())
        record = upstream.get(api_id)
        if record:
            meta[code] = {
                "name": record["name"],
                "ptcgoCode": record.get("ptcgoCode") or code,
                "releaseDate": record.get("releaseDate", ""),
                "series": record.get("series", ""),
            }
        elif code.upper() in MANUAL_META:
            meta[code] = dict(MANUAL_META[code.upper()])
        else:
            meta[code] = {"name": code, "ptcgoCode": code, "releaseDate": "", "series": ""}

    ordered = sorted(codes, key=lambda c: (meta[c]["releaseDate"] or "9999", c))
    for index, code in enumerate(ordered):
        meta[code]["order"] = index
        meta[code]["count"] = card_count(code)
        meta[code]["era"] = era_of(code)

    json.dump(meta, open(META_PATH, "w"), indent=2, sort_keys=True)

    # --- sets.json: name, block, chronological number, format legality
    existing = {entry["name"]: entry for entry in json.load(open(SETS_JSON))}
    for code in ordered:
        record = meta[code]
        legal = []
        if code in json.load(open(FORMATS_JSON))["formats"][0].get("sets", []):
            legal.append(formats["Standard"])
        if code in json.load(open(FORMATS_JSON))["formats"][1].get("sets", []):
            legal.append(formats["Expanded"])
        if code in json.load(open(FORMATS_JSON))["formats"][2].get("sets", []):
            legal.append(formats["Legacy"])
        entry = existing.get(code, {})
        entry.update({
            "name": code,
            "externalId": record["ptcgoCode"],
            "number": 1000 + record["order"],
            "count": record["count"],
            "filter": True,
            "block": record["era"],
            "legalFormats": legal,
            "featuredArchetypes": entry.get("featuredArchetypes", []),
            "visibleUnfilterable": False,
            "promo": "PROMO" in code.upper(),
        })
        existing[code] = entry
    ordered_entries = sorted(existing.values(), key=lambda e: e.get("number", 0))
    json.dump(ordered_entries, open(SETS_JSON, "w"), indent=2)

    # --- one BoosterPackDef script per set, named properly
    written = 0
    for code in ordered:
        target_dir = os.path.join(PRODUCTS_DIR, code.lower())
        target = os.path.join(target_dir, f"{code.lower()}.py")
        if os.path.exists(target):
            continue
        os.makedirs(target_dir, exist_ok=True)
        guid = str(uuid.uuid5(PRODUCT_NAMESPACE, code.upper()))
        name = meta[code]["name"]
        with open(target, "w") as f:
            f.write(
                "from spirit.game.data_utils import BoosterPackDef\n\n"
                f'product = BoosterPackDef(\n'
                f'    guid="{guid}",\n'
                f'    key="{code}",\n'
                f'    name="{name}",\n'
                f'    image_url="{pack_image(code)}",\n'
                f')\n'
            )
        written += 1

    print(f"sets catalogued: {len(meta)} | product scripts written: {written}")
    for code in ordered:
        print(f"  {meta[code]['order']:>2}. {code:<11} {meta[code]['name']:<34} {meta[code]['releaseDate']:<11} {meta[code]['era']}")


if __name__ == "__main__":
    main()
