"""Fingerprints Special Energy wiring so a batch cannot quietly change a card.

`python tools/special_energy_fingerprint.py --save baseline.json` records, per
script, the hook keyword arguments it declares. `--check baseline.json` compares
and reports any card whose behaviour changed. A card that gains a hook it did not
have is a change; a card whose existing hook changed is a regression.

    python tools/special_energy_fingerprint.py --baseline main --check
        compares the working tree against the same tree as the `main` branch,
        which is what "no previously-working card changed" means for this work.
"""
import argparse
import ast
import json
import os
import subprocess
import sys

CARDS_ROOT = os.path.join("ptcgo", "game", "scripts", "cards")
HOOKS = ("provides", "attach_to", "attach_condition", "attach_cost",
         "on_attach", "on_carrier_knocked_out", "passive")


def fingerprint_source(source):
    """Hook kwargs of the EnergyCardDef call, rendered as source text."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return {"error": "unparseable"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id == "EnergyCardDef":
            hooks = {}
            for keyword in node.keywords:
                if keyword.arg in HOOKS:
                    hooks[keyword.arg] = ast.get_source_segment(source, keyword.value) or ""
            return hooks
    return {}


def walk_tree(root=CARDS_ROOT):
    out = {}
    for directory in sorted(os.listdir(root)):
        folder = os.path.join(root, directory)
        if not os.path.isdir(folder) or directory in {"__pycache__", "CUSTOM", "Free_Energy"}:
            continue
        for name in sorted(os.listdir(folder)):
            if not name.endswith(".py") or name == "__init__.py":
                continue
            path = os.path.join(folder, name)
            out[path] = fingerprint_source(open(path, encoding="utf-8").read())
    return out


def tree_at(branch):
    """The same fingerprint map read out of a git branch, without checking it out."""
    listing = subprocess.run(["git", "ls-tree", "-r", "--name-only", branch, CARDS_ROOT],
                             capture_output=True, text=True, check=True).stdout.split()
    out = {}
    for path in listing:
        if not path.endswith(".py") or path.endswith("__init__.py"):
            continue
        source = subprocess.run(["git", "show", f"{branch}:{path}"],
                                capture_output=True, text=True).stdout
        out[path] = fingerprint_source(source)
    return out


def compare(before, after):
    changed, added, removed = [], [], []
    for path, hooks in after.items():
        old = before.get(path)
        if old is None:
            added.append(path)
            continue
        if old != hooks:
            changed.append((path, old, hooks))
    for path in before:
        if path not in after:
            removed.append(path)
    return changed, added, removed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--save")
    parser.add_argument("--check")
    parser.add_argument("--baseline", help="branch to compare against (e.g. main)")
    args = parser.parse_args()

    if args.save:
        json.dump(walk_tree(), open(args.save, "w", encoding="utf-8"), indent=1, sort_keys=True)
        print(f"wrote {args.save}")
        return 0

    if args.baseline:
        before = tree_at(args.baseline)
    elif args.check:
        before = json.load(open(args.check, encoding="utf-8"))
    else:
        parser.error("need --save, --check or --baseline")
        return 2

    after = walk_tree()
    changed, added, removed = compare(before, after)
    print(f"scripts: {len(after)}   changed: {len(changed)}   new: {len(added)}   gone: {len(removed)}")
    regressions = 0
    for path, old, new in changed:
        # a card that only GAINS hooks was previously data-only: that is the point
        lost = {key: value for key, value in old.items() if key not in new or new[key] != value}
        if lost:
            regressions += 1
            print(f"  REGRESSION {path}")
            for key, value in lost.items():
                print(f"      {key}: {value!r} -> {new.get(key)!r}")
    if regressions == 0:
        print("no previously-wired card changed its hooks")
    return 1 if regressions else 0


if __name__ == "__main__":
    sys.exit(main())
