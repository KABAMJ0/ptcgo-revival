from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import is_supporter_card

card = ItemCardDef(
    guid="bfa47baa-7bbc-5476-85bb-c7cd8c06c96c",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RotoStick.Name",
    display_name="Roto-Stick",
    searchable_by=["Roto-Stick", "Item"],
    subtypes=["Item"],
    collector_number=127,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    effect=look_at_top(4, take=1, predicate=is_supporter_card)
)
