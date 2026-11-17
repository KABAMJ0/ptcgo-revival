from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3e21516f-bf55-5646-be38-7a54e2ccd3bc",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
