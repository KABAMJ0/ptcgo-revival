from ptcgo.game.card_effects.trainers import team_yell_grunt, opponent_has_energy_attached
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="5310e99f-68c1-5675-8c70-7f989ffb9e9e",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamYellGrunt.Name",
    display_name="Team Yell Grunt",
    searchable_by=["Team Yell Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=184,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=team_yell_grunt,
    condition=opponent_has_energy_attached
)
