from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="70d139a3-ae95-535c-a2fd-c822a92a7d6c",
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
