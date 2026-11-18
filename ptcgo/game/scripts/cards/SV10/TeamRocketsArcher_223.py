from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_both_then_draw, team_rocket_ko_last_turn

card = SupporterCardDef(
    guid="4598e795-0c7f-5273-99a7-6a8327fd48fd",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsArcher.Name",
    display_name="Team Rocket's Archer",
    searchable_by=["Team Rocket's Archer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=223,
    set_code="SV10",
    rarity=Rarities.Rare,
    effect=shuffle_both_then_draw(5, 3), condition=team_rocket_ko_last_turn()
)
