from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="2eb5ba3a-6e28-56af-a897-a3059b45f176",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwatter.Name",
    display_name="Energy Swatter",
    searchable_by=["Energy Swatter", "Item"],
    subtypes=["Item"],
    collector_number=73,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
