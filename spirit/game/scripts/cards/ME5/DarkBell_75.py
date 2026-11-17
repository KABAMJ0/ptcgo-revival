from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="1ba045ba-0a51-556c-a326-6328e3550ed7",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DarkBell.Name",
    display_name="Dark Bell",
    searchable_by=["Dark Bell", "Item"],
    subtypes=["Item"],
    collector_number=75,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
