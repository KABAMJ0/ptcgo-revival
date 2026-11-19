from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes
from ptcgo.game.card_effects.passives_common import team_hp_bonus
from ptcgo.game.data_utils import def_for

def _stage_of(pokemon) -> int:
    definition = def_for(getattr(pokemon, "archetype_id", "") or "")
    stage = getattr(definition, "stage", None)
    return int(getattr(stage, "value", stage)) if stage is not None else -1
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="325e1feb-7c9c-53cc-bb9a-290e604ea12c",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AspertiaCityGym.Name",
    display_name="Aspertia City Gym",
    searchable_by=["Aspertia City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=127,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    passive=team_hp_bonus(20, pred=lambda p, c: PokemonTypes.COLORLESS.value in (p.get_attribute(AttrID.POKEMON_TYPES) or []))
)
