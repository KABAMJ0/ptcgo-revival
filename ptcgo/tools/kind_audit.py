"""Flag bodies whose kind of effect the card's own text never names.

The Captain's rule (2026-11-19): never install a body whose kind is not the kind the
printed text names -- a damage body on a heal clause is worse than a stub, because
`unimplemented` is visible in every count while a wrong-kind body is invisible to the
loader, the GUID gate, the fingerprint and smoke alike.

For each Attack/Ability block with a real body and printed text, this reads the intent
verbs out of the text, then looks for a matching signal in the body (its effect
expression plus any helper it calls in the same file). A block is reported when the
text names an action the body has no trace of and the body is nothing but damage.

Usage:
  python -m ptcgo.tools.kind_audit [--files LIST] [--filled] [--all]
"""
import argparse
import ast
import os
import re
import subprocess
import sys
from typing import Dict, List, Optional, Tuple

CARDS_ROOT = os.path.join("ptcgo", "game", "scripts", "cards")

# intent -> patterns in the printed text
INTENTS: List[Tuple[str, str]] = [
    ("heal", r"heal \d+ damage|heal all damage|remove \d+ damage counter|heal \d+"),
    ("draw", r"\bdraw (\d+|a|up to) card|\bdraw \d+|\bdraw a card|draw cards"),
    ("search", r"search your deck|search (his or her|their|your opponent's) deck"),
    ("mill", r"discard the top|from the top of .{0,20}deck|put the top \d+ cards"),
    ("discard", r"discard (a|an|all|up to|\d+) .{0,30}(card|energy)"),
    ("counters", r"put \d+ damage counter"),
    ("condition", r"(is )?now (asleep|confused|paralyzed|poisoned|burned)"),
    ("protect", r"prevent all damage|isn't affected by|is not affected by|no effect on"),
    ("attach", r"\battach\b"),
    ("switch", r"switch .{0,40}(active|benched)|\bretreat"),
    ("shuffle", r"shuffle"),
    ("prize", r"take \d+ (more )?prize"),
    ("look", r"look at the top \d+|look at (the top|your)"),
]

# intent -> signal patterns in the body source
SIGNALS: Dict[str, str] = {
    "heal": r"heal|remove_damage|cure",
    "draw": r"draw",
    "search": r"search",
    "mill": r"mill|discard_from_top|deck_top|top_card",
    "discard": r"discard",
    "counters": r"counter",
    "condition": r"condition|asleep|confused|paralyzed|poisoned|burned",
    "protect": r"prevent|protect|shield|ignore_modifier|no_weakness|unafflicted",
    "attach": r"attach",
    "switch": r"switch|gust|retreat",
    # a search helper shuffles as part of putting the card in hand, so the
    # "shuffle your deck" rider needs no separate signal
    "shuffle": r"shuffle|search",
    "prize": r"prize",
    "look": r"look|peek|top_card|reorder",
}

PURE_DAMAGE = {"damage_per", "flip_damage", "bonus_if", "flip_gate", "damage_if",
               "damage_per_extra_energy", "damage_per_energy", "deal_damage"}

# Kinds that cannot be what the other kinds' wording asks for: a body that only
# discards Energy is not a "does 20 damage to each benched Pokemon" attack, and a
# body that only confuses is not a "draw 3 cards" attack. Used to catch the shape
# the pure-damage rule misses -- an effect body on the wrong block of the same card.
CONFLICTING = {"discard", "attach", "heal", "draw", "mill", "counters", "switch", "protect"}


def card_files() -> List[str]:
    out = []
    for code in sorted(os.listdir(CARDS_ROOT)):
        folder = os.path.join(CARDS_ROOT, code)
        if not os.path.isdir(folder) or code == "__pycache__":
            continue
        for name in sorted(os.listdir(folder)):
            if name.endswith(".py") and name != "__init__.py":
                out.append(os.path.join(folder, name))
    return out


def helper_source(tree, name: str, src: str) -> str:
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
            return ast.get_source_segment(src, node) or ""
    return ""


def body_source(tree, expression, src: str) -> str:
    """The effect expression plus any helper it names, from the same file."""
    text = ast.unparse(expression)
    names = {n.id for n in ast.walk(expression) if isinstance(n, ast.Name)}
    for name in sorted(names):
        text += "\n" + helper_source(tree, name, src)
    return text


def audit_file(path: str) -> List[str]:
    src = open(path, encoding="utf-8").read()
    tree = ast.parse(src, path)
    findings = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or getattr(node.func, "id", "") not in ("Attack", "Ability"):
            continue
        kw = {k.arg: k.value for k in node.keywords}
        effect = kw.get("effect", kw.get("passive"))
        if effect is None or ast.unparse(effect) in ("unimplemented", "None"):
            continue
        text = kw.get("game_text")
        try:
            printed = ast.literal_eval(text) if text is not None else ""
        except (ValueError, SyntaxError):
            continue
        if not printed:
            continue
        title = ast.literal_eval(kw["title"]) if "title" in kw else "?"
        body = body_source(tree, effect, src)
        primary = getattr(getattr(effect, "func", None), "id", "") if isinstance(effect, ast.Call) else ""
        missing = []
        for intent, pattern in INTENTS:
            if not re.search(pattern, printed, re.I):
                continue
            if not re.search(SIGNALS[intent], body, re.I):
                missing.append(intent)
        named = [intent for intent, pattern in INTENTS if re.search(pattern, printed, re.I)]
        shown = [intent for intent in named if re.search(SIGNALS[intent], body, re.I)]
        if missing and primary in PURE_DAMAGE:
            findings.append(
                f"{path}: {title!r} -- text names {', '.join(missing)}; "
                f"body is {primary}(...) | {printed[:90]}")
        elif named and not shown and set(named) & CONFLICTING:
            findings.append(
                f"{path}: {title!r} -- text names {', '.join(named)}; body shows "
                f"{', '.join(sorted(i for i in CONFLICTING if re.search(SIGNALS[i], body, re.I)))}"
                f" | {printed[:90]}")
    return findings


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m ptcgo.tools.kind_audit",
                                     description="Report bodies whose kind the printed text never names.")
    parser.add_argument("--files", help="File listing card scripts to audit, one path per line.")
    parser.add_argument("--filled", action="store_true",
                        help="Audit the card scripts this branch changed against the merge base.")
    parser.add_argument("--all", action="store_true", help="Audit every card script in the tree.")
    args = parser.parse_args(argv)
    if args.filled:
        base = subprocess.run(["git", "merge-base", "HEAD", "main"], capture_output=True,
                              text=True).stdout.strip() or "main"
        changed = subprocess.run(["git", "diff", "--name-only", base, "HEAD", "--", CARDS_ROOT],
                                 capture_output=True, text=True).stdout.split()
        paths = [p for p in changed if os.path.exists(p)]
    elif args.files:
        paths = [line.strip() for line in open(args.files, encoding="utf-8") if line.strip()]
    elif args.all:
        paths = card_files()
    else:
        parser.error("give --files LIST, --filled or --all")
    findings: List[str] = []
    for path in paths:
        try:
            findings += audit_file(path)
        except SyntaxError as exc:
            print(f"UNPARSED {path}: {exc}")
    for line in findings:
        print(line)
    print(f"\n{len(findings)} wrong-kind bodies over {len(paths)} scripts")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
