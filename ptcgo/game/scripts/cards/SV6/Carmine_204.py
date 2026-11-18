from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="33973eb2-d5eb-54e5-912a-b9035bb02988",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Carmine.Name",
    display_name="Carmine",
    searchable_by=["Carmine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=204,
    set_code="SV6",
    rarity=Rarities.Rare,
    effect=discard_hand_draw(5)
)
