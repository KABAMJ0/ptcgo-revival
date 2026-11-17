from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c5326647-dd87-5aa8-9bc6-ceb2cd9887ac",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=7,
    set_code="POP5",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
