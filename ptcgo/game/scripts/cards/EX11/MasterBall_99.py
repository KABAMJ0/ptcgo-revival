from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="077bf8e6-857a-5ee4-8e9c-8ecd9a5a4e89",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball", "Item"],
    subtypes=["Item"],
    collector_number=99,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
