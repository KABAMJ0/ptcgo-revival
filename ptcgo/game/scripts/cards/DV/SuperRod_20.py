from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="fc5a47d9-5dfb-5eaa-8c89-eca0cfd3c316",
    key="DV",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperRod.Name",
    display_name="Super Rod",
    searchable_by=["Super Rod", "Item"],
    subtypes=["Item"],
    collector_number=20,
    set_code="DV",
    rarity=Rarities.RareHolo,
    effect=unimplemented
)
