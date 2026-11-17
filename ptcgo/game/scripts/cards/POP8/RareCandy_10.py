from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_from_hand

card = ItemCardDef(
    guid="1e8f8a30-89dd-57e2-94bf-751d82481f0f",
    key="POP8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=10,
    set_code="POP8",
    rarity=Rarities.Uncommon,
    effect=evolve_from_hand()
)
