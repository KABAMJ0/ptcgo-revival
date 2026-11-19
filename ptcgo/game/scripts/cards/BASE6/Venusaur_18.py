from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.card_effects.support_common import can_move_energy, move_energy_between
from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.data_utils import Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_can_move_grass = can_move_energy(basic_energy_of("grass"))


def _can_trans(board, player_id, pokemon):
    return unafflicted(board, player_id, pokemon) \
        and _can_move_grass(board, player_id, pokemon)


card = PokemonCardDef(
    guid="f4ca7b3b-693a-5996-a0a6-3f3b0a3170d5",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name",
    display_name="Venusaur",
    searchable_by=["Venusaur", "Stage 2", "Venusaur"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="BASE6",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Energy Trans",
            game_text="As often as you like during your turn (before your attack), you may take 1 Grass Energy card attached to 1 of your Pok\u00e9mon and attach it to a different one. This power can't be used if Venusaur is affected by a Special Condition.",
            activation=Activations.UNLIMITED,
            condition=_can_trans,
            effect=move_energy_between(basic_energy_of("grass"), count=1),
        ),
        Attack(
            title="Solarbeam",
            cost={PokemonTypes.GRASS: 4},
            damage=60,
        ),
    ],
)