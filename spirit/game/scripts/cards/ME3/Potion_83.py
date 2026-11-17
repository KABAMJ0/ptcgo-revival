from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8fd688f9-2bd2-5b53-9aa3-b46d3b4eed62",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=83,
    set_code="ME3",
    rarity=Rarities.Common,
    effect=unimplemented
)
