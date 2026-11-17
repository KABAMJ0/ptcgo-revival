from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="77238d5a-3ae4-5c56-8694-c4b5ba992dff",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeHerb.Name",
    display_name="Life Herb",
    searchable_by=["Life Herb", "Item"],
    subtypes=["Item"],
    collector_number=108,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
