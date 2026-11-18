"""Dumps the PTCGO client's metadata into a protocol reference.

Reads the shipped assemblies with dnfile (no IL execution, no client needed) and
writes two files under notes/:

    client-metadata.jsonl   every type: base, members, JSON names, attributes
    client-protocol.md      every NetworkMessageEvent DTO as a JSON shape

Usage:
    python tools_client_dump.py                 # all PIE assemblies
    python tools_client_dump.py pie-src.dll     # one assembly
"""
import json
import os
import sys

import dnfile

DEFAULT_DIR = os.path.expanduser(
    "~/Documents/New Folder/game/ptcgo/client/PokemonTradingCardGameOnline/"
    "Pokemon Trading Card Game Online_Data/Managed")
DEFAULT_DLLS = ["pie-src.dll", "pie-core.dll", "sausage-core.dll", "core.dll",
                "ProtobufMessages.dll"]
NOTES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes")

PRIMS = {
    0x01: "void", 0x02: "bool", 0x03: "char", 0x04: "sbyte", 0x05: "byte",
    0x06: "short", 0x07: "ushort", 0x08: "int", 0x09: "uint", 0x0A: "long",
    0x0B: "ulong", 0x0C: "float", 0x0D: "double", 0x0E: "string",
    0x16: "TypedReference", 0x18: "IntPtr", 0x19: "UIntPtr", 0x1C: "object",
}
TABLE = {0x00: "Module", 0x01: "TypeRef", 0x02: "TypeDef", 0x04: "Field",
         0x06: "MethodDef", 0x08: "Param", 0x0A: "MemberRef", 0x11: "StandAloneSig",
         0x1B: "TypeSpec", 0x2B: "MethodSpec", 0x70: "UserString"}


class Cursor:
    def __init__(self, data):
        self.data = data
        self.i = 0

    def byte(self):
        value = self.data[self.i]
        self.i += 1
        return value

    def peek(self):
        return self.data[self.i]

    def compressed(self):
        b = self.byte()
        if b & 0x80 == 0:
            return b
        if b & 0xC0 == 0x80:
            return ((b & 0x3F) << 8) | self.byte()
        return ((b & 0x1F) << 24) | (self.byte() << 16) | (self.byte() << 8) | self.byte()


