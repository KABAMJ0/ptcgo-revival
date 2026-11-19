from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _rest(ctx, counters):
    await ctx.deal_damage()
    target = ctx.attacker
    await ctx.cure_all_conditions(target)
    await ctx.heal(counters * 10, target)
    await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)

card = PokemonCardDef(
    guid="82993508-572c-5f8d-ba30-4791313c399d",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    display_name="Jigglypuff",
    searchable_by=["Jigglypuff", "Basic", "Jigglypuff"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=39,
    abilities=[
        Attack(
            title="Doubleslap",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Rest",
            game_text="Remove all Special Conditions and 3 damage counters from Jigglypuff (all if there are less than 3). Jigglypuff is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=lambda ctx: _rest(ctx, 3),
        ),
    ],
)