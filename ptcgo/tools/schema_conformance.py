"""Gate: what a card script sets, read against the client's own data model.

The client is the authority on its own attributes and it is unforgiving in two
specific ways:

  * An attribute id the client does not define has no definition to build, so
    `MutableAttributes.GetAttribute` hands back `MissingAttributes.GetAttribute`
    -- an `Attribute<object>` whose value is null. Nothing reads it and nothing
    logs it. Our value silently does not exist on the client.
  * An attribute id the client *does* define is deserialized against that
    definition's own CLR type: `AttributeAnalyzer.Analyze` calls
    `analyzer.ConsumeValue(tokens, attributeDefinition.ValueType)` and then
    `MutableAttribute<V>` hard-casts `(V)value`. A number where the client
    declared a string, or an int where it declared a float, is not a
    conversion -- it is an exception on the client's load path.

So every attribute we send is one of three things: readable, dropped, or a
crash. This tool says which, per attribute, over every card script.

Where the truth comes from (client repo, not committed here):

  schema/types.tsv                    the wire shape: `dwd.Protobuf.Archetype`
                                      {guid: UUID, attributes: List<Attribute>},
                                      `dwd.Protobuf.Attribute` {A: Int32 name,
                                      a: Object}, `dwd.Protobuf.Object` one-of
                                      STRING/BOOL/INT/FLOAT/UUID/JSON.
  decompiled/pie-src/P/F.cs           the archetype attribute table: 184
  decompiled/core/.../CoreAttributes  `AttributeDefinition<V>(key)` declarations,
                                      which is where each id's CLR type is fixed.
  decompiled/core/.../AttributeAnalyzer.cs, MutableAttribute.cs
                                      the deserialize-then-cast behaviour above.

`ptcgo/database/json_data/client_attribute_types.json` holds the id -> CLR type
table those files declare, with its provenance. It is the only client-derived
data this repo keeps, and it is derived metadata (188 pairs), not client source:
the same ids are already in `ptcgo/game/attributes.py`. Regenerate it from a
client checkout with `--client PATH --write-table`.

Usage:
  python -m ptcgo.tools.schema_conformance                # verdict table + counts
  python -m ptcgo.tools.schema_conformance --report out.md
  python -m ptcgo.tools.schema_conformance --client ~/poke --write-table

Exit status is 1 when a card sets an attribute the client cannot read (unknown
id or a wire type its definition cannot consume), 0 otherwise.
"""

import argparse
import json
import os
import re
import sys
from typing import Dict, Iterable, List, Optional, Set, Tuple

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TABLE = os.path.join(ROOT, "ptcgo", "database", "json_data", "client_attribute_types.json")

INT32_MIN, INT32_MAX = -2147483648, 2147483647

# Our writer tag -> the `dwd.Protobuf.Object.Type` it sets (data_sync._write_attr).
TAG_WIRE = {
    "json": "JSON",
    "string": "STRING",
    "int": "INT",
    "float": "FLOAT",
    "bool": "BOOL",
    "uuid": "UUID",
}

# Enum-backed attributes the client declares as `X?` (an Int32 in protobuf) or
# `X[]` (a JSON array).
CLIENT_ENUMS = {
    "CardOrientations", "CardTypes", "FoilEffects", "FoilMasks", "GenderTypes",
    "PokemonStage", "ProductTypes", "PokemonTypes", "Rarities", "TrainerTypes",
    "SpecialConditions", "SuppressEffects", "PokemonTeams",
}

SCALAR_WIRE = {
    "int": "INT", "short": "INT", "byte": "INT", "uint": "INT",
    "float": "FLOAT", "double": "FLOAT", "bool": "BOOL", "string": "STRING",
}

# Struct wrappers around a Guid: the client reads these from a guid, and our
# writer sends either a UUID field or the bare guid string.
GUID_WRAPPERS = {"ArchetypeID", "EntityID", "DeckID", "ScenarioID", "SolitaireID", "AbilityID"}

