from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack
from ptcgo.game.card_effects.attacks_common import lock_all_attacks
from ptcgo.game.session.effects import full_stack

async def star_guardian(ctx):
    """VSTAR Power: if the opponent has exactly 1 Prize left, you may make
    them discard 1 of their Benched Pokemon and all attached cards."""
    if not await ctx.ask_yes_no(
        "Choose 1 of your opponent's Benched Pokémon? They discard that "
        "Pokémon and all attached cards."
    ):
        return
    target = await ctx.choose_pokemon(
        ctx.opponent_bench(), "Choose 1 of your opponent's Benched Pokémon"
    )
    if target is None:
        return
    await ctx.discard_cards(full_stack(target))


def _star_guardian_condition(board, player_id, pokemon):
    opponent_id = next(p for p in board.player_ids if p != player_id)
    prizes = board.find_player_area(opponent_id, "prizePile")
    bench = board.find_player_area(opponent_id, "bench")
    return bool(prizes) and len(prizes.children) == 1 and bool(bench and bench.children)

card = PokemonCardDef(
    guid="3e8ee7e2-8400-53a6-9bb9-3bcf5d92c678",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegigigasVSTAR.Name",
    display_name="Regigigas VSTAR",
    searchable_by=["Regigigas VSTAR", "VSTAR", "RegigigasVSTAR"],
    subtypes=["VSTAR"],
    collector_number=55,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloVSTAR,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RegigigasV.Name",
    family_id=486,
    abilities=[
        Ability(
            title="Star Guardian",
            game_text="During your turn, if your opponent has exactly 1 Prize card remaining, you may choose 1 of your opponent's Benched Pok\u00e9mon. They discard that Pok\u00e9mon and all attached cards. (You can't use more than 1 VSTAR Power in a game.)",
            effect=star_guardian,
            condition=_star_guardian_condition,
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=230,
            effect=lock_self_attack(),
        ),
    ],
)