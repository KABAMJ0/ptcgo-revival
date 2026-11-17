from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="7f3d1151-4e54-55b4-90f0-277d08bb70a8",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearchProfessorSada.Name",
    display_name="Professor's Research (Professor Sada)",
    searchable_by=["Professor's Research (Professor Sada)", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SV1",
    rarity=Rarities.Rare,
    effect=discard_hand_draw(7)
)
