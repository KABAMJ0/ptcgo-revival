from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="a9fda174-92be-5c3a-81c7-ce7eb789ea19",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrangeTimepiece.Name",
    display_name="Strange Timepiece",
    searchable_by=["Strange Timepiece", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
