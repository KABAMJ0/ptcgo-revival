from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="db5d42c0-50e1-5cd1-934b-0d0f12b62488",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=118,
    set_code="DP1",
    rarity=Rarities.Common,
    effect=unimplemented
)
