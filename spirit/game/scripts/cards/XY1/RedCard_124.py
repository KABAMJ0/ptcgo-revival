from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e8649a0c-d2c5-5642-9348-08ae57e58148",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedCard.Name",
    display_name="Red Card",
    searchable_by=["Red Card", "Item"],
    subtypes=["Item"],
    collector_number=124,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
