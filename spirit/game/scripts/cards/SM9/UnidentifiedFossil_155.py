from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="16fbb732-6b44-529c-a0e8-d1101d7b16a7",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UnidentifiedFossil.Name",
    display_name="Unidentified Fossil",
    searchable_by=["Unidentified Fossil", "Item"],
    subtypes=["Item"],
    collector_number=155,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
