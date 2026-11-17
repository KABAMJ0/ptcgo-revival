from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="e6bff2d9-34e5-5e42-9141-742d41de1a81",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearch.Name",
    display_name="Professor's Research",
    searchable_by=["Professor's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=88,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    effect=discard_hand_draw(7)
)
