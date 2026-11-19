from ptcgo.game.data_utils import (
    Activations, PokemonCardDef, Attack, Ability, unimplemented,
)
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.pokemon import (
    has_pokemon_subtype, is_basic_fire_energy, is_pokemon_ex,
)
from ptcgo.game.card_effects.support_common import (
    attach_from_hand, hand_attach_condition,
)
from ptcgo.game.session.passives import effective_pokemon_types


def _is_benched_fire(pokemon) -> bool:
    return (not is_in_active_spot(pokemon)
            and PokemonTypes.FIRE.value
            in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or []))


def _has_fire_mega_evolution_ex(board, player_id) -> bool:
    """A Fire Mega Evolution Pokemon ex of this player is in play."""
    return any(has_pokemon_subtype(pokemon, "MEGA") and is_pokemon_ex(pokemon)
               and PokemonTypes.FIRE.value
               in effective_pokemon_types(board, pokemon)
               for pokemon in board.pokemon_in_play(player_id))


_attach_gate = hand_attach_condition(
    is_basic_fire_energy, target="choice", target_pred=_is_benched_fire)


def _excited_turbo_condition(board, player_id, pokemon) -> bool:
    """Fire Mega Evolution ex in play, a Basic Fire Energy in hand, and a
    Benched Fire Pokemon to hold it."""
    return (_has_fire_mega_evolution_ex(board, player_id)
            and _attach_gate(board, player_id, pokemon))


card = PokemonCardDef(
    guid="27623938-4395-54be-a348-de7ff4e82c35",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorioex.Name",
    display_name="Oricorio ex",
    searchable_by=["Oricorio ex", "Basic", "ex", "Oricorioex"],
    subtypes=["Basic", "ex"],
    collector_number=110,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=741,
    abilities=[
        Ability(
            title="Excited Turbo",
            game_text="As often as you like during your turn, if you have any Fire Mega Evolution Pok\u00e9mon ex in play, you may use this Ability. Attach a Basic Fire Energy card from your hand to 1 of your Benched Fire Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_excited_turbo_condition,
            effect=attach_from_hand(
                is_basic_fire_energy, count=1, target="choice",
                target_pred=_is_benched_fire),
        ),
        Attack(
            title="Fire Wing",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)