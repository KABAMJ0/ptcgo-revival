from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d88a17b4-5202-54db-999d-2b1a4256cc78",
    key="TK2B",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=10,
    set_code="TK2B",
    rarity=Rarities.Common,
    effect=unimplemented
)
