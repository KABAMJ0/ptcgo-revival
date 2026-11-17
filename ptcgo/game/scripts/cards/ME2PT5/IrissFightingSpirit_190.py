from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect
from ptcgo.game.card_effects.trainers import with_discard_cost

card = SupporterCardDef(
    guid="7088b1a6-a95d-5fc2-a168-dae5e9c2e6b0",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IrissFightingSpirit.Name",
    display_name="Iris's Fighting Spirit",
    searchable_by=["Iris's Fighting Spirit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=190,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, draw_until_effect(6))
)
