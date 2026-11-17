"""Trainer effect coverage: audit `effect=unimplemented` trainer card scripts.

Parses scripts with `ast` (never imports them: importing a card script
registers definitions as a side effect) and joins each card to its printed
rules text from the set JSON next to it, so stubs can be grouped by the text
they are supposed to implement instead of by set or card name.

    ./venv/bin/python tools/trainer_coverage.py                 # summary + top groups
    ./venv/bin/python tools/trainer_coverage.py --top 60
    ./venv/bin/python tools/trainer_coverage.py --json out.json # full work-item list
    ./venv/bin/python tools/trainer_coverage.py --grep switch   # inspect one family
"""

import argparse
import ast
import json
import os
import re
import sys
from collections import Counter, defaultdict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS_ROOT = os.path.join(REPO_ROOT, "spirit", "game", "scripts", "cards")
SKIP_DIRS = {"__pycache__"}

TRAINER_CLASSES = {
    "ItemCardDef", "SupporterCardDef", "StadiumCardDef",
    "PokemonToolCardDef", "FossilItemCardDef", "TrainerCardDef",
}

# Reminder text carried by every card of a class; it says nothing about the
# effect and would otherwise split identical effects into separate groups.
# Matched per SENTENCE (search, not full match) because the legacy printings
# wire it into the same paragraph as the effect.
REMINDER_PATTERNS = [re.compile(p) for p in (
    r"^you may play as many item cards as you like during your turn ?(\(before your attack\))?\.?$",
    r"^you may play only (1|one) supporter card during your turn ?(\(before your attack\))?\.?$",
    r"^you can play only one supporter card each turn\.$",
    r"^when you play this card, put it next to your active pokemon\.$",
    r"^when your turn ends, discard this card\.$",
    r"^you may play only (1|one) stadium card during your turn ?(\(before your attack\))?\.?$",
    r"^this card stays in play when you play it\.?$",
    r"^discard this card if another stadium card comes into play\.?$",
    r"^attach a pokemon tool to (1|one) of your pokemon that doesn'?t already have a pokemon tool attached( to it)?\.?$",
    r"^you may attach any number of pokemon tools? to your pokemon during your turn\.?$",
    r"^you may attach only (1|one) pokemon tool to each pokemon, and it stays attached\.?$",
    r"^\(pokemon ex, pokemon v[a-z_]*, etc\. have rule boxes\.\)$",
    r"^\(you still need the necessary energy to use this attack\.\)$",
    r"^\(before your attack\)$",
    r"^you may play any number of item cards during your turn\.?$",
    r"^you may play only 1 supporter card during your turn\.?$",
    r"^you may play only 1 stadium card during your turn\.?$",
    r"^put it next to the active spot,? and discard it if another stadium comes into play\.?$",
    r"^a stadium with the same name can'?t be played\.?$",
    r"^attach a pokemon tool to 1 of your pokemon that doesn'?t already have a pokemon tool attached\.?$",
)]

NUMBER_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
}

# Frequency families, checked in order against the normalized text. These are
# labels for the report and for choosing what to implement first.
FAMILIES = [
    ("gust", r"switch in .{0,40}opponent'?s benched|opponent'?s benched .{0,20}to the active"),
    ("draw", r"\bdraw\b"),
    ("search-hand", r"search your deck"),
    ("shuffle-hand-draw", r"shuffle your hand into your deck"),
    ("look-top", r"look at the top"),
    ("recover-discard", r"discard pile"),
    ("discard", r"discard"),
    ("energy-accel", r"attach .{0,40}energy"),
    ("switch-self", r"switch your active pokemon"),
    ("heal", r"heal|damage counter"),
    ("damage-mod", r"(more|less) damage"),
    ("status-condition", r"asleep|paralyzed|confused|burned|poisoned"),
    ("coin-flip", r"flip a coin|flip [0-9#]"),
    ("prizes", r"prize card"),
    ("lost-zone", r"lost zone"),
    ("tool-passive", r"this card is attached|the pokemon this card is attached to"),
    ("stadium", r"each pokemon in play|once during each player'?s turn|retreat cost"),
    ("lock", r"can'?t (play|use|attack|retreat)"),
    ("ability", r"abilit"),
]


