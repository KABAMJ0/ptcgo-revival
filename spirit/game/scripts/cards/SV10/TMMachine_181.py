from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ecca6db6-927b-5c0f-bc8f-80ec67368173",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TMMachine.Name",
    display_name="TM Machine",
    searchable_by=["TM Machine", "Item", "MEGA"],
    subtypes=["Item", "MEGA"],
    collector_number=181,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
