from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e74b1a10-66f3-56ec-9833-3992e2bb1c15",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RebootPod.Name",
    display_name="Reboot Pod",
    searchable_by=["Reboot Pod", "Item", "Future", "ACE SPEC"],
    subtypes=["Item", "Future", "ACE SPEC"],
    collector_number=158,
    set_code="SV5",
    rarity=Rarities.Rare,
    effect=unimplemented
)