DEFINITION = re.compile(r"AttributeDefinition<((?:[^<>]|<[^<>]*>)+)>\((\d+)\)")


def expected_wires(clr: str) -> Set[str]:
    """Wire classes the client can consume for one declared CLR type.

    Empty means the client type is an opaque named class whose JSON shape this
    table cannot judge (a `Streak`, an obfuscated `f`); those report unverified
    rather than passing silently.
    """
    name = clr.strip()
    nullable = name.endswith("?")
    base = name[:-1] if nullable else name
    if base in CLIENT_ENUMS:
        return {"INT"} if nullable else {"JSON"}
    if base == "long":
        # ProtobufExtensions.ToObject turns an INT object into an Int32, and
        # MutableAttribute<long?> then casts (long)(object)Int32 -- an
        # InvalidCastException that TryToIAttribute swallows. A long only arrives
        # through JSON.Deserialize, so this is the one scalar that cannot travel
        # as a protobuf INT.
        return {"JSON"}
    if base in SCALAR_WIRE:
        return {SCALAR_WIRE[base]}
    if base == "LocalizableText":
        return {"JSON"}
    if base in GUID_WRAPPERS:
        # TypedID/BareID are rebuilt only by ToObject's UUID branch
        # (Guid.TryGuidConvert -> CreateID) or by a JSON string. Sending the
        # wrapper as a protobuf STRING returns the raw string, which the
        # factory's (V)value cast cannot take, so the attribute is dropped.
        return {"UUID", "JSON"}
    if base.endswith("[]") or "<" in base or base.startswith("global::"):
        return {"JSON"}
    return set()


def load_client_table(path: str = TABLE) -> Dict[int, str]:
    with open(path, encoding="utf-8") as f:
        payload = json.load(f)
    return {int(k): v for k, v in payload["types"].items()}


def parse_client(root: str) -> Tuple[Dict[int, str], Dict[str, object]]:
    """Rebuild the id -> CLR type table from a client checkout."""
    types: Dict[int, str] = {}
    files = 0
    for dirpath, _, names in os.walk(os.path.join(root, "decompiled")):
        for name in names:
            if not name.endswith(".cs"):
                continue
            with open(os.path.join(dirpath, name), encoding="utf-8", errors="replace") as f:
                text = f.read()
            if "AttributeDefinition<" not in text:
                continue
            files += 1
            for line in text.splitlines():
                if "AttributeDefinition<" not in line:
                    continue
                found = DEFINITION.findall(line)
                if found:
                    clr, key = found[-1]
                    types[int(key)] = clr
    schema = os.path.join(root, "schema", "types.tsv")
    facts: Dict[str, object] = {"definitions_in_files": files}
    if os.path.exists(schema):
        with open(schema, encoding="utf-8") as f:
            rows = [line.rstrip("\n").split("\t") for line in f]
        facts["schema_rows"] = len(rows)
        facts["archetype_fields"] = [
            (r[2], r[3]) for r in rows
            if len(r) > 3 and r[0] == "PROP" and r[1] == "dwd.Protobuf.Archetype"
        ]
        facts["object_type_enum"] = [
            (r[2], int(r[3])) for r in rows
            if len(r) > 3 and r[0] == "ENUMVAL" and r[1] == "dwd.Protobuf.Object+Type"
        ]
    return types, facts


