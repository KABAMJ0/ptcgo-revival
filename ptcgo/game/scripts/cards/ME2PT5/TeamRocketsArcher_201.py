from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_both_then_draw, team_rocket_ko_last_turn

card = SupporterCardDef(
    guid="12b2a860-fa29-577f-8511-434461d6e945",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsArcher.Name",
    display_name="Team Rocket's Archer",
    searchable_by=["Team Rocket's Archer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=201,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=shuffle_both_then_draw(5, 3), condition=team_rocket_ko_last_turn()
)
