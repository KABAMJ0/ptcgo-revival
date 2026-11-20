from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import retreat_cost_modifier
from ptcgo.game.card_effects.trainers import team_aqua_target


def _not_team_aqua(pokemon, board) -> bool:
    return not team_aqua_target(pokemon)

card = StadiumCardDef(
    guid="b153aa0a-2aa0-5609-b220-9f77233a7231",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquasSecretBase.Name",
    display_name="Team Aqua's Secret Base",
    searchable_by=["Team Aqua's Secret Base", "Stadium"],
    subtypes=["Stadium"],
    collector_number=28,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    passive=retreat_cost_modifier(1, pred=_not_team_aqua),
)
