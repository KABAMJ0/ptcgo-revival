from ptcgo.game.data_utils import (
    Activations, PokemonCardDef, Attack, Ability, unimplemented,
)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import has_pokemon_subtype, is_pokemon_ex


async def excited_dash(ctx):
    """Switch this Benched Pokemon with the Active Pokemon."""
    await ctx.switch_active(ctx.player_id, ctx.source)


def _excited_dash_condition(board, player_id, pokemon) -> bool:
    """On the Bench, with a Mega Evolution Pokemon ex of yours in play."""
    if pokemon is board.active_pokemon(player_id):
        return False
    return any(has_pokemon_subtype(other, "MEGA") and is_pokemon_ex(other)
               for other in board.pokemon_in_play(player_id))


card = PokemonCardDef(
    guid="fc68e24d-f92e-52fb-a166-cf3c5e735ccd",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Linoone.Name",
    display_name="Linoone",
    searchable_by=["Linoone", "Stage 1", "Linoone"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name",
    family_id=263,
    abilities=[
        Ability(
            title="Excited Dash",
            game_text="Once during your turn, if this Pok\u00e9mon is on your Bench, and if you have any Mega Evolution Pok\u00e9mon ex in play, you may use this Ability. Switch this Pok\u00e9mon with your Active Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_excited_dash_condition,
            effect=excited_dash,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)