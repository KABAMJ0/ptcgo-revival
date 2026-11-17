from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="4f341586-b7d6-57e6-8554-7d98c69c7d5b",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearchProfessorTuro.Name",
    display_name="Professor's Research (Professor Turo)",
    searchable_by=["Professor's Research (Professor Turo)", "Supporter"],
    subtypes=["Supporter"],
    collector_number=190,
    set_code="SV1",
    rarity=Rarities.Rare,
    effect=discard_hand_draw(7)
)
