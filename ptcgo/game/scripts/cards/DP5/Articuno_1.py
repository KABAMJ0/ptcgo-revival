from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import spread_damage

async def blizzard(ctx):
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, ctx.ability.title)
    if heads and heads[0]:
        await spread_damage(10)(ctx)
    else:
        await spread_damage(10, side="mine")(ctx)


card = PokemonCardDef(
    guid="14d9b6be-3576-5b58-9244-d7039be978ec",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic", "Articuno"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="DP5",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Ability(
            title="Freezing Screech",
            game_text="Once during your turn, when you put Articuno from your hand onto your Bench, you may flip a coin. If heads, choose 1 of the Defending Pok\u00e9mon. That Pok\u00e9mon is now Paralyzed.",
            effect=unimplemented,
        ),
        Attack(
            title="Blizzard",
            game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. If tails, this attack does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=blizzard,
        ),
    ],
)