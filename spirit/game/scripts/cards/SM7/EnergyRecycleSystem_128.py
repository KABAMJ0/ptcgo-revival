from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="5d36af85-9b3d-50d4-9078-07db64b03353",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycleSystem.Name",
    display_name="Energy Recycle System",
    searchable_by=["Energy Recycle System", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
