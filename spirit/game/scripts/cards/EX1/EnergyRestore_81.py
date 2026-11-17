from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8cd8946f-ab9b-58d5-9933-247457900a71",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRestore.Name",
    display_name="Energy Restore",
    searchable_by=["Energy Restore", "Item"],
    subtypes=["Item"],
    collector_number=81,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
