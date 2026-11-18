from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n_prize_bonus

card = SupporterCardDef(
    guid="ecbb8c35-c33b-5ff4-a583-853de36e5a40",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EmceesHype.Name",
    display_name="Emcee's Hype",
    searchable_by=["Emcee's Hype", "Supporter"],
    subtypes=["Supporter"],
    collector_number=220,
    set_code="SV10",
    rarity=Rarities.Rare,
    effect=draw_n_prize_bonus(2, 2, 3)
)
