"""Wires Special Energy scripts to behaviour helpers, by printed text.

The scripts are data: `EnergyCardDef(guid=..., is_special=True)`. Behaviour lives in
`ptcgo/game/card_effects/energies.py`. This tool pairs a card's printed rules text
(from the set JSON) with the keyword arguments that express it and inserts them
into the script, so a wired card still reads as a card.

    python tools/special_energy_wire.py            # dry run: what would change
    python tools/special_energy_wire.py --apply    # write the scripts
"""
import argparse
import ast
import glob
import json
import os
import re
import sys

CARDS_ROOT = os.path.join("ptcgo", "game", "scripts", "cards")
SKIP_DIRS = {"__pycache__", "CUSTOM", "Free_Energy"}
HOOKS = ("provides", "attach_to", "attach_condition", "attach_cost",
         "on_attach", "on_carrier_knocked_out", "passive")

# family -> (regex over normalised text, kwargs, required flags)
# Text is lowercased, punctuation collapsed and "pokemon" stripped of its accent
# by normalise(). Every pattern is anchored so a card whose wording differs by a
# clause falls through instead of being wired to the wrong shape.
FAMILIES = [
    (
        # Prism Energy: Colorless by default, every type on a Basic. Checked first
        # because its text also contains the unconditional clause.
        "prism-energy",
        r"(if the pokemon[^.]{0,60}?is a basic pokemon|if this card is attached to a basic pokemon), "
        r"(this card|it) provides every type of energy but provides only 1 energy at a time",
        "passive=PrismEnergyPassive()",
        (),
    ),
    (
        # Multi Energy: every type, but only Colorless once another Special Energy
        # sits on the same Pokemon.
        "multi-energy",
        r"provides every type of energy but provides only 1 energy at a time.*"
        r"(provides colorless energy when attached to a pokemon that already has special energy|"
        r"has any other special energy attached, this card provides colorless energy instead)",
        "provides=ALL_TYPES_ONE_AT_A_TIME,\n    passive=MultiEnergyPassive()",
        (),
    ),
    (
        "double-colourless",
        r"^((double )?colorless energy (card )?provides?|provides?) colorless ?colorless energy",
        "provides=DOUBLE_COLORLESS",
        (),
    ),
    (
        "unit-energy",
        r"attached to a pokemon, it provides (grass, fire, and water|lightning, psychic, and metal|"
        r"fighting, darkness, and fairy) energy but provides only 1 energy at a time",
        None,
        ("unit",),
    ),
    (
        "blend-energy",
        r"provides (grass, fire, psychic, or darkness|water, lightning, fighting, or metal) energy "
        r"but provides only 1 energy at a time",
        None,
        ("blend",),
    ),
    (
        "attach-evolved-excluding-ex",
        r"can be attached only to an evolved pokemon( \(excluding pokemon-ex\))?",
        "attach_to=evolved_excluding_ex" if False else None,
        ("evolved",),
    ),
    (
        "attach-evolved",
        r"(can be attached only to|can only be attached to) (an )?evolved pokemon|can only be attached to evolution pokemon",
        "attach_to=pokemon_is_evolved",
        (),
    ),
    (
        "attach-type",
        r"can only be attached to (grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy|dragon) pokemon",
        None,
        ("type",),
    ),
    (
        "attach-strike",
        r"can only be attached to (?:a )?(rapid|single|fusion) strike pokemon",
        None,
        ("strike",),
    ),
    (
        "attach-named",
        r"can (?:only be attached to|be attached only to) (?:a pokemon with )?(team rocket's|team aqua|team magma)( pokemon| in its name)",
        None,
        ("named",),
    ),
    (
        # the plain "every type, one at a time" family; anything conditional is
        # caught by BLOCKED below and left alone
        "all-types-one-at-a-time",
        r"provides every type of (basic )?energy but provides only 1 energy at a time",
        "provides=ALL_TYPES_ONE_AT_A_TIME",
        (),
    ),
]

# Wording that asks for a primitive the engine does not have yet. Reported, never
# wired, because a half-wired card plays by different rules than it is printed with.
BLOCKED = [
    (r"provides .{0,30} and ?/ ?or .{0,30} energy but provides 2 energy at a time"
     r"|provides .{0,20} and .{0,20} energy but provides 2 energy at a time",
     "two-specific-types-at-a-time provision (pairs helper missing)"),
    (r"ultra beast", "Ultra Beast subtype gate plus a damage passive"),
    (r"1 fewer prize", "prize-count passive with a once-per-game gate"),
    (r"put it in the lost zone instead|lost zone instead", "Prism Star lost-zone rule"),
    (r"\bδ\b|delta species", "delta-species marker not tracked on cards"),
    (r"provides? 4 energy at a time", "four-at-once provision not expressible"),
    (r"if you have 3 or more stage 2", "conditional on board count"),
    (r"discard .{0,40} at the end of (the|your) turn", "no end-of-turn discard timer for energies"),
    (r"can('|no)t retreat", "retreat lock from an energy needs the passive wired (batch 3)"),
    (r"damage done .{0,60}(reduced|increased) by", "damage modifier passive (batch 3)"),
    (r"more damage to the active", "damage modifier passive (batch 3)"),
]

