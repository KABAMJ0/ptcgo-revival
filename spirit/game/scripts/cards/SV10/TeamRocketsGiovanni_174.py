from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import switch_team_then_gust

card = SupporterCardDef(
    guid="1d21c21f-ec82-513a-8b41-7e4ec93cc7e9",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsGiovanni.Name",
    display_name="Team Rocket's Giovanni",
    searchable_by=["Team Rocket's Giovanni", "Supporter"],
    subtypes=["Supporter"],
    collector_number=174,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=switch_team_then_gust("team rocket")
)