class Assembly:
    """One assembly's metadata, with names, JSON names and parsed signatures."""

    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.pe = dnfile.dnPE(path)
        t = self.pe.net.mdtables
        self.t = t
        self.typedefs = list(t.TypeDef.rows)
        self.fields = list(t.Field.rows)
        self.methods = list(t.MethodDef.rows)
        self.props = list(getattr(t, "Property").rows) if getattr(t, "Property", None) else []
        self.typedef_names = {}
        self.typeref_names = {}
        self.enclosing = {}
        self.field_owner = {}
        self.method_owner = {}
        self.json_names = {}      # field row -> json key
        self.field_attrs = {}     # field row -> [attribute names]
        self.type_attrs = {}      # typedef row -> [attr names]
        self._index()

    # ------------------------------------------------------------------ index
    def _index(self):
        for i, row in enumerate(self.typedefs, start=1):
            self.typedef_names[i] = self._full_name(row)
        if getattr(self.t, "TypeRef", None):
            for i, row in enumerate(self.t.TypeRef.rows, start=1):
                self.typeref_names[i] = self._full_name(row)
        if getattr(self.t, "NestedClass", None):
            for row in self.t.NestedClass.rows:
                self.enclosing[row.NestedClass.row_index] = row.EnclosingClass.row_index
        for i, row in enumerate(self.typedefs, start=1):
            if row.FieldList:
                begin = row.FieldList[0].row_index
                end = next((r.FieldList[0].row_index for r in self.typedefs[i:] if r.FieldList),
                           len(self.fields) + 1)
                for fi in range(begin, end):
                    self.field_owner[fi] = i
            if row.MethodList:
                begin = row.MethodList[0].row_index
                end = next((r.MethodList[0].row_index for r in self.typedefs[i:] if r.MethodList),
                           len(self.methods) + 1)
                for mi in range(begin, end):
                    self.method_owner[mi] = i
        self._read_attributes()

    def _read_attributes(self):
        if not getattr(self.t, "CustomAttribute", None):
            return
        for ca in self.t.CustomAttribute.rows:
            parent_table = getattr(ca.Parent.table, "name", "")
            row = ca.Parent.row_index
            attr_name = self._attr_type_name(ca.Type)
            args = self._attr_strings(ca.Value.value if ca.Value else b"")
            if parent_table == "Field":
                if attr_name.endswith("JsonNameAttribute") and args:
                    self.json_names[row] = args[0]
                if attr_name:
                    self.field_attrs.setdefault(row, []).append(
                        ".".join(part for part in (attr_name.rsplit(".", 1)[-1], *args) if part))
            elif parent_table == "TypeDef":
                self.type_attrs.setdefault(row, []).append(".".join(
                    part for part in (attr_name, *args) if part))

    def _attr_type_name(self, coded):
        table = getattr(coded.table, "name", "")
        if table == "TypeRef":
            return self.typeref_names.get(coded.row_index, "")
        if table == "MemberRef":
            mr = self.t.MemberRef.rows[coded.row_index - 1]
            cls = mr.Class
            if getattr(cls.table, "name", "") == "TypeRef":
                return self.typeref_names.get(cls.row_index, "")
            return ""
        return ""

    @staticmethod
    def _attr_strings(data):
        if len(data) < 4:
            return []
        c = Cursor(data)
        c.i = 2
        try:
            length = c.compressed()
            return [data[c.i:c.i + length].decode("utf-8", "replace")]
        except Exception:
            return []

    @staticmethod
    def _full_name(row):
        ns = str(row.TypeNamespace or "")
        name = str(row.TypeName or "")
        return f"{ns}.{name}" if ns else name

    # ------------------------------------------------------------------ types
    def nested_name(self, position):
        if not position:
            return None
        chain = [self.typedef_names.get(position, f"<row {position}>")]
        while position in self.enclosing:
            position = self.enclosing[position]
            chain.append(self.typedef_names.get(position, f"<row {position}>"))
        return "+".join(reversed(chain))

    def type_name(self, coded):
        table = getattr(coded.table, "name", "")
        if table == "TypeDef":
            return self.nested_name(coded.row_index)
        if table == "TypeRef":
            return self.typeref_names.get(coded.row_index, "")
        return ""

    def resolve_coded(self, coded):
        """TypeDefOrRef coded index from a signature blob -> CLR name."""
        tag = coded & 0x3
        index = coded >> 2
        if tag == 0:
            return self.nested_name(index) if index else ""
        if tag == 1:
            return self.typeref_names.get(index, f"<TypeRef {index}>")
        return f"<TypeSpec {index}>"

    def parse_type(self, c):
        while c.peek() in (0x1F, 0x20):
            c.byte()
            c.compressed()
        et = c.byte()
        if et in PRIMS:
            return {"kind": "prim", "name": PRIMS[et]}
        if et in (0x11, 0x12):
            return {"kind": "class", "name": self.resolve_coded(c.compressed())}
        if et == 0x15:
            c.byte()
            raw = self.resolve_coded(c.compressed())
            count = c.compressed()
            args = [self.parse_type(c) for _ in range(count)]
            short = raw.rsplit(".", 1)[-1]
            if short.startswith("Nullable"):
                return {**args[0], "nullable": True}
            if short.startswith("Dictionary"):
                return {"kind": "dict", "key": args[0], "value": args[1] if len(args) > 1 else None}
            return {"kind": "list", "of": args[0] if args else None}
        if et == 0x1D:
            return {"kind": "list", "of": self.parse_type(c)}
        if et == 0x14:
            inner = self.parse_type(c)
            c.compressed()
            for _ in range(c.compressed()):
                c.compressed()
            for _ in range(c.compressed()):
                c.compressed()
            return {"kind": "list", "of": inner}
        if et == 0x0F:
            return self.parse_type(c)
        if et in (0x13, 0x1E):
            return {"kind": "var", "index": c.compressed()}
        if et == 0x1B:
            c.compressed()
            return {"kind": "fnptr"}
        return {"kind": "unknown", "element": et}

    def field_signature(self, row):
        c = Cursor(row.Signature.value)
        c.byte()
        return self.parse_type(c)

    def property_signature(self, row):
        c = Cursor(row.Type.value)
        c.byte()
        c.compressed()
        return self.parse_type(c)

    def method_signature(self, row):
        if not getattr(row, "Signature", None):
            return None
        c = Cursor(row.Signature.value)
        c.byte()
        generic = c.compressed()
        count = c.compressed()
        ret = self.parse_type(c)
        params = [self.parse_type(c) for _ in range(count)]
        return {"returns": ret, "params": params, "generic_params": generic}

    # ---------------------------------------------------------------- members
    def members(self, position, include_private=False):
        out = {"fields": [], "properties": [], "methods": []}
        row = self.typedefs[position - 1]
        if row.FieldList:
            begin = row.FieldList[0].row_index
            end = next((r.FieldList[0].row_index for r in self.typedefs[position:] if r.FieldList),
                       len(self.fields) + 1)
            for fi in range(begin, end):
                field = self.fields[fi - 1]
                name = str(field.Name)
                if name.startswith("<") or name == "value__":
                    continue
                if name.startswith("_") and not include_private:
                    continue
                try:
                    typ = self.field_signature(field)
                except Exception:
                    typ = {"kind": "unparsed"}
                out["fields"].append({
                    "row": fi,
                    "name": name,
                    "json": self.json_names.get(fi, name),
                    "type": typ,
                    "attributes": self.field_attrs.get(fi, []),
                })
        if row.MethodList:
            begin = row.MethodList[0].row_index
            end = next((r.MethodList[0].row_index for r in self.typedefs[position:] if r.MethodList),
                       len(self.methods) + 1)
            for mi in range(begin, end):
                method = self.methods[mi - 1]
                try:
                    sig = self.method_signature(method)
                except Exception:
                    sig = None
                out["methods"].append({"row": mi, "name": str(method.Name),
                                       "rva": getattr(method, "Rva", 0), "signature": sig})
        if getattr(self.t, "PropertyMap", None):
            for mapping in self.t.PropertyMap.rows:
                if mapping.Parent.row_index != position:
                    continue
                for index in mapping.PropertyList:
                    prop = self.props[index.row_index - 1]
                    try:
                        typ = self.property_signature(prop)
                    except Exception:
                        typ = {"kind": "unparsed"}
                    out["properties"].append({"name": str(prop.Name), "type": typ})
        return out

    def base_name(self, position):
        row = self.typedefs[position - 1]
        ext = row.Extends
        if ext is None or not hasattr(ext, "row_index"):
            return None
        table = getattr(getattr(ext, "table", None), "name", "")
        if table == "TypeDef":
            return self.nested_name(ext.row_index) if ext.row_index else None
        if table == "TypeRef":
            return self.typeref_names.get(ext.row_index)
        return None

    def enum_values(self, position, depth=0):
        row = self.typedefs[position - 1]
        if not row.FieldList or depth > 1:
            return None
        if self.base_name(position) != "System.Enum":
            return None
        values = []
        begin = row.FieldList[0].row_index
        end = next((r.FieldList[0].row_index for r in self.typedefs[position:] if r.FieldList),
                   len(self.fields) + 1)
        for fi in range(begin, end):
            name = str(self.fields[fi - 1].Name)
            if name != "value__":
                values.append(name)
        return values

    def find(self, fragment):
        return [i for i, name in self.typedef_names.items() if fragment.lower() in name.lower()]


