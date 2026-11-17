from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="05ad62a2-580f-5aa8-ab96-b43e5a3a6a66",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
