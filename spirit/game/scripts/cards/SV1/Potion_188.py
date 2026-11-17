from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="4f662ed8-8ac0-5bb3-81dc-3564e657c9eb",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=188,
    set_code="SV1",
    rarity=Rarities.Common,
    effect=unimplemented
)
