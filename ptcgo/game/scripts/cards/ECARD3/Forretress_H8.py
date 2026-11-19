from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.support_common import switch_self_attack


async def _spinning_blow(ctx):
    results = await ctx.flip_coins(2, "Spinning Blow")
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.deal_damage(20 * heads)
    if heads == 2:
        await switch_self_attack(damage=0)(ctx)


async def _scatterbomb(ctx):
    results = await ctx.flip_coins(2, "Scatterbomb")
    heads = sum(1 for result in results if result)
    tails = len(results) - heads
    if heads:
        for pokemon in ctx.opponent_bench():
            await ctx.deal_damage(10 * heads, target=pokemon, apply_modifiers=False)
    if tails:
        for pokemon in ctx.my_bench():
            await ctx.deal_damage(10 * tails, target=pokemon, apply_modifiers=False)


card = PokemonCardDef(
    guid="3a1b6170-a247-5560-9219-6b0bf39418b9",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Forretress.Name",
    display_name="Forretress",
    searchable_by=["Forretress", "Stage 1", "Forretress"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Attack(
            title="Spinning Blow",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads. If both coins are heads, switch Forretress with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=_spinning_blow,
        ),
        Attack(
            title="Scatterbomb",
            game_text="Flip 2 coins. For each heads, do 10 damage to each of your opponent's Benched Pok\u00e9mon. For each tails, do 10 damage to each of your own Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=_scatterbomb,
        ),
    ],
)