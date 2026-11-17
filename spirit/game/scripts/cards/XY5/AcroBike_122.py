from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top

card = ItemCardDef(
    guid="09c2a182-8a5a-5c10-acac-589fd1281f95",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcroBike.Name",
    display_name="Acro Bike",
    searchable_by=["Acro Bike", "Item"],
    subtypes=["Item"],
    collector_number=122,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=look_at_top(2, take=1)
)
