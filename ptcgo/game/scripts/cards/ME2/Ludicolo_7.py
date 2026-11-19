from ptcgo.game.data_utils import (
    Activations, PokemonCardDef, Attack, Ability, unimplemented,
)
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import has_pokemon_subtype, is_pokemon_ex
from ptcgo.game.card_effects.support_common import heal_targets
from ptcgo.game.session.passives import effective_max_hp, effective_pokemon_types


def _has_grass_mega_evolution_ex(board, player_id) -> bool:
    """A Grass Mega Evolution Pokemon ex of this player is in play."""
    return any(has_pokemon_subtype(pokemon, "MEGA") and is_pokemon_ex(pokemon)
               and PokemonTypes.GRASS.value
               in effective_pokemon_types(board, pokemon)
               for pokemon in board.pokemon_in_play(player_id))


def _excited_heal_condition(board, player_id, pokemon) -> bool:
    """The offer needs a Grass Mega Evolution ex in play AND something to heal."""
    if not _has_grass_mega_evolution_ex(board, player_id):
        return False
    return any(p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
               for p in board.pokemon_in_play(player_id))


card = PokemonCardDef(
    guid="3a59454c-762f-59e7-92e9-875e47900ca2",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo",
    searchable_by=["Ludicolo", "Stage 2", "Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    family_id=270,
    abilities=[
        Ability(
            title="Excited Heal",
            game_text="Once during your turn, if you have any Grass Mega Evolution Pok\u00e9mon ex in play, you may use this Ability. Heal 60 damage from 1 of your Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_excited_heal_condition,
            effect=heal_targets(60, scope="choice"),
        ),
        Attack(
            title="Lunge Out",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)