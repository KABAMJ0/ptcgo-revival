from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="2adff3ff-c196-5a82-93bb-3ed3868ea4a7",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=108,
    set_code="ME4",
    rarity=Rarities.Rare,
    effect=unimplemented
)
