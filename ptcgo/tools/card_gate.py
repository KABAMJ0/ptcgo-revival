"""Pre-merge gate: the three card detectors, over a diff range.

Runs on the card scripts a range touched and reports only violations that are **new**
in the range. Three detectors, each of which has already shipped a real defect past
the loader, the GUID gate, the fingerprint and smoke:

  kind    a body whose kind is not the kind its own printed text names
          (a damage body under a heal clause, a discard-Energy body under a
          "does 20 to each benched Pokemon" clause)
  number  a numeric literal in the body that the card's own text never mentions,
          allowing sums and differences ("10 damage plus 20 more" may be 30)
  base    an explicit base= on damage_per / flip_damage / bonus_if that disagrees
          with the printed damage= (the client shows one number and the engine pays
          another)

Quiet on legacy noise: a violation is only reported when the same (detector, block,
detail) is absent from the base revision of that file. A gate that fails on existing
defects gets switched off within a day.

Usage:
  python -m ptcgo.tools.card_gate --since <rev>            # one verdict line per file
  python -m ptcgo.tools.card_gate --since <rev> --quiet    # summary plus failing files only

Needs ptcgo/tools/kind_audit.py beside it (both files ship together in a tree that has
this one); on a branch that lacks it the gate says so and prints the command to fetch it.
  python -m ptcgo.tools.card_gate --since <rev> --sample 20

Exit status is 1 when the range adds a violation, 0 otherwise.
"""
import argparse
import ast
import os
import random
import subprocess
import sys
from typing import Dict, List, Optional, Set, Tuple

try:
    from ptcgo.tools.kind_audit import INTENTS, PURE_DAMAGE, SIGNALS, block_conflict
except ImportError:  # a lane whose branch predates the companion module
    sys.exit(
        "card_gate needs ptcgo/tools/kind_audit.py from the same tree, and this branch "
        "does not have it.\nEither rebase onto a branch that does, or take both files "
        "from origin/main and keep them:\n"
        "  git show origin/main:ptcgo/tools/kind_audit.py > ptcgo/tools/kind_audit.py\n"
        "  git show origin/main:ptcgo/tools/card_gate.py   > ptcgo/tools/card_gate.py")

CARDS_ROOT = os.path.join("ptcgo", "game", "scripts", "cards")
BASE_FNS = {"damage_per", "flip_damage", "bonus_if"}
# numbers that are structural rather than printed (HOME-14's read-back list)
IGNORE_KWARGS = {"coins", "count", "take", "minimum", "max_count", "counters", "index"}


def changed_files(since: str) -> List[str]:
    out = subprocess.run(["git", "diff", "--name-only", since, "--", CARDS_ROOT],
                         capture_output=True, text=True).stdout.split()
    return [p for p in out if p.endswith(".py")]


def file_at(rev: str, path: str) -> Optional[str]:
    result = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else None


def keyword_arg(kwargs: Dict[str, ast.keyword], name: str):
    return kwargs.get(name)


def literal(node):
    if isinstance(node, ast.Constant):
        return node.value
    return None


def damage_value(kw: Dict[str, ast.keyword]) -> Optional[int]:
    """The printed damage as an int.

    Three cards in the tree carry a string ('30+' on ECARD3/MiracleSphere_129..131):
    the operator is a client-side suffix, so '30+' and '30×' both compare as 30. An
    unreadable value returns None rather than raising -- a detector that dies mid-range
    hands the lane a clean exit code it did not earn.
    """
    if "damage" not in kw:
        return None
    raw = literal(kw["damage"].value)
    if isinstance(raw, bool):
        return None
    if isinstance(raw, int):
        return raw
    if isinstance(raw, str):
        match = __import__("re").match(r"\s*(\d+)", raw)
        if match:
            return int(match.group(1))
    return None


def block_identity(kw: Dict[str, ast.keyword]) -> str:
    title = literal(kw["title"].value) if "title" in kw else "?"
    return str(title)


def is_local_name(tree, expression) -> bool:
    """A bare name this file defines; an imported factory is opaque to the detector."""
    if not isinstance(expression, ast.Name):
        return True
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == expression.id:
            return True
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                if (alias.asname or alias.name) == expression.id:
                    return False
    return True


def body_source(tree, expression, src: str) -> str:
    text = ast.unparse(expression)
    if not isinstance(expression, ast.Call):
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                    and node.name == getattr(expression, "id", ""):
                text += "\n" + (ast.get_source_segment(src, node) or "")
    else:
        names = {n.id for n in ast.walk(expression) if isinstance(n, ast.Name)}
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in names:
                text += "\n" + (ast.get_source_segment(src, node) or "")
    return text


def numbers_in_body(expression) -> Set[int]:
    found = set()
    for node in ast.walk(expression):
        if isinstance(node, ast.Call):
            ignored = {k.arg for k in node.keywords if k.arg in IGNORE_KWARGS}
            for kw in node.keywords:
                if kw.arg in IGNORE_KWARGS:
                    continue
                for sub in ast.walk(kw.value):
                    if isinstance(sub, ast.Constant) and type(sub.value) is int:
                        found.add(sub.value)
            # positional arguments of count_* helpers are structural too
            if getattr(node.func, "id", "").startswith("count_"):
                continue
            for arg in node.args:
                if isinstance(arg, ast.Call) and getattr(arg.func, "id", "").startswith("count_"):
                    continue
                for sub in ast.walk(arg):
                    if isinstance(sub, ast.Constant) and type(sub.value) is int:
                        found.add(sub.value)
        elif isinstance(node, ast.Compare) or isinstance(node, ast.BinOp):
            continue
    return found


