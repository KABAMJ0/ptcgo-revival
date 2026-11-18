"""Per-set booster pack rules: guaranteed slots, rarity weighting and no-duplicates.

The generic builder in `ptcgo/game/models/product.py` pulls 4 commons, 4 uncommons,
a reverse holo and a hit, all weighted only by rarity. That is right for most
sets and wrong for a few, where the real product has a fixed pull structure:

* the 30th Celebration set guarantees one of its four Pikachus in every pack, and
  its three Mew printings are the rarest cards in the set — not something you
  should see several of in a single pack.

Rules live in `ptcgo/database/json_data/pack_rules.json`, keyed by set code:

    {
      "ME55": {
        "guaranteed": [{"names": ["Pikachu"], "count": 1, "rarity_at_most": null}],
        "weight_multiplier": {"Mew": 0.02},
        "unique_per_pack": ["Mew", "Pikachu"]
      }
    }

`guaranteed` forces a slot from the named cards; `weight_multiplier` scales a
name's chance in the ordinary rarity draw; `unique_per_pack` means a pack may not
contain the same card twice. Anything unspecified behaves exactly as before.
"""

import json
import logging
import os

RULES_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "database", "json_data", "pack_rules.json"))

_rules_cache = None


def load_rules() -> dict:
    """The rules table, loaded once. Missing or malformed file means no rules."""
    global _rules_cache
    if _rules_cache is None:
        try:
            with open(RULES_PATH, encoding="utf-8") as f:
                _rules_cache = json.load(f)
        except (OSError, ValueError) as e:
            if os.path.exists(RULES_PATH):
                logging.warning(f"[Packs] pack_rules.json unreadable: {e}")
            _rules_cache = {}
    return _rules_cache


def rules_for(set_key: str) -> dict:
    return load_rules().get((set_key or "").upper(), {}) or {}


def name_of(card) -> str:
    return (getattr(card, "display_name", None) or "").strip()


def multiplier_for(set_key: str, card) -> float:
    """Rarity-draw weight multiplier for one card, 1.0 when the set has no rule."""
    table = rules_for(set_key).get("weight_multiplier") or {}
    return float(table.get(name_of(card), 1.0))


def guaranteed_picks(set_key: str, cards) -> list:
    """Cards forced into every pack of this set, by name."""
    picks = []
    for slot in rules_for(set_key).get("guaranteed") or []:
        names = {n.strip() for n in slot.get("names") or []}
        count = int(slot.get("count") or 1)
        pool = [c for c in cards if name_of(c) in names]
        if not pool:
            continue
        for _ in range(count):
            picks.append(pool)
    return picks


def dedupe(pack_guids, cards_by_guid, set_key: str) -> list:
    """Drop later copies of a card whose name may appear only once per pack."""
    unique_names = {n.strip() for n in (rules_for(set_key).get("unique_per_pack") or [])}
    if not unique_names:
        return pack_guids
    seen, kept = set(), []
    for guid in pack_guids:
        card = cards_by_guid.get(guid)
        name = name_of(card) if card is not None else None
        if name in unique_names:
            if name in seen:
                continue
            seen.add(name)
        kept.append(guid)
    return kept
