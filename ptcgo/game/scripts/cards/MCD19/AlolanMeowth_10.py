from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def spoil_the_fun(ctx):
    turn_state = getattr(ctx.board, "turn_state", None)
    first_turn = turn_state is not None and turn_state.turn_number <= 2
    went_second = ctx.session.first_player_id not in (None, ctx.player_id)
    await ctx.deal_damage(70 if first_turn and went_second else 10)


card = PokemonCardDef(
    guid="e36ca5f8-9c26-592b-bbaa-d1424db7ad6b",
    key="MCD19",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMeowth.Name",
    display_name="Alolan Meowth",
    searchable_by=["Alolan Meowth", "Basic", "AlolanMeowth"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="MCD19",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=52,
    abilities=[
        Attack(
            title="Spoil the Fun",
            game_text="If you go second, this attack does 60 more damage during your first turn.",
            cost={},
            damage=10,
            damage_operator="+",
            effect=spoil_the_fun,
        ),
    ],
)