def type_label(typ):
    if not typ:
        return "?"
    kind = typ.get("kind")
    nullable = "?" if typ.get("nullable") else ""
    if kind == "prim":
        return typ["name"] + nullable
    if kind == "class":
        return typ["name"] + nullable
    if kind == "list":
        return f"List<{type_label(typ.get('of'))}>"
    if kind == "dict":
        return f"Map<{type_label(typ.get('key'))}, {type_label(typ.get('value'))}>"
    if kind == "var":
        return f"!{typ.get('index')}"
    return kind or "?"


class Protocol:
    """Collects message DTOs and renders their JSON shape."""

    def __init__(self, assemblies):
        self.assemblies = assemblies
        self.by_name = {}
        for asm in assemblies:
            for position, name in asm.typedef_names.items():
                self.by_name.setdefault(name, (asm, position))
                nested = asm.nested_name(position)
                if nested:
                    self.by_name.setdefault(nested, (asm, position))

    def resolve(self, name):
        return self.by_name.get(name)

    def is_message(self, asm, position):
        seen = 0
        base = asm.base_name(position)
        while base and seen < 6:
            if base.endswith("NetworkMessageEvent"):
                return True
            found = self.resolve(base)
            if not found:
                return False
            asm, position = found
            base = asm.base_name(position)
            seen += 1
        return False

    def ancestry(self, name, limit=6):
        current = name
        out = []
        for _ in range(limit):
            found = self.resolve(current)
            if not found:
                break
            asm, position = found
            base = asm.base_name(position)
            if not base:
                break
            out.append(base)
            current = base
        return out

    def label_for(self, typ):
        if typ and typ.get("kind") == "class":
            if "dwd.core.ids.TypedID" in self.ancestry(typ["name"]):
                return "Guid"
        return type_label(typ)

    def shape(self, typ, depth=0, seen=None):
        seen = seen or set()
        if not typ:
            return None
        kind = typ.get("kind")
        if kind == "prim":
            return {"type": typ["name"], **({"nullable": True} if typ.get("nullable") else {})}
        if kind == "list":
            return {"list": self.shape(typ.get("of"), depth + 1, seen)}
        if kind == "dict":
            return {"map": {"key": self.label_for(typ.get("key")),
                            "value": self.shape(typ.get("value"), depth + 1, seen)}}
        if kind != "class":
            return {"type": type_label(typ)}
        name = typ["name"]
        if "dwd.core.ids.TypedID" in self.ancestry(name):
            return {"type": "Guid"}          # TypedID carries a System.Guid, sent as a string
        found = self.resolve(name)
        if not found or depth > 7 or name in seen:
            return {"type": name}
        asm, position = found
        values = asm.enum_values(position)
        if values is not None:
            return {"enum": name, "values": values}
        members = asm.members(position)
        names = {m["name"] for m in members["methods"]}
        base = asm.base_name(position) or ""
        if "Dictionary" in base or ("get_Item" in names and "get_Count" in names):
            value = None
            for prop in members["properties"]:
                if prop["name"] == "Item":
                    value = prop["type"]
            return {"map": {"key": "string", "value": self.shape(value, depth + 1, seen) if value else None}}
        fields = {}
        for field in members["fields"]:
            fields[field["json"]] = self.shape(field["type"], depth + 1, seen | {name})
        if not fields:
            for field in asm.members(position, include_private=True)["fields"]:
                fields[field["json"].lstrip("_")] = self.shape(field["type"], depth + 1, seen | {name})
        if not fields:
            for parent in self.ancestry(name, limit=3):
                found_parent = self.resolve(parent)
                if not found_parent:
                    continue
                parent_fields = found_parent[0].members(found_parent[1], include_private=True)["fields"]
                if parent_fields:
                    for field in parent_fields:
                        fields[field["json"].lstrip("_")] = self.shape(
                            field["type"], depth + 1, seen | {name})
                    break
        if not fields:
            return {"type": name}
        return {"type": name, "fields": fields}


