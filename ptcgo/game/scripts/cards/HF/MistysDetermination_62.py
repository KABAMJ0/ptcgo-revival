from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import with_discard_cost

card = SupporterCardDef(
    guid="493e7048-1e85-5b6d-8959-f0dcb579bb85",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysDetermination.Name",
    display_name="Misty's Determination",
    searchable_by=["Misty's Determination", "Supporter"],
    subtypes=["Supporter"],
    collector_number=62,
    set_code="HF",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, look_at_top(8, take=1))
)
