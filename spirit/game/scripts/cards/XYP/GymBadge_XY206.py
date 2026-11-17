from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="a4b9bea5-5654-591c-ae16-983a4f58725c",
    key="XYP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymBadge.Name",
    display_name="Gym Badge",
    searchable_by=["Gym Badge", "Item"],
    subtypes=["Item"],
    collector_number=206,
    set_code="XYP",
    rarity=Rarities.RarePromo,
    effect=unimplemented
)
