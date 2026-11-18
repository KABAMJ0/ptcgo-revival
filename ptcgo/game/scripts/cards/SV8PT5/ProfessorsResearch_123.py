from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="211f4bcf-df4d-5d1f-8cec-9bd5692b6713",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearch.Name",
    display_name="Professor's Research",
    searchable_by=["Professor's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=123,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    effect=discard_hand_draw(7)
)
