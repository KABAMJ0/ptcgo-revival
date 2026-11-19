from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.card_effects.passives_common import team_hp_bonus
from ptcgo.game.data_utils import def_for

def _stage_of(pokemon) -> int:
    definition = def_for(getattr(pokemon, "archetype_id", "") or "")
    stage = getattr(definition, "stage", None)
    return int(getattr(stage, "value", stage)) if stage is not None else -1
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="f349fdc6-52b6-50d8-a701-0234e66b83f0",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SnowpointTemple.Name",
    display_name="Snowpoint Temple",
    searchable_by=["Snowpoint Temple", "Stadium"],
    subtypes=["Stadium"],
    collector_number=134,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    passive=team_hp_bonus(20, pred=lambda p, c: _stage_of(p) == 0)
)
