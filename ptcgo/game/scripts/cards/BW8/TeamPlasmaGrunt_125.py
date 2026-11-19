from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_contains, draw_n, with_discard_cost

_TEAM_PLASMA = card_named_contains("Team Plasma")



card = SupporterCardDef(
    guid="2c39126b-92c3-5ab9-96a0-55801cdea99b",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamPlasmaGrunt.Name",
    display_name="Team Plasma Grunt",
    searchable_by=["Team Plasma Grunt", "Supporter", "Team Plasma"],
    subtypes=["Supporter", "Team Plasma"],
    collector_number=125,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, draw_n(4), predicate=_TEAM_PLASMA)
)
