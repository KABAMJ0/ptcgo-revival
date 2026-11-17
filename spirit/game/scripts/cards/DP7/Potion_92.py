from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b4f031af-021c-55f2-b952-0223a54becbb",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=92,
    set_code="DP7",
    rarity=Rarities.Common,
    effect=unimplemented
)
