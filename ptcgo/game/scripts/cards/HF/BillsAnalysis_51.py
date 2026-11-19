from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_trainer_card

card = SupporterCardDef(
    guid="77d98f91-a8a6-5b96-99ca-7162fa1d19d3",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsAnalysis.Name",
    display_name="Bill's Analysis",
    searchable_by=["Bill's Analysis", "Supporter"],
    subtypes=["Supporter"],
    collector_number=51,
    set_code="HF",
    rarity=Rarities.Rare,
    effect=look_at_top(7, take=2, predicate=is_trainer_card, minimum=0)
)
