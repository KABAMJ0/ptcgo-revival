from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="544a6355-c821-5bc8-b64c-f6cf3daf2fd2",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearch.Name",
    display_name="Professor's Research",
    searchable_by=["Professor's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=125,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    effect=discard_hand_draw(7)
)
