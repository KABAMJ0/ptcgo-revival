from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c7651559-33b8-541f-891d-2ac331157bb5",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=115,
    set_code="ME1",
    rarity=Rarities.Common,
    effect=unimplemented
)
