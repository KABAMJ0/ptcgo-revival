from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import with_discard_cost

card = SupporterCardDef(
    guid="8b744459-4c3c-5148-a10a-73465def16e9",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysDetermination.Name",
    display_name="Misty's Determination",
    searchable_by=["Misty's Determination", "Supporter"],
    subtypes=["Supporter"],
    collector_number=108,
    set_code="XY12",
    rarity=Rarities.RareUltra,
    effect=with_discard_cost(1, look_at_top(8, take=1))
)
