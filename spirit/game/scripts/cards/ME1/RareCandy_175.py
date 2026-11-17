from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="03a6ed5f-004e-5eaa-bdaa-a7a15255bdda",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=175,
    set_code="ME1",
    rarity=Rarities.Rare,
    effect=unimplemented
)
