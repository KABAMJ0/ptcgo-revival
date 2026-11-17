from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="0bc691ac-d9a9-578b-b6e6-f29578c12227",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearchProfessorTuro.Name",
    display_name="Professor's Research (Professor Turo)",
    searchable_by=["Professor's Research (Professor Turo)", "Supporter"],
    subtypes=["Supporter"],
    collector_number=241,
    set_code="SV1",
    rarity=Rarities.Rare,
    effect=discard_hand_draw(7)
)
