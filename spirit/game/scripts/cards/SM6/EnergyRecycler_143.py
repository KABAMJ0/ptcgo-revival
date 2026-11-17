from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="522c6d24-1020-5d70-951e-41ae92eaf0d0",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycler.Name",
    display_name="Energy Recycler",
    searchable_by=["Energy Recycler", "Item"],
    subtypes=["Item"],
    collector_number=143,
    set_code="SM6",
    rarity=Rarities.RareSecret,
    effect=unimplemented
)
