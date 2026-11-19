from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _antler_swipe(ctx):
    heads = await ctx.flip_coins(1, "Antler Swipe")
    if heads and heads[0]:
        if ctx.defender is not None:
            await ctx.deal_damage(20, target=ctx.defender, apply_modifiers=False)
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pok\u00e9mon") or bench[0]
    await ctx.deal_damage(20, target=target, apply_modifiers=False)

card = PokemonCardDef(
    guid="e367bced-5648-50f5-add5-0cd7ca416aa4",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stantler.Name",
    display_name="Stantler",
    searchable_by=["Stantler", "Basic", "Stantler"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=234,
    abilities=[
        Attack(
            title="Threaten",
            game_text="Flip a coin. If heads, look at your opponent's hand. If he or she has any Trainer cards there, choose 1 of them. Your opponent shuffles that card into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Antler Swipe",
            game_text="Flip a coin. If heads, this attack does 20 damage to the Defending Pok\u00e9mon (don't apply Weakness or Resistance). If tails and your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 20 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_antler_swipe,
        ),
    ],
)
