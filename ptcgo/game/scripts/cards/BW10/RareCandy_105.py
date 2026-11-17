from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_from_hand

card = ItemCardDef(
    guid="6a7bcfd6-023a-59bf-9932-9053b3d78b08",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=105,
    set_code="BW10",
    rarity=Rarities.RareSecret,
    effect=evolve_from_hand()
)
