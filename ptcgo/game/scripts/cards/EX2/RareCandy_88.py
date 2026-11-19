from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="dd3e4199-d5fd-535e-b54d-1323fd7c8790",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
