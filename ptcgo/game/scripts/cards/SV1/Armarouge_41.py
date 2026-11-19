from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.pokemon import is_fire_energy
from ptcgo.game.card_effects.support_common import move_energy_between
from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


def _fire_off_offered(board, player_id, pokemon):
    active = board.active_pokemon(player_id)
    bench = board.find_player_area(player_id, "bench")
    if active is None or bench is None:
        return False
    return any(is_fire_energy(energy)
               for benched in bench.children
               for energy in board.attached_energies(benched))


card = PokemonCardDef(
    guid="bfdcd24d-7dfb-5527-8447-ddacab96af06",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armarouge.Name",
    display_name="Armarouge",
    searchable_by=["Armarouge", "Stage 1", "Armarouge"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Ability(
            title="Fire Off",
            game_text="As often as you like during your turn, you may move a Fire Energy from 1 of your Benched Pok\u00e9mon to your Active Pok\u00e9mon.",
            effect=move_energy_between(is_fire_energy, count=1, from_pool="bench",
                                      to_pool="active",
                                      prompt="Choose a Fire Energy to move to your Active Pok\u00e9mon"),
            activation=Activations.UNLIMITED,
            condition=_fire_off_offered,
        ),
        Attack(
            title="Flame Cannon",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)