def verdict(attr_id: int, tag: str, value, table: Dict[int, str]) -> Tuple[str, str]:
    """(verdict, detail) for one attribute we would send."""
    wire = TAG_WIRE.get(tag)
    if wire is None:
        return "bad-value", f"unknown writer tag {tag!r}"

    if wire == "INT":
        try:
            as_int = int(value)
        except (TypeError, ValueError):
            return "bad-value", f"{value!r} is not an int"
        if not INT32_MIN <= as_int <= INT32_MAX:
            return "bad-value", f"{as_int} overflows the client's Int32"
    elif wire == "FLOAT":
        try:
            float(value)
        except (TypeError, ValueError):
            return "bad-value", f"{value!r} is not a float"
    elif wire == "UUID":
        import uuid
        try:
            uuid.UUID(str(value))
        except (TypeError, ValueError):
            return "bad-value", f"{value!r} is not a GUID"
    elif wire == "JSON":
        if not isinstance(value, str):
            return "bad-value", f"{value!r} is not a JSON string"
        try:
            json.loads(value)
        except ValueError:
            return "bad-value", "value does not parse as JSON"

    clr = table.get(attr_id)
    if clr is None:
        return "unknown-id", "not in the client's attribute table"
    allowed = expected_wires(clr)
    if not allowed:
        return "unverified", f"client type {clr} is opaque"
    if wire not in allowed:
        return "mismatch", f"client declares {clr}, we send {tag}"
    return "ok", ""


def _attr_ref(node) -> Optional[int]:
    """The AttrID member an expression names, through `str(...)`/`int(...)` wrapping."""
    import ast

    while isinstance(node, ast.Call) and len(node.args) == 1:
        node = node.args[0]
    # AttrID.HP or AttrID.HP.value
    if isinstance(node, ast.Attribute) and node.attr == "value":
        node = node.value
    if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) \
            and node.value.id == "AttrID":
        try:
            return int(getattr(_attr_id_enum(), node.attr))
        except AttributeError:
            return None
    return None


def _tag_of(node) -> Optional[str]:
    """The `"type": "<tag>"` constant of an attribute spec dict literal."""
    import ast

    if not isinstance(node, ast.Dict):
        return None
    for key, value in zip(node.keys, node.values):
        if isinstance(key, ast.Constant) and key.value == "type" \
                and isinstance(value, ast.Constant) and isinstance(value.value, str):
            return value.value
    return None


def scan_sources(root: Optional[str] = None) -> List[dict]:
    """Every attribute spec the server sources build as a literal: (id, tag, where).

    Catches both shapes the writer uses -- `{str(AttrID.X.value): {"type": t, ...}}`
    inside a dict literal, and `final_attrs[str(AttrID.X.value)] = {"type": t, ...}`.
    It reads the source, so an id produced by a variable is invisible to it; the
    loader pass above covers the card scripts, this one covers the rest.
    """
    import ast

    root = root or os.path.join(ROOT, "ptcgo")
    found: List[dict] = []
    for dirpath, _, names in os.walk(root):
        for name in names:
            if not name.endswith(".py"):
                continue
            path = os.path.join(dirpath, name)
            try:
                with open(path, encoding="utf-8") as f:
                    tree = ast.parse(f.read(), filename=path)
            except (SyntaxError, UnicodeDecodeError):
                continue
            rel = os.path.relpath(path, ROOT)
            for node in ast.walk(tree):
                if isinstance(node, ast.Dict):
                    for key, value in zip(node.keys, node.values):
                        attr_id = _attr_ref(key) if key is not None else None
                        tag = _tag_of(value)
                        if attr_id is not None and tag is not None:
                            found.append({"id": attr_id, "tag": tag,
                                          "where": f"{rel}:{node.lineno}"})
                elif isinstance(node, ast.Assign) and len(node.targets) == 1:
                    target = node.targets[0]
                    if isinstance(target, ast.Subscript):
                        attr_id = _attr_ref(target.slice)
                        tag = _tag_of(node.value)
                        if attr_id is not None and tag is not None:
                            found.append({"id": attr_id, "tag": tag,
                                          "where": f"{rel}:{node.lineno}"})
    return found


