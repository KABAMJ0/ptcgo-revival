from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="03c640e5-6ab0-5487-8f7f-bf01e656ab6e",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=123,
    set_code="ME2",
    rarity=Rarities.Rare,
    effect=unimplemented
)
