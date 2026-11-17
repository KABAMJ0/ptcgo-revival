from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b3c053a3-7fb3-5fcc-805a-99f7f7c21ad2",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="ME1",
    rarity=Rarities.Common,
    effect=unimplemented
)
