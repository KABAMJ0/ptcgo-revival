"""Check every `ctx.<field>` a card body reads against what the engine actually sets.

The class none of the other lenses sees: `on_ko_from_attack`'s rider reading
`ctx.attacker` where that path only provides `ctx.ko_attacker`. The body is the right
kind, its numbers come from the card's text, it loads clean and it resolves -- and then
it does nothing, because the attribute it read was never set on that path.

Two classes are reported, and neither is a hard failure until a lane asks for it:

  unknown     a field that exists on no ctx the engine builds (a typo, or a deleted field)
  wrong-path  a field the engine sets only on one path, read on another -- the class that
              cost us Innards Out

The inventory is built by scanning the engine, not by importing it: EffectContext's own
members, every `ctx.<name> = ...` assignment anywhere in session/ with the enclosing
function, and every property. When the path a body is registered for cannot be decided,
the field is reported as `unknown-path` rather than guessed at.

Usage:
  python -m ptcgo.tools.ctx_check --all
  python -m ptcgo.tools.ctx_check --files LIST
  python -m ptcgo.tools.ctx_check --all --summary-only
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

# engine functions whose ctx carries the knockout hook's extra fields
KO_PATH_HINTS = ("knockout", "ko_", "_fire_knockout", "between_turns")
TRIGGER_FIELDS = {"ko_attacker": ("KNOCKED_OUT",), "ko_from_attack": ("KNOCKED_OUT",),
                  "ko_source": ("KNOCKED_OUT",), "ko_pokemon": ("KNOCKED_OUT",)}


def engine_files() -> List[str]:
    out = []
    for root in ENGINE_ROOTS:
        for dirpath, _dirs, files in os.walk(root):
            if "__pycache__" in dirpath:
                continue
            out += [os.path.join(dirpath, f) for f in files if f.endswith(".py")]
    return sorted(out)


def enclosing_chain(tree, target) -> List[str]:
    """Every function containing `target`, innermost first.

    A knockout field is often set inside a closure (`_setup`) that lives in
    `resolve_knockouts`, so the innermost name alone says nothing about the path.
    """
    chain = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.lineno <= target.lineno <= (node.end_lineno or node.lineno):
                chain.append((node.lineno, node.name))
    return [name for _line, name in sorted(chain, reverse=True)]


def build_inventory() -> Tuple[Set[str], Dict[str, Set[str]], Set[str]]:
    """(fields set anywhere on a ctx, field -> enclosing engine functions, class members)."""
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
                            inner_targets = []
                            if isinstance(inner, ast.Assign):
                                inner_targets = inner.targets
                            elif isinstance(inner, ast.AnnAssign) and inner.target is not None:
                                inner_targets = [inner.target]
                            if inner_targets:
                                for target in inner_targets:
                                    if (isinstance(target, ast.Attribute)
                                            and isinstance(target.value, ast.Name)
                                            and target.value.id in ("self", "ctx")):
                                        members.add(target.attr)
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
                if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name):
                    if target.value.id in ("ctx", "c", "hook_ctx", "effect_ctx"):
                        assigned[target.attr].add("|".join(enclosing_chain(tree, node)))
    return set(assigned) | members, assigned, members


def ko_only(field: str, assigned: Dict[str, Set[str]]) -> bool:
    """True when every place the engine sets this field sits on the knockout path."""
    chains = assigned.get(field)
    if not chains:
        return False
    return all(any(hint in name.lower() for hint in KO_PATH_HINTS for name in chain.split("|"))
               for chain in chains)


def path_of(call: ast.Call) -> str:
    cls = getattr(call.func, "id", "")
    kw = {k.arg: k.value for k in call.keywords}
    trigger = ""
    for name in ("trigger", "condition"):
        if name in kw:
            text = ast.unparse(kw[name])
            if "KNOCKED_OUT" in text:     # ON_KNOCKED_OUT, ON_ALLY_KNOCKED_OUT, ...
                trigger = "ON_KNOCKED_OUT"
    if trigger:
        return "trigger"
    return "attack" if cls == "Attack" else "ability"


def ctx_fields(expression, src: str, tree) -> Set[str]:
    """Every `ctx.<field>` the body reads, following one level of local helpers."""
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


def check_file(path: str, fields: Set[str], assigned: Dict[str, Set[str]]) -> List[Tuple[str, str, str]]:
    src = open(path, encoding="utf-8").read()
    try:
        tree = ast.parse(src, path)
    except SyntaxError:
        return []
    out: List[Tuple[str, str, str]] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or getattr(node.func, "id", "") not in ("Attack", "Ability"):
            continue
        kw = {k.arg: k for k in node.keywords}
        effect = kw.get("effect", kw.get("passive"))
        if effect is None or ast.unparse(effect.value) == "unimplemented":
            continue
        title = ast.literal_eval(kw["title"].value) if "title" in kw else "?"
        path_kind = path_of(node)
        for field in sorted(ctx_fields(effect.value, src, tree)):
            if field in fields:
                if ko_only(field, assigned) and path_kind != "trigger":
                    out.append(("wrong-path", title,
                                f"ctx.{field} is set only on the knockout hook path, "
                                f"this block is a {path_kind}"))
                continue
            if field in TRIGGER_FIELDS:
                out.append(("wrong-path", title, f"ctx.{field} only exists on {TRIGGER_FIELDS[field]}"))
            else:
                out.append(("unknown", title, f"ctx.{field} exists on no ctx the engine builds"))
    return out


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m ptcgo.tools.ctx_check",
                                     description="Report ctx fields a card body reads that the "
                                                 "engine never sets on that path.")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--files")
    parser.add_argument("--summary-only", action="store_true")
    parser.add_argument("--limit", type=int, default=40)
    args = parser.parse_args(argv)
    fields, assigned, members = build_inventory()
    print(f"ctx inventory: {len(fields)} fields, {len(assigned)} assigned in the engine, "
          f"{len(members)} class members", flush=True)
    if args.files:
        paths = [line.strip() for line in open(args.files, encoding="utf-8") if line.strip()]
    elif args.all:
        paths = []
        for code in sorted(os.listdir(CARDS_ROOT)):
            folder = os.path.join(CARDS_ROOT, code)
            if not os.path.isdir(folder) or code == "__pycache__":
                continue
            paths += [os.path.join(folder, f) for f in sorted(os.listdir(folder))
                      if f.endswith(".py") and f != "__init__.py"]
    else:
        parser.error("give --all or --files LIST")
    counts: Dict[str, int] = defaultdict(int)
    shown = 0
    for path in paths:
        for kind, block, detail in check_file(path, fields, assigned):
            counts[kind] += 1
            if not args.summary_only and shown < args.limit:
                print(f"[{kind}] {path} :: {block} :: {detail}")
                shown += 1
    print(f"\n{sum(counts.values())} findings over {len(paths)} scripts: "
          + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
