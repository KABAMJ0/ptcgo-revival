from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="c8904062-e8ac-5c98-8b22-e1548f1a257e",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TownMap.Name",
    display_name="Town Map",
    searchable_by=["Town Map", "Item"],
    subtypes=["Item"],
    collector_number=150,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
