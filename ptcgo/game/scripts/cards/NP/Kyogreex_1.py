from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type

async def major_flood(ctx):
    await ctx.deal_damage()
    await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda card: energy_provides_type(card, PokemonTypes.WATER.value),
        prompt="Discard a Water Energy card",
    )
    for target in list(ctx.my_bench()) + list(ctx.opponent_bench()):
        await ctx.deal_damage(10, target=target, apply_modifiers=False)

card = PokemonCardDef(
    guid="b8f84ba8-14ae-5294-bf44-23cd8d55539c",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogreex.Name",
    display_name="Kyogre ex",
    searchable_by=["Kyogre ex", "Basic", "EX", "Kyogreex"],
    subtypes=["Basic", "EX"],
    collector_number=1,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Major Flood",
            game_text="Discard a Water Energy card attached to Kyogre ex. Does 10 damage to each Benched Pok\u00e9mon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 4},
            damage=60,
            effect=major_flood,
        ),
    ],
)