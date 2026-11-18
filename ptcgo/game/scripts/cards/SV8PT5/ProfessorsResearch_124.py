from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="4ee5acd4-3e2f-5c89-bb76-f2f38900e905",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearch.Name",
    display_name="Professor's Research",
    searchable_by=["Professor's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    effect=discard_hand_draw(7)
)
