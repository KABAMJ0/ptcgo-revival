from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_turn_boost

card = SupporterCardDef(
    guid="fa368c4f-f5f1-568a-abd6-199c9a693d29",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BucksTraining.Name",
    display_name="Buck's Training",
    searchable_by=["Buck's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    effect=draw_then_turn_boost(2, 10)
)
