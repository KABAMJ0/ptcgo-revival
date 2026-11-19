"""Which localization ids the client can render, and which of ours it cannot.

The 2020 client renders a `{"id": ...}` field (a LocalizableText) by looking the id
up in its own localization database. core.dll's `LocalizationLookup.Localize` is
`lookup.TryGetValue(id.ToLower()) ?? id`, so an id the database lacks is drawn
literally, and any id that is not a key at all is drawn as plain text. That is the
whole rule: a key resolves, anything else is the text.

Two kinds of id reach the client from here:

* Literal ids, written into a packet as `{"id": ...}`. If the string is a client
  key it resolves, otherwise it is shown as written. `literal_ids()` scans the
  server sources for those and reports the ones shaped like a key that the client
  does not have — a decode of this scan is what "series.base" was.
* Derived ids: the client builds the key itself from a value we send. pie-src's
  collection formats `"series.{0}"` with a set's block, and a set's own label is
  `string.Format(<template>, code.ToLowerInvariant())` (CollectionUI's
  `get_Label`). No literal we send can fix those; the key has to exist, either in
  the client's database or in `custom_labels.json`, which data_sync merges into
  the localization release it hands the client.

Run: python -m ptcgo.tools.localization_keys [--report PATH]
Exit code 1 when an id the server would send cannot be rendered, 0 when all can.
"""

import argparse
import ast
import json
import os
import re
import sqlite3
import sys
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOC_DB = os.path.join(ROOT, "ptcgo", "database", "game_data", "LocalizationDB-UTF16.db")
CUSTOM_LABELS = os.path.join(ROOT, "ptcgo", "database", "json_data", "custom_labels.json")
SETS = os.path.join(ROOT, "ptcgo", "database", "json_data", "sets.json")
SET_META = os.path.join(ROOT, "ptcgo", "database", "json_data", "set_meta.json")
SOURCES = os.path.join(ROOT, "ptcgo")

# A key: dot-separated segments of word characters, the way the client's database
# spells them ("series.bw", "playmat.endgame.tokens", "cards.stat.height.cm.100"),
# or one of the client's `ids_*` names. Text with a space or a sentence mark is
# never a key and is drawn as written.
KEY = re.compile(r"^(?:[A-Za-z][A-Za-z0-9_]*(?:\.[A-Za-z0-9_{}]+)+|ids_[A-Za-z0-9_]+)$")

# Source trees that hold no server-emitted id: card and effect scripts address
# their own pattern names, and the generated protobuf package is wire shapes.
SKIP = ("game/scripts/cards", "game/card_effects", "protobuf")


def client_keys(path=LOC_DB):
    """The client's own key -> text map, keyed lowercased as its lookup keys it."""
    con = sqlite3.connect(Path(path).resolve().as_uri() + "?mode=ro", uri=True)
    try:
        return {key.lower(): value for key, value in con.execute("select key, value from Lookup")}
    finally:
        con.close()


def served_keys(path=CUSTOM_LABELS):
    """Keys the server adds to the release it sends (custom_labels.json), lowercased."""
    with open(path, encoding="utf-8") as f:
        return {key.lower(): value for key, value in json.load(f).items()}


def _load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def derived_keys(sets_path=SETS, meta_path=SET_META):
    """Keys the client composes from a value we send: (surface, key)."""
    rows = []
    meta = _load(meta_path)
    for entry in _load(sets_path):
        block = entry.get("block")
        if isinstance(block, str) and block:
            rows.append(("collection series header", f"series.{block}"))
            rows.append(("collection series filter", f"collection.filter.series.{block}"))
        code = entry.get("name")
        if isinstance(code, str) and code:
            rows.append(("collection set label", f"set.name.{code}"))
            rows.append(("set list / setname label", f"setname.{code}"))
    del meta
    return rows


def _string_constants(tree):
    """Module-level NAME = "literal" pairs, so `{"id": NO_DECK_KEY}` resolves."""
    out = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant) \
                and isinstance(node.value.value, str):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    out[target.id] = node.value.value
    return out


