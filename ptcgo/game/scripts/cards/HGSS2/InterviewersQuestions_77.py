from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_energy_card

card = SupporterCardDef(
    guid="597533d4-85b6-55bc-bda6-ed08f2894372",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.InterviewersQuestions.Name",
    display_name="Interviewer's Questions",
    searchable_by=["Interviewer's Questions", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="HGSS2",
    rarity=Rarities.Uncommon,
    effect=look_at_top(8, take=8, predicate=is_energy_card, minimum=0)
)
