from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _final_gambit(ctx):
    """80 to the Defending Pokemon; the 80 self-hit only on two tails."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(2, "Final Gambit")
    if results and not any(results):
        await ctx.deal_damage(80, target=ctx.attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="bb4cc7d9-4581-5a55-a4bf-82906056acda",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Basculin.Name",
    display_name="Basculin",
    searchable_by=["Basculin", "Basic", "Basculin"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="BW2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=550,
    abilities=[
        Attack(
            title="Flail",
            game_text="Does 10 damage times the number of damage counters on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Final Gambit",
            game_text="Flip 2 coins. If both of them are tails, this Pok\u00e9mon does 80 damage to itself.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=_final_gambit,
        ),
    ],
)