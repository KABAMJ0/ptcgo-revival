from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.support_common import gust_then
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

async def _sleep_inducer(ctx):
    async def _asleep(inner, new_active):
        await inner.apply_special_condition(new_active, SpecialConditions.ASLEEP)
    await gust_then(_asleep)(ctx)


async def _rapture_pollen(ctx):
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, "Rapture Pollen")
    if heads and heads[0]:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
    else:
        await ctx.heal(20, ctx.attacker)

card = PokemonCardDef(
    guid="770b5610-43fb-5853-8c95-3b237f20521a",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Parasect.Name",
    display_name="Parasect",
    searchable_by=["Parasect", "Stage 1", "Parasect"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name",
    family_id=46,
    abilities=[
        Attack(
            title="Sleep Inducer",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon and switch the Defending Pok\u00e9mon with it. The new Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            effect=_sleep_inducer,
        ),
        Attack(
            title="Rapture Pollen",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep. If tails, remove 2 damage counters from Parasect.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=_rapture_pollen,
        ),
    ],
)
