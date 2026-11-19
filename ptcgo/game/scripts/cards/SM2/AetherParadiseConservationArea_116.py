from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.passives_common import pokemon_of_types
from ptcgo.game.card_effects.trainers import is_basic_pokemon, stadium_takes_less_for


_GRASS_OR_LIGHTNING = pokemon_of_types(
    PokemonTypes.GRASS.value, PokemonTypes.LIGHTNING.value)


def _basic_grass_or_lightning(pokemon) -> bool:
    """A Basic Grass or Basic Lightning Pokemon."""
    return is_basic_pokemon(pokemon) and _GRASS_OR_LIGHTNING(pokemon)


card = StadiumCardDef(
    guid="9b047b0c-08d7-59a2-9c03-dcf509f6f918",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AetherParadiseConservationArea.Name",
    display_name="Aether Paradise Conservation Area",
    searchable_by=["Aether Paradise Conservation Area", "Stadium"],
    subtypes=["Stadium"],
    collector_number=116,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    passive=stadium_takes_less_for(30, _basic_grass_or_lightning),
)
