"""Wire trainer card scripts to the shared effect library.

Reads every `effect=unimplemented` trainer script, asks trainer_patterns for a
wiring, and rewrites the script so it imports the factory and passes it as
`effect=`. Scripts whose text does not match a pattern are left untouched and
keep doing nothing.

    ./venv/bin/python tools/trainer_wire.py --dry-run          # report only
    ./venv/bin/python tools/trainer_wire.py --limit 5 --dry-run
    ./venv/bin/python tools/trainer_wire.py --rule draw        # one pattern
    ./venv/bin/python tools/trainer_wire.py                    # write

The rewrite is deliberately literal: the script keeps its own def block and
only gains an import and an effect expression, so a wired script is still
reviewable as data.
"""

import argparse
import os
import re
import sys

_TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_TOOLS_DIR)
sys.path.insert(0, _TOOLS_DIR)
sys.path.insert(0, _REPO_ROOT)

import trainer_coverage as coverage
import trainer_patterns as patterns
from spirit.game.card_effects import support_common, trainers

STUB = "effect=unimplemented"
IDENTIFIER = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def symbols_in(expr):
    """Every library name an expression references, nesting included.

    Resolved against the two effect modules rather than parsed out of the
    argument list, so a predicate built inside a combinator
    (`any_of(is_pokemon_card, is_basic_energy_card)`) still imports its parts.
    """
    names = set()
    for name in IDENTIFIER.findall(expr):
        if hasattr(trainers, name) or hasattr(support_common, name):
            names.add(name)
    return names


def module_for(symbol):
    if hasattr(trainers, symbol):
        return "trainers"
    if hasattr(support_common, symbol):
        return "support_common"
    raise KeyError(f"{symbol} is not defined in the trainer effect library")


def rewrite(source, expr, symbols=None):
    """The wired script source, or None when the stub marker is missing."""
    if STUB not in source:
        return None
    symbols = symbols if symbols is not None else symbols_in(expr)
    wired = source.replace(STUB, "effect=" + expr)
    if "unimplemented" not in wired:
        wired = re.sub(r"(from spirit\.game\.data_utils import [^\n]*?), unimplemented",
                       r"\1,", wired)
        wired = re.sub(r"(from spirit\.game\.data_utils import unimplemented, )", "", wired)
    by_module = {}
    for symbol in symbols:
        by_module.setdefault(module_for(symbol), []).append(symbol)
    lines = [f"from spirit.game.card_effects.{module} import {', '.join(sorted(names))}"
             for module, names in sorted(by_module.items())]
    newline_imports = "\n".join(lines)
    # Place the effect imports right after the last spirit.game import line.
    anchors = list(re.finditer(r"^from spirit\.game\.[^\n]*\n", wired, re.M))
    if anchors:
        at = anchors[-1].end()
        wired = wired[:at] + newline_imports + "\n" + wired[at:]
    else:
        wired = newline_imports + "\n" + wired
    return wired


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--rule", help="only wire scripts whose rule id matches this regex")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args(argv)

    rule_filter = re.compile(args.rule) if args.rule else None
    scripts = coverage.collect()
    stubs = [s for s in scripts if s.is_stub]

    plan = []
    for script in stubs:
        found = patterns.resolve(script.game_text)
        if found is None:
            continue
        if rule_filter and not rule_filter.search(found["rule"]):
            continue
        plan.append((script, found))

    if args.limit:
        plan = plan[:args.limit]

    # Validate every rewrite before touching the tree: a mid-run failure must
    # not leave half the batch wired.
    rewrites = []
    skipped = []
    for script, found in plan:
        path = os.path.join(coverage.REPO_ROOT, script.path)
        with open(path, "r", encoding="utf-8") as handle:
            source = handle.read()
        wired = rewrite(source, found["expr"])
        if wired is None:
            skipped.append((script.path, "no stub marker"))
            continue
        rewrites.append((script, found, path, wired))

    written = 0
    for script, found, path, wired in rewrites:
        if args.verbose or args.dry_run:
            print(f"{script.path}\n    {found['rule']}: effect={found['expr']}")
        if not args.dry_run:
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(wired)
            written += 1

    print(f"\n{'would wire' if args.dry_run else 'wired'}: {len(rewrites)}"
          f" of {len(stubs)} stubs")
    if skipped:
        print(f"skipped: {len(skipped)}")
        for path, why in skipped[:10]:
            print(f"  {path}: {why}")
    return 0 if not skipped else 1


if __name__ == "__main__":
    sys.exit(main())
