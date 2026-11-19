from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def lightning_burn(ctx):
    """Printed 30, then on heads 30 more to a chosen Benched Pokemon (no
    Weakness or Resistance) and on tails 30 to Zapdos itself."""
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, "Lightning Burn")
    bench = ctx.opponent_bench()
    if heads and heads[0] and bench:
        target = await ctx.choose_pokemon(
            bench, "Choose a Benched Pokemon to take 30",
            player_id=ctx.opponent_id) or bench[0]
        await ctx.deal_damage(30, target=target, apply_modifiers=False)
    elif not (heads and heads[0]):
        await ctx.deal_damage(30, target=ctx.attacker, apply_modifiers=False)

card = PokemonCardDef(
    guid="4ef04ac1-5d9e-56e3-a3dd-caa99ea2931b",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic", "Zapdos"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Attack(
            title="Lightning Burn",
            game_text="Flip a coin. If heads, and if your opponent has any Benched Pok\u00e9mon, choose 1 of them. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) If tails, Zapdos does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=30,
            effect=lightning_burn,
        ),
    ],
)