def audit_sources(table: Dict[int, str]) -> dict:
    """Pass B: static conformance of every attribute spec literal in the server."""
    names = {member.value: member.name for member in _attr_id_enum()}
    rows: Dict[int, dict] = {}
    for site in scan_sources():
        state, detail = verdict(site["id"], site["tag"], _PLACEHOLDER.get(site["tag"]), table)
        row = rows.get(site["id"])
        if row is None:
            row = rows[site["id"]] = {
                "id": site["id"], "name": names.get(site["id"], ""),
                "client_type": table.get(site["id"], ""), "tag": site["tag"],
                "verdict": state, "detail": detail, "sites": [],
            }
        row["sites"].append(site["where"])
        rank = {"unknown-id": 3, "mismatch": 3, "bad-value": 3, "unverified": 2, "ok": 1}
        if rank.get(state, 0) > rank.get(row["verdict"], 0):
            row["verdict"], row["detail"], row["tag"] = state, detail, site["tag"]
    counts: Dict[str, int] = {}
    for row in rows.values():
        counts[row["verdict"]] = counts.get(row["verdict"], 0) + 1
    counts["attributes"] = len(rows)
    return {"rows": rows, "counts": counts}


# Stand-in values so the static pass still exercises the value checks.
_PLACEHOLDER = {"int": 0, "float": 0.0, "bool": True, "string": "", "json": "{}",
                "uuid": "00000000-0000-0000-0000-000000000000"}


def collect() -> Iterable[Tuple[object, Dict[str, dict]]]:
    """(definition, attribute dict) for every card script in the tree."""
    from ptcgo.game.content.definitions import CARD_DEFS_BY_GUID

    from ptcgo.game.scripts.cards import loader
    if not loader.cards:
        loader.load_all()
    for definition in CARD_DEFS_BY_GUID.values():
        yield definition, definition.to_archetype_dict()["attributes"]


def audit(table: Dict[int, str]) -> dict:
    """Per-attribute verdicts over every card the tree ships."""
    names = {member.value: member.name for member in _attr_id_enum()}
    rows: Dict[int, dict] = {}
    cards = 0
    emitted: Set[int] = set()

    for definition, attributes in collect():
        cards += 1
        for raw_id, spec in attributes.items():
            attr_id = int(raw_id)
            emitted.add(attr_id)
            tag = spec.get("type") if isinstance(spec, dict) else None
            value = spec.get("value") if isinstance(spec, dict) else None
            state, detail = verdict(attr_id, tag, value, table)
            row = rows.get(attr_id)
            if row is None:
                row = rows[attr_id] = {
                    "id": attr_id,
                    "name": names.get(attr_id, ""),
                    "client_type": table.get(attr_id, ""),
                    "tag": tag,
                    "verdict": state,
                    "detail": detail,
                    "cards": 0,
                    "example": None,
                    "sample": None,
                }
            row["cards"] += 1
            # A card that sets an id badly outranks one that sets it well.
            rank = {"unknown-id": 3, "mismatch": 3, "bad-value": 3, "unverified": 2, "ok": 1}
            if rank.get(state, 0) > rank.get(row["verdict"], 0):
                row["verdict"], row["detail"], row["tag"] = state, detail, tag
            if row["example"] is None:
                row["example"] = f"{definition.set_code}/{definition.collector_number}"
                row["sample"] = str(value)[:60]

    counts: Dict[str, int] = {}
    for row in rows.values():
        counts[row["verdict"]] = counts.get(row["verdict"], 0) + 1
    counts["cards"] = cards
    counts["attributes"] = len(rows)
    counts["client_ids"] = len(table)
    counts["client_ids_unset"] = len([k for k in table if k not in emitted])
    return {"rows": rows, "counts": counts, "emitted": emitted}


def _attr_id_enum():
    from ptcgo.game.attributes import AttrID
    return AttrID


