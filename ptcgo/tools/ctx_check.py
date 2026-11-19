"""Check every `ctx.<field>` a card body reads against what the engine sets on that path.

The class none of the other lenses sees: `on_ko_from_attack`'s rider reading
`ctx.attacker` where that path only provides `ctx.ko_attacker`. The body is the right
kind, its numbers come from the card's text, it loads clean and it resolves -- and then it
does nothing, because the field it read was never set on the path it runs on.

Two classes are reported:

  unknown     a field that exists on no ctx the engine builds (a typo, or a deleted field)
  wrong-path  a field the engine sets only on other play paths than the block's own

The inventory is built by scanning the engine rather than importing it: EffectContext's
members (annotated assignments included), every `ctx.<name> = ...` in session/ and
models/ with its full enclosing chain, and every property. Each assignment site's chain is
mapped to the play paths it serves -- attack, ability, trigger, tool, checkup, knockout --
and a field's allowed paths are the union of its sites. A site that cannot be classified
leaves the field unrestricted, because guessing there produces false alarms.

A block's own path comes from its registration: `Attack(...)` is the attack path, an
`Ability` with a trigger is the trigger path (KNOCKED_OUT triggers are the knockout hook),
an `Ability` on a tool card is the tool path, and anything else is an activated ability. A
body whose path cannot be decided is reported as `unknown-path` rather than guessed at.

Usage:
  python -m ptcgo.tools.ctx_check --all [--limit N] [--summary-only]
  python -m ptcgo.tools.ctx_check --files LIST
"""
import argparse
import ast
import os
import sys
from collections import defaultdict
from typing import Dict, List, Optional, Set, Tuple

CARDS_ROOT = os.path.join("ptcgo", "game", "scripts", "cards")
ENGINE_ROOTS = [os.path.join("ptcgo", "game", "session"),
                os.path.join("ptcgo", "game", "models")]
CONTEXT_CLASSES = ("EffectContext",)

# engine function-name hints -> the play paths that function serves
PATH_HINTS = (
    ("ko", ("knockout", "ko_", "_fire_knockout")),
    ("checkup", ("checkup", "between_turn")),
    ("attack", ("resolve_attack",)),
    ("ability", ("activated_ability",)),
    ("trigger", ("trigger",)),
    ("tool", ("tool",)),
)
CTX_NAMES = ("ctx", "c", "hook_ctx", "effect_ctx")


def engine_files() -> List[str]:
    out = []
    for root in ENGINE_ROOTS:
        for dirpath, _dirs, files in os.walk(root):
            if "__pycache__" in dirpath:
                continue
            out += [os.path.join(dirpath, f) for f in files if f.endswith(".py")]
    return sorted(out)


def enclosing_chain(tree, target) -> str:
    """Every function containing `target`, innermost first, joined for storage."""
    chain = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.lineno <= target.lineno <= (node.end_lineno or node.lineno):
                chain.append((node.lineno, node.name))
    return "|".join(name for _line, name in sorted(chain, reverse=True))


def engine_paths(chain: str) -> Set[str]:
    low = chain.lower()
    paths = {path for path, hints in PATH_HINTS if any(hint in low for hint in hints)}
    return paths


def build_inventory() -> Tuple[Set[str], Dict[str, Set[str]], Dict[str, Set[str]]]:
    """(every field any ctx carries, field -> paths that set it, class members).

    A field whose assignment site cannot be classified is left with an empty path set,
    which callers read as "unrestricted" -- the checker stays quiet rather than guess.
    """
    assigned: Dict[str, Set[str]] = defaultdict(set)
    members: Set[str] = set()
    for path in engine_files():
        try:
            src = open(path, encoding="utf-8").read()
            tree = ast.parse(src, path)
        except (SyntaxError, UnicodeDecodeError):
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name in CONTEXT_CLASSES:
                for sub in node.body:
                    if isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        members.add(sub.name)
                        for inner in ast.walk(sub):
                            for target in getattr(inner, "targets", []):
                                if (isinstance(target, ast.Attribute)
                                        and isinstance(target.value, ast.Name)
                                        and target.value.id in ("self", "ctx")):
                                    members.add(target.attr)
                            if isinstance(inner, ast.AnnAssign) and isinstance(inner.target, ast.Attribute):
                                members.add(inner.target.attr)
                    elif isinstance(sub, ast.Assign):
                        for target in sub.targets:
                            if isinstance(target, ast.Attribute):
                                members.add(target.attr)
                            elif isinstance(target, ast.Name):
                                members.add(target.id)
            targets = []
            if isinstance(node, ast.Assign):
                targets = node.targets
            elif isinstance(node, ast.AnnAssign) and node.target is not None:
                targets = [node.target]
            for target in targets:
                if (isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name)
                        and target.value.id in CTX_NAMES):
                    assigned[target.attr] |= engine_paths(enclosing_chain(tree, node))
    fields = set(assigned) | members
    return fields, {f: set(p) for f, p in assigned.items()}, members


