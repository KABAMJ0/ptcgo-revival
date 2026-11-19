from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _thunderstorm(ctx):
    """Coin for each of the opponent's Benched Pokemon: heads deals 20 to that
    one (no W/R on the Bench); then 10 damage per tails to this Pokemon."""
    await ctx.deal_damage()
    tails = 0
    for target in ctx.opponent_bench():
        heads = await ctx.flip_coins(1, "Thunderstorm")
        if heads and heads[0]:
            await ctx.deal_damage(20, target=target, apply_modifiers=False)
        else:
            tails += 1
    if tails and ctx.attacker is not None:
        await ctx.deal_damage(10 * tails, target=ctx.attacker,
                              apply_modifiers=False)

card = PokemonCardDef(
    guid="ce842b11-f744-5647-b475-d58bf112f344",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic", "Zapdos"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="BASE3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Attack(
            title="Thunderstorm",
            game_text="For each of your opponent's Benched Pok\u00e9mon, flip a coin. If heads, this attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Then, Zapdos does 10 damage times the number of tails to itself.",
            cost={PokemonTypes.LIGHTNING: 4},
            damage=40,
            effect=_thunderstorm,
        ),
    ],
)