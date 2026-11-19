"""Fill our own stubs from our own wired cards.

Two passes over `ptcgo/game/scripts/cards`, reference and target both inside our
tree (unlike `reuse_effects`, which is per-set and mostly used to import a new
set):

1. whole card: a stub whose gameplay signature equals an implemented card's
   (class, name, stats, every attack/ability title+text+cost+damage, trainer
   text) is replaced by that card's script, keeping the stub's identity fields
   and its GUID.
2. identical text: a stub Attack/Ability whose normalized `game_text` equals an
   implemented one takes that call's effect keywords plus the imports and helpers
   they need, on a copy.

A text match whose source hard-codes its own printed damage (and this card prints
a different one) is skipped as a damage mismatch.

`effect`/`passive` bodies are copied, never written: a card-level
`effect=unimplemented` stub carries no printed text in our tree, so it cannot be
matched this way and is reported as unreachable.

Usage:
  python -m ptcgo.tools.reprint_filler --dry-run [--report report.txt]
  python -m ptcgo.tools.reprint_filler --apply [--only SM1,SM2] [--loose]
                                       [--same-set] [--allow-mismatch]
"""
import argparse
import ast
import builtins
import dis
import os
import sys
import types
from typing import Dict, List, Optional, Tuple

from ptcgo.tools.reuse_effects import (CARDS_ROOT, Script, Transplant, _ability_calls,
                                      _int_literals, _is_unimpl, _lit, _rank, all_scripts,
                                      apply_transplants, copy_whole_card, loose_norm, norm)


def set_folders() -> List[str]:
    return sorted(d for d in os.listdir(CARDS_ROOT)
                  if os.path.isdir(os.path.join(CARDS_ROOT, d)) and d != "__pycache__")


