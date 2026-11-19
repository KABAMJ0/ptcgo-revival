from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def exhausted_tackle(ctx):
    heads = await ctx.flip_coins(1, "Exhausted Tackle")
    if heads and heads[0]:
        await ctx.deal_damage(30)
    else:
        await ctx.deal_damage(30, target=ctx.attacker, apply_modifiers=False)

card = PokemonCardDef(
    guid="367837ca-dd38-5ecc-9e48-96bc07bdbf2e",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth",
    searchable_by=["Meowth", "Basic", "Meowth"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title="Exhausted Tackle",
            game_text="Flip a coin. If heads, this attack does 30 damage to your opponent's Active Pok\u00e9mon. If tails, this Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=exhausted_tackle,
        ),
    ],
)