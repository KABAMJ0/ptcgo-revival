from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d31b1943-452c-54a0-b602-16d652bf348f",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ResearchRecord.Name",
    display_name="Research Record",
    searchable_by=["Research Record", "Item"],
    subtypes=["Item"],
    collector_number=84,
    set_code="COL",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
