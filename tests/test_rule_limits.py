"""Rule-box mechanics the client prints and the server has to enforce.

The client draws these rules and refuses nothing itself, so every check here drives the
path the server actually takes: `validate_deck` for the deck limits (the same call
`data_sync.handle_validate_decks` makes) and `prize_value` for the prize a knockout pays
(`game_session.resolve_knockouts` reads it verbatim at `count = prize_value(...)`).
"""

import os
import sys
import unittest
import uuid

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ptcgo.game.attributes import AttrID, CardType, DeckFormat
from ptcgo.game.content.definitions import has_rule_box, prize_value
from ptcgo.game.decks.validation import validate_deck
from ptcgo.game.scripts.cards import loader as card_loader

UNLIMITED = [DeckFormat.UNLIMITED.value]


def load():
    if not card_loader.cards:
        card_loader.load_all()
    return card_loader.cards


def cards_with_subtype(subtype, card_type=None):
    out = []
    for card in load():
        if not any(str(s).lower() == subtype.lower() for s in (card.subtypes or [])):
            continue
        if card_type is not None and card.get_attribute_value(AttrID.CARD_TYPE) != card_type:
            continue
        out.append(card)
    return out


def basic_energy():
    for card in load():
        if card.get_attribute_value(AttrID.CARD_TYPE) == CardType.ENERGY.value \
                and not card.get_attribute_value(AttrID.IS_SPECIAL_ENERGY):
            return card
    raise AssertionError("no basic energy in the tree")


def deck_of(cards):
    """A legal 60-card deck: the cards asked for, padded with basic energy."""
    guids = [c.guid.lower() for c in cards]
    filler = basic_energy().guid.lower()
    while len(guids) < 60:
        guids.append(filler)
    return {"deckID": str(uuid.uuid4()), "deckName": "Limits", "piles": {"deck": guids}}


def explanations(deck):
    return " | ".join(
        str((detail.get("explanation") or {}).get("id", ""))
        for row in validate_deck(deck, UNLIMITED)
        for detail in row["results"])


class Prizes(unittest.TestCase):
    def test_a_tag_team_pokemon_pays_three_prizes(self):
        tag_teams = [c for c in cards_with_subtype("TAG TEAM", CardType.POKEMON.value)
                     if any(s == "GX" for s in c.subtypes)]
        self.assertGreater(len(tag_teams), 100, "the corpus should hold the TAG TEAM block")
        wrong = [f"{c.set_code}/{c.collector_number} {c.display_name} -> {prize_value(c.guid)}"
                 for c in tag_teams if prize_value(c.guid) != 3]
        self.assertEqual(wrong, [], "TAG TEAM Pokemon-GX must pay 3 prizes")
        self.assertTrue(has_rule_box(tag_teams[0].guid))

    def test_a_plain_gx_still_pays_two(self):
        gx = [c for c in cards_with_subtype("GX", CardType.POKEMON.value)
              if not any(s == "TAG TEAM" for s in c.subtypes)]
        self.assertTrue(gx)
        self.assertEqual({prize_value(c.guid) for c in gx}, {2})

    def test_a_tag_team_supporter_is_not_a_prize_giver(self):
        supporters = cards_with_subtype("TAG TEAM", CardType.TRAINER.value)
        self.assertTrue(supporters)
        self.assertEqual({prize_value(c.guid) for c in supporters}, {1})


class DeckLimits(unittest.TestCase):
    def test_two_ace_specs_are_refused(self):
        ace = cards_with_subtype("ACE SPEC")[:2]
        self.assertEqual(len(ace), 2)
        self.assertIn("ACE SPEC", explanations(deck_of(ace)))

    def test_two_radiant_pokemon_are_refused(self):
        radiant = [c for c in cards_with_subtype("Radiant", CardType.POKEMON.value)][:2]
        self.assertEqual(len(radiant), 2)
        self.assertIn("Radiant", explanations(deck_of(radiant)))

    def test_two_prism_stars_of_one_name_are_refused(self):
        prism = cards_with_subtype("Prism Star")
        single = prism[0]
        self.assertIn("Prism Star", explanations(deck_of([single, single])))

    def test_one_of_each_is_accepted(self):
        ace = cards_with_subtype("ACE SPEC")[0]
        radiant = cards_with_subtype("Radiant", CardType.POKEMON.value)[0]
        prism = cards_with_subtype("Prism Star")[0]
        text = explanations(deck_of([ace, radiant, prism]))
        self.assertNotIn("ACE SPEC", text)
        self.assertNotIn("Radiant", text)
        self.assertNotIn("Prism Star", text)

    def test_a_plain_deck_raises_none_of_these(self):
        text = explanations(deck_of([]))
        self.assertNotIn("ACE SPEC", text)
        self.assertNotIn("Radiant", text)
        self.assertNotIn("Prism Star", text)


if __name__ == "__main__":
    unittest.main()
