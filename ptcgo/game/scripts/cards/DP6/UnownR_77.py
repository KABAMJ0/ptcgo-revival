from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Activations
from ptcgo.game.session.effects import full_stack
from ptcgo.game.session.passives import is_basic_energy


async def _retire(ctx):
    """RETIRE: Unown R and its attachments leave play without a Knock Out."""
    pokemon = ctx.source
    await ctx.discard_cards(full_stack(pokemon))
    await ctx.draw_cards(1)


async def _hidden_power_move(ctx):
    """Hidden Power (Unown R): move any basic Energy anywhere on your side."""
    await ctx.move_energy_freely(
        ctx.my_pokemon_in_play(), ctx.my_pokemon_in_play(),
        predicate=is_basic_energy, max_count=None,
        prompt="Choose a basic Energy to move")

card = PokemonCardDef(
    guid="cee5d918-476c-5532-9d1b-6ce1d06de7ac",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownR.Name",
    display_name="Unown [R]",
    searchable_by=["Unown [R]", "Basic", "UnownR"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="RETIRE",
            game_text="Once during your turn, if Unown R is on your Bench, you may discard Unown R and all cards attached to it. (This doesn't count as a Knocked Out Pok\u00e9mon.) Then, draw a card.",
                        activation=Activations.ONCE_PER_TURN,
                        condition=lambda board, player_id, pokemon: not is_in_active_spot(pokemon),
            effect=_retire,
        ),
        Attack(
            title="Hidden Power",
            game_text="Move any number of basic Energy cards attached to your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={},
            effect=_hidden_power_move,
        ),
    ],
)