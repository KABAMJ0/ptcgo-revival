"""The ban map the client parses, in the vocabulary it parses.

`AllBannedCardsByFormat.cards` is `{guid: "Modified,Expanded,..."}`. The client splits
each value on commas into a HashSet of format tokens (`BannedItemManager.Add`) and its
popup names a format only when the token is one it carries, so an empty map, a name like
"Standard" or a prose reason all read as "no ban at all".
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ptcgo.game.attributes import AttrID, DeckFormat
from ptcgo.game.decks import card_bans
from ptcgo.game.decks.formats import FormatManager
from ptcgo.game.scripts.cards import loader as card_loader
from ptcgo.packets.handlers import data_sync


def load():
    if not card_loader.cards:
        card_loader.load_all()
    return card_loader.cards


class Vocabulary(unittest.TestCase):
    def test_the_tokens_are_the_five_the_client_knows(self):
        # CardBannedInfoClickBehaviour.orderedList
        self.assertEqual(set(data_sync.BAN_FORMAT_TOKENS),
                         {"ThemeDeck", "Modified", "Expanded", "Legacy", "Unlimited"})

    def test_standard_travels_as_modified(self):
        self.assertEqual(data_sync.BAN_TOKEN_BY_FORMAT[DeckFormat.STANDARD.value], "Modified")

    def test_every_mapped_token_is_a_token_the_client_knows(self):
        self.assertTrue(set(data_sync.BAN_TOKEN_BY_FORMAT.values())
                        <= set(data_sync.BAN_FORMAT_TOKENS))


class Map(unittest.TestCase):
    def setUp(self):
        load()
        self.manager = FormatManager()
        self.guid = card_loader.cards[0].guid.lower()

    def test_a_server_ban_carries_every_format(self):
        original = card_bans.banned
        card_bans.banned = lambda: {self.guid: {"reason": "test", "banned_by": "test"}}
        try:
            cards = data_sync._banned_cards_by_format()
        finally:
            card_bans.banned = original
        self.assertEqual(set(cards[self.guid].split(",")), set(data_sync.BAN_FORMAT_TOKENS))

    def test_a_format_ban_carries_only_that_format(self):
        card = card_loader.cards[0]
        fmt = self.manager.by_guid(DeckFormat.EXPANDED.value)
        self.assertIsNotNone(fmt)
        original = list(fmt.banned_cards)
        fmt.banned_cards = [
            f"{card.key}/{card.get_attribute_value(AttrID.COLLECTOR_NUMBER)}"]
        self.manager._ref_cache.pop(fmt.guid, None)
        try:
            cards = data_sync._banned_cards_by_format()
        finally:
            fmt.banned_cards = original
            self.manager._ref_cache.pop(fmt.guid, None)
        self.assertEqual(cards[self.guid], "Expanded")

    def test_no_bans_is_an_empty_map_not_a_crash(self):
        original = card_bans.banned
        card_bans.banned = lambda: {}
        try:
            cards = data_sync._banned_cards_by_format()
        finally:
            card_bans.banned = original
        self.assertEqual(cards, {})


if __name__ == "__main__":
    unittest.main()
