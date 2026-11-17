from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0ece8f3c-1daf-59c2-a0b8-26c754acda62",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRestore.Name",
    display_name="Energy Restore",
    searchable_by=["Energy Restore", "Item"],
    subtypes=["Item"],
    collector_number=106,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
