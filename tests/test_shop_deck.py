"""The shipped Dragapult ex shop deck: 60 cards, sold for 200 Trainer Tokens."""

import unittest
import uuid

from ptcgo.game.attributes import AttrID
from ptcgo.game.decks.validation import valid_format_names
from ptcgo.game.scripts.cards import loader as card_loader
from ptcgo.game.scripts.products import loader as product_loader


def dragapult():
    product_loader.load_all()
    for product in product_loader.products:
        if getattr(product, "name", "") == "Dragapult ex":
            return product
    return None


class ShopDeckTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        card_loader.load_all()

    def test_the_deck_sells_for_two_hundred_tokens(self):
        from ptcgo.database.economy_data import list_shop_items
        guid = str(uuid.uuid5(uuid.NAMESPACE_URL, "ptcgo:deck:dragapult-ex-shop"))
        rows = [r for r in list_shop_items() if r["product_guid"].lower() == guid.lower()]
        self.assertTrue(rows, "the Dragapult ex deck has no shop row, so nobody can buy it")
        row = rows[0]
        self.assertTrue(row["enabled"])
        self.assertEqual(row["price"], 200)
        self.assertEqual(row["currency"], AttrID.TRAINER_TOKENS.value)

    def test_the_product_is_sixty_playable_cards(self):
        product = dragapult()
        self.assertIsNotNone(product, "the Dragapult ex deck product is missing")
        self.assertEqual(len(product.contents), 60)
        # Every entry resolves to a real card, or the deck would grant nothing.
        for guid in product.contents:
            self.assertIn(guid, card_loader.cards_by_guid)

    def test_the_deck_is_legal_somewhere(self):
        product = dragapult()
        self.assertIsNotNone(product)
        formats = valid_format_names(product.to_deck_dict())
        self.assertTrue(formats, "the shop deck is illegal in every format")


if __name__ == "__main__":
    unittest.main()