def _sentences(text: str):
    """Split effect text into sentences on '. ' / ' ' after a period, keeping
    a trailing sentence without its terminator."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p]


def canonical_text(rules) -> str:
    """The card's effect text with class reminder sentences removed, number
    words turned into digits, and whitespace/unicode normalized. Number words
    become digits so a template can capture "draw 3" and "draw two" alike."""
    PARENTHETICAL = re.compile(
        r"\s*\((?:pokemon ex, pokemon v[^)]*|you still need[^)]*|before your attack)\)",
        re.I)
    kept = []
    for line in (PARENTHETICAL.sub("", r) for r in (rules or [])):
        for sentence in _sentences(line):
            probe = re.sub(r"\s+", " ", sentence).strip().lower()
            probe = probe.replace("\u2019", "'").replace("\u00e9", "e")
            if any(p.match(probe) for p in REMINDER_PATTERNS):
                continue
            kept.append(sentence.strip())
    text = " ".join(kept)
    text = text.replace("\u2019", "'").replace("\u2018", "'") \
               .replace("\u201c", '"').replace("\u201d", '"') \
               .replace("\u2014", "-").replace("\u2013", "-") \
               .replace("\u00e9", "e").replace("\u00d7", "x")
    text = text.lower()
    def _num(match):
        return str(NUMBER_WORDS.get(match.group(1), match.group(1)))
    text = re.sub(r"\b(%s)\b" % "|".join(NUMBER_WORDS), _num, text)
    text = re.sub(r"\b(an?)\b", "1", text)
    # Patterns are written without punctuation, so the canonical text drops
    # every non-alphanumeric character (quotes included: "opponent's" becomes
    # "opponents"). Cards whose wording differs by a clause still differ.
    # Apostrophes vanish rather than split a word: "opponent's" is
    # "opponents", "doesn't" is "doesnt", "it's" is "its".
    text = text.replace("'", "")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_text(text: str) -> str:
    """Grouping signature: the canonical text with every number masked."""
    text = re.sub(r"\d+", "#", text)
    return re.sub(r"\s+", " ", text).strip()


def family_of(signature: str) -> str:
    for name, pattern in FAMILIES:
        if re.search(pattern, signature):
            return name
    return "other"


class CardScript:
    __slots__ = ("path", "set_code", "display_name", "number", "card_class",
                 "effect_name", "game_text")

    def __init__(self, path, set_code, display_name, number, card_class,
                 effect_name, game_text):
        self.path = path
        self.set_code = set_code
        self.display_name = display_name
        self.number = number
        self.card_class = card_class
        self.effect_name = effect_name
        self.game_text = game_text

    @property
    def is_stub(self):
        return self.effect_name == "unimplemented"


def _call_name(node):
    if isinstance(node, ast.Call):
        fn = node.func
        if isinstance(fn, ast.Name):
            return fn.id
        if isinstance(fn, ast.Attribute):
            return fn.attr
    return None


def _kwarg(call, name):
    for kw in call.keywords:
        if kw.arg == name:
            return kw.value
    return None


def _const(node, default=None):
    if node is None:
        return default
    if isinstance(node, ast.Constant):
        return node.value
    return default


def parse_script(path):
    try:
        with open(path, "r", encoding="utf-8") as handle:
            tree = ast.parse(handle.read(), filename=path)
    except (SyntaxError, UnicodeDecodeError):
        return None
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = _call_name(node)
        if name not in TRAINER_CLASSES:
            continue
        effect = _kwarg(node, "effect")
        effect_name = effect.id if isinstance(effect, ast.Name) else None
        return CardScript(
            path=os.path.relpath(path, REPO_ROOT),
            set_code=_const(_kwarg(node, "set_code")),
            display_name=_const(_kwarg(node, "display_name")),
            number=_const(_kwarg(node, "collector_number")),
            card_class=name,
            effect_name=effect_name,
            game_text=_const(_kwarg(node, "game_text"), ""),
        )
    return None


_SET_JSON_CACHE = {}


def rules_by_number(set_dir):
    """collector_number -> rules lines, from the set's card JSON."""
    if set_dir in _SET_JSON_CACHE:
        return _SET_JSON_CACHE[set_dir]
    table = {}
    try:
        entries = sorted(os.listdir(set_dir))
    except OSError:
        entries = []
    for entry in entries:
        if not entry.endswith(".json") or entry.endswith(".json.bak"):
            continue
        try:
            with open(os.path.join(set_dir, entry), "r", encoding="utf-8") as handle:
                cards = json.load(handle)
        except (OSError, ValueError):
            continue
        if not isinstance(cards, list):
            continue
        for card in cards:
            if not isinstance(card, dict):
                continue
            rules = card.get("rules")
            if not rules:
                continue
            try:
                number = int(card.get("number"))
            except (TypeError, ValueError):
                continue
            table.setdefault(number, rules)
    _SET_JSON_CACHE[set_dir] = table
    return table