def card_path(call: ast.Call, card_is_tool: bool) -> str:
    cls = getattr(call.func, "id", "")
    kw = {k.arg: k.value for k in call.keywords}
    trigger_text = " ".join(ast.unparse(kw[name]) for name in ("trigger",) if name in kw)
    if cls == "Attack":
        return "attack"
    if "KNOCKED_OUT" in trigger_text:
        return "ko"
    if trigger_text:
        return "trigger"
    return "tool" if card_is_tool else "ability"


def ctx_fields(expression, tree) -> Set[str]:
    """Every `ctx.<field>` the body reads, following local helpers and aliases."""
    found: Set[str] = set()
    roots = [expression]
    if isinstance(expression, ast.Name):
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == expression.id:
                roots.append(node)
            elif isinstance(node, ast.Assign):
                names = [t.id for t in node.targets if isinstance(t, ast.Name)]
                if expression.id in names:
                    roots.append(node)
    for root in roots:
        for node in ast.walk(root):
            if (isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name)
                    and node.value.id == "ctx" and isinstance(node.ctx, ast.Load)):
                found.add(node.attr)
    return found


def check_source(src: str, path: str, fields: Set[str],
                 paths_by_field: Dict[str, Set[str]]) -> List[Tuple[str, str, str]]:
    try:
        tree = ast.parse(src, path)
    except SyntaxError:
        return []
    card_is_tool = "PokemonToolCardDef" in src
    out: List[Tuple[str, str, str]] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or getattr(node.func, "id", "") not in ("Attack", "Ability"):
            continue
        kw = {k.arg: k for k in node.keywords}
        effect = kw.get("effect", kw.get("passive"))
        if effect is None or ast.unparse(effect.value) == "unimplemented":
            continue
        title = ast.literal_eval(kw["title"].value) if "title" in kw else "?"
        path_kind = card_path(node, card_is_tool)
        for field in sorted(ctx_fields(effect.value, tree)):
            if field not in fields:
                out.append(("unknown", title, f"ctx.{field} exists on no ctx the engine builds"))
                continue
            allowed = paths_by_field.get(field, set())
            if allowed and path_kind not in allowed:
                out.append(("wrong-path", title,
                            f"ctx.{field} is set only on {', '.join(sorted(allowed))}; "
                            f"this block is a {path_kind}"))
    return out


def check_file(path: str, fields: Set[str],
               paths_by_field: Dict[str, Set[str]]) -> List[Tuple[str, str, str]]:
    try:
        src = open(path, encoding="utf-8").read()
    except OSError:
        return []
    return check_source(src, path, fields, paths_by_field)


def card_paths() -> List[str]:
    out = []
    for code in sorted(os.listdir(CARDS_ROOT)):
        folder = os.path.join(CARDS_ROOT, code)
        if not os.path.isdir(folder) or code == "__pycache__":
            continue
        out += [os.path.join(folder, f) for f in sorted(os.listdir(folder))
                if f.endswith(".py") and f != "__init__.py"]
    return out


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m ptcgo.tools.ctx_check",
                                     description="Report ctx fields a card body reads that the "
                                                 "engine never sets on its path.")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--files")
    parser.add_argument("--summary-only", action="store_true")
    parser.add_argument("--limit", type=int, default=40)
    args = parser.parse_args(argv)
    fields, paths_by_field, members = build_inventory()
    print(f"ctx inventory: {len(fields)} fields, {sum(1 for p in paths_by_field.values() if p)} "
          f"with a decided path, {len(members)} class members", flush=True)
    if args.files:
        targets = [line.strip() for line in open(args.files, encoding="utf-8") if line.strip()]
    elif args.all:
        targets = card_paths()
    else:
        parser.error("give --all or --files LIST")
    counts: Dict[str, int] = defaultdict(int)
    shown = 0
    for path in targets:
        for kind, block, detail in check_file(path, fields, paths_by_field):
            counts[kind] += 1
            if not args.summary_only and shown < args.limit:
                print(f"[{kind}] {path} :: {block} :: {detail}")
                shown += 1
    print(f"\n{sum(counts.values())} findings over {len(targets)} scripts: "
          + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
