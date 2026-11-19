from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes
from ptcgo.game.card_effects.passives_common import condition_immunity_passive
from ptcgo.game.data_utils import def_for

def _stage_of(pokemon) -> int:
    definition = def_for(getattr(pokemon, "archetype_id", "") or "")
    stage = getattr(definition, "stage", None)
    return int(getattr(stage, "value", stage)) if stage is not None else -1
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="755abe03-b6d9-5bf6-b528-7d69d32a5e04",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SidneysStadium.Name",
    display_name="Sidney's Stadium",
    searchable_by=["Sidney's Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=82,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    passive=condition_immunity_passive(protects=lambda t, c: PokemonTypes.DARKNESS.value in (t.get_attribute(AttrID.POKEMON_TYPES) or []))
)
