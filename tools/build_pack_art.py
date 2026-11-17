#!/usr/bin/env python3
"""Give every set a booster pack sleeve.

The upstream project ships artwork for about twenty sets; everything else falls back to
`booster_generic.png`, so the shop shows a wall of identical packs. This pulls
each set's official logo from pokemontcg.io and composes a 512x512 pack sleeve
in the client's expected layout (square, transparent, art centred): an era
coloured gradient with the set logo and its name.

    ./venv/bin/python tools/build_pack_art.py [--force]
"""

import glob
import io
import json
import os
import sys
import time
import urllib.request

from PIL import Image, ImageDraw, ImageFont

SETS_API = "https://api.pokemontcg.io/v2/sets?pageSize=250"
OUT_DIR = os.path.join("ptcgo", "assets", "products", "custom_packs")
CARDS_DIR = os.path.join("ptcgo", "game", "scripts", "cards")
META_PATH = os.path.join("ptcgo", "database", "json_data", "set_meta.json")

# How each era's sleeve is tinted.
ERA_PALETTE = {
    "BW": ((28, 32, 58), (74, 96, 168)),
    "SWSH": ((22, 34, 58), (36, 120, 172)),
    "SV": ((46, 18, 54), (168, 54, 96)),
    "OTHER": ((30, 28, 26), (120, 96, 54)),
    "UNLIMITED": ((26, 30, 34), (96, 108, 120)),
}

FONT_PATHS = (
    "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/liberation/LiberationSans-Bold.ttf",
)


def font(size):
    for path in FONT_PATHS:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()


def get(url, tries=5):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "spirit-art/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception:
            time.sleep(1.2 * (i + 1))
    return None


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def compose(code, name, era, logo_bytes):
    top, bottom = ERA_PALETTE.get(era, ERA_PALETTE["OTHER"])
    img = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    for y in range(512):
        t = y / 511
        draw.line([(0, y), (512, y)],
                  fill=(int(top[0] + (bottom[0] - top[0]) * t),
                        int(top[1] + (bottom[1] - top[1]) * t),
                        int(top[2] + (bottom[2] - top[2]) * t), 255))
    # sleeve edges: a bright foil border with a darker inner rule
    draw.rounded_rectangle([6, 6, 505, 505], radius=18, outline=(240, 214, 130, 255), width=6)
    draw.rounded_rectangle([18, 18, 493, 493], radius=12, outline=(255, 255, 255, 60), width=2)

    if logo_bytes:
        try:
            logo = Image.open(io.BytesIO(logo_bytes)).convert("RGBA")
            box_w, box_h = 400, 240
            ratio = min(box_w / logo.width, box_h / logo.height)
            logo = logo.resize((max(1, int(logo.width * ratio)), max(1, int(logo.height * ratio))), Image.LANCZOS)
            img.alpha_composite(logo, ((512 - logo.width) // 2, 96 + (box_h - logo.height) // 2))
        except Exception:
            pass

    draw.text((256, 380), code, font=font(44), fill=(255, 255, 255, 235), anchor="mm")
    fnt = font(26)
    for i, line in enumerate(wrap(draw, name, fnt, 420)[:2]):
        draw.text((256, 428 + i * 30), line, font=fnt, fill=(226, 226, 236, 210), anchor="mm")
    draw.text((256, 480), "BOOSTER", font=font(20), fill=(240, 214, 130, 235), anchor="mm")
    return img


def main():
    force = "--force" in sys.argv
    os.makedirs(OUT_DIR, exist_ok=True)
    meta = json.load(open(META_PATH))
    blob = get(SETS_API)
    if not blob:
        raise SystemExit("could not fetch the set list")
    upstream = {s["id"].upper(): s for s in json.loads(blob)["data"]}

    api_overrides = {
        "COL": "COL1", "TATM": "DC1", "TWENTIETHANN": "G1", "SL": "SM35", "DM": "SM75",
        "GUM": "DET1", "HF": "SM115", "SVAULT": "SMA", "PROMO_HGSS": "HSP",
        "PROMO_XY": "XYP", "PROMO_SM": "SMP", "DV": "DV1", "PROMO_BW": "BWP",
        "PROMO_SWSH": "SWSHP", "CZ": "SWSH12PT5",
    }

    made = skipped = failed = 0
    for code in sorted(os.path.basename(p) for p in glob.glob(os.path.join(CARDS_DIR, "*")) if os.path.isdir(p)):
        if code.startswith("__"):
            continue
        target = os.path.join(OUT_DIR, f"{code.lower()}_booster.png")
        if os.path.exists(target) and not force:
            skipped += 1
            continue
        record = meta.get(code, {})
        name = record.get("name") or code
        era = record.get("era") or "OTHER"
        api_id = api_overrides.get(code.upper(), code.upper())
        upstream_set = upstream.get(api_id)
        logo_bytes = None
        if upstream_set:
            logo = ((upstream_set.get("images") or {}).get("logo"))
            if logo:
                logo_bytes = get(logo)
        if logo_bytes is None and not os.path.exists(os.path.join(OUT_DIR, "booster_generic.png")):
            failed += 1
            continue
        compose(code, name, era, logo_bytes).save(target)
        made += 1
    print(f"pack art written: {made} | already present: {skipped} | without logo: {failed}")


if __name__ == "__main__":
    main()
