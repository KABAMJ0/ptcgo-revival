from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="98d907b6-dfad-554c-9368-8a3c1788d7a9",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
