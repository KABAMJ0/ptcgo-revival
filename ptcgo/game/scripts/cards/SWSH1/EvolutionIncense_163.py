from ptcgo.game.card_effects.trainers import evolution_incense
from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="74403d98-c7f0-5c0c-8cf8-82bb6f1a51b6",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EvolutionIncense.Name",
    display_name="Evolution Incense",
    searchable_by=["Evolution Incense", "Item"],
    subtypes=["Item"],
    collector_number=163,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=evolution_incense
)