def shape_json(shape):
    if not shape:
        return None
    if "list" in shape:
        return [shape_json(shape["list"])]
    if "map" in shape:
        return {"<key>": shape_json(shape["map"]["value"])}
    if "enum" in shape:
        return " | ".join(shape["values"])
    if "fields" in shape:
        return {key: shape_json(value) for key, value in shape["fields"].items()}
    return shape.get("type", "?")


def simple_name(name):
    return name.rsplit(".", 1)[-1].split("+")[-1]


def sample_value(shape, depth=0):
    """A minimal value of this shape: empty lists/maps, zeroed scalars."""
    if not shape:
        return None
    if "list" in shape:
        return []
    if "map" in shape:
        return {}
    if "enum" in shape:
        return shape["values"][0] if shape["values"] else None
    if "fields" in shape:
        if depth > 3:
            return {}
        return {key: sample_value(value, depth + 1) for key, value in shape["fields"].items()}
    type_name = shape.get("type", "")
    if type_name in ("int", "long", "short", "byte", "sbyte", "uint", "ulong", "ushort"):
        return 0
    if type_name == "bool":
        return False
    if type_name == "double" or type_name == "float":
        return 0.0
    if type_name == "string":
        return ""
    return None


def render_shape(shape, indent=0):
    pad = "  " * indent
    if shape is None:
        return "null"
    if "list" in shape:
        inner = render_shape(shape["list"], indent + 1)
        if "\n" in inner or inner.startswith("{"):
            return "[\n" + "  " * (indent + 1) + inner + "\n" + pad + "]"
        return f"[{inner}]"
    if "map" in shape:
        key_type = shape["map"]["key"]
        value = shape["map"]["value"]
        inner = render_shape(value, indent + 1) if value else "null"
        return "{\n" + pad + f'  "<{key_type} key>": ' + inner + "\n" + pad + "}"
    if "enum" in shape:
        return '"' + " | ".join(shape["values"]) + '"'
    if "fields" in shape:
        lines = [f'{pad}  "{key}": {render_shape(value, indent + 1)}'
                 for key, value in shape["fields"].items()]
        return "{\n" + ",\n".join(lines) + "\n" + pad + "}"
    return f"<{shape.get('type', '?')}>"


