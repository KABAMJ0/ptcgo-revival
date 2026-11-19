from ptcgo.game.data_utils import StadiumCardDef, unimplemented, def_for
from ptcgo.game.card_effects.passives_common import (
    attack_cost_modifier, bench_capacity_passive, team_damage_boost_passive,
    pokemon_of_types,
)
from ptcgo.game.attributes import Rarities, AttrID, PokemonTypes
from ptcgo.game.card_effects.pokemon import has_pokemon_subtype


def has_tera(player_id, board) -> bool:
    """Area Zero Underdepths: the raise applies only while that player has a
    Tera Pokemon in play. Called as (player_id, board) by the capacity hook."""
    if board is None:
        return False
    for pokemon in board.pokemon_in_play(player_id):
        if has_pokemon_subtype(pokemon, "Tera"):
            return True
    return False


def area_zero_cap(player_id, board) -> int:
    return 8 if has_tera(player_id, board) else 5

def area_zero_passive():
    return bench_capacity_passive(8, mode="raise", raise_pred=has_tera)


card = StadiumCardDef(
    guid="5a29f77d-a55a-5428-96d9-9feaab82c8f3",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AreaZeroUnderdepths.Name",
    display_name="Area Zero Underdepths",
    searchable_by=["Area Zero Underdepths", "Stadium"],
    subtypes=["Stadium"],
    collector_number=131,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    passive=area_zero_passive()
)
