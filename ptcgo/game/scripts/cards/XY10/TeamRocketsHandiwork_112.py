from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import mill_opponent_per_heads

card = SupporterCardDef(
    guid="7117ef04-9e42-5aa4-a20e-39951495e458",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsHandiwork.Name",
    display_name="Team Rocket's Handiwork",
    searchable_by=["Team Rocket's Handiwork", "Supporter"],
    subtypes=["Supporter"],
    collector_number=112,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=mill_opponent_per_heads(2, 2)
)
