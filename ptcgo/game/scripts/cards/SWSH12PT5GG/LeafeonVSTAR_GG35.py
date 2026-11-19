from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.card_effects.passives_common import TakesLessPassive

async def ivy_star(ctx):
    """You may switch 1 of your opponent's Benched Pokémon with their Active
    Pokémon."""
    opp_active = ctx.opponent_active()
    opp_bench = ctx.opponent_bench()
    if opp_active is None or not opp_bench or ctx.effects_blocked(opp_active):
        return
    if not await ctx.ask_yes_no(
        "Switch 1 of your opponent's Benched Pokémon with their Active Pokémon?"
    ):
        return
    target = await ctx.choose_pokemon(
        opp_bench, "Choose the opponent's new Active Pokémon"
    )
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


def _ivy_star_condition(board, player_id, pokemon):
    opponent_id = next(p for p in board.player_ids if p != player_id)
    bench = board.find_player_area(opponent_id, "bench")
    return bool(board.active_pokemon(opponent_id)) and bool(bench and bench.children)

card = PokemonCardDef(
    guid="3b52d26b-baa4-5a58-9e3a-13e84cb6f26a",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonVSTAR.Name",
    display_name="Leafeon VSTAR",
    searchable_by=["Leafeon VSTAR", "VSTAR", "LeafeonVSTAR"],
    subtypes=["VSTAR"],
    collector_number=35,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloVSTAR,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonV.Name",
    family_id=470,
    abilities=[
        Ability(
            title="Ivy Star",
            game_text="During your turn, you may switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. (You can't use more than 1 VSTAR Power in a game.)",
            effect=ivy_star,
            condition=_ivy_star_condition,
        ),
        Attack(
            title="Leaf Guard",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=protect_next_turn(reduce=30),
        ),
    ],
)