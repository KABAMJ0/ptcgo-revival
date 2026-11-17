from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3afedf74-0a26-5162-9f9d-2bacb3ed80a1",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="DP5",
    rarity=Rarities.Common,
    effect=unimplemented
)
