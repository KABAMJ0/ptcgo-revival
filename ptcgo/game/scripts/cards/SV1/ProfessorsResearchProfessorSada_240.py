from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="718f4f44-68a0-5f3a-bf88-9a01aadc928b",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearchProfessorSada.Name",
    display_name="Professor's Research (Professor Sada)",
    searchable_by=["Professor's Research (Professor Sada)", "Supporter"],
    subtypes=["Supporter"],
    collector_number=240,
    set_code="SV1",
    rarity=Rarities.Rare,
    effect=discard_hand_draw(7)
)
