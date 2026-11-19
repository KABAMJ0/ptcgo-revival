from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, is_stage_two
from ptcgo.game.card_effects.passives_common import pokemon_of_types
from ptcgo.game.card_effects.support_common import attach_from_hand


_GRASS_FIRE_WATER = pokemon_of_types(
    PokemonTypes.GRASS.value, PokemonTypes.FIRE.value, PokemonTypes.WATER.value)


def _stage_two_grass_fire_water(pokemon) -> bool:
    """A Stage 2 Grass, Fire or Water Pokemon."""
    return is_stage_two(pokemon) and _GRASS_FIRE_WATER(pokemon)


card = SupporterCardDef(
    guid="82d93bf4-a25f-5210-94ce-bccc27c2168e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TheMaskedRoyal.Name",
    display_name="The Masked Royal",
    searchable_by=["The Masked Royal", "Supporter"],
    subtypes=["Supporter"],
    collector_number=139,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=attach_from_hand(
        is_basic_energy_card, count=1, target="choice",
        target_pred=_stage_two_grass_fire_water,
        prompt="Choose a basic Energy card to attach to 1 of your Stage 2 Grass, Fire or Water Pok\u00e9mon"),
)
