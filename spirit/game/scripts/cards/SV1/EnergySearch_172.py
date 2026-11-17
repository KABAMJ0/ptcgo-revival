from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="46f48070-76c6-5e20-8f2f-682bdd057eb2",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=172,
    set_code="SV1",
    rarity=Rarities.Common,
    effect=unimplemented
)
