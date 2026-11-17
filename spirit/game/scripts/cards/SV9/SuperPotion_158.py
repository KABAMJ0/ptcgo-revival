from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b81031be-c19d-5c53-bab4-175f89fe8d30",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperPotion.Name",
    display_name="Super Potion",
    searchable_by=["Super Potion", "Item"],
    subtypes=["Item"],
    collector_number=158,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
