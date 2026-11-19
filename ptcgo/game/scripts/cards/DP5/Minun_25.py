from ptcgo.game.card_effects.attacks_common import named_in_play
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def spark_plus(ctx):
    """20 to the Active, and 20 to a chosen Benched Pokemon with Plusle out."""
    await ctx.deal_damage(20)
    bench = list(ctx.opponent_bench())
    if not bench or not named_in_play("Plusle", side="mine")(ctx):
        return
    pick = await ctx.choose_pokemon(bench, "Choose a Benched Pok\u00e9mon")
    if pick is not None:
        await ctx.deal_damage(20, target=pick, apply_modifiers=False)

card = PokemonCardDef(
    guid="e420174f-c5ed-5873-a669-da8a21f7014f",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name",
    display_name="Minun",
    searchable_by=["Minun", "Basic", "Minun"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="DP5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=312,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="(+) Spark",
            game_text="If Plusle is on your Bench, this attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=spark_plus,
        ),
    ],
)