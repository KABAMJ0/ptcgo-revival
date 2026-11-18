from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_trainer_card

card = SupporterCardDef(
    guid="60363378-785f-56fb-9abe-55a1e4219a06",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsAnalysis.Name",
    display_name="Bill's Analysis",
    searchable_by=["Bill's Analysis", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    effect=look_at_top(7, take=2, predicate=is_trainer_card, minimum=0)
)
