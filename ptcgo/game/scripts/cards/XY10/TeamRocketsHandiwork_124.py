from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import mill_opponent_per_heads

card = SupporterCardDef(
    guid="b0a3f91f-e4d7-5357-9f5a-00e623edd536",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsHandiwork.Name",
    display_name="Team Rocket's Handiwork",
    searchable_by=["Team Rocket's Handiwork", "Supporter"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    effect=mill_opponent_per_heads(2, 2)
)
