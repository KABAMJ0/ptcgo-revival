from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_both_then_draw, team_rocket_ko_last_turn

card = SupporterCardDef(
    guid="0063e060-895d-5494-8243-1756cccc6df5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsArcher.Name",
    display_name="Team Rocket's Archer",
    searchable_by=["Team Rocket's Archer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=170,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=shuffle_both_then_draw(5, 3), condition=team_rocket_ko_last_turn()
)
