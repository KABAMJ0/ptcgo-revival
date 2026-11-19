from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import extra_energy_beyond_cost
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def _lightning_cut(ctx):
    results = await ctx.flip_coins(1, "Lightning Cut")
    if results and results[0]:
        await ctx.deal_damage(40)
        for pokemon in ctx.opponent_bench():
            await ctx.deal_damage(10, target=pokemon)
        return
    await ctx.deal_damage(30)
    if ctx.attacker is not None:
        await ctx.deal_damage(10, target=ctx.attacker, apply_modifiers=False)


async def _water_slash(ctx):
    extra = extra_energy_beyond_cost(ctx, PokemonTypes.WATER)
    await ctx.deal_damage(50 + 10 * extra, ignore_resistance=True)


card = PokemonCardDef(
    guid="5bb03942-cef5-5f7d-b9c2-6b131073414c",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningKabutops.Name",
    display_name="Shining Kabutops",
    searchable_by=["Shining Kabutops", "Basic", "ShiningKabutops"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=141,
    abilities=[
        Attack(
            title="Lightning Cut",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 10 more damage and does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) If tails, this attack does 30 damage and Shining Kabutops does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.LIGHTNING: 1},
            damage=30,
            damage_operator="+",
            effect=_lightning_cut,
        ),
        Attack(
            title="Water Slash",
            game_text="Does 50 damage plus 10 more damage for each Water Energy attached to Shining Kabutops but not used to pay for this attack's Energy cost. Don't apply Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.WATER: 2},
            damage=50,
            damage_operator="+",
            effect=_water_slash,
        ),
    ],
)