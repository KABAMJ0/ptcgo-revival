from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import team_aqua_target, stadium_retreat_shift

def _not_team_aqua(pokemon):
    return not team_aqua_target(pokemon)


card = StadiumCardDef(
    guid="0a0b1ff6-c5b0-5cee-b5a1-f2a785a8a4da",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaHideout.Name",
    display_name="Team Aqua Hideout",
    searchable_by=["Team Aqua Hideout", "Stadium"],
    subtypes=["Stadium"],
    collector_number=78,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    passive=stadium_retreat_shift(1, _not_team_aqua)
)
