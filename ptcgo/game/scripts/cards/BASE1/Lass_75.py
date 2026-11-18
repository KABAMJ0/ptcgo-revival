from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import both_shuffle_trainers_into_decks

card = ItemCardDef(
    guid="da0753bd-4246-5ff7-b80b-1581a9594eeb",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lass.Name",
    display_name="Lass",
    searchable_by=["Lass"],
    subtypes=[],
    collector_number=75,
    set_code="BASE1",
    rarity=Rarities.Rare,
    effect=both_shuffle_trainers_into_decks()
)
