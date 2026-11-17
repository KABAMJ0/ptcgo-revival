from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="2fb45df5-1462-5682-b672-8d8f943fcaa9",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NestBall.Name",
    display_name="Nest Ball",
    searchable_by=["Nest Ball", "Item"],
    subtypes=["Item"],
    collector_number=123,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
