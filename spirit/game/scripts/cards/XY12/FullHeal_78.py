from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="42fe7d77-0208-55ed-af0d-799ba83d0b1e",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullHeal.Name",
    display_name="Full Heal",
    searchable_by=["Full Heal", "Item"],
    subtypes=["Item"],
    collector_number=78,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
