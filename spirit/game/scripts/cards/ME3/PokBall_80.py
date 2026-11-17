from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="96b14318-bad1-54f5-8302-700bc15a0e6d",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="ME3",
    rarity=Rarities.Common,
    effect=unimplemented
)
