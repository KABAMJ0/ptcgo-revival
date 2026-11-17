from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import switch_team_then_gust

card = SupporterCardDef(
    guid="6adab2ee-0197-5cad-8a15-a287c7c3dd6b",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsGiovanni.Name",
    display_name="Team Rocket's Giovanni",
    searchable_by=["Team Rocket's Giovanni", "Supporter"],
    subtypes=["Supporter"],
    collector_number=204,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=switch_team_then_gust("team rocket")
)
