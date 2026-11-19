from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import PokemonTypes
from ptcgo.game.card_effects.passives_common import takes_less_passive, pokemon_of_types
from ptcgo.game.attributes import AttrID, PokemonTypes
from ptcgo.game.data_utils import def_for

def _stage_of(pokemon) -> int:
    definition = def_for(getattr(pokemon, "archetype_id", "") or "")
    stage = getattr(definition, "stage", None)
    return int(getattr(stage, "value", stage)) if stage is not None else -1
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="f23f97e2-ad14-5c48-82f6-a579786983fa",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SproutTower.Name",
    display_name="Sprout Tower",
    searchable_by=["Sprout Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=97,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    passive=takes_less_passive(30, protects="each", attacker_pred=pokemon_of_types(PokemonTypes.COLORLESS.value))
)
