from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import switch_team_then_gust

card = SupporterCardDef(
    guid="1083321e-ab6e-5ca7-8658-011d6f59adf3",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsGiovanni.Name",
    display_name="Team Rocket's Giovanni",
    searchable_by=["Team Rocket's Giovanni", "Supporter"],
    subtypes=["Supporter"],
    collector_number=238,
    set_code="SV10",
    rarity=Rarities.Rare,
    effect=switch_team_then_gust("team rocket")
)
