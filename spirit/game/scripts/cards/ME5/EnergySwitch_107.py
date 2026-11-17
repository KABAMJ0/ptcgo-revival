from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="98b2f4f6-ea23-519c-9a92-12de0f384ab1",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=107,
    set_code="ME5",
    rarity=Rarities.Rare,
    effect=unimplemented
)
