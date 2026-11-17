from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e1e5dd66-c185-5c10-86f7-0ee7597858fd",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
