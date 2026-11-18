from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="fc33059c-0ec5-5d9c-bd5f-6c827a7fe105",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyPickup.Name",
    display_name="Energy Pickup",
    searchable_by=["Energy Pickup", "Item"],
    subtypes=["Item"],
    collector_number=132,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