def load_targets(only: Optional[List[str]]) -> List[Script]:
    broken = []
    stubs: List[Script] = []
    for code in set_folders():
        if only and code not in only:
            continue
        folder = os.path.join(CARDS_ROOT, code)
        for name in sorted(os.listdir(folder)):
            if not name.endswith(".py") or name == "__init__.py":
                continue
            try:
                script = Script(os.path.join(folder, name))
            except (SyntaxError, UnicodeDecodeError) as exc:
                broken.append(f"{code}/{name}: {exc}")
                continue
            if script.card is not None and not script.implemented():
                stubs.append(script)
    for line in broken:
        print(f"UNPARSED {line}")
    return stubs


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m ptcgo.tools.reprint_filler",
        description="Fill stubs of ptcgo/game/scripts/cards from our own wired cards "
                    "(whole-card reprints, then identical attack/ability text).")
    parser.add_argument("--apply", action="store_true", help="Write the files (default: dry run).")
    parser.add_argument("--dry-run", action="store_true", help="Report only (the default).")
    parser.add_argument("--only", default="", help="Comma-separated set folders to fill.")
    parser.add_argument("--loose", action="store_true", help="Also match across era wording changes.")
    parser.add_argument("--same-set", action="store_true",
                        help="Allow a reference from the stub's own set folder (off by default, "
                             "as in reuse_effects).")
    parser.add_argument("--allow-mismatch", action="store_true",
                        help="Fill text matches even when the source hard-codes a different damage.")
    parser.add_argument("--report", help="Write every matching pair to this file.")
    args = parser.parse_args(argv)
    only = [s for s in args.only.split(",") if s]
    if args.apply and args.dry_run:
        parser.error("--apply and --dry-run are exclusive")

    stubs = load_targets(only or None)
    refs = [s for s in all_scripts("__none__") if s.card is not None]
    print(f"{len(refs)} scripts as reference, {len(stubs)} stubs to fill", flush=True)

    by_sig: Dict[tuple, List[Script]] = {}
    for ref in refs:
        if ref.implemented():
            sig = ref.signature()
            if sig:
                by_sig.setdefault(sig, []).append(ref)
    exact: Dict[str, List[Tuple[Script, object]]] = {}
    loose: Dict[str, List[Tuple[Script, object]]] = {}
    for ref in refs:
        for call in _ability_calls(ref.tree):
            kw = {k.arg: k.value for k in call.keywords}
            effect = kw.get("effect", kw.get("passive"))
            if effect is None or _is_unimpl(effect) or "game_text" not in kw:
                continue
            text = _lit(kw["game_text"])
            if not text:
                continue
            exact.setdefault(norm(text), []).append((ref, call))
            if args.loose:
                loose.setdefault(loose_norm(text), []).append((ref, call))

    pairs: List[str] = []
    refused: List[str] = []
    whole = text_hits = mismatches = misses = 0
    per_set: Dict[str, List[int]] = {}

    def bump(code, index):
        row = per_set.setdefault(code, [0, 0])
        row[index] += 1

    remaining = []
    for stub in stubs:
        rank = _rank([code_prefix(stub.set_code)])
        cands = [r for r in by_sig.get(stub.signature(), [])
                 if args.same_set or r.set_code != stub.set_code]
        if not cands:
            remaining.append(stub)
            continue
        ref = sorted(cands, key=rank)[0]
        whole += 1
        bump(stub.set_code, 0)
        pairs.append(f"CARD     {stub.set_code}/{stub.stem} <- {ref.set_code}/{ref.stem}")
        if args.apply:
            new_src = copy_whole_card(stub, ref)
            bad = undefined_names(new_src, stub.path) or use_before_bind(new_src, stub.path)
            if bad:
                refused.append(f"REFUSED  {stub.set_code}/{stub.stem} <- {ref.set_code}/{ref.stem}: "
                               f"undefined {', '.join(bad)}")
            else:
                with open(stub.path, "w", encoding="utf-8") as fh:
                    fh.write(new_src)

    for stub in remaining:
        rank = _rank([code_prefix(stub.set_code)])
        plans = []
        for call in _ability_calls(stub.tree):
            kw = {k.arg: k for k in call.keywords}
            if "effect" not in kw or not _is_unimpl(kw["effect"].value):
                continue
            title = _lit(kw["title"].value, "?")
            text = _lit(kw.get("game_text").value if "game_text" in kw else None, "")
            kind = getattr(call.func, "id", None)
            candidates = [(r, c) for r, c in exact.get(norm(text), [])
                          if (args.same_set or r.set_code != stub.set_code)
                          and getattr(c.func, "id", None) == kind]
            tag = ""
            if not candidates and args.loose:
                candidates = [(r, c) for r, c in loose.get(loose_norm(text), [])
                              if (args.same_set or r.set_code != stub.set_code)
                              and getattr(c.func, "id", None) == kind]
                tag = " LOOSE"
            if not candidates:
                misses += 1
                continue
            ref, ref_call = sorted(candidates, key=lambda rc: rank(rc[0]))[0]
            plan = Transplant(ref, ref_call)
            if any(_is_unimpl(k.value) for k in plan.extra):
                misses += 1
                continue
            mine = _lit(kw["damage"].value, 0) if "damage" in kw else 0
            if mine != plan.damage and not args.allow_mismatch:
                unexplained = unexplained_literals(plan, text)
                if unexplained or plan.hardcodes_damage(text):
                    mismatches += 1
                    pairs.append(f"MISMATCH {stub.set_code}/{stub.stem} | {title} | "
                                 f"{ref.set_code}/{ref.stem} prints {plan.damage}, this card "
                                 f"prints {mine}; copied body carries "
                                 f"{unexplained or [plan.damage]}")
                    continue
            plans.append((kw["effect"], plan))
            text_hits += 1
            bump(stub.set_code, 1)
            pairs.append(f"TEXT     {stub.set_code}/{stub.stem} | {title} <- "
                         f"{ref.set_code}/{ref.stem}{tag} | {norm(text)[:60]}")
        if plans and args.apply:
            new_src = apply_transplants(stub, plans)
            bad = undefined_names(new_src, stub.path) or use_before_bind(new_src, stub.path)
            if bad:
                refused.append(f"REFUSED  {stub.set_code}/{stub.stem}: undefined {', '.join(bad)}")
            else:
                with open(stub.path, "w", encoding="utf-8") as fh:
                    fh.write(new_src)

    mode = "applied" if args.apply else "dry run"
    print(f"\n{mode}: {whole} whole-card reprints, {text_hits} identical-text entries, "
          f"{mismatches} damage mismatches skipped, {misses} unmatched entries")
    for line in refused:
        print(line)
    print(f"refused: {len(refused)}")
    print(f"files touched: {sum(1 for c, r in per_set.items() if r[0] or r[1])} set folders")
    for code in sorted(per_set):
        print(f"  {code:12s} cards={per_set[code][0]:4d} entries={per_set[code][1]:4d}")
    if args.report:
        with open(args.report, "w", encoding="utf-8") as fh:
            fh.write("\n".join(pairs + refused) + "\n")
        print(f"pairs written to {args.report}")
    return 0


