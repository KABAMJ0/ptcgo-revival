from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0527456a-4dae-5504-be0a-fce98650295e",
    key="XYP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymBadge.Name",
    display_name="Gym Badge",
    searchable_by=["Gym Badge", "Item"],
    subtypes=["Item"],
    collector_number=208,
    set_code="XYP",
    rarity=Rarities.RarePromo,
    effect=unimplemented
)