def _inner_name(shape):
    if not shape:
        return "?"
    if "type" in shape:
        return shape["type"] + ("?" if shape.get("nullable") else "")
    return type_label(shape)


def main():
    targets = sys.argv[1:] or DEFAULT_DLLS
    assemblies = []
    for name in targets:
        path = name if os.path.isabs(name) else os.path.join(DEFAULT_DIR, name)
        if not os.path.exists(path):
            print(f"skip missing {path}")
            continue
        print(f"reading {os.path.basename(path)}")
        assemblies.append(Assembly(path))

    os.makedirs(NOTES, exist_ok=True)

    # ---------------------------------------------------- full metadata dump
    meta_path = os.path.join(NOTES, "client-metadata.jsonl")
    types = 0
    with open(meta_path, "w", encoding="utf-8") as out:
        for asm in assemblies:
            for position in asm.typedef_names:
                members = asm.members(position)
                record = {
                    "assembly": asm.name,
                    "name": asm.nested_name(position),
                    "base": asm.base_name(position),
                    "attributes": asm.type_attrs.get(position, []),
                    "fields": [
                        {"name": f["name"], "json": f["json"], "type": type_label(f["type"]),
                         "attributes": [a for a in f.get("attributes", [])]}
                        for f in members["fields"]],
                    "properties": [
                        {"name": p["name"], "type": type_label(p["type"])}
                        for p in members["properties"]],
                    "methods": [
                        {"name": m["name"], "returns": type_label((m["signature"] or {}).get("returns")),
                         "params": [type_label(p) for p in (m["signature"] or {}).get("params", [])]}
                        for m in members["methods"] if not m["name"].startswith("<")],
                    "enumValues": asm.enum_values(position) or [],
                }
                out.write(json.dumps(record, ensure_ascii=False) + "\n")
                types += 1
    print(f"wrote {meta_path}: {types} types")

    # ------------------------------------------------------ protocol document
    protocol = Protocol(assemblies)
    messages = []
    for asm in assemblies:
        for position in asm.typedef_names:
            if protocol.is_message(asm, position):
                messages.append((asm.nested_name(position), asm.members(position)))
    messages.sort(key=lambda item: item[0])

    proto_path = os.path.join(NOTES, "client-protocol.md")
    with open(proto_path, "w", encoding="utf-8") as out:
        out.write("# PTCGO client protocol — message DTOs\n\n")
        out.write("Generated by `tools_client_dump.py` from the shipped assemblies. "
                  "Each block is the JSON the client will accept for that message: keys are "
                  "`JsonName` values where declared (lowercase by convention), otherwise the "
                  "CLR member name, and `A | B | C` is an enum's allowed names. "
                  "Types in `<...>` are DTOs declared elsewhere in this file.\n\n")
        out.write(f"- assemblies: {', '.join(asm.name for asm in assemblies)}\n")
        out.write(f"- message types: {len(messages)}\n\n")
        out.write("## Index\n\n")
        for name, _ in messages:
            anchor = name.replace(".", "").replace("+", "-").lower()
            out.write(f"- [{name}](#{anchor})\n")
        out.write("\n")
        for name, members in messages:
            out.write(f"## {name}\n\n")
            out.write("```json\n")
            shape = {"type": name, "fields": {
                f["json"]: protocol.shape(f["type"], 1, {name}) for f in members["fields"]}}
            out.write(render_shape(shape) + "\n")
            out.write("```\n\n")
    print(f"wrote {proto_path}: {len(messages)} messages")

    try:
        from ptcgo.network.message_names import InboundMsg, OutboundMsg
        inbound = {m.value for m in InboundMsg}
        outbound = {m.value for m in OutboundMsg}
    except Exception:
        inbound, outbound = set(), set()

    def direction(full_name, simple_name):
        lowered = full_name.lower()
        if ".outgoing." in lowered:
            return "client → server"
        if ".incoming." in lowered:
            return "server → client"
        if simple_name in inbound:
            return "client → server"
        if simple_name in outbound:
            return "server → client"
        return "unclassified"

    # effect classes: they ride inside game payloads, so their shapes matter too
    effect_rows = []
    for asm in assemblies:
        for position in asm.typedef_names:
            if any("DwdJsonEffect" in attr for attr in asm.type_attrs.get(position, [])):
                effect_rows.append((asm.nested_name(position), asm.members(position)))
    effect_rows.sort(key=lambda item: item[0])
    if effect_rows:
        effects_path = os.path.join(NOTES, "client-effects.md")
        with open(effects_path, "w", encoding="utf-8") as out:
            out.write("# Client effect payloads\n\n")
            out.write("Types carrying `[DwdJsonEffect]`: they are serialised inside game "
                      "messages (entity moves, attack effects, data carriers), so their keys "
                      "have to match exactly as well. Shapes are rendered the same way as "
                      "`client-protocol.md`.\n\n")
            out.write(f"- effect types: **{len(effect_rows)}**\n\n")
            for name, members in effect_rows:
                shape = {"type": name, "fields": {
                    f["json"]: protocol.shape(f["type"], 1, {name}) for f in members["fields"]}}
                out.write(f"## {simple_name(name)}\n\n```json\n{render_shape(shape)}\n```\n\n")
        print(f"wrote {effects_path}: {len(effect_rows)} effect types")

    # minimal payloads, for implementing a handler in one copy-paste
    skeletons = os.path.join(NOTES, "client-skeletons.md")
    with open(skeletons, "w", encoding="utf-8") as out:
        out.write("# Minimal payloads per message\n\n")
        out.write("Generated by `tools_client_dump.py`: for every message the client "
                  "deserialises, the smallest payload of the right shape — scalars zeroed, "
                  "lists and maps empty, nested objects present. These are shapes, not "
                  "valid game states: a field the client dereferences may still need a real "
                  "value.\n\n")
        for name, members in messages:
            shape = {"type": name, "fields": {
                f["json"]: protocol.shape(f["type"], 1, {name}) for f in members["fields"]}}
            out.write(f"## {simple_name(name)}\n\n```json\n")
            out.write(json.dumps({"messageName": simple_name(name),
                                  **sample_value(shape)}, indent=2, ensure_ascii=False))
            out.write("\n```\n\n")
    print(f"wrote {skeletons}: {len(messages)} payloads")

    index_path = os.path.join(NOTES, "client-messages.md")
    with open(index_path, "w", encoding="utf-8") as out:
        out.write("# Client message index\n\n")
        out.write("One line per message type with its direction and top-level JSON keys. "
                  "Direction comes from the client's own `incoming`/`outgoing` namespaces, "
                  "otherwise from this server's InboundMsg/OutboundMsg enums. Full shapes "
                  "are in `client-protocol.md`.\n\n")
        for name, members in messages:
            keys = ", ".join(f"`{f['json']}`" for f in members["fields"]) or "_no fields_"
            out.write(f"- **{name}** _({direction(name, name.rsplit('.', 1)[-1])})_ — {keys}\n")
    print(f"wrote {index_path}: {len(messages)} messages")

    json_path = os.path.join(NOTES, "client-protocol.json")
    with open(json_path, "w", encoding="utf-8") as out:
        payload = {
            "assemblies": [asm.name for asm in assemblies],
            "messages": {
                name: {f["json"]: shape_json(protocol.shape(f["type"], 1, {name}))
                       for f in members["fields"]}
                for name, members in messages
            },
        }
        json.dump(payload, out, indent=1, ensure_ascii=False)
    print(f"wrote {json_path}")

    # every enum, for reference
    enum_path = os.path.join(NOTES, "client-enums.md")
    rows = []
    for asm in assemblies:
        for position, name in asm.typedef_names.items():
            values = asm.enum_values(position)
            if values:
                rows.append((asm.nested_name(position), values))
    rows.sort()
    with open(enum_path, "w", encoding="utf-8") as out:
        out.write("# PTCGO client enums\n\n")
        out.write(f"{len(rows)} enums, read from the assemblies by `tools_client_dump.py`.\n\n")
        for name, values in rows:
            out.write(f"- **{name}** — {', '.join(values)}\n")
    print(f"wrote {enum_path}: {len(rows)} enums")


if __name__ == "__main__":
    main()
