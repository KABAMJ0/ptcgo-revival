from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d6a497b6-2857-5a3f-b530-a25a7cff95f4",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcroBike.Name",
    display_name="Acro Bike",
    searchable_by=["Acro Bike", "Item"],
    subtypes=["Item"],
    collector_number=123,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
