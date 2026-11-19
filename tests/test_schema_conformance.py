"""The client's attribute type contract, and the checker that reads it.

`AttributeAnalyzer` deserializes an attribute against its own definition's CLR type
and `MutableAttribute<V>` casts `(V)value`; `ProtobufExtensions.TryToIAttribute`
does the same through `ToObject` and swallows the failure, dropping the attribute.
So a value of the wrong wire type is either an exception or a silent drop. These
tests pin the rule table, and prove the checker reports both directions -- a tool
that only ever says "ok" is worse than no tool.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ptcgo.tools import schema_conformance as sc

TABLE = {
    10140: "LocalizableText",
    200490: "int?",
    200570: "PokemonTypes[]",
    200300: "CardTypes?",
    200780: "int?",
    10000: "ArchetypeID",
    201640: "ArchetypeID",
    201100: "float?",
    10560: "long?",
    200610: "FoilEffects?",
    201505: "ArchetypeID[]",
}


def v(attr_id, tag, value):
    return sc.verdict(attr_id, tag, value, TABLE)[0]


class Verdicts(unittest.TestCase):
    def test_a_correct_pair_passes(self):
        self.assertEqual(v(200490, "int", 120), "ok")
        self.assertEqual(v(10140, "json", '{"id": "name"}'), "ok")
        self.assertEqual(v(200300, "int", 0), "ok")
        self.assertEqual(v(200570, "json", '["FIRE"]'), "ok")
        self.assertEqual(v(201640, "uuid", "0430a361-71fc-5cbc-ac62-f324e5b32c40"), "ok")
        self.assertEqual(v(201100, "float", 0.5), "ok")

    def test_an_id_the_client_does_not_define_is_flagged(self):
        self.assertEqual(v(999999, "int", 1), "unknown-id")

    def test_a_wrong_wire_type_is_flagged(self):
        # int where the client declared a string, string where it declared an int
        self.assertEqual(v(200490, "string", "120"), "mismatch")
        self.assertEqual(v(200300, "string", "Pokemon"), "mismatch")
        # a LocalizableText is JSON, never a protobuf STRING
        self.assertEqual(v(10140, "string", "Charizard"), "mismatch")
        # a typed id cannot travel as a protobuf STRING: ToObject returns the raw
        # string and the factory's (ArchetypeID)value cast throws, so it is dropped
        self.assertEqual(v(10000, "string", "0430a361-71fc-5cbc-ac62-f324e5b32c40"),
                         "mismatch")

    def test_a_long_cannot_travel_as_a_protobuf_int(self):
        # ToObject turns an INT object into an Int32, which (long)(object) cannot take
        self.assertEqual(v(10560, "int", 1760000000), "mismatch")
        self.assertEqual(v(10560, "json", "1760000000"), "ok")

    def test_values_that_do_not_fit_the_wire_field_are_flagged(self):
        self.assertEqual(v(200780, "int", 2 ** 31), "bad-value")
        self.assertEqual(v(10140, "json", "not json"), "bad-value")
        self.assertEqual(v(201640, "uuid", "nope"), "bad-value")

    def test_an_opaque_client_type_is_unverified_rather_than_ok(self):
        self.assertEqual(v(201040, "json", "{}"), "unknown-id")
        table = {201040: "f"}
        self.assertEqual(sc.verdict(201040, "json", "{}", table)[0], "unverified")


class Table(unittest.TestCase):
    def test_the_committed_table_carries_the_client_types(self):
        table = sc.load_client_table()
        self.assertGreaterEqual(len(table), 180)
        # spot checks against decompiled/pie-src/P/F.cs and CoreAttributes.cs
        self.assertEqual(table[200490], "int?")       # HP
        self.assertEqual(table[10140], "LocalizableText")  # Name
        self.assertEqual(table[201870], "EntityID[]")  # playmat attack sources
        self.assertEqual(table[200740], "PieAbilityDescription[]")  # abilities

    def test_guid_wrappers_accept_a_uuid_and_a_json_string_only(self):
        self.assertEqual(sc.expected_wires("ArchetypeID"), {"UUID", "JSON"})
        self.assertEqual(sc.expected_wires("PokemonStage?"), {"INT"})
        self.assertEqual(sc.expected_wires("LocalizableText[]"), {"JSON"})
        self.assertEqual(sc.expected_wires("f"), set())


if __name__ == "__main__":
    unittest.main()
