from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="a91304eb-cb72-51b6-8ec9-9701e874c2c6",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=85,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
