from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="4687a700-ef09-5260-931b-ae80400de0e9",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
