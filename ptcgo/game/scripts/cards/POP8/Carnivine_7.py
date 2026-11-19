from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import (
    AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)


async def swallow_up(ctx):
    defender, holder = ctx.defender, ctx.attacker
    if (defender is not None and holder is not None
            and defender.get_attribute(AttrID.HP, 0)
            < holder.get_attribute(AttrID.HP, 0)):
        await ctx.deal_damage(60)
    else:
        await ctx.deal_damage(30)


async def wring_out(ctx):
    await ctx.deal_damage(20)
    results = await ctx.flip_coins(1, "Wring Out")
    if not (results and results[0]):
        return
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
    await ctx.discard_energy_from(defender, 1)

card = PokemonCardDef(
    guid="10ab8da3-bcf3-5471-996a-f53a652ebd50",
    key="POP8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name",
    display_name="Carnivine",
    searchable_by=["Carnivine", "Basic", "Carnivine"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="POP8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=455,
    abilities=[
        Attack(
            title="Swallow Up",
            game_text="Before doing damage, count the remaining HP of the Defending Pok\u00e9mon and Carnivine. If the Defending Pok\u00e9mon has fewer remaining HP than Carnivine's, this attack does 60 damage instead.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=swallow_up,
        ),
        Attack(
            title="Wring Out",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed and discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            effect=wring_out,
        ),
    ],
)