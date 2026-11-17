from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="63cf7a3b-f397-5b5e-910f-796ce35f137e",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearch.Name",
    display_name="Professor's Research",
    searchable_by=["Professor's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=155,
    set_code="SV9",
    rarity=Rarities.Common,
    effect=discard_hand_draw(7)
)