def collect():
    scripts = []
    for set_code in sorted(os.listdir(CARDS_ROOT)):
        set_dir = os.path.join(CARDS_ROOT, set_code)
        if set_code in SKIP_DIRS or not os.path.isdir(set_dir):
            continue
        rules_table = rules_by_number(set_dir)
        for entry in sorted(os.listdir(set_dir)):
            if not entry.endswith(".py") or entry.startswith("__"):
                continue
            script = parse_script(os.path.join(set_dir, entry))
            if script is None:
                continue
            rules = rules_table.get(script.number) if isinstance(script.number, int) else None
            script.game_text = canonical_text(rules or []) or script.game_text
            scripts.append(script)
    return scripts


def build_report(scripts):
    stubs = [s for s in scripts if s.is_stub]
    groups = defaultdict(list)
    for script in stubs:
        signature = normalize_text(script.game_text) if script.game_text else ""
        groups[signature].append(script)
    ordered = sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    return stubs, ordered


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--top", type=int, default=40,
                        help="show the N largest text groups")
    parser.add_argument("--json", dest="json_path",
                        help="write the full stub list to this path")
    parser.add_argument("--grep", help="only show groups whose text matches this regex")
    parser.add_argument("--fingerprint",
                        help="write path -> effect for EVERY trainer script, so a "
                             "before/after diff proves no working card changed")
    args = parser.parse_args(argv)

    scripts = collect()
    stubs, ordered = build_report(scripts)
    implementable = sum(1 for s in stubs if s.game_text)
    named = Counter(s.display_name for s in stubs)

    print(f"trainer scripts parsed : {len(scripts)}")
    print(f"already implemented    : {len(scripts) - len(stubs)}")
    print(f"stubs                  : {len(stubs)} "
          f"({implementable} with rules text, {len(stubs) - implementable} without)")
    print(f"distinct texts         : {len(ordered)}")
    print(f"distinct card names    : {len(named)}")

    family_scripts = Counter()
    family_groups = Counter()
    for signature, members in ordered:
        family_scripts[family_of(signature)] += len(members)
        family_groups[family_of(signature)] += 1
    print("\nFAMILY                  SCRIPTS   GROUPS")
    for family, count in family_scripts.most_common():
        print(f"{family:<22}{count:>9}{family_groups[family]:>9}")

    pattern = re.compile(args.grep, re.I) if args.grep else None
    shown = 0
    print(f"\nTOP TEXT GROUPS (largest first, {args.top} shown)")
    for signature, members in ordered:
        if pattern and not pattern.search(signature):
            continue
        if shown >= args.top:
            break
        shown += 1
        names = Counter(m.display_name for m in members)
        label = ", ".join(f"{n} x{c}" for n, c in names.most_common(3))
        print(f"\n[{len(members):>4}] {signature[:220] or '<no rules text>'}")
        print(f"       {label}")

    if args.fingerprint:
        payload = {s.path: s.effect_name for s in scripts}
        with open(args.fingerprint, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=0, sort_keys=True)
        print(f"wrote {len(payload)} script fingerprints to {args.fingerprint}")

    if args.json_path:
        payload = [{
            "signature": signature,
            "family": family_of(signature),
            "count": len(members),
            "names": sorted({m.display_name for m in members}),
            "paths": [m.path for m in members],
        } for signature, members in ordered]
        with open(args.json_path, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=1)
        print(f"\nwrote {len(payload)} groups to {args.json_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
