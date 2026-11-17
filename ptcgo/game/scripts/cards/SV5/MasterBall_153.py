from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="969544e8-7930-5b65-8bd8-5549fa17c61a",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=153,
    set_code="SV5",
    rarity=Rarities.Rare,
    effect=unimplemented
)
