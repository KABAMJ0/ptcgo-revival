"""Dragapult ex — a shop deck any player can buy for 200 Trainer Tokens.

The list is the community Dragapult ex / Munkidori build: spread with Phantom
Dive, then move the damage counters off your own board with Munkidori's ability.
Printings are the newest main-set print of each card so the deck validates in
Expanded and Standard. Basic Energy comes from set printings rather than
Free_Energy so the deck is a complete 60-card product.

No artwork was made for this one, so the shop shows the server's placeholder
image; drop a real image URL in `image_url` when there is one.
"""

import uuid

from ptcgo.config import PLACEHOLDER_IMG
from ptcgo.game.data_utils import DeckEntry, ThemeDeckDef

# Stable identity: derived once so a reload never mints a new product GUID.
_GUID = str(uuid.uuid5(uuid.NAMESPACE_URL, "ptcgo:deck:dragapult-ex-shop"))


product = ThemeDeckDef(
    guid=_GUID,
    # The shop groups products into tabs by this key: a real set code puts the deck
    # under that set. "NoSet" leaves it in a group the client never renders a tab for.
    key="SV6",
    name="Dragapult ex",
    description="Spread damage with Phantom Dive, then move the counters with Munkidori.",
    image_url=PLACEHOLDER_IMG,
    # The client's shop puts decks in its deck category on the theme-deck flag, and
    # theme_legal=False keeps it out of Theme format: this list is not an approved
    # theme deck and must not pretend to be one.
    theme_legal=False,
    contents=[
        DeckEntry("SV6/128", 4),  # Dreepy
        DeckEntry("SV6/129", 4),  # Drakloak
        DeckEntry("SV6/200", 3),  # Dragapult ex
        DeckEntry("SV6/95", 2),   # Munkidori
        DeckEntry("SV8PT5/4", 2),  # Budew
        DeckEntry("SV6PT5/92", 1),  # Fezandipiti ex
        DeckEntry("ME3/121", 1),    # Meowth ex
        DeckEntry("SV2/156", 1),    # Dunsparce
        DeckEntry("SV2/229", 1),    # Dudunsparce
        DeckEntry("SV3PT5/146", 1),  # Moltres
        DeckEntry("ME2PT5/192", 4),  # Lillie's Determination
        DeckEntry("SV6/223", 4),     # Buddy-Buddy Poffin
        DeckEntry("ME2PT5/198", 4),  # Poké Pad
        DeckEntry("SV1/168", 4),     # Crushing Hammer
        DeckEntry("SV1/196", 3),     # Ultra Ball
        DeckEntry("SWSH2/200", 3),   # Boss's Orders
        DeckEntry("SV8/251", 2),     # Night Stretcher
        DeckEntry("SV8PT5/171", 2),  # Crispin
        DeckEntry("ME1/127", 2),     # Risky Ruins
        DeckEntry("SV6/165", 1),     # Unfair Stamp
        DeckEntry("ME3/123", 1),     # Rosa's Encouragement
        DeckEntry("SV4PT5/228", 1),  # Judge
        DeckEntry("ME4/113", 1),     # Special Red Card
        DeckEntry("SWSH8/284", 3),   # Fire Energy
        DeckEntry("SWSH6/232", 3),   # Psychic Energy
        DeckEntry("SWSH7/236", 2),   # Darkness Energy
    ],
)
