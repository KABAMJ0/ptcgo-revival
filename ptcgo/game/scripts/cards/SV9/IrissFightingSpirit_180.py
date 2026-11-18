from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect
from ptcgo.game.card_effects.trainers import with_discard_cost

card = SupporterCardDef(
    guid="7bfad5b8-6f08-59a0-b620-8ef1148d3156",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IrissFightingSpirit.Name",
    display_name="Iris's Fighting Spirit",
    searchable_by=["Iris's Fighting Spirit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=180,
    set_code="SV9",
    rarity=Rarities.Rare,
    effect=with_discard_cost(1, draw_until_effect(6))
)
