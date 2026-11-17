from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import with_discard_cost

card = SupporterCardDef(
    guid="63afda62-82d4-572b-87d4-2b9ade7723d9",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysDetermination.Name",
    display_name="Misty's Determination",
    searchable_by=["Misty's Determination", "Supporter"],
    subtypes=["Supporter"],
    collector_number=80,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, look_at_top(8, take=1))
)
