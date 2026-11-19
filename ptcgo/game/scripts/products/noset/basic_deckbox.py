from ptcgo.game.data_utils import DeckBoxDef
from ptcgo.game.attributes import DefaultCosmetic, DeckBoxShape

product = DeckBoxDef(
    guid=DefaultCosmetic.DECK_BOX.value,
    key="core",
    name="Basic Deck Box",
    image_url="_default_deckbox",
    shape=DeckBoxShape.TWO_TONE
)
