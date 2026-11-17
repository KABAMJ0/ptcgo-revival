from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import switch_team_then_gust

card = SupporterCardDef(
    guid="457d07c6-b7a5-542a-9367-be2d158bfe5d",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsGiovanni.Name",
    display_name="Team Rocket's Giovanni",
    searchable_by=["Team Rocket's Giovanni", "Supporter"],
    subtypes=["Supporter"],
    collector_number=225,
    set_code="SV10",
    rarity=Rarities.Rare,
    effect=switch_team_then_gust("team rocket")
)
