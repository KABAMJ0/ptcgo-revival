from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6c657c87-c8ce-58f2-bc6e-dd8b85989243",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymBadge.Name",
    display_name="Gym Badge",
    searchable_by=["Gym Badge", "Item"],
    subtypes=["Item"],
    collector_number=207,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    effect=unimplemented
)
