from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="456f5154-79bb-567c-b554-91d300008321",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatBall.Name",
    display_name="Great Ball",
    searchable_by=["Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=118,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
