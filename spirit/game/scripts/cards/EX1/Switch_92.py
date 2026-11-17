from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="09f19685-9fc7-5223-9db5-909a6fb89907",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=92,
    set_code="EX1",
    rarity=Rarities.Common,
    effect=unimplemented
)