def analyze(src: str, path: str) -> List[Tuple[str, str, str]]:
    """(detector, block, detail) violations in one card script.

    Never raises: an unreadable block becomes a named finding, so a lane can see the
    oddity instead of reading a truncated run as a clean verdict.
    """
    try:
        tree = ast.parse(src, path)
    except SyntaxError as exc:
        return [("parse", "file", f"cannot parse: {exc.msg} (line {exc.lineno})")]
    out: List[Tuple[str, str, str]] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or getattr(node.func, "id", "") not in ("Attack", "Ability"):
            continue
        kw = {k.arg: k for k in node.keywords}
        effect = kw.get("effect", kw.get("passive"))
        if effect is None or ast.unparse(effect.value) == "unimplemented":
            continue
        block = block_identity(kw)
        try:
            out.extend(_analyse_block(tree, kw, effect, src))
        except Exception as exc:  # noqa: BLE001 - report, never die mid-range
            out.append(("parse", block, f"{type(exc).__name__}: {exc}"))
    return out


def _analyse_block(tree, kw, effect, src) -> List[Tuple[str, str, str]]:
    out: List[Tuple[str, str, str]] = []
    block = block_identity(kw)
    printed_text = literal(kw["game_text"].value) if "game_text" in kw else ""
    printed_text = printed_text or ""
    body = body_source(tree, effect.value, src)
    primary = getattr(getattr(effect.value, "func", None), "id", "")
    missing = block_conflict(printed_text, body, primary) if is_local_name(tree, effect.value) else []
    if missing:
        out.append(("kind", block, f"text names {', '.join(missing)}; body is {primary or 'a helper'}"))

    printed_damage = damage_value(kw)
    known = {int(n) for n in __import__("re").findall(r"\d+", printed_text)}
    if printed_damage is not None:
        known.add(int(printed_damage))
    allowed = set(known)
    for a in known:
        for b in known:
            allowed.add(a + b)
            allowed.add(abs(a - b))
    if "damage counter" in printed_text.lower():
        # the engine stores damage, the card prints counters
        for a in list(allowed):
            allowed.add(a * 10)
            if a % 10 == 0:
                allowed.add(a // 10)
    stray = sorted(n for n in numbers_in_body(effect.value) if n not in allowed and n not in (0, 1))
    if stray:
        out.append(("number", block, f"body carries {stray}, text has {sorted(known)}"))

    operator = literal(kw["damage_operator"].value) if "damage_operator" in kw else ""
    if isinstance(effect.value, ast.Call) and primary in BASE_FNS and printed_damage is not None:
        if operator in ("", "+") and not (primary == "flip_damage"
                                          and any(k.arg == "per_heads" for k in effect.value.keywords)):
            for k in effect.value.keywords:
                if k.arg == "base":
                    base_value = literal(k.value)
                    if isinstance(base_value, int) and base_value != printed_damage:
                        out.append(("base", block, f"base={base_value} but damage={printed_damage}"))
    return out


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m ptcgo.tools.card_gate",
                                     description="Report card-body violations newly introduced in a range.")
    parser.add_argument("--since", required=True, help="Base revision to compare HEAD against.")
    parser.add_argument("--quiet", action="store_true",
                        help="Print the summary and files with new violations only, not a "
                             "verdict line per clean file.")
    parser.add_argument("--sample", type=int, default=0,
                        help="Print N randomly sampled new violations for a false-positive check.")
    parser.add_argument("--seed", type=int, default=0, help="Sampling seed.")
    args = parser.parse_args(argv)

    paths = changed_files(args.since)
    new_all: List[Tuple[str, str, str, str]] = []
    files_with_new = 0
    for path in paths:
        try:
            head_src = open(path, encoding="utf-8").read()
        except OSError:
            continue
        base_src = file_at(args.since, path)
        head_hits = set(analyze(head_src, path))
        base_hits = set(analyze(base_src, path)) if base_src is not None else set()
        fresh = sorted(head_hits - base_hits)
        if fresh:
            files_with_new += 1
            print(f"{path}")
            for detector, block, detail in fresh:
                print(f"   [{detector}] {block}: {detail}")
                new_all.append((path, detector, block, detail))
        elif not args.quiet:
            print(f"{path}: clean")

    print(f"\n{len(paths)} changed card scripts, {files_with_new} with new violations, "
          f"{len(new_all)} new violations")
    if args.sample and new_all:
        random.seed(args.seed)
        for path, detector, block, detail in random.sample(new_all, min(args.sample, len(new_all))):
            print(f"SAMPLE [{detector}] {path} :: {block} :: {detail}")
    return 1 if new_all else 0


if __name__ == "__main__":
    sys.exit(main())
