from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="fb38792c-fec6-5aaf-b357-c22d7627de15",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRestore.Name",
    display_name="Energy Restore",
    searchable_by=["Energy Restore", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
