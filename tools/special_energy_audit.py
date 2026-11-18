"""Audits Special Energy scripts: printed rules text vs. wired behaviour.

Every `EnergyCardDef(..., is_special=True)` script either declares hooks
(`provides`, `attach_to`, `attach_condition`, `attach_cost`, `on_attach`,
`on_carrier_knocked_out`, `passive`) or is data only. This pairs each script with
its printed text from the set JSON so the unwired ones can be grouped by what they
actually ask for.

    python tools/special_energy_audit.py               # summary + groups
    python tools/special_energy_audit.py --list        # every card, unwired first
    python tools/special_energy_audit.py --json out.json
"""
import argparse
import ast
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

CARDS_ROOT = os.path.join("ptcgo", "game", "scripts", "cards")
HOOKS = ("provides", "attach_to", "attach_condition", "attach_cost",
         "on_attach", "on_carrier_knocked_out", "passive")
SKIP_DIRS = {"__pycache__", "CUSTOM", "Free_Energy"}

_ENERGY_TYPE = re.compile(
    r"\b(fire|water|lightning|grass|psychic|fighting|darkness|metal|fairy|dragon|colorless)"
    r"\b", re.I)
_NUMBER_WORDS = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10",
}


def normalize(text: str) -> str:
    """Same shape as the effect-pattern tables: numbers and types templated out."""
    value = (text or "").lower()
    value = re.sub(r"\s+", " ", value).strip()
    for word, digit in _NUMBER_WORDS.items():
        value = re.sub(rf"\b{word}\b", digit, value)
    value = _ENERGY_TYPE.sub("<type>", value)
    value = re.sub(r"\b\d+\b", "N", value)
    value = re.sub(r"[.\s]+$", "", value)
    return value


def parse_script(path):
    source = open(path, encoding="utf-8").read()
    tree = ast.parse(source, filename=path)
    call = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id == "EnergyCardDef":
            call = node
            break
    if call is None:
        return None
    kwargs = {kw.arg: kw.value for kw in call.keywords if kw.arg}
    special = False
    if "is_special" in kwargs and isinstance(kwargs["is_special"], ast.Constant):
        special = bool(kwargs["is_special"].value)
    wired = sorted(name for name in HOOKS if name in kwargs)
    return {
        "special": special,
        "hooks": wired,
        "energy_type": getattr(kwargs.get("energy_type"), "attr", None),
        "has_energy_value": "energy_value" in kwargs,
    }


def set_index():
    """{(set_dir_upper, number): printed rules text}"""
    index = {}
    for path in glob.glob(os.path.join(CARDS_ROOT, "*", "*.json")):
        try:
            cards = json.load(open(path, encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        set_dir = os.path.basename(os.path.dirname(path)).upper()
        for card in cards:
            rules = card.get("rules") or []
            if not rules and card.get("text"):
                rules = [card["text"]]
            text = " ".join(rules).strip()
            try:
                number = int(str(card.get("number", "")).split("/")[0])
            except ValueError:
                continue
            index[(set_dir, number)] = text
    return index


def collect():
    index = set_index()
    rows = []
    for directory in sorted(os.listdir(CARDS_ROOT)):
        if directory in SKIP_DIRS or not os.path.isdir(os.path.join(CARDS_ROOT, directory)):
            continue
        for path in sorted(glob.glob(os.path.join(CARDS_ROOT, directory, "*.py"))):
            if os.path.basename(path) == "__init__.py":
                continue
            info = parse_script(path)
            if not info or not info["special"]:
                continue
            stem = os.path.splitext(os.path.basename(path))[0]
            name, _, number = stem.rpartition("_")
            try:
                number = int(number)
            except ValueError:
                number = None
            rows.append({
                "path": path,
                "set": directory,
                "number": number,
                "name": name,
                "text": index.get((directory.upper(), number), ""),
                "hooks": info["hooks"],
                "energy_type": info["energy_type"],
            })
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--json")
    args = parser.parse_args()

    rows = collect()
    wired = [r for r in rows if r["hooks"]]
    unwired = [r for r in rows if not r["hooks"]]
    missing_text = [r for r in unwired if not r["text"]]

    print(f"special energy scripts: {len(rows)}  wired: {len(wired)}  data only: {len(unwired)}")
    print(f"unwired without printed text: {len(missing_text)}")

    groups = defaultdict(list)
    for row in unwired:
        groups[normalize(row["text"])].append(row)
    ordered = sorted(groups.items(), key=lambda item: -len(item[1]))
    print(f"distinct unwired texts: {len(ordered)}")
    print("\ntop shapes:")
    for text, cards in ordered[:25]:
        sample = cards[0]["name"]
        print(f"  {len(cards):3d}  {sample[:28]:28s} {text[:96]}")

    if args.list:
        print("\n--- unwired, by name ---")
        for row in sorted(unwired, key=lambda r: r["name"]):
            hooks = ",".join(row["hooks"]) or "-"
            print(f"{row['set']:10s} {str(row['number']):>4s} {row['name'][:34]:34s} "
                  f"[{hooks}] {row['text'][:90]}")

    if args.json:
        json.dump(rows, open(args.json, "w", encoding="utf-8"), indent=1)
        print(f"\nwrote {args.json}")


if __name__ == "__main__":
    main()
