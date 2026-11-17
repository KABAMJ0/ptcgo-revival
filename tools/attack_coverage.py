"""Attack/ability wording audit for Pokemon card scripts.

Parses card scripts with `ast` (never imports them) and groups every still
`effect=unimplemented` attack / ability on a Pokemon card by its normalized
game text, so recurring wording becomes one work item instead of one card.

Usage:
    python tools/attack_coverage.py                    # summary + top patterns
    python tools/attack_coverage.py --top 40           # longer ranking
    python tools/attack_coverage.py --json out.json    # full pattern list
    python tools/attack_coverage.py --set SWSH8        # one set only
    python tools/attack_coverage.py --grep "each energy"
"""

import argparse
import ast
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Optional

CARDS_ROOT = os.path.join("spirit", "game", "scripts", "cards")
SKIP_DIRS = {"__pycache__", "CUSTOM", "Free_Energy"}
POKEMON_CLASSES = {"PokemonCardDef", "PokemonReprintCardDef"}
ABILITY_CALLS = {"Attack", "Ability"}

_NUMBER = re.compile(r"\b\d+\b")
_ENERGY_TYPES = re.compile(
    r"\b(fire|water|lightning|grass|psychic|fighting|darkness|metal|fairy|dragon|colorless)"
    r" energy\b"
)


def normalize(text: str) -> str:
    """Collapse wording to a template: digits -> N, energy types -> <type>."""
    value = re.sub(r"\s+", " ", (text or "").strip().lower())
    value = _ENERGY_TYPES.sub("<type> energy", value)
    value = _NUMBER.sub("N", value)
    return value


@dataclass
class Entry:
    card_name: str
    set_code: str
    kind: str            # "Attack" | "Ability"
    title: str
    text: str
    template: str = field(init=False)

    def __post_init__(self):
        self.template = normalize(self.text)


@dataclass
class Totals:
    scripts: int = 0
    unimplemented: int = 0
    implemented: int = 0


def _kwarg(call: ast.Call, name: str, positional: int) -> Optional[ast.expr]:
    for kw in call.keywords:
        if kw.arg == name:
            return kw.value
    if positional < len(call.args):
        return call.args[positional]
    return None


def _const(node) -> str:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return ""


def _is_unimplemented(node) -> bool:
    return isinstance(node, ast.Name) and node.id == "unimplemented"


def parse_script(path: str, set_code: str, totals: Totals) -> List[Entry]:
    source = open(path, encoding="utf-8").read()
    if "unimplemented" not in source:
        totals.scripts += 1
        return []
    try:
        tree = ast.parse(source, filename=path)
    except SyntaxError as exc:
        print(f"warning: cannot parse {path}: {exc}", file=sys.stderr)
        return []

    card_call = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call) \
                and isinstance(node.value.func, ast.Name) \
                and node.value.func.id in POKEMON_CLASSES | {"TrainerCardDef", "ItemCardDef",
                                                            "SupporterCardDef", "StadiumCardDef",
                                                            "PokemonToolCardDef", "EnergyCardDef"}:
            card_call = node.value
            break
    if card_call is None:
        return []

    is_pokemon = card_call.func.id in POKEMON_CLASSES
    totals.scripts += 1
    stem = os.path.splitext(os.path.basename(path))[0]
    card_name = stem.rsplit("_", 1)[0]

    entries: List[Entry] = []
    for node in ast.walk(card_call):
        if node is card_call or not isinstance(node, ast.Call):
            continue
        if not isinstance(node.func, ast.Name) or node.func.id not in ABILITY_CALLS:
            continue
        effect = _kwarg(node, "effect", 3)
        if effect is None:
            totals.implemented += 1
            continue
        if not _is_unimplemented(effect):
            totals.implemented += 1
            continue
        totals.unimplemented += 1
        if not is_pokemon:
            continue
        entries.append(Entry(card_name=card_name, set_code=set_code,
                             kind=node.func.id,
                             title=_const(_kwarg(node, "title", 0)),
                             text=_const(_kwarg(node, "game_text", 1))))
    return entries


def scan(only_set: Optional[str] = None) -> tuple[List[Entry], Totals]:
    entries: List[Entry] = []
    totals = Totals()
    for set_code in sorted(os.listdir(CARDS_ROOT)):
        set_dir = os.path.join(CARDS_ROOT, set_code)
        if not os.path.isdir(set_dir) or set_code in SKIP_DIRS:
            continue
        if only_set and set_code != only_set:
            continue
        for filename in sorted(os.listdir(set_dir)):
            if filename.endswith(".py") and filename != "__init__.py":
                entries.extend(parse_script(os.path.join(set_dir, filename), set_code, totals))
    return entries, totals


def report(entries: List[Entry], totals: Totals, top: int, grep: Optional[str]):
    groups: Dict[str, List[Entry]] = defaultdict(list)
    for entry in entries:
        groups[entry.template].append(entry)
    ranked = sorted(groups.items(), key=lambda kv: -len(kv[1]))

    attacks = sum(1 for e in entries if e.kind == "Attack")
    print(f"Pokemon scripts scanned          {totals.scripts}")
    print(f"Pokemon attack/ability entries   {attacks + sum(1 for e in entries if e.kind == 'Ability')} unimplemented")
    print(f"Other unimplemented entries      {totals.unimplemented - len(entries)} (trainers/energy)")
    print(f"Implemented entries (all cards)  {totals.implemented}")
    print(f"Distinct Pokemon wording        {len(groups)}")
    covered = 0
    print()
    print(f"{'COUNT':>6}  {'KIND':<8} TEMPLATE")
    for template, items in ranked:
        if grep and grep.lower() not in template:
            continue
        covered += 1
        if covered > top:
            break
        kinds = "/".join(sorted({i.kind for i in items}))
        sample = items[0]
        print(f"{len(items):>6}  {kinds:<8} {template[:110]}")
        if len(items) > 1:
            print(f"{'':>16} e.g. {sample.card_name} ({sample.set_code}, {sample.title})")
    return ranked


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--top", type=int, default=25)
    parser.add_argument("--json", help="write every pattern with its cards here")
    parser.add_argument("--set", help="single set code")
    parser.add_argument("--grep", help="only templates containing this text")
    args = parser.parse_args()

    entries, totals = scan(only_set=args.set)
    ranked = report(entries, totals, args.top, args.grep)

    if args.json:
        payload = [{
            "count": len(items),
            "kinds": sorted({i.kind for i in items}),
            "template": template,
            "cards": [{"name": i.card_name, "set": i.set_code, "title": i.title} for i in items],
        } for template, items in ranked]
        with open(args.json, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=1)
        print(f"\nwrote {len(payload)} patterns to {args.json}")


if __name__ == "__main__":
    main()
