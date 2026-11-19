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
    from ptcgo.tools.ctx_check import build_inventory, check_source as ctx_check_source
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
    """Card scripts the range touches, including ones git does not track yet."""
    out = subprocess.run(["git", "diff", "--name-only", since, "--", CARDS_ROOT],
                         capture_output=True, text=True).stdout.split()
    fresh = subprocess.run(["git", "ls-files", "--others", "--exclude-standard", "--", CARDS_ROOT],
                           capture_output=True, text=True).stdout.split()
    return [p for p in dict.fromkeys(out + fresh) if p.endswith(".py")]


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


def module_alias(tree, name: str, src: str) -> str:
    """Source of a module-level `name = factory(...)` / `name, _ = factory(...)` binding."""
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets = []
            for target in node.targets:
                if isinstance(target, ast.Name):
                    targets.append(target.id)
                elif isinstance(target, ast.Tuple):
                    targets += [e.id for e in target.elts if isinstance(e, ast.Name)]
            if name in targets:
                return ast.get_source_segment(src, node) or ""
    return ""


def body_source(tree, expression, src: str) -> str:
    text = ast.unparse(expression)
    if not isinstance(expression, ast.Call):
        name = getattr(expression, "id", "")
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
                text += "\n" + (ast.get_source_segment(src, node) or "")
        text += "\n" + module_alias(tree, name, src)
    else:
        names = {n.id for n in ast.walk(expression) if isinstance(n, ast.Name)}
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in names:
                text += "\n" + (ast.get_source_segment(src, node) or "")
        for name in sorted(names):
            alias = module_alias(tree, name, src)
            if alias:
                text += "\n" + alias
    return text


def numbers_in_body(expression) -> Set[int]:
    found = set()
    lambdas = set()
    for node in ast.walk(expression):
        if isinstance(node, ast.Lambda):
            for sub in ast.walk(node):
                if isinstance(sub, ast.Constant) and type(sub.value) is int:
                    lambdas.add(id(sub))
    for node in ast.walk(expression):
        if isinstance(node, ast.Lambda):
            continue
        if isinstance(node, ast.Call):
            ignored = {k.arg for k in node.keywords if k.arg in IGNORE_KWARGS}
            for kw in node.keywords:
                if kw.arg in IGNORE_KWARGS:
                    continue
                for sub in ast.walk(kw.value):
                    if isinstance(sub, ast.Constant) and type(sub.value) is int \
                            and id(sub) not in lambdas:
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


WRAPPER_KWARGS = ("then", "also", "after", "on_success", "effect")


def primary_of(expression) -> str:
    """The factory that actually does the work, looking through a wrapper's rider."""
    if not isinstance(expression, ast.Call):
        return ""
    for keyword in expression.keywords:
        if keyword.arg in WRAPPER_KWARGS and isinstance(keyword.value, ast.Call):
            inner = primary_of(keyword.value)
            if inner:
                return inner
    return getattr(expression.func, "id", "")


def _analyse_block(tree, kw, effect, src) -> List[Tuple[str, str, str]]:
    out: List[Tuple[str, str, str]] = []
    block = block_identity(kw)
    printed_text = literal(kw["game_text"].value) if "game_text" in kw else ""
    printed_text = printed_text or ""
    body = body_source(tree, effect.value, src)
    primary = primary_of(effect.value)
    missing = block_conflict(printed_text, body, primary) if is_local_name(tree, effect.value) else []
    if missing:
        out.append(("kind", block, f"text names {', '.join(missing)}; body is {primary or 'a helper'}"))

    printed_damage = damage_value(kw)
    if not printed_text.strip():
        return out          # nothing printed: nothing to read back
    known = {int(n) for n in __import__("re").findall(r"\d+", printed_text)}
    colorless = printed_text.lower().count("colorless")
    if colorless and not known:
        known.add(colorless)   # 'ColorlessColorless less' is 2
    known.add(99)              # sentinel: 99 means 'any number'
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
    parser.add_argument("--ctx-warn", action="store_true",
                        help="Report ctx findings (unknown / wrong-path fields) without failing "
                             "the gate. Off by default: they fail, but only when the range adds one.")
    parser.add_argument("--quiet", action="store_true",
                        help="Print the summary and files with new violations only, not a "
                             "verdict line per clean file.")
    parser.add_argument("--sample", type=int, default=0,
                        help="Print N randomly sampled new violations for a false-positive check.")
    parser.add_argument("--seed", type=int, default=0, help="Sampling seed.")
    args = parser.parse_args(argv)

    paths = changed_files(args.since)
    ctx_fields, ctx_paths, _members = build_inventory()
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
        head_ctx = set((f"ctx-{kind}", block, detail)
                       for kind, block, detail in ctx_check_source(head_src, path, ctx_fields, ctx_paths))
        base_ctx = set((f"ctx-{kind}", block, detail)
                       for kind, block, detail in ctx_check_source(base_src, path, ctx_fields, ctx_paths)) \
            if base_src is not None else set()
        fresh_ctx = sorted(head_ctx - base_ctx)
        if fresh or fresh_ctx:
            files_with_new += 1
            print(f"{path}")
            for detector, block, detail in fresh:
                print(f"   [{detector}] {block}: {detail}")
                new_all.append((path, detector, block, detail))
            for detector, block, detail in fresh_ctx:
                print(f"   [{detector}] {block}: {detail}" + ("  (warn)" if args.ctx_warn else ""))
                if not args.ctx_warn:
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
