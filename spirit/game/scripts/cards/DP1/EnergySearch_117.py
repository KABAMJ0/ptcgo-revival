from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="280e484f-8f49-5a3b-a9e3-9633764a2c22",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=117,
    set_code="DP1",
    rarity=Rarities.Common,
    effect=unimplemented
)
