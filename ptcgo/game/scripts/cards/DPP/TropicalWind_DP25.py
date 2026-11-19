from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tropical_wind

card = ItemCardDef(
    guid="8420000c-d47f-5caf-a3f1-73fd7547a6c9",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalWind.Name",
    display_name="Tropical Wind",
    searchable_by=["Tropical Wind", "Item"],
    subtypes=["Item"],
    collector_number=25,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    effect=tropical_wind(2, 1)
)
