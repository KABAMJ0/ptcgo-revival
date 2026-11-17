from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="35d23b4c-20d2-55a6-8cdf-7313cd0f60af",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
