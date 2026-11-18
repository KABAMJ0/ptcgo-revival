from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_opponent_switch

card = SupporterCardDef(
    guid="ed4d4c30-6603-572f-ae29-8ed0102f0daf",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ryme.Name",
    display_name="Ryme",
    searchable_by=["Ryme", "Supporter"],
    subtypes=["Supporter"],
    collector_number=194,
    set_code="SV3",
    rarity=Rarities.Common,
    effect=draw_then_opponent_switch(3)
)
