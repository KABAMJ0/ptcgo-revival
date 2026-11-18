"""Every localization id the server sends must be one the client can draw.

The client draws a LocalizableText by looking its id up in its own localization
database (core.dll `LocalizationLookup.Localize`: the value for `id.ToLower()`, or
the id itself when there is none). So a key the database lacks is printed as the
key — the "series.base" a player saw — while an id that is not a key at all is
printed as the text, which is why plain text is the right fallback.

Two families have to hold:

* Ids the client derives. It builds `series.<block>` from a set's block and the
  set label from `<template>.<code>`, so the value we send is only as good as the
  key it lands on. `custom_labels.json` supplies the ones the client ships without.
* Ids we write. Each `{"id": ...}` in a packet, the strings handed to a handler's
  message argument, and the data-driven ones (prompts, scenarios, quests, league
  opponents, redemption reasons) must be either a key the client holds or plain
  text.

The check reads the client's own LocalizationDB, which ships in the repository,
alongside the labels the localization handler serves on top of it.
"""

import unittest

from ptcgo.tools import localization_keys as keys


class LocalizationIdsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = keys.client_keys()
        cls.served = keys.served_keys()
        cls.rows = keys.audit(cls.client, cls.served)
        cls.bad = keys.problems(cls.rows)

    def test_every_emitted_id_resolves(self):
        offenders = "\n".join(
            f"  {row['surface']}: {row['id']} ({row['source']})" for row in self.bad)
        self.assertEqual([], [f"{r['surface']}: {r['id']}" for r in self.bad], offenders)

    def test_reported_series_label_resolves(self):
        """series.base is the id that started this: the client derives it from a
        set block, and it must not reach a player as a raw key."""
        for block in ("base", "neo", "ecard", "gym", "ex", "dp", "pl", "pop",
                      "promos", "swsh", "sv", "me", "custom"):
            key = f"series.{block}"
            self.assertTrue(key in self.client or key in self.served,
                            f"{key} is drawn as the key itself")

    def test_set_labels_resolve_for_every_set(self):
        """The client labels a set from its code, so every set we ship needs the
        label in whichever namespace it asks for."""
        missing = [key for surface, key in keys.derived_keys()
                   if surface.startswith(("collection set label", "set list"))
                   and key.lower() not in self.client and key.lower() not in self.served]
        self.assertEqual([], missing)

    def test_served_labels_do_not_override_the_client(self):
        """custom_labels.json only fills gaps: a label for a key the client already
        ships would replace the client's own wording."""
        overridden = sorted(key for key in self.served if key in self.client)
        self.assertEqual([], overridden)

    def test_plain_text_is_not_a_key(self):
        """A sentence is drawn as written, but a sentence that happens to equal a
        key would be replaced by that key's text, so no id may be both."""
        collided = [row["id"] for row in self.rows
                    if not (row["derived"] or row.get("is_key")) and row["client"]]
        self.assertEqual([], collided)


if __name__ == "__main__":
    unittest.main()
