#!/usr/bin/env python3
"""Fill the gaps in the client's filter vocabulary.

The 2020 client renders a filter label by looking up a key it derives from the
value the server sends -- `collection.filter.series.<slug>` for a series,
`deckbuilder.cardfilters.rarity.<slug>` for a rarity, and so on. Anything we send
that it has no key for shows up as the raw key, which is what a screen full of
"collection.filter.series.mega evolution" was.

This compares the labels that client ships with the values our card data can
actually produce, and writes the missing ones to
`ptcgo/database/json_data/custom_labels.json`. The localization handler merges
that file at startup, so the labels travel with the repository instead of being
hard-coded in the handler.

    ./venv/bin/python tools/build_labels.py [--db PATH] [--dry-run]
"""

import argparse
import json
import os
import re
import sqlite3
import sys
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DB = os.path.join(ROOT, "ptcgo", "database", "game_data", "LocalizationDB-UTF16.db")
OUT_PATH = os.path.join(ROOT, "ptcgo", "database", "json_data", "custom_labels.json")
FILTER = "deckbuilder.cardfilters."

sys.path.insert(0, ROOT)

from ptcgo.game.attributes import AttrID, CardType, PokemonStage, PokemonTypes, Rarities, TrainerType
from ptcgo.game.scripts.cards import loader

# series slug -> the name the filter should show
SERIES = {
    "base": "Base", "neo": "Neo", "ecard": "E-Card", "gym": "Gym", "ex": "EX",
    "dp": "Diamond & Pearl", "pl": "Platinum", "hgss": "HeartGold & SoulSilver",
    "bw": "Black & White", "xy": "XY", "sm": "Sun & Moon",
    "swsh": "Sword & Shield", "sv": "Scarlet & Violet", "me": "Mega Evolution",
    "pop": "POP Series", "promos": "Promos", "custom": "Custom",
}

RARITY_NAMES = {
    "rareultra": "Ultra Rare", "raresecret": "Secret Rare",
    "rarerainbow": "Rainbow Rare", "rarepromo": "Promo",
    "rareradiant": "Radiant Rare", "amazing": "Amazing Rare",
    "ace": "ACE SPEC", "breakrare": "BREAK Rare", "unset": "Unset",
}

# mechanics our cards carry that the client may need an attribute label for
ATTRIBUTES = {
    "v": "Pokémon V", "vmax": "Pokémon VMAX", "vstar": "Pokémon VSTAR",
    "vunion": "Pokémon V-UNION", "ex": "Pokémon ex", "tera": "Tera",
    "radiant": "Radiant", "prism": "Prism Star", "ace": "ACE SPEC",
    "break": "BREAK", "restored": "Restored", "legend": "Legend",
    "ultrabeast": "Ultra Beast",
}

POKEMON_NAMES = {
    "stage1": "Stage 1", "stage2": "Stage 2",
    "v": "Pokémon V", "ex": "Pokémon ex", "gx": "Pokémon-GX",
    "vmax": "Pokémon VMAX", "vstar": "Pokémon VSTAR", "vunion": "Pokémon V-UNION",
    "break": "Pokémon BREAK", "restored": "Restored", "legend": "Legend",
    "levelup": "Level-Up", "mega": "Mega Evolution", "sp": "Pokémon SP",
}

TRAINER_NAMES = {
    "pokemontool": "Pokémon Tool", "pokemontoolf": "Pokémon Tool F",
    "technicalmachine": "Technical Machine",
}


def client_keys(db_path):
    con = sqlite3.connect(Path(db_path).resolve().as_uri() + "?mode=ro", uri=True)
    try:
        return {key.lower() for key, in con.execute("select key from Lookup")}
    finally:
        con.close()


def slug(name):
    return re.sub(r"[\s_-]+", "", name.lower()).replace("é", "e")


def card_filter_labels(card):
    """Yield filter keys from the published archetype and its script subtypes."""
    attrs = card.to_archetype_attributes("")

    def value(attr, default=None):
        return attrs.get(str(attr.value), {}).get("value", default)

    rarity = Rarities(value(AttrID.RARITY)).name
    rarity_slug = slug(rarity)
    words = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", rarity).replace("Chr ", "Character ")
    rarity_name = RARITY_NAMES.get(rarity_slug, words[:1].upper() + words[1:])
    yield f"{FILTER}rarity.{rarity_slug}", rarity_name
    yield f"{FILTER}tooltips.rarity{rarity_slug}", rarity_name

    elements = value(AttrID.POKEMON_TYPES, [])
    if isinstance(elements, str):
        elements = json.loads(elements)
    for element in elements:
        element_name = PokemonTypes(element).name
        yield f"{FILTER}{slug(element_name)}type", f"{element_name.replace('_', ' ').title()} Type"

    card_type = value(AttrID.CARD_TYPE)
    if card_type in (CardType.POKEMON, CardType.LEGEND_HALF):
        pokemon_kinds = set(card.subtypes)
        if (stage := value(AttrID.STAGE)) is not None:
            pokemon_kinds.add(PokemonStage(stage).name.title())
        for kind in sorted(pokemon_kinds):
            kind_slug = slug(kind)
            yield f"{FILTER}pokemontype.{kind_slug}", POKEMON_NAMES.get(kind_slug, kind)

    if card_type == CardType.TRAINER:
        kind = TrainerType(value(AttrID.TRAINER_TYPE)).name
        kind_slug = slug(kind)
        kind_name = TRAINER_NAMES.get(kind_slug, kind.replace("_", " ").title())
        yield f"{FILTER}trainercards.{kind_slug}", kind_name
        for subtype in card.subtypes:
            if (kind_slug := slug(subtype)) in TRAINER_NAMES:
                yield f"{FILTER}trainercards.{kind_slug}", TRAINER_NAMES[kind_slug]

    if card_type == CardType.ENERGY:
        kind = "Special" if value(AttrID.IS_SPECIAL_ENERGY, False) else "Basic"
        yield f"{FILTER}energycards.{kind.lower()}", f"{kind} Energy"

    for subtype in card.subtypes:
        if (mechanic := slug(subtype)) in ATTRIBUTES:
            yield f"{FILTER}attributes.{mechanic}", ATTRIBUTES[mechanic]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    try:
        have = client_keys(args.db)
    except sqlite3.Error as error:
        ap.error(f"could not read client labels from {args.db}: {error}")

    existing = {}
    if os.path.exists(OUT_PATH):
        with open(OUT_PATH, encoding="utf-8") as f:
            existing = json.load(f)
    labels = dict(existing)

    def want(key, value):
        if key not in have:
            labels.setdefault(key, value)

    for slug, name in SERIES.items():
        want(f"collection.filter.series.{slug}", f"<i>{name}</i> Series")
    cards = loader.load_all()
    if loader.last_errors:
        ap.error(f"could not audit all cards: {len(loader.last_errors)} load errors")
    for card in cards:
        for key, name in card_filter_labels(card):
            want(key, name)

    if args.dry_run:
        for key in sorted(labels.keys() - existing.keys()):
            print(f"  {key} = {labels[key]}")
        print(f"{len(labels) - len(existing)} labels missing")
        return

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(labels, f, indent=2, sort_keys=True)
        f.write("\n")
    print(f"wrote {len(labels)} labels to {OUT_PATH} ({len(labels) - len(existing)} new)")


if __name__ == "__main__":
    main()
