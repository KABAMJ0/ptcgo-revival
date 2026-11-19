from ptcgo.game.card_effects.attacks_common import damage_per, count_energy
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _is_grass(energy):
    return energy_provides_type(energy, PokemonTypes.GRASS.value)


def energy_reload_condition(board, player_id, pokemon):
    if pokemon is None:
        return False
    others = [p for p in board.pokemon_in_play(player_id) if p is not pokemon]
    return any(_is_grass(energy) for p in others
               for energy in board.attached_energies(p))


async def energy_reload(ctx):
    me = ctx.source
    others = [p for p in ctx.my_pokemon_in_play() if p is not me]
    if me is None or not others:
        return False
    moved = await ctx.move_energy_freely(
        others, [me], predicate=_is_grass, max_count=1,
        prompt="Choose a Grass Energy to move to this Pokémon",
    )
    return bool(moved)


card = PokemonCardDef(
    guid="c2ab2388-8d93-5255-9415-d669e729b781",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningGenesect.Name",
    display_name="Shining Genesect",
    searchable_by=["Shining Genesect", "Basic", "ShiningGenesect"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SL",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=649,
    abilities=[
        Ability(
            title="Energy Reload",
            game_text="Once during your turn (before your attack), you may move a Grass Energy from 1 of your other Pok\u00e9mon to this Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=energy_reload_condition,
            effect=energy_reload,
        ),
        Attack(
            title="Gaia Blaster",
            game_text="This attack does 20 more damage times the amount of Grass Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.GRASS), 20, base=50),
        ),
    ],
)