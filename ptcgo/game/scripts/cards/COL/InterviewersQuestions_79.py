from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_energy_card

card = SupporterCardDef(
    guid="7d35118e-006d-5f26-a93b-2c9c6865e080",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.InterviewersQuestions.Name",
    display_name="Interviewer's Questions",
    searchable_by=["Interviewer's Questions", "Supporter"],
    subtypes=["Supporter"],
    collector_number=79,
    set_code="COL",
    rarity=Rarities.Uncommon,
    effect=look_at_top(8, take=8, predicate=is_energy_card, minimum=0)
)