TYPE_NAMES = {
    "grass": "PokemonTypes.GRASS", "fire": "PokemonTypes.FIRE", "water": "PokemonTypes.WATER",
    "lightning": "PokemonTypes.LIGHTNING", "psychic": "PokemonTypes.PSYCHIC",
    "fighting": "PokemonTypes.FIGHTING", "darkness": "PokemonTypes.DARKNESS",
    "metal": "PokemonTypes.METAL", "fairy": "PokemonTypes.FAIRY",
    "dragon": "PokemonTypes.DRAGON", "colorless": "PokemonTypes.COLORLESS",
}

DAMAGE_COUNTER_ON_ATTACH = re.compile(
    r"when you attach this card from your hand to 1 of your pokemon, (put 1 damage counter on that pokemon|"
    r"it does 10 damage to that pokemon)")


def normalise(text):
    value = (text or "").lower().replace("’", "'").replace("é", "e")
    value = re.sub(r"\s+", " ", value)
    value = value.replace("pokémon", "pokemon")
    return value.strip()


def set_texts():
    index = {}
    for path in glob.glob(os.path.join(CARDS_ROOT, "*", "*.json")):
        try:
            cards = json.load(open(path, encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        set_dir = os.path.basename(os.path.dirname(path)).upper()
        for card in cards:
            rules = card.get("rules") or []
            text = " ".join(rules).strip()
            try:
                number = int(str(card.get("number", "")).split("/")[0])
            except ValueError:
                continue
            index[(set_dir, number)] = text
    return index


def energy_call(path):
    tree = ast.parse(open(path, encoding="utf-8").read(), filename=path)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id == "EnergyCardDef":
            return node
    return None


def existing_kwargs(call):
    return {kw.arg for kw in call.keywords if kw.arg}


def plan_for(text, is_special_text=True):
    """Returns (family, kwargs_snippet, note) or (None, None, reason)."""
    low = normalise(text)
    if not low:
        return None, None, "no printed text"
    for pattern, reason in BLOCKED:
        if re.search(pattern, low):
            return None, None, reason
    for name, pattern, snippet, extra in FAMILIES:
        if not re.search(pattern, low):
            continue
        if extra == ("evolved",):
            excluding = "(excluding pokemon-ex)" in low or "excluding pokemon-ex" in low
            return name, "attach_to=" + ("evolved_excluding_ex" if excluding else "pokemon_is_evolved"), ""
        if extra == ("type",):
            listed = re.search(
                r"can only be attached to (grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy|dragon) pokemon",
                low)
            if not listed:
                return None, None, "type not parsed"
            return name, f"attach_to=pokemon_of_type({TYPE_NAMES[listed.group(1)]})", ""
        if extra == ("strike",):
            listed = re.search(r"can only be attached to (?:a )?(rapid|single|fusion) strike pokemon", low)
            marker = {"rapid": "Rapid Strike", "single": "Single Strike", "fusion": "Fusion Strike"}[listed.group(1)]
            return name, f'attach_to=pokemon_with_subtype("{marker}")', ""
        if extra == ("named",):
            listed = re.search(r"(team rocket's|team aqua|team magma)", low)
            fragment = {"team rocket's": "Team Rocket", "team aqua": "Team Aqua", "team magma": "Team Magma"}[listed.group(1)]
            return name, f'attach_to=pokemon_named_like("{fragment}")', ""
        if extra == ("unit",) or extra == ("blend",):
            listed = re.search(
                r"(grass, fire, and water|lightning, psychic, and metal|fighting, darkness, and fairy|"
                r"grass, fire, psychic, or darkness|water, lightning, fighting, or metal)", low)
            if not listed:
                return None, None, "energy types not parsed"
            types = [part.strip() for part in re.split(r",| and | or ", listed.group(1)) if part.strip()]
            args = ", ".join(TYPE_NAMES[t] for t in types if t in TYPE_NAMES)
            return name, f"provides=one_at_a_time({args})", ""
        snippet_used = snippet
        if DAMAGE_COUNTER_ON_ATTACH.search(low):
            snippet_used += ",\n    on_attach=rainbow_on_attach"
        return name, snippet_used, ""
    return None, None, "no family matched"


IMPORT_LINE = "from ptcgo.game.card_effects.energies import "

NEEDED = {
    "DOUBLE_COLORLESS": ["DOUBLE_COLORLESS"],
    "ALL_TYPES_ONE_AT_A_TIME": ["ALL_TYPES_ONE_AT_A_TIME"],
    "one_at_a_time(": ["one_at_a_time"],
    "rainbow_on_attach": ["rainbow_on_attach"],
    "PrismEnergyPassive()": ["PrismEnergyPassive"],
    "MultiEnergyPassive()": ["MultiEnergyPassive"],
    "attach_to=evolved_excluding_ex": ["evolved_excluding_ex"],
    "attach_to=pokemon_is_evolved": ["pokemon_is_evolved"],
    "attach_to=pokemon_of_type(": ["pokemon_of_type"],
    "attach_to=pokemon_with_subtype(": ["pokemon_with_subtype"],
    "attach_to=pokemon_named_like(": ["pokemon_named_like"],
}


def ensure_imports(path, snippet):
    """Adds or extends the energies import line for everything the snippet uses."""
    wanted = []
    for marker, names in NEEDED.items():
        if marker in snippet:
            wanted.extend(names)
    if not wanted:
        return
    lines = open(path, encoding="utf-8").read().splitlines()
    for index, line in enumerate(lines):
        if line.startswith(IMPORT_LINE):
            existing = [part.strip() for part in line[len(IMPORT_LINE):].split(",") if part.strip()]
            merged = existing + [name for name in wanted if name not in existing]
            lines[index] = IMPORT_LINE + ", ".join(merged)
            open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
            return
    first_card = next(i for i, line in enumerate(lines) if line.startswith("card ="))
    lines.insert(first_card, "")
    lines.insert(first_card + 1, IMPORT_LINE + ", ".join(wanted))
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")


def apply_snippet(path, call, snippet):
    """Inserts the kwargs before the call's closing paren, matching its indent."""
    source = open(path, encoding="utf-8").read()
    lines = source.splitlines(keepends=True)
    start_line = call.lineno - 1
    end_line = call.end_lineno - 1

    # continuation lines share the indent of the call's first keyword line
    keyword_indent = None
    for line in lines[start_line + 1:end_line + 1]:
        stripped = line.strip()
        if stripped:
            keyword_indent = line[: len(line) - len(line.lstrip())]
            break
    if keyword_indent is None:
        keyword_indent = re.match(r"\s*", lines[start_line]).group(0) + "    "

    end_text = lines[end_line]
    tail = end_text[call.end_col_offset:]           # whatever follows the ")"
    body_lines = lines[start_line:end_line]         # everything before the closing line
    closing = end_text[:call.end_col_offset].rstrip()
    opens_on_own_line = closing == ""

    new_kwargs = []
    for part in snippet.split("\n"):
        piece = part.strip().rstrip(",")
        if piece:
            new_kwargs.append(f"{keyword_indent}{piece},\n")

    if opens_on_own_line:
        # the call ends with a line that is only ")"
        rebuilt = body_lines + new_kwargs + [keyword_indent[:-4] + ")" + tail]
    else:
        last = body_lines[-1]
        rebuilt = body_lines[:-1] + [last.rstrip().rstrip(",") + ",\n"] + new_kwargs
        indent = re.match(r"\s*", lines[start_line]).group(0)
        rebuilt.append(indent + ")" + tail)
    lines[start_line:end_line + 1] = rebuilt
    open(path, "w", encoding="utf-8").write("".join(lines))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--family")
    args = parser.parse_args()

    texts = set_texts()
    rows = []
    for directory in sorted(os.listdir(CARDS_ROOT)):
        if directory in SKIP_DIRS:
            continue
        for path in sorted(glob.glob(os.path.join(CARDS_ROOT, directory, "*.py"))):
            if os.path.basename(path) == "__init__.py":
                continue
            call = energy_call(path)
            if call is None:
                continue
            kwargs = {kw.arg: kw.value for kw in call.keywords if kw.arg}
            if not (isinstance(kwargs.get("is_special"), ast.Constant) and kwargs["is_special"].value):
                continue
            if HOOKS and any(name in kwargs for name in HOOKS):
                continue
            stem = os.path.splitext(os.path.basename(path))[0]
            number = stem.rpartition("_")[2]
            try:
                number = int(number)
            except ValueError:
                continue
            text = texts.get((directory.upper(), number), "")
            family, snippet, reason = plan_for(text)
            rows.append({"path": path, "family": family, "snippet": snippet,
                         "reason": reason, "text": text, "name": stem.rpartition("_")[0]})

    matched = [r for r in rows if r["family"]]
    if args.family:
        matched = [r for r in matched if r["family"] == args.family]
    print(f"unwired special energies: {len(rows)}  matched to a family: {len(matched)}")
    for row in matched:
        print(f"  {row['family']:26s} {row['path']}")
        print(f"      {row['snippet'].replace(chr(10), ' ')}")
        print(f"      text: {row['text'][:110]}")
    unmatched = [r for r in rows if not r["family"]]
    print(f"\nleft unwired: {len(unmatched)}")

    if args.apply and matched:
        for row in matched:
            call = energy_call(row["path"])
            apply_snippet(row["path"], call, row["snippet"])
            ensure_imports(row["path"], row["snippet"])
        print(f"applied to {len(matched)} scripts")


if __name__ == "__main__":
    main()
