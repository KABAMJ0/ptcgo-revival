from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ba4e49c8-3fab-584e-b664-207889afcbbe",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperPotion.Name",
    display_name="Super Potion",
    searchable_by=["Super Potion", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
