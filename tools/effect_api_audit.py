"""Static audit of effect code that a script-level smoke test cannot reach.

Two failure classes cost this project real bugs:

1. calling an EffectContext method with a keyword it does not accept
   (`ctx.reveal_cards(of_player=...)` instead of `to_player=`), and
2. using a module-level name that was never imported (`random.choice`).

Neither raises until a specific card is actually played, so `effect_smoke`
can report PASS while the card throws in a real match. This walks the effect
modules with `ast`, resolves every `ctx.<method>(...)` call against the real
`EffectContext` signature, and reports names that are not bound anywhere in
their module.

Usage: python tools/effect_api_audit.py [paths...]
"""

import ast
import inspect
import sys
import builtins
from typing import Dict, List, Tuple

DEFAULT_PATHS = [
    "ptcgo/game/card_effects/patterns.py",
    "ptcgo/game/card_effects/attacks_common.py",
    "ptcgo/game/card_effects/passives_common.py",
    "ptcgo/game/card_effects/support_common.py",
    "ptcgo/game/card_effects/pokemon.py",
    "ptcgo/game/card_effects/trainers.py",
    "ptcgo/game/card_effects/energies.py",
]


def effect_context_methods() -> Dict[str, inspect.Signature]:
    from ptcgo.game.session.effects import EffectContext
    methods = {}
    for name, member in inspect.getmembers(EffectContext):
        if name.startswith("__"):
            continue
        try:
            methods[name] = inspect.signature(member)
        except (TypeError, ValueError):
            continue
    return methods


def _bound_names(tree: ast.Module) -> set:
    """Every name the module binds at module scope or inside a function."""
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                names.add((alias.asname or alias.name).split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                names.add(alias.asname or alias.name)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.add(node.name)
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            names.add(node.id)
        elif isinstance(node, ast.arg):
            names.add(node.arg)
        elif isinstance(node, ast.ExceptHandler) and node.name:
            names.add(node.name)
        elif isinstance(node, ast.Global):
            names.update(node.names)
    return names


def audit(path: str, methods: Dict[str, inspect.Signature]) -> List[str]:
    problems: List[str] = []
    source = open(path, encoding="utf-8").read()
    tree = ast.parse(source, filename=path)
    bound = _bound_names(tree) | set(dir(builtins))

    for node in ast.walk(tree):
        # unused/undefined globals
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            if node.id not in bound:
                problems.append(
                    f"{path}:{node.lineno}: name '{node.id}' is not defined")

        # ctx.<method>(...) against the real signature
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if not isinstance(func, ast.Attribute) or \
                not isinstance(func.value, ast.Name) or func.value.id != "ctx":
            continue
        signature = methods.get(func.attr)
        if signature is None:
            problems.append(
                f"{path}:{node.lineno}: ctx has no method '{func.attr}'")
            continue
        parameters = signature.parameters
        accepts_kwargs = any(p.kind == p.VAR_KEYWORD
                             for p in parameters.values())
        for keyword in node.keywords:
            if keyword.arg is None:
                continue
            if keyword.arg not in parameters and not accepts_kwargs:
                problems.append(
                    f"{path}:{node.lineno}: ctx.{func.attr}() has no keyword "
                    f"'{keyword.arg}' (accepts: "
                    f"{', '.join(list(parameters)[1:]) or 'none'})")
        positional = len([a for a in node.args
                          if not isinstance(a, ast.Starred)])
        slots = [p for p in list(parameters.values())[1:]
                 if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)]
        has_varargs = any(p.kind == p.VAR_POSITIONAL
                          for p in parameters.values())
        if positional > len(slots) and not has_varargs:
            problems.append(
                f"{path}:{node.lineno}: ctx.{func.attr}() takes at most "
                f"{len(slots)} positional arguments, {positional} given")
    return problems


def audit_pattern_table(path: str) -> List[str]:
    """Pattern-table sanity: every builder must exist and must actually return
    its effect (a builder ending without `return effect` silently binds
    nothing, which looks identical to "no card uses this wording")."""
    problems: List[str] = []
    tree = ast.parse(open(path, encoding="utf-8").read(), filename=path)
    builders = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            builders[node.name] = node
    table = None
    for node in tree.body:
        if isinstance(node, ast.Assign) and \
                any(getattr(t, "id", "") == "_PATTERNS" for t in node.targets):
            table = node.value
        elif isinstance(node, ast.AnnAssign) and \
                getattr(node.target, "id", "") == "_PATTERNS":
            table = node.value
    if table is None:
        return [f"{path}: no _PATTERNS table found"]
    seen = set()
    for element in getattr(table, "elts", []):
        if not isinstance(element, ast.Tuple) or len(element.elts) != 3:
            continue
        name_node, _, builder_node = element.elts
        name = getattr(name_node, "value", None)
        if name in seen:
            problems.append(f"{path}: duplicate pattern name '{name}'")
        seen.add(name)
        builder = getattr(builder_node, "id", None)
        if builder not in builders:
            problems.append(f"{path}: pattern '{name}' uses unknown builder "
                            f"'{builder}'")
            continue
        body = builders[builder].body
        if not body or not isinstance(body[-1], ast.Return):
            problems.append(f"{path}: builder '{builder}' (pattern '{name}') "
                            f"never returns its effect")
    return problems


def main():
    paths = sys.argv[1:] or DEFAULT_PATHS
    methods = effect_context_methods()
    total: List[str] = []
    if not sys.argv[1:]:
        total.extend(audit_pattern_table("ptcgo/game/card_effects/patterns.py"))
    for path in paths:
        try:
            total.extend(audit(path, methods))
        except FileNotFoundError:
            print(f"skip (missing): {path}")
    for problem in total:
        print(problem)
    print(f"\n{len(total)} effect-API problems across {len(paths)} modules")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
