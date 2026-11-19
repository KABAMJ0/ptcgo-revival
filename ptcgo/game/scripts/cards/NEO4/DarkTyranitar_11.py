from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import bare_mill
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _mountain_smasher(ctx):
    fighting = [energy for energy in ctx.attached_energies(ctx.attacker)
                if energy_provides_type(energy, PokemonTypes.FIGHTING.value)]
    if not fighting:
        return
    results = await ctx.flip_coins(len(fighting), "Mountain Smasher")
    heads = sum(1 for result in results if result)
    if heads <= 0:
        return
    await ctx.deal_damage(20 * heads)
    await bare_mill(heads, opponent=True)(ctx)


async def _fling_away(ctx):
    """Fling Away: 30 instead of 50, plus 30 on a Benched Pokemon."""
    bench = ctx.opponent_bench()
    if not bench:
        await ctx.deal_damage()
        return
    await ctx.deal_damage(30)
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokemon")
    if target is not None:
        await ctx.deal_damage(30, target=target, apply_modifiers=False)

card = PokemonCardDef(
    guid="670e39b1-2ace-5ac0-bca3-fd84f7a3a8af",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkTyranitar.Name",
    display_name="Dark Tyranitar",
    searchable_by=["Dark Tyranitar", "Stage 2", "DarkTyranitar"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPupitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Mountain Smasher",
            game_text="Flip a number of coins equal to the number of Fighting Energy cards attached to Dark Tyranitar. This attack does 20 damage times the number of heads. Then, for each heads, discard the top card from your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="x",
            effect=_mountain_smasher,
        ),
        Attack(
            title="Fling Away",
            game_text="If your opponent has any Benched Pok\u00e9mon, this attack does 30 damage instead of 50 and choose 1 of those Benched Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=_fling_away,
        ),
    ],
)