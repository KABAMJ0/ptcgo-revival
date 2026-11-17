from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="64e7e879-e03d-5f40-9186-42ca8a258e6a",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WarpPoint.Name",
    display_name="Warp Point",
    searchable_by=["Warp Point", "Item"],
    subtypes=["Item"],
    collector_number=116,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
