from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6c657c87-c8ce-58f2-bc6e-dd8b85989243",
    key="XYP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymBadge.Name",
    display_name="Gym Badge",
    searchable_by=["Gym Badge", "Item"],
    subtypes=["Item"],
    collector_number=207,
    set_code="XYP",
    rarity=Rarities.RarePromo,
    effect=unimplemented
)
