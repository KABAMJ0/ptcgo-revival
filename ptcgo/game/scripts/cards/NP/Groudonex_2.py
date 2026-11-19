from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type

async def major_earthquake(ctx):
    await ctx.deal_damage()
    await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda card: energy_provides_type(card, PokemonTypes.FIGHTING.value),
        prompt="Discard a Fighting Energy card",
    )
    for target in ctx.my_bench():
        await ctx.deal_damage(10, target=target, apply_modifiers=False)

card = PokemonCardDef(
    guid="593a0993-c363-5349-a1eb-42f314a8c31a",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudonex.Name",
    display_name="Groudon ex",
    searchable_by=["Groudon ex", "Basic", "EX", "Groudonex"],
    subtypes=["Basic", "EX"],
    collector_number=2,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(
            title="Major Earthquake",
            game_text="Discard a Fighting Energy card attached to Groudon ex. Does 10 damage to your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 4},
            damage=80,
            effect=major_earthquake,
        ),
    ],
)