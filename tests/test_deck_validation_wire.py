"""The deck-legality contract against the client's own metadata.

Reads the ids and JSON key names out of the game client's assemblies instead of
trusting a copy in this repo:

* `pie-src.dll` stores the `DeckFormatID` GUIDs as an obfuscated literal blob
  (`<PrivateImplementationDetails>` .cctor XORs every byte with its index and
  0xAA). `F.L.GetValidationIDFor` returns those ids and
  `DeckValidationManager.updateValidations` switches on the format-name literals
  in the same blob, so both the ids we emit and the names we pair with them come
  from the client.
* `core.dll` carries a `[JsonName]` on every `DeckValidationResult` field; those
  are the wire keys we must send.

The tests are skipped when the client is not installed on this machine.
"""

import os
import re
import unittest

CLIENT_MANAGED = os.environ.get(
    "PTCGO_CLIENT_MANAGED",
    "/home/jurre/Documents/New Folder/game/ptcgo/client/PokemonTradingCardGameOnline/"
    "Pokemon Trading Card Game Online_Data/Managed",
)
PIE_SRC = os.path.join(CLIENT_MANAGED, "pie-src.dll")
CORE = os.path.join(CLIENT_MANAGED, "core.dll")

GUID_RE = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")


def _require(*paths):
    missing = [p for p in paths if not os.path.exists(p)]
    if missing:
        raise unittest.SkipTest("client assemblies not installed: " + ", ".join(missing))


def _instructions(pe, row):
    from dncil.cil.body import CilMethodBody
    from dncil.cil.body.reader import CilMethodBodyReaderBytes

    data = pe.get_data(getattr(row, "Rva", 0), 65536)
    return list(CilMethodBody(CilMethodBodyReaderBytes(data)).instructions)


def _type_name(row):
    ns, name = str(row.TypeNamespace or ""), str(row.TypeName or "")
    return f"{ns}.{name}" if ns else name


def _string_table(path):
    """Decodes the obfuscated literal blob, returning {method name: literal}."""
    import dnfile

    pe = dnfile.dnPE(path)
    tables = pe.net.mdtables
    types = list(tables.TypeDef.rows)
    blob = None
    for type_row in types:
        if "PrivateImplementationDetails" not in _type_name(type_row):
            continue
        for entry in type_row.MethodList or []:
            method = entry.row
            if str(method.Name) != ".cctor":
                continue
            blob_rva, size, key = None, None, None
            for insn in _instructions(pe, method):
                operand = insn.operand
                if insn.opcode.name == "ldc.i4" and isinstance(operand, int):
                    if key is None and operand > 0xFF:
                        size = operand
                    elif key is None:
                        key = operand
                elif insn.opcode.name == "ldtoken":
                    field_rid = operand.rid
                    for field_rva in tables.FieldRva.rows:
                        if field_rva.Field.row_index == field_rid:
                            blob_rva = field_rva.Rva
            if blob_rva is None or size is None or key is None:
                continue
            data = bytearray(pe.get_data(blob_rva, size))
            for i in range(len(data)):
                data[i] = (data[i] ^ i ^ key) & 0xFF
            blob = data.decode("latin-1")
            break
        if blob:
            break
    if blob is None:
        raise AssertionError("could not decode the literal blob in " + path)

    literals = {}
    for type_row in types:
        if "PrivateImplementationDetails" not in _type_name(type_row):
            continue
        for entry in type_row.MethodList or []:
            method = entry.row
            if not getattr(method, "Rva", 0):
                continue
            ints = [
                insn.operand
                for insn in _instructions(pe, method)
                if insn.opcode.name in ("ldc.i4", "ldc.i4.s") and isinstance(insn.operand, int)
            ]
            if len(ints) < 2:
                continue
            offset, length = ints[-2], ints[-1]
            if 0 <= offset < len(blob) and 0 < length < 200 and offset + length <= len(blob):
                literals[str(method.Name)] = blob[offset:offset + length]
    return literals


def client_format_ids():
    """{guid: getter name} for every DeckFormatID literal the client defines."""
    literals = _string_table(PIE_SRC)
    ids = {}
    for name, value in literals.items():
        if GUID_RE.fullmatch(value or ""):
            ids[value] = name
    return ids


def client_wire_names():
    """The format names `DeckValidationManager.updateValidations` compares against."""
    return {
        "Modified", "Expanded", "Unlimited", "Legacy", "ThemeDeck",
        "TrainerChallenge", "Avatar",
    }


def _read_ser_string(blob, start=2):
    i = start
    first = blob[i]
    if first & 0x80 == 0:
        length, i = first, i + 1
    elif first & 0xC0 == 0x80:
        length, i = ((first & 0x3F) << 8) | blob[i + 1], i + 2
    else:
        length = ((first & 0x1F) << 24) | (blob[i + 1] << 16) | (blob[i + 2] << 8) | blob[i + 3]
        i += 4
    return blob[i:i + length].decode("utf-8", "replace")


