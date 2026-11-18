from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="daa3103a-db7f-5247-81c6-da2c40e1b582",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeHerb.Name",
    display_name="Life Herb",
    searchable_by=["Life Herb", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
