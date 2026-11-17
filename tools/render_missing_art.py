#!/usr/bin/env python3
"""Render a card face for cards whose official scan does not exist.

pokemontcg.io carries records for some promos with no image behind them (the
McDonald's sets, Tropical Tidal Wave, a few XY promos). Rather than leave those
cards invisible, draw a readable face from the card's own data: name, HP, type,
attacks and their text, so the card is identifiable in the collection.

    ./venv/bin/python tools/render_missing_art.py
"""

import glob
import json
import os
import re

from PIL import Image, ImageDraw, ImageFont

CARDS_DIR = "ptcgo/game/scripts/cards"
ASSETS_DIR = "ptcgo/assets/cards"
TYPE_COLORS = {
    "Grass": (60, 140, 70), "Fire": (170, 60, 40), "Water": (40, 100, 170),
    "Lightning": (190, 160, 40), "Psychic": (120, 60, 150), "Fighting": (150, 100, 60),
    "Darkness": (60, 60, 70), "Metal": (110, 120, 130), "Colorless": (150, 145, 135),
    "Dragon": (140, 110, 40), "Fairy": (190, 110, 160),
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


def card_records(code):
    out = {}
    for path in glob.glob(os.path.join(CARDS_DIR, code, "*.json")):
        try:
            for card in json.load(open(path)):
                out[f"{card.get('name','')}_{card.get('number','')}"] = card
        except Exception:
            continue
    return out


def wrap(draw, text, font_obj, width):
    words, lines, current = text.split(), [], ""
    for word in words:
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=font_obj) <= width:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def render(card, path, code):
    width = height = 1024
    types = card.get("types") or ["Colorless"]
    base = TYPE_COLORS.get(types[0], (90, 90, 110))
    img = Image.new("RGBA", (width, height), (18, 18, 24, 255))
    draw = ImageDraw.Draw(img)

    for y in range(height):
        t = y / height
        draw.line([(0, y), (width, y)],
                  fill=(int(base[0] * (1.1 - 0.4 * t)), int(base[1] * (1.1 - 0.4 * t)),
                        int(base[2] * (1.2 - 0.3 * t)), 255))

    draw.rounded_rectangle([36, 36, width - 36, height - 36], radius=44,
                           outline=(240, 210, 120, 255), width=12)
    draw.rectangle([80, 250, width - 80, 620], fill=(20, 20, 28, 255),
                   outline=(240, 210, 120, 255), width=5)
    draw.text((110, 130), card.get("name", "Unknown"), font=font(60), fill=(255, 255, 255, 255))
    hp = card.get("hp")
    if hp:
        draw.text((width - 260, 130), f"HP {hp}", font=font(52), fill=(255, 120, 120, 255))
    draw.text((110, 200), " / ".join(card.get("subtypes") or []) or card.get("supertype", ""),
              font=font(30), fill=(225, 220, 235, 255))
    draw.text((130, 400), "artwork unavailable", font=font(44), fill=(180, 175, 195, 255))
    draw.text((130, 470), "rendered locally from card data", font=font(30),
              fill=(160, 155, 175, 255))

    y = 660
    for attack in (card.get("attacks") or [])[:2]:
        draw.text((100, y), attack.get("name", ""), font=font(44), fill=(255, 255, 255, 255))
        damage = attack.get("damage", "")
        if damage:
            draw.text((width - 240, y), str(damage), font=font(44), fill=(255, 255, 255, 255))
        y += 54
        for line in wrap(draw, attack.get("text", "") or "", font(26), width - 220)[:3]:
            draw.text((100, y), line, font=font(26), fill=(225, 220, 235, 255))
            y += 32
        y += 14

    draw.text((100, height - 110), f"{code} {card.get('number','')}", font=font(26),
              fill=(240, 210, 120, 255))
    img.save(path)


def main():
    missing = []
    for script in glob.glob(os.path.join(CARDS_DIR, "*", "*.py")):
        code = script.split(os.sep)[-2]
        stem = os.path.splitext(os.path.basename(script))[0]
        if not os.path.exists(os.path.join(ASSETS_DIR, code, f"{stem}.png")):
            missing.append((code, stem))

    print(f"missing artwork: {len(missing)}")
    by_set = {}
    for code, stem in missing:
        by_set.setdefault(code, []).append(stem)

    for code, stems in by_set.items():
        records = card_records(code)
        os.makedirs(os.path.join(ASSETS_DIR, code), exist_ok=True)
        for stem in stems:
            card = records.get(stem, {"name": stem.rsplit("_", 1)[0], "number": stem.rsplit("_", 1)[-1]})
            render(card, os.path.join(ASSETS_DIR, code, f"{stem}.png"), code)
    print(f"rendered {len(missing)} placeholder faces")


if __name__ == "__main__":
    main()