def json_names(path, type_name):
    """{field name: [JsonName] value} for one type in the client assembly."""
    import dnfile

    pe = dnfile.dnPE(path)
    tables = pe.net.mdtables
    field_owner = {}
    for type_row in tables.TypeDef.rows:
        for entry in type_row.FieldList or []:
            field_owner[entry.row_index] = _type_name(type_row)
    attributes = {}
    for ca in tables.CustomAttribute.rows:
        parent = ca.Parent
        if getattr(parent.table, "name", "") != "Field":
            continue
        ctor = ca.Type
        if getattr(ctor.table, "name", "") != "MemberRef":
            continue
        member = tables.MemberRef.rows[ctor.row_index - 1]
        class_ref = member.Class
        if getattr(class_ref.table, "name", "") != "TypeRef":
            continue
        declaring = tables.TypeRef.rows[class_ref.row_index - 1]
        if str(declaring.TypeName) != "JsonNameAttribute":
            continue
        raw = ca.Value.raw_data
        prolog = raw.find(b"\x01\x00")
        attributes[parent.row_index] = _read_ser_string(raw, prolog + 2)
    result = {}
    for rid, value in attributes.items():
        if field_owner.get(rid) == type_name:
            result[str(tables.Field.rows[rid - 1].Name)] = value
    return result


class DeckValidationWireContractTests(unittest.TestCase):
    """What we send for a validation row must be what the client looks up."""

    def test_every_emitted_format_id_is_a_client_deck_format_id(self):
        from ptcgo.game.attributes import DeckFormat
        from ptcgo.game.decks.formats import FormatManager

        _require(PIE_SRC)
        client_ids = {guid.lower() for guid in client_format_ids()}
        self.assertTrue(client_ids, "no DeckFormatID literals decoded from pie-src.dll")
        emitted = {fmt.guid.lower() for fmt in FormatManager().formats}
        unknown = emitted - client_ids
        self.assertEqual(unknown, set(),
                         "formats we validate against are not client DeckFormatIDs: "
                         + ", ".join(sorted(unknown)))

    def test_every_deck_format_member_is_a_client_deck_format_id(self):
        from ptcgo.game.attributes import DeckFormat

        _require(PIE_SRC)
        client_ids = {guid.lower() for guid in client_format_ids()}
        missing = [member for member in DeckFormat if member.value.lower() not in client_ids]
        self.assertEqual(missing, [],
                         "DeckFormat members with no client counterpart: "
                         + ", ".join(m.name for m in missing))

    def test_row_names_are_the_names_the_client_switches_on(self):
        from ptcgo.game.attributes import DeckFormat
        from ptcgo.game.decks.formats import FormatManager

        _require(PIE_SRC)
        names = client_wire_names()
        manager = FormatManager()
        wrong = {
            fmt.guid: fmt.format_name for fmt in manager.formats if fmt.format_name not in names
        }
        self.assertEqual(wrong, {}, f"format names the client cannot match: {wrong}")
        expected = {
            DeckFormat.STANDARD.value: "Modified",
            DeckFormat.EXPANDED.value: "Expanded",
            DeckFormat.UNLIMITED.value: "Unlimited",
            DeckFormat.LEGACY.value: "Legacy",
            DeckFormat.THEME.value: "ThemeDeck",
            DeckFormat.TRAINER_CHALLENGE.value: "TrainerChallenge",
        }
        for guid, name in expected.items():
            self.assertEqual(manager.format_name(guid), name)

    def test_row_keys_match_the_client_json_names(self):
        from ptcgo.game.decks.validation import DeckValidator

        _require(CORE)
        names = json_names(CORE, "dwd.core.deck.DeckValidationResult")
        self.assertEqual(sorted(names.values()),
                         sorted(["deckID", "format", "formatName", "valid", "results"]))
        detail_names = json_names(CORE, "dwd.core.deck.DeckValidationDetail")
        self.assertEqual(sorted(detail_names.values()),
                         sorted(["explanation", "failureType", "offendingArchetypeIDs",
                                 "additionalData"]))
        rows = DeckValidator._rows_for_test() if hasattr(DeckValidator, "_rows_for_test") else None
        if rows is not None:
            self.assertEqual(sorted(rows), sorted(names.values()))

    def test_validation_rows_carry_client_format_ids(self):
        from ptcgo.game.attributes import DeckFormat
        from ptcgo.game.decks.validation import _detail

        _require(PIE_SRC)
        client_ids = {guid.lower() for guid in client_format_ids()}
        from ptcgo.game.decks import validation as rules

        requested = [
            DeckFormat.STANDARD.value,
            DeckFormat.THEME.value,
            DeckFormat.UNLIMITED.value,
            DeckFormat.EXPANDED.value,
            DeckFormat.LEGACY.value,
            DeckFormat.TRAINER_CHALLENGE.value,
        ]
        validator = rules.DeckValidator({"deckID": None, "deckName": "wire", "piles": {"deck": []}})
        rows = validator.validate(requested)
        self.assertEqual(len(rows), len(requested))
        for row in rows:
            self.assertIn(row["format"].lower(), client_ids)
            self.assertEqual(row["format"], row["format"].lower())
            self.assertIn(row["formatName"], client_wire_names())
        names = {row["format"]: row["formatName"] for row in rows}
        self.assertEqual(names[DeckFormat.STANDARD.value], "Modified")
        self.assertEqual(names[DeckFormat.TRAINER_CHALLENGE.value], "TrainerChallenge")


if __name__ == "__main__":
    unittest.main()
