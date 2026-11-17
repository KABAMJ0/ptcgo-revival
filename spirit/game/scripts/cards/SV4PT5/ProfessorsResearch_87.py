from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="e03995fa-18c1-581c-b3f2-c1358e69170c",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearch.Name",
    display_name="Professor's Research",
    searchable_by=["Professor's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=87,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    effect=discard_hand_draw(7)
)
