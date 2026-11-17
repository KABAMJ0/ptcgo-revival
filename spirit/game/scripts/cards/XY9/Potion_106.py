from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0b7f5f46-38ed-5ece-96ab-9e445bcb12a6",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=106,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