def unexplained_literals(plan: Transplant, text: str) -> List[int]:
    """Numbers the copied body carries that this card's printed text never mentions.

    When two cards share a wording but print different damage, the source's body
    usually hard-codes its own number as `base=`. If any integer in the copied code
    is not a number from the shared wording, the fill would silently deal the other
    card's damage (XY8/Xerneas_107 put `base=70` into two 50-damage Toxtricity),
    so it is refused.
    """
    literals = set()
    for keyword in plan.extra:
        literals |= _int_literals(keyword.value)
    for code in plan.defs.values():
        literals |= _int_literals(ast.parse(code))
    printed = {int(n) for n in __import__("re").findall(r"\d+", text or "")}
    return sorted(literals - printed)


def undefined_names(src: str, path: str) -> List[str]:
    """Global names a generated script loads but never binds.

    A copied effect can reference a helper the transplant did not carry; that
    imports fine and fails at load with NameError, so a fill is only written when
    this comes back empty.
    """
    tree = ast.parse(src, path)
    bound = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            bound.add(node.name)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            bound |= {a.asname or a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    bound.add(target.id)
                elif isinstance(target, ast.Tuple):
                    bound |= {e.id for e in target.elts if isinstance(e, ast.Name)}
    missing = set()
    stack = [compile(src, path, "exec")]
    while stack:
        code = stack.pop()
        stack += [c for c in code.co_consts if isinstance(c, types.CodeType)]
        for ins in dis.get_instructions(code):
            if ins.opname in ("LOAD_GLOBAL", "LOAD_NAME") \
                    and ins.argval not in bound and not hasattr(builtins, ins.argval):
                missing.add(ins.argval)
    return sorted(missing)


def _immediate_loads(node) -> set:
    """Names an expression loads right away: function and lambda bodies are skipped."""
    loads = set()

    class Visitor(ast.NodeVisitor):
        def visit_Name(self, child):
            if isinstance(child.ctx, ast.Load):
                loads.add(child.id)

        def _enter(self, child):
            for default in child.args.defaults:
                self.visit(default)
            for default in child.args.kw_defaults:
                if default is not None:
                    self.visit(default)
            for dec in getattr(child, "decorator_list", []):
                self.visit(dec)

        def visit_Lambda(self, child):
            self._enter(child)

        def visit_FunctionDef(self, child):
            self._enter(child)

        def visit_AsyncFunctionDef(self, child):
            self._enter(child)

    Visitor().visit(node)
    return loads


def use_before_bind(src: str, path: str) -> List[str]:
    """Module-level names an expression loads before anything binds them.

    A copied helper that is only bound further down the file still imports
    cleanly and then raises NameError at load (found on SM11/Sableye's granted
    ability), so ordering is checked, not just presence.
    """
    tree = ast.parse(src, path)
    bound, problems = set(), []
    for node in tree.body:
        binds, loads = set(), set()
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            binds = {node.name}
            for sub in list(node.decorator_list) + list(getattr(node, "bases", [])):
                loads |= _immediate_loads(sub)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                for default in list(node.args.defaults) + list(node.args.kw_defaults):
                    if default is not None:
                        loads |= _immediate_loads(default)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            binds = {a.asname or a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    binds.add(target.id)
                elif isinstance(target, ast.Tuple):
                    binds |= {e.id for e in target.elts if isinstance(e, ast.Name)}
            loads = _immediate_loads(node.value)
        else:
            loads = _immediate_loads(node)
        early = sorted(n for n in loads if n not in bound and not hasattr(builtins, n))
        if early:
            problems.append(f"line {node.lineno}: {', '.join(early)}")
        bound |= binds
    return problems


def code_prefix(code: str) -> str:
    prefix = "".join(c for c in code if c.isalpha())
    return prefix or code


if __name__ == "__main__":
    sys.exit(main())
