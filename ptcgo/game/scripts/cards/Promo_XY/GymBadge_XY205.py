from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="1d33efd0-6852-5ef1-992a-dabbdc0fc41d",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymBadge.Name",
    display_name="Gym Badge",
    searchable_by=["Gym Badge", "Item"],
    subtypes=["Item"],
    collector_number=205,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    effect=unimplemented
)
