from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_opponent_switch

card = SupporterCardDef(
    guid="26456e2d-8a34-5603-b799-8f8497e0a33f",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ryme.Name",
    display_name="Ryme",
    searchable_by=["Ryme", "Supporter"],
    subtypes=["Supporter"],
    collector_number=221,
    set_code="SV3",
    rarity=Rarities.Rare,
    effect=draw_then_opponent_switch(3)
)
