from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="17eebe32-6e11-5f1b-95c3-b6073cd4322b",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxPotion.Name",
    display_name="Max Potion",
    searchable_by=["Max Potion", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
