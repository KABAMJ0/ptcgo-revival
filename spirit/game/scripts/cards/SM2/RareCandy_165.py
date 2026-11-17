from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ddf1f204-3901-5a6b-b22d-01e558e84584",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=165,
    set_code="SM2",
    rarity=Rarities.RareSecret,
    effect=unimplemented
)
