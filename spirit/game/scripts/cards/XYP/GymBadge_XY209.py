from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="4336f396-eb76-52d4-9e33-f6ac7e894ddd",
    key="XYP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymBadge.Name",
    display_name="Gym Badge",
    searchable_by=["Gym Badge", "Item"],
    subtypes=["Item"],
    collector_number=209,
    set_code="XYP",
    rarity=Rarities.RarePromo,
    effect=unimplemented
)
