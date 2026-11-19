from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="9b9d55c4-2b9e-5d76-b3c0-570933196e01",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=94,
    set_code="EX10",
    rarity=Rarities.Common,
    effect=unimplemented
)
