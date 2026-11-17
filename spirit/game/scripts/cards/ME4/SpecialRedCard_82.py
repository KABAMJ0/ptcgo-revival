from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="4e8d59dd-a91a-5f93-8a84-542bdc58d6a7",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpecialRedCard.Name",
    display_name="Special Red Card",
    searchable_by=["Special Red Card", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
