#!/usr/bin/env python3
"""Install official booster pack art supplied by the operator.

Takes a folder of images named by set code (SWSH6.png, bw2.jpg, SV3PT5.webp ...)
and does the three things that make them show up in the shop:

  1. normalises each to the 512x512 transparent square the client renders
  2. writes it as spirit/assets/products/custom_packs/<code>_booster.png
  3. points that set's BoosterPackDef at it

    ./venv/bin/python tools/install_pack_art.py ~/Downloads/packs [--dry-run]
"""

import glob
import json
import os
import re
import sys

from PIL import Image

OUT_DIR = os.path.join("spirit", "assets", "products", "custom_packs")
PRODUCTS = os.path.join("spirit", "game", "scripts", "products")
CARDS = os.path.join("spirit", "game", "scripts", "cards")
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".avif"}


META_PATH = os.path.join("spirit", "database", "json_data", "set_meta.json")


def known_codes():
    return {os.path.basename(p) for p in glob.glob(os.path.join(CARDS, "*")) if os.path.isdir(p)}


def _slug(text):
    return re.sub(r"[^a-z0-9]+", "", (text or "").lower())


def match_set(stem, codes, meta):
    """Resolve a filename to a set code: by code, then by official set name."""
    cleaned = re.sub(r"^\d{4}-\d{2}-\d{2}[_-]*", "", stem).strip()   # drop a date prefix
    for candidate in (cleaned, stem):
        low = candidate.strip().lower()
        for code in codes:
            if code.lower() == low:
                return code
        for code, record in meta.items():
            if code not in codes:
                continue
            if _slug(record.get("name")) == _slug(candidate):
                return code
    # last resort: a set name contained in the filename
    hay = _slug(cleaned)
    best = None
    for code, record in meta.items():
        if code not in codes:
            continue
        slug = _slug(record.get("name"))
        if not slug:
            continue
        if (slug in hay or (hay and hay in slug)) and (
                best is None or len(slug) > len(_slug(meta[best].get("name")))):
            best = code
    return best


def normalise(src, dst):
    im = Image.open(src).convert("RGBA")
    if im.width > 4 and im.height > 4:
        bbox = im.getbbox()
        if bbox:
            im = im.crop(bbox)
    canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    ratio = min(496 / im.width, 496 / im.height)
    scaled = im.resize((max(1, int(im.width * ratio)), max(1, int(im.height * ratio))), Image.LANCZOS)
    canvas.alpha_composite(scaled, ((512 - scaled.width) // 2, (512 - scaled.height) // 2))
    canvas.save(dst)
    return im.size


def wire(code, dry):
    """Points the set's BoosterPackDef at its new art."""
    target = f"{code.lower()}_booster"
    changed = 0
    for path in glob.glob(os.path.join(PRODUCTS, code.lower(), "*.py")):
        body = open(path).read()
        if 'key="' not in body:
            continue
        new = re.sub(r'image_url="[^"]*"', f'image_url="{target}"', body)
        if new != body:
            if not dry:
                open(path, "w").write(new)
            changed += 1
    return changed


def main():
    if len(sys.argv) < 2:
        raise SystemExit("usage: install_pack_art.py <folder> [--dry-run]")
    folder = os.path.expanduser(sys.argv[1])
    dry = "--dry-run" in sys.argv
    codes = known_codes()
    meta = json.load(open(META_PATH)) if os.path.exists(META_PATH) else {}
    installed = skipped = 0
    for name in sorted(os.listdir(folder)):
        stem, ext = os.path.splitext(name)
        if ext.lower() not in IMAGE_EXTS:
            continue
        match = match_set(stem, codes, meta)
        if match is None:
            print(f"  no set matches '{name}'")
            skipped += 1
            continue
        dst = os.path.join(OUT_DIR, f"{match.lower()}_booster.png")
        if dry:
            print(f"  would install {name} -> {os.path.basename(dst)}")
        else:
            os.makedirs(OUT_DIR, exist_ok=True)
            size = normalise(os.path.join(folder, name), dst)
            wired = wire(match, dry)
            print(f"  {match}: {name} ({size[0]}x{size[1]}) -> {os.path.basename(dst)}, {wired} product(s) rewired")
        installed += 1
    print(f"installed {installed}, unmatched {skipped}")


if __name__ == "__main__":
    main()
