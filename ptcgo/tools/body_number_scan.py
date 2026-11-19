"""Whole-tree check: numbers inside installed effect bodies that the card's own
text never mentions.

The gap this closes is the donor-body class. A body copied from another
printing of the same sentence carries that printing's numbers, and every gate
stays green: the loader loads, the GUIDs are unique, the fingerprint is
unchanged and smoke only sees that something ran. `XY8/Xerneas_107` was a
`base=70` lifted from a 70-damage Sylveon print while its own text says 10, and
`reprint_filler` copies from reference cards like that one.

The check is deliberately blunt and advisory: every integer literal passed to a
body is compared with the integers the card's own `game_text`, `damage` and
cost mention. A number the text never mentions may be legitimate (a coin count,
a counter count, a type id), so this prints a list to triage, never a gate.

Run: PYTHONPATH=. python -m ptcgo.tools.body_number_scan [--min 10] [--top 40]
"""

import argparse
import ast
import collections
import glob
import re
from typing import Dict, List, Tuple

CARD_GLOB = "ptcgo/game/scripts/cards/*/*.py"
CARD_DEFS = ("PokemonCardDef", "TrainerCardDef", "EnergyCardDef",
             "PokemonToolCardDef", "StadiumCardDef")
_ENTRY_DEFS = ("Attack", "Ability")
_NUMBER_RE = re.compile(r"\d+")


def _ints_in_text(text: str) -> List[int]:
    return [int(m) for m in _NUMBER_RE.findall(text or "")]


def _own_numbers(entry: ast.Call) -> set:
    """Every number the card's own printed text and fields mention."""
    owned = set()
    for kw in entry.keywords:
        if kw.arg == "game_text" and isinstance(kw.value, ast.Constant) \
                and isinstance(kw.value.value, str):
            owned.update(_ints_in_text(kw.value.value))
        elif kw.arg == "damage" and isinstance(kw.value, ast.Constant) \
                and isinstance(kw.value.value, int):
            owned.add(kw.value.value)
        elif kw.arg == "cost":
            owned.update(_ints_from_tree(kw.value))
        elif kw.arg == "title" and isinstance(kw.value, ast.Constant) \
                and isinstance(kw.value.value, str):
            owned.update(_ints_in_text(kw.value.value))
    return owned


def _with_sums(owned: set) -> set:
    """Text often states a total additively ("10 damage plus 20 more"), so a
    body holding the sum is right even though the number never appears."""
    extended = set(owned)
    for a in owned:
        for b in owned:
            if a + b <= 400:
                extended.add(a + b)
    return extended


def _ints_from_tree(node: ast.AST) -> set:
    return {n.value for n in ast.walk(node)
            if isinstance(n, ast.Constant) and isinstance(n.value, int)
            and not isinstance(n.value, bool)}


def _body_ints(entry: ast.Call) -> List[Tuple[int, str]]:
    """(number, enclosing call name) for every literal handed to the body."""
    out: List[Tuple[int, str]] = []
    for kw in entry.keywords:
        if kw.arg != "effect":
            continue
        for node in ast.walk(kw.value):
            if not isinstance(node, ast.Call):
                continue
            name = ""
            func = node.func
            if isinstance(func, ast.Name):
                name = func.id
            elif isinstance(func, ast.Attribute):
                name = func.attr
            for arg in list(node.args) + [k.value for k in node.keywords]:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, int) \
                        and not isinstance(arg.value, bool):
                    out.append((arg.value, name))
    return out


def scan(minimum: int = 10) -> Dict[str, List[Tuple[int, str, str]]]:
    findings: Dict[str, List[Tuple[int, str, str]]] = collections.defaultdict(list)
    for path in sorted(glob.glob(CARD_GLOB)):
        try:
            tree = ast.parse(open(path, encoding="utf-8").read())
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            func = node.func
            name = func.id if isinstance(func, ast.Name) else getattr(func, "attr", "")
            if name not in CARD_DEFS:
                continue
            for kw in node.keywords:
                if kw.arg != "abilities" or not isinstance(kw.value, ast.List):
                    continue
                for entry in kw.value.elts:
                    if not isinstance(entry, ast.Call):
                        continue
                    ename = entry.func.id if isinstance(entry.func, ast.Name) else ""
                    if ename not in _ENTRY_DEFS:
                        continue
                    owned = _with_sums(_own_numbers(entry))
                    title = ""
                    for k in entry.keywords:
                        if k.arg == "title" and isinstance(k.value, ast.Constant):
                            title = str(k.value.value)
                    for number, call_name in _body_ints(entry):
                        if number < minimum or number in owned:
                            continue
                        findings[path].append((number, call_name, title))
    return findings


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--min", type=int, default=10,
                    help="smallest number worth reporting (default 10)")
    ap.add_argument("--top", type=int, default=40,
                    help="how many files to print (default 40)")
    args = ap.parse_args()

    findings = scan(args.min)
    total = sum(len(v) for v in findings.values())
    print(f"files with a number the card's text never mentions: {len(findings)}")
    print(f"totals: {total}")
    ranked = sorted(findings.items(), key=lambda kv: -len(kv[1]))
    for path, rows in ranked[:args.top]:
        shown = ", ".join(f"{n} ({call})" for n, call, _ in rows[:6])
        print(f"{path}  [{len(rows)}]: {shown}")
    if len(ranked) > args.top:
        print(f"... {len(ranked) - args.top} more files")


if __name__ == "__main__":
    main()
