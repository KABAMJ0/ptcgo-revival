from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import team_rocket_great_ball

card = ItemCardDef(
    guid="4a73083a-4121-5a47-824d-6d3de0f3c216",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsGreatBall.Name",
    display_name="Team Rocket's Great Ball",
    searchable_by=["Team Rocket's Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=205,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=team_rocket_great_ball()
)
