from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="d40b8509-300e-57bd-89d3-a5a9f26d23bb",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=95,
    set_code="EX10",
    rarity=Rarities.Common,
    effect=unimplemented
)
