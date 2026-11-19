from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import is_water_energy
from ptcgo.game.card_effects.support_common import move_energy_between


def _wash_out_condition(board, player_id, pokemon) -> bool:
    """A Water Energy on the Bench and an Active Pokemon to move it to."""
    if board.active_pokemon(player_id) is None:
        return False
    bench = board.find_player_area(player_id, "bench")
    return any(is_water_energy(energy)
               for benched in (bench.children if bench else [])
               for energy in board.attached_energies(benched))


card = PokemonCardDef(
    guid="24a7c96c-03ac-5122-84d3-2a186d80bfba",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name",
    display_name="Dewgong",
    searchable_by=["Dewgong", "Stage 1", "Dewgong"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    family_id=86,
    abilities=[
        Ability(
            title="Wash Out",
            game_text="As often as you like during your turn, you may use this Ability. Move a Water Energy from 1 of your Benched Pok\u00e9mon to your Active Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            effect=move_energy_between(is_water_energy, count=1, from_pool="bench",
                                       to_pool="active",
                                       prompt="Choose a Water Energy to move"),
            condition=_wash_out_condition,
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 2},
            damage=60,
        ),
    ],
)