def render(result: dict, table: Dict[int, str]) -> str:
    rows = sorted(result["rows"].values(), key=lambda r: (-{"unknown-id": 4, "mismatch": 3,
                                                             "bad-value": 2, "unverified": 1,
                                                             "ok": 0}.get(r["verdict"], 0),
                                                         r["id"]))
    order = ("unknown-id", "mismatch", "bad-value", "unverified", "ok")
    out: List[str] = []
    counts = result["counts"]
    out.append(f"{counts['cards']} cards, {counts['attributes']} distinct attribute ids, "
               f"client table has {counts['client_ids']} ids "
               f"({counts['client_ids_unset']} of them never set here)")
    out.append("  ".join(f"{v}={counts.get(v, 0)}" for v in order))
    out.append("")
    out.append(f"{'id':>7}  {'our name':<26} {'client type':<26} {'send':<6} {'verdict':<11} cards  detail")
    for row in rows:
        out.append(
            f"{row['id']:>7}  {(row['name'] or '-')[:26]:<26} {(row['client_type'] or '-')[:26]:<26} "
            f"{(row['tag'] or '-')[:6]:<6} {row['verdict']:<11} {row['cards']:>5}  {row['detail']}"
        )
    out.append("")
    out.append("client ids no card sets: " + ", ".join(
        f"{k}({table[k]})" for k in sorted(table) if k not in result["emitted"]))
    return "\n".join(out)


def render_sources(result: dict, table: Dict[int, str]) -> str:
    rows = sorted(result["rows"].values(),
                  key=lambda r: (-{"unknown-id": 4, "mismatch": 3, "bad-value": 2,
                                   "unverified": 1, "ok": 0}.get(r["verdict"], 0), r["id"]))
    order = ("unknown-id", "mismatch", "bad-value", "unverified", "ok")
    counts = result["counts"]
    out: List[str] = []
    out.append(f"sources: {counts['attributes']} distinct attribute ids written as literals")
    out.append("  ".join(f"{v}={counts.get(v, 0)}" for v in order))
    out.append("")
    out.append(f"{'id':>7}  {'our name':<26} {'client type':<26} {'send':<6} {'verdict':<11} sites  detail")
    for row in rows:
        out.append(
            f"{row['id']:>7}  {(row['name'] or '-')[:26]:<26} {(row['client_type'] or '-')[:26]:<26} "
            f"{(row['tag'] or '-')[:6]:<6} {row['verdict']:<11} {len(row['sites']):>5}  {row['detail']}"
        )
        if row["verdict"] != "ok":
            out.append("         " + ", ".join(row["sites"][:4]))
    return "\n".join(out)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--table", default=TABLE, help="id -> client CLR type table")
    parser.add_argument("--client", help="client checkout to rebuild the table from")
    parser.add_argument("--write-table", action="store_true",
                        help="with --client, save the rebuilt table")
    parser.add_argument("--scripts-only", action="store_true",
                        help="skip the static pass over the rest of the server")
    parser.add_argument("--report", help="also write this markdown to PATH")
    args = parser.parse_args(argv)

    facts = {}
    if args.client:
        table, facts = parse_client(args.client)
        if args.write_table:
            with open(TABLE, "w", encoding="utf-8") as f:
                json.dump({
                    "_source": {
                        "repository": "decompiled client (private, not committed here)",
                        "derivation": "AttributeDefinition<V>(key) declarations",
                        "commit": os.environ.get("CLIENT_COMMIT", ""),
                        "ids": len(table),
                    },
                    "types": {str(k): v for k, v in sorted(table.items())},
                }, f, indent=1)
                f.write("\n")
    else:
        table = load_client_table(args.table)

    result = audit(table)
    print(render(result, table))
    if facts:
        print("\nclient facts: " + json.dumps(facts))

    failing = result["counts"].get("unknown-id", 0) + result["counts"].get("mismatch", 0) \
        + result["counts"].get("bad-value", 0)

    sections = [render(result, table)]
    if not args.scripts_only:
        sources = audit_sources(table)
        print("\n" + render_sources(sources, table))
        failing += sources["counts"].get("unknown-id", 0) + sources["counts"].get("mismatch", 0) \
            + sources["counts"].get("bad-value", 0)
        sections.append(render_sources(sources, table))

    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            f.write("\n\n".join("```\n" + s + "\n```" for s in sections) + "\n")

    return 1 if failing else 0


if __name__ == "__main__":
    sys.exit(main())
