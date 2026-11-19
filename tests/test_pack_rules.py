"""Pack rules: the 30th Celebration set's fixed pull structure.

Every ME55 pack carries exactly one of the set's Pikachu prints and never two,
and no pack carries more than one Mew printing. Sets without a rule entry keep
the ordinary 10-card shape.
"""

import collections
import unittest

from ptcgo.game.attributes import AttrID
from ptcgo.game.content import pack_rules
from ptcgo.game.models.product import BoosterPack
from ptcgo.game.scripts.cards import loader as card_loader


def pack_for(set_key: str) -> BoosterPack:
    return BoosterPack(guid=f"test-{set_key}", key=set_key,
                       attributes={str(AttrID.SET_KEY): {"type": "string", "value": set_key}})


class PackRulesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        card_loader.load_all()
        cls.by_guid = {c.guid: c for c in card_loader.cards}

    def names(self, pack):
        return [self.by_guid[guid].display_name for guid in pack if guid in self.by_guid]

    def test_rules_load(self):
        self.assertTrue(pack_rules.rules_for("ME55"), "ME55 pack rules are missing")
        self.assertEqual(pack_rules.rules_for("SWSH8"), {})

    def test_me55_guarantees_one_pikachu_and_never_two(self):
        booster = pack_for("ME55")
        counts = collections.Counter()
        for _ in range(200):
            pack = booster.open("-1")
            self.assertEqual(len(pack), 10)
            counts[self.names(pack).count("Pikachu")] += 1
        self.assertEqual(counts[1], 200, f"Pikachu count per pack was {dict(counts)}")

    def test_me55_never_repeats_the_chase_cards(self):
        booster = pack_for("ME55")
        mew_counts = collections.Counter()
        for _ in range(200):
            pack = booster.open("-1")
            names = self.names(pack)
            self.assertLessEqual(names.count("Mew"), 1)
            self.assertLessEqual(names.count("Pikachu"), 1)
            mew_counts[names.count("Mew")] += 1
        # A Mew is a chase pull, not an every-pack card.
        self.assertLess(sum(c for n, c in mew_counts.items() if n), 200)

    def test_sets_declare_their_own_pack_size(self):
        """Base Set held eleven cards, a McDonald's promo pack five."""
        for set_key, size in (("BASE1", 11), ("ECARD1", 9), ("POP9", 3), ("MCD11", 4), ("MCD22", 4)):
            booster = pack_for(set_key)
            for _ in range(10):
                self.assertEqual(len(booster.open("-1")), size, set_key)

    def test_unruled_sets_keep_the_ten_card_pack(self):
        for set_key in ("SWSH8", "SV3", "CEL25"):
            booster = pack_for(set_key)
            for _ in range(5):
                self.assertEqual(len(booster.open("-1")), 10, set_key)


if __name__ == "__main__":
    unittest.main()
