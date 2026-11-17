from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="20cb2f33-aecf-515c-9814-de3290e3e5d0",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Repel.Name",
    display_name="Repel",
    searchable_by=["Repel", "Item"],
    subtypes=["Item"],
    collector_number=126,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
