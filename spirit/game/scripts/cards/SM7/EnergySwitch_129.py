from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d0b23b56-24c4-5fe3-b9ca-5112a8618520",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=129,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
