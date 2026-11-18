#!/usr/bin/env python3
"""Create a test deck out of the newly imported Scarlet & Violet cards.

Builds a legal 60-card Standard deck (Charizard ex, Obsidian Flames) straight
from the card scripts, so it exercises data, set codes, format legality and the
deck wire shape at once. The account already owns four of every card from the
admin "grant all" pass, so no extra granting is needed.

Run it with the server stopped, so the deck write cannot race the server's
own writes:

    ./venv/bin/python tools/make_test_deck.py --user brandon

Then start the server again and the deck appears in the client's deck list.
"""

import argparse

from ptcgo.database.player_data import save_deck
from ptcgo.database.accounts import get_account_by_username
from ptcgo.game.content.starter import build_deck_data, resolve_decklist
from ptcgo.game.scripts.cards import loader as card_loader
from ptcgo.game.attributes import AttrID

# (count, set code, collector number)
CHARIZARD_EX_DECKLIST = [
    # Pokemon -- 16
    (4, "SV3", 26),      # Charmander
    (3, "SV3", 27),      # Charmeleon
    (3, "SV3", 125),     # Charizard ex
    (2, "SV3", 162),     # Pidgey
    (2, "SV3", 164),     # Pidgeot ex
    (2, "SV3PT5", 151),  # Mew ex
    # Trainers -- 32
    (4, "SV3", 186),     # Arven
    (4, "SV1", 196),     # Ultra Ball
    (4, "SV1", 181),     # Nest Ball
    (4, "SV1", 191),     # Rare Candy
    (4, "SV1", 194),     # Switch
    (4, "SV4PT5", 87),   # Professor's Research
    (3, "SV2", 185),     # Iono
    (3, "SV2", 188),     # Super Rod
    (2, "SV5", 144),     # Buddy-Buddy Poffin
    # Energy -- 12
    (12, "SVE", 2),      # Basic Fire Energy
]

DECK_NAME = "Charizard ex (SV test)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", default="brandon")
    ap.add_argument("--name", default=DECK_NAME)
    args = ap.parse_args()

    card_loader.load_all()
    account = get_account_by_username(args.user)
    if not account:
        raise SystemExit(f"no account named {args.user}")
    account_id = account["account_id"] if isinstance(account, dict) else account.account_id

    deck_data = build_deck_data(args.name, CHARIZARD_EX_DECKLIST)
    guids = deck_data["piles"]["deck"]
    print(f"resolved {len(guids)}/60 cards")
    if len(guids) != 60:
        raise SystemExit("decklist did not resolve to 60 cards -- check the set/number pairs")

    index = {}
    for card in card_loader.cards:
        index[card.guid] = card
    pokemon = [g for g in guids if index[g].get_attribute_value(AttrID.CARD_TYPE) == 0]
    print(f"pokemon in deck: {len(pokemon)}")

    save_deck(account_id, deck_data["deckID"], args.name, deck_data, is_avatar=False)
    print(f"deck saved: {args.name} ({deck_data['deckID']}) for {args.user}")


if __name__ == "__main__":
    main()
