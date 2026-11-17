from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="181ca5af-d3d9-5444-9dc5-4ba89efda8a5",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=117,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