def _strings(node, constants):
    """The literal strings a value expression can be, following names and `or`."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return [node.value]
    if isinstance(node, ast.Name) and isinstance(constants.get(node.id), str):
        return [constants[node.id]]
    if isinstance(node, ast.BoolOp) and isinstance(node.op, ast.Or):
        return [value for branch in node.values for value in _strings(branch, constants)]
    return []


# A handler that takes the message text as an argument rather than a dict value
# ("_join_failed", "_send_error", "_loc"). Its string arguments are ids too.
ARGUMENT = re.compile(r"(?:_error|_join_failed|_send_error|_purchase_failed|_send_invalid|_loc)$")


def _call_arg_values(node, constants):
    """The strings a message-text argument of a call would send."""
    func = node.func
    name = func.attr if isinstance(func, ast.Attribute) else getattr(func, "id", "")
    if not ARGUMENT.search(name or ""):
        return []
    return [value for arg in node.args for value in _strings(arg, constants)]


def _dict_id_values(node, constants):
    """The strings an `{"id": <value>}` dict literal would send."""
    if not isinstance(node, ast.Dict) or len(node.keys) != 1:
        return []
    key = node.keys[0]
    if not (isinstance(key, ast.Constant) and key.value == "id"):
        return []
    return _strings(node.values[0], constants)


def literal_ids(root=SOURCES):
    """Ids written into packets: (source, line, id)."""
    rows = []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in ("__pycache__",))
        for name in sorted(files):
            if not name.endswith(".py"):
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, ROOT)
            if any(rel.startswith(os.path.join("ptcgo", skip)) for skip in SKIP):
                continue
            try:
                with open(path, encoding="utf-8") as f:
                    tree = ast.parse(f.read())
            except (OSError, SyntaxError) as error:
                print(f"cannot parse {rel}: {error}", file=sys.stderr)
                continue
            constants = _string_constants(tree)
            for node in ast.walk(tree):
                values = _dict_id_values(node, constants)
                if isinstance(node, ast.Call):
                    values += _call_arg_values(node, constants)
                for value in values:
                    rows.append((rel, node.lineno, value))
    return rows


def data_ids():
    """Ids carried by data rather than written into a packet: (surface, id)."""
    from ptcgo.database import economy_data
    from ptcgo.game.content import trainer_challenge
    from ptcgo.game.progression import quests
    from ptcgo.game.session import constants
    from ptcgo.packets.handlers import data_sync

    rows = []
    for _, name, description, _ in data_sync.LEAGUE_SCENARIOS:
        rows.append(("league scenario name", name))
        rows.append(("league scenario description", description))
    for reason in (economy_data.CODE_INVALID, economy_data.CODE_EXPIRED,
                   economy_data.CODE_USED):
        rows.append(("code redemption reason", reason))
    for template in quests.load_catalog():
        rows.append(("quest title", template["title"]))
        rows.append(("quest description", template["description"]))
    for entry in trainer_challenge.leagues():
        for opponent in entry.opponents:
            rows.append(("league opponent name", opponent.name))
    for name, value in vars(constants).items():
        if name.startswith(("PROMPT_", "TEXT_", "LOC_KEY_")) and isinstance(value, str):
            rows.append(("game prompt or label", value))
    return rows


def audit(keys=None, served=None):
    """Every id we emit, whether the client can render it, and who supplies it."""
    keys = client_keys() if keys is None else keys
    served = served_keys() if served is None else served
    rows = []
    for surface, key in derived_keys():
        low = key.lower()
        rows.append({
            "surface": surface, "id": key, "derived": True,
            "client": low in keys, "server": low in served, "source": "",
        })
    for source, line, value in literal_ids():
        rows.append(_literal("message field", value, keys, served, f"{source}:{line}"))
    for surface, value in data_ids():
        rows.append(_literal(surface, value, keys, served, ""))
    return rows


def _literal(surface, value, keys, served, source):
    low = value.lower()
    return {
        "surface": surface, "id": value, "derived": False, "source": source,
        "client": low in keys, "server": low in served, "is_key": bool(KEY.match(value)),
    }


def problems(rows):
    """Ids that cannot render as intended.

    A derived key or a literal id shaped like one is drawn as the key when the
    client has never heard of it, which is the reported bug. Plain text renders
    as written, so it is fine unless it equals a key: then the client would swap
    that key's text in for it, which is a bug the other way round.
    """
    return [row for row in rows if _defect(row)]


def _defect(row):
    if row["derived"] or row.get("is_key"):
        return not (row["client"] or row["server"])
    return row["client"]


def _markdown(rows, bad):
    lines = [
        "| surface | id the server sends | client has it | drawn as |",
        "| --- | --- | --- | --- |",
    ]
    for row in rows:
        held = "yes" if row["client"] else "no"
        if row["derived"] or row.get("is_key"):
            drawn = "the key itself" if not (row["client"] or row["server"]) else ""
        else:
            drawn = "the text" if not row["client"] else "**the key's text**"
        lines.append(f"| {row['surface']} | `{row['id']}` | {held} | {drawn} |")
    lines.append("")
    lines.append(f"{len(rows)} ids, {len(bad)} unrenderable.")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", help="write the inventory table here")
    parser.add_argument("--db", default=LOC_DB)
    parser.add_argument("--served", default=CUSTOM_LABELS)
    args = parser.parse_args()

    rows = audit(client_keys(args.db), served_keys(args.served))
    bad = problems(rows)
    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            f.write(_markdown(rows, bad) + "\n")
        print(f"wrote {args.report}")
    derived = [r for r in rows if r["derived"]]
    print(f"derived ids: {len(derived)}, literal ids: {len(rows) - len(derived)}")
    if not bad:
        print("unrenderable localization ids: 0")
        return 0
    print(f"unrenderable localization ids: {len(bad)}")
    for row in bad:
        where = f"  ({row['source']})" if row.get("source") else ""
        print(f"  {row['surface']}: {row['id']}{where}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
