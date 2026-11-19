from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tropical_wind

card = ItemCardDef(
    guid="8fd4b34b-663b-5669-9f7a-f95f857f150f",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalWind.Name",
    display_name="Tropical Wind",
    searchable_by=["Tropical Wind", "Item"],
    subtypes=["Item"],
    collector_number=5,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    effect=tropical_wind(2, 1)
)
