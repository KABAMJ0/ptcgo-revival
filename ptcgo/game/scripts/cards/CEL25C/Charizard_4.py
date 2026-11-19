from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.data_utils import Activations


def _can_energy_burn(board, player_id, pokemon=None):
    return pokemon is not None and bool(board.attached_energies(pokemon))


async def energy_burn(ctx):
    turn = getattr(getattr(ctx.board, "turn_state", None), "turn_number", None)
    ctx.rewrite_energy_types([PokemonTypes.FIRE.value], pokemon=ctx.source,
                             through_turn=turn)

card = PokemonCardDef(
    guid="a9e9e867-6bd8-56a3-95fd-cac8891c038b",
    key="CEL25C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="CEL25C",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=6,
    abilities=[
        Ability(
            title="Energy Burn",
            game_text="As often as you like during your turn (before your attack), you may turn all Energy attached to Charizard into Fire Energy for the rest of the turn. This power can't be used if Charizard is Asleep, Confused, or Paralyzed.",
            activation=Activations.UNLIMITED,
            condition=_can_energy_burn,
            effect=energy_burn,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 Energy cards attached to Charizard in order to use this attack.",
            cost={PokemonTypes.FIRE: 4},
            damage=100,
            effect=unimplemented,
        ),
    ],
)