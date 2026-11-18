from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_bottom

card = SupporterCardDef(
    guid="91023469-6138-59fd-ad9f-ad70b3aa872d",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksVisit.Name",
    display_name="Professor Oak's Visit",
    searchable_by=["Professor Oak's Visit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=122,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    effect=draw_then_bottom(3, 1)
)
