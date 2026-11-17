from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="a7bb2bcb-775a-520e-8502-5d43f5227aac",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=194,
    set_code="SV1",
    rarity=Rarities.Common,
    effect=unimplemented
)
