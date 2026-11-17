from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="675f5b04-41be-5b3c-8610-da16a9f81e8d",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
