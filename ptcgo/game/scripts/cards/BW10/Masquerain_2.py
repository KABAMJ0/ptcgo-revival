from ptcgo.game.data_utils import (
    PokemonCardDef, Attack, Ability, Activations, unimplemented,
)
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, \
    Rarities, TrainerType


def _my_tools(ctx) -> list:
    return [tool for tool, holder in ctx.tools_in_play()
            if holder.owning_player_id == ctx.player_id]


def _has_tool(board, player_id, pokemon) -> bool:
    for held in board.pokemon_in_play(player_id):
        for child in held.children:
            if child.get_attribute(AttrID.TRAINER_TYPE) == \
                    TrainerType.POKEMON_TOOL.value:
                return True
    return False


async def tool_reversal(ctx) -> None:
    tools = _my_tools(ctx)
    if not tools:
        return
    picks = await ctx.choose_cards(
        tools, 1, prompt="Choose a Pokémon Tool to put into your hand")
    if picks:
        await ctx.put_in_hand(list(picks))


card = PokemonCardDef(
    guid="b309100b-2846-5fa2-ad95-e60d102f1cb2",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name",
    display_name="Masquerain",
    searchable_by=["Masquerain", "Stage 1", "Team Plasma", "Masquerain"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=2,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    family_id=283,
    abilities=[
        Ability(
            title="Tool Reversal",
            game_text="As often as you like during your turn (before your attack), you may put a Pok\u00e9mon Tool card attached to 1 of your Pok\u00e9mon into your hand.",
            activation=Activations.UNLIMITED,
            condition=_has_tool,
            effect=tool_reversal,
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)