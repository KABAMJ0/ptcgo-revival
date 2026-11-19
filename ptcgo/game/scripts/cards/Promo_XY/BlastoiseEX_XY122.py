from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def rapid_spin(ctx):
    """Printed 30; switch this Pokemon with a Benched one, then the opponent
    switches their Active with one of theirs."""
    await ctx.deal_damage()
    mine = ctx.my_bench()
    if mine:
        target = await ctx.choose_pokemon(mine, "Choose a Benched Pokemon to switch in")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    theirs = [p for p in ctx.opponent_bench()]
    if theirs:
        target = await ctx.choose_pokemon(theirs, "Choose their new Active Pokemon")
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)


card = PokemonCardDef(
    guid="4ca96bbb-b936-520f-972a-efe18f7ef593",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseEX.Name",
    display_name="Blastoise-EX",
    searchable_by=["Blastoise-EX", "Basic", "EX", "BlastoiseEX"],
    subtypes=["Basic", "EX"],
    collector_number=122,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=9,
    abilities=[
        Attack(
            title="Rapid Spin",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. The, your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=rapid_spin,
        ),
        Attack(
            title="Splash Bomb",
            game_text="Flip a coin. If heads, this Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.WATER: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)