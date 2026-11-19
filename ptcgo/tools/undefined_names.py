"""Find names a module uses but never binds -- the `NameError` at play time that
the loader, the GUID gate, the fingerprint and smoke all pass.

One lane shipped `evolve_from_deck` calling `isinstance(x, PokemonEntity)` with no
import; every card that reached it raised at play time and nothing reported it. A
wired card that raises is worse than a stub, so this is a gate, not a review.

    PYTHONPATH=. venv/bin/python -m ptcgo.tools.undefined_names
    PYTHONPATH=. venv/bin/python -m ptcgo.tools.undefined_names --path ptcgo/game · --quiet

How it decides: the module's symbol table is walked scope by scope. A symbol that
is REFERENCED and GLOBAL in some scope must be bound at module level (import,
def, class, assignment) or be a builtin; anything else raises when that line
runs. A `from x import *` in the module makes the answer unknowable and is
reported rather than guessed.
"""
import argparse
import builtins
import os
import symtable
import sys

# Names the interpreter binds in every module.
MODULE_DUNDERS = {"__file__", "__name__", "__doc__", "__package__", "__path__",
                  "__spec__", "__loader__", "__builtins__"}
BUILTINS = set(dir(builtins)) | MODULE_DUNDERS
SKIP_DIRS = {"__pycache__", ".git", "venv", "node_modules"}


def module_bindings(table) -> set:
    """Names the MODULE scope binds: imports, defs, classes, assignments."""
    bound = set()
    for symbol in table.get_symbols():
        if symbol.is_assigned() or symbol.is_imported() or symbol.is_namespace():
            bound.add(symbol.get_name())
    return bound


def star_imports(source: str) -> bool:
    return any(line.strip().startswith("from ") and line.strip().endswith("import *")
               for line in source.splitlines())


def missing_names(path: str):
    """(name, scope) pairs the module references and never binds."""
    source = open(path, encoding="utf-8").read()
    if star_imports(source):
        return None
    try:
        table = symtable.symtable(source, path, "exec")
    except SyntaxError as exc:
        return [("<syntax error>", str(exc))]
    bound = module_bindings(table)
    missing = []

    def walk(scope):
        for symbol in scope.get_symbols():
            name = symbol.get_name()
            if symbol.is_global() and symbol.is_referenced() \
                    and name not in bound and name not in BUILTINS:
                missing.append((name, scope.get_name()))
        for child in scope.get_children():
            walk(child)

    walk(table)
    return missing


def iter_files(root: str):
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in sorted(files):
            if name.endswith(".py"):
                yield os.path.join(dirpath, name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", action="append",
                        default=["ptcgo/game", "ptcgo/tools"],
                        help="roots to sweep (repeatable)")
    parser.add_argument("--quiet", action="store_true",
                        help="print only the count and offending files")
    args = parser.parse_args()

    offenders = 0
    unknown = []
    for root in args.path:
        if not os.path.isdir(root):
            continue
        for path in iter_files(root):
            result = missing_names(path)
            if result is None:
                unknown.append(path)
                continue
            if not result:
                continue
            offenders += len(result)
            print(f"\n{path}")
            seen = set()
            for name, scope in result:
                if (name, scope) in seen:
                    continue
                seen.add((name, scope))
                print(f"    {name}  (used in {scope})")

    print(f"\nundefined names: {offenders}"
          + (f"  modules with a star import (not checked): {len(unknown)}"
             if unknown else ""))
    return 1 if offenders else 0


if __name__ == "__main__":
    sys.exit(main())
