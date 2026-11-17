from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="cc52aec2-94e6-5c3e-982d-251870211213",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearch.Name",
    display_name="Professor's Research",
    searchable_by=["Professor's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=85,
    set_code="ZSV10PT5",
    rarity=Rarities.Uncommon,
    effect=discard_hand_draw(7)
)
