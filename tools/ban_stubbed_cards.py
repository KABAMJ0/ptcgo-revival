#!/usr/bin/env python3
"""Ban every card that still has an unimplemented effect, so nobody plays a card whose text
does nothing. Dry run by default: nothing is written until you pass --apply.

    python tools/ban_stubbed_cards.py                      # report only
    python tools/ban_stubbed_cards.py --apply              # ban them (asks to confirm)
    python tools/ban_stubbed_cards.py --apply --sync       # also lift bans on cards fixed since
    python tools/ban_stubbed_cards.py --undo               # lift every ban this script made
    python tools/ban_stubbed_cards.py --sets SV10,SV4      # limit to some sets
    python tools/ban_stubbed_cards.py --exclude-sets DP1   # skip some sets
    python tools/ban_stubbed_cards.py --kind pokemon       # pokemon | trainer | all
    python tools/ban_stubbed_cards.py --csv stubbed.csv    # write the list to a file

Cards already banned by an admin are never touched or unbanned. Bans made here carry
banned_by="stub-ban-script", so --sync and --undo only ever remove their own. The server
caches the ban list: restart it (sudo systemctl restart spirit-ptcgo) after --apply, --sync
or --undo. Run it from the repo root, with the server's environment (venv, database settings).
"""
import argparse
import ast
import csv
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS_ROOT = os.path.join("ptcgo", "game", "scripts", "cards")
SKIP_DIRS = {"__pycache__", "CUSTOM", "Free_Energy"}
MARKER = "stub-ban-script"
POKEMON_DEFS = {"PokemonCardDef", "PokemonReprintCardDef"}


def _kw(call, name):
    for k in call.keywords:
        if k.arg == name:
            return k.value
    return None


def scan(sets=None, exclude=None, kind="all"):
    """Returns [{guid, set, file, name, kind, titles}] for every card with a stubbed effect."""
    out = []
    for d, _, files in sorted(os.walk(CARDS_ROOT)):
        set_code = os.path.basename(d)
        if set_code in SKIP_DIRS or any(x in d for x in SKIP_DIRS):
            continue
        if sets and set_code not in sets:
            continue
        if exclude and set_code in exclude:
            continue
        for f in sorted(files):
            if not f.endswith(".py") or f == "__init__.py":
                continue
            path = os.path.join(d, f)
            try:
                tree = ast.parse(open(path, encoding="utf-8").read())
            except Exception as e:
                print(f"skip {path}: {e}", file=sys.stderr)
                continue
            card = next((c for c in ast.walk(tree)
                         if isinstance(c, ast.Call) and isinstance(c.func, ast.Name)
                         and c.func.id.endswith("CardDef") and _kw(c, "guid") is not None), None)
            if card is None:
                continue
            guid = _kw(card, "guid")
            if not (isinstance(guid, ast.Constant) and isinstance(guid.value, str)):
                continue
            is_pokemon = card.func.id in POKEMON_DEFS
            if (kind == "pokemon" and not is_pokemon) or (kind == "trainer" and is_pokemon):
                continue
            titles = []
            for c in ast.walk(card):
                if isinstance(c, ast.Call) and isinstance(c.func, ast.Name) and c.func.id in ("Attack", "Ability"):
                    for arg in ("effect", "passive"):
                        v = _kw(c, arg)
                        if isinstance(v, ast.Name) and v.id == "unimplemented":
                            t = _kw(c, "title")
                            titles.append(t.value if isinstance(t, ast.Constant) else "?")
            # trainer / energy scripts carry the stub as the card's own effect
            for arg in ("effect", "on_play", "passive"):
                v = _kw(card, arg)
                if isinstance(v, ast.Name) and v.id == "unimplemented":
                    titles.append("card effect")
            if titles:
                name = _kw(card, "display_name")
                out.append({"guid": guid.value.lower(), "set": set_code, "file": f[:-3],
                            "name": name.value if isinstance(name, ast.Constant) else f[:-3],
                            "kind": "pokemon" if is_pokemon else "trainer", "titles": titles})
    return out


def reason_for(row):
    text = "Effect not implemented yet: " + ", ".join(row["titles"])
    return text[:300]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="write the bans (default is a dry run)")
    ap.add_argument("--sync", action="store_true", help="lift this script's bans on cards no longer stubbed")
    ap.add_argument("--undo", action="store_true", help="lift every ban this script made")
    ap.add_argument("--sets"); ap.add_argument("--exclude-sets")
    ap.add_argument("--kind", choices=("all", "pokemon", "trainer"), default="all")
    ap.add_argument("--csv"); ap.add_argument("--yes", action="store_true", help="skip the confirmation")
    a = ap.parse_args()
    os.chdir(ROOT)
    sets = {s.strip() for s in a.sets.split(",")} if a.sets else None
    excl = {s.strip() for s in a.exclude_sets.split(",")} if a.exclude_sets else None

    rows = [] if a.undo else scan(sets, excl, a.kind)
    if a.csv:
        with open(a.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f); w.writerow(["guid", "set", "card", "kind", "stubbed"])
            for r in rows:
                w.writerow([r["guid"], r["set"], r["name"], r["kind"], "; ".join(r["titles"])])
        print(f"wrote {a.csv}")

    from collections import Counter
    if not a.undo:
        print(f"{len(rows)} cards have a stubbed effect")
        for s, n in Counter(r["set"] for r in rows).most_common(12):
            print(f"  {s:<14}{n:>5}")

    if not (a.apply or a.undo):
        print("\nDry run: nothing was changed. Add --apply to ban these cards.")
        return 0

    from ptcgo.database import db_session, CardBan  # needs the server's environment
    with db_session() as session:
        existing = {b.archetype_id.lower(): b for b in session.query(CardBan)}
        if a.undo:
            mine = [b for b in existing.values() if b.banned_by == MARKER]
            if not a.yes and input(f"Lift {len(mine)} bans made by this script? [y/N] ").lower() != "y":
                return 1
            for b in mine:
                session.delete(b)
            print(f"lifted {len(mine)} bans")
            return 0
        new = [r for r in rows if r["guid"] not in existing]
        skipped = len(rows) - len(new)
        lift = []
        if a.sync:
            still = {r["guid"] for r in scan(None, None, "all")}
            lift = [b for g, b in existing.items() if b.banned_by == MARKER and g not in still]
        print(f"will ban {len(new)} cards ({skipped} already banned), lift {len(lift)}")
        if not a.yes and input("Apply? [y/N] ").lower() != "y":
            return 1
        for r in new:
            session.add(CardBan(archetype_id=r["guid"], reason=reason_for(r), banned_by=MARKER))
        for b in lift:
            session.delete(b)
    print("done. Restart the server so it reloads the ban list.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
