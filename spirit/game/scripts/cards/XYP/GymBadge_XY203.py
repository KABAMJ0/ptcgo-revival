from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d55a84b8-e829-59e9-b5ad-4385c293296b",
    key="XYP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymBadge.Name",
    display_name="Gym Badge",
    searchable_by=["Gym Badge", "Item"],
    subtypes=["Item"],
    collector_number=203,
    set_code="XYP",
    rarity=Rarities.RarePromo,
    effect=unimplemented
)
