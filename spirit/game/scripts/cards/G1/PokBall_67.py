from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d66bc6e5-8f65-5960-97eb-eef758905fd3",
    key="G1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=67,
    set_code="G1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
