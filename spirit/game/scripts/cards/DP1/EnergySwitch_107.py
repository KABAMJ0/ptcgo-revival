from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e298d179-ea27-5e2d-9abc-6522c0a21cb1",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=107,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
