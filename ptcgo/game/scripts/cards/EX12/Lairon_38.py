from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _rest(ctx, counters):
    await ctx.deal_damage()
    target = ctx.attacker
    await ctx.cure_all_conditions(target)
    await ctx.heal(counters * 10, target)
    await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)

card = PokemonCardDef(
    guid="9a469c54-cb4b-588f-ba01-3933d0af8432",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    display_name="Lairon",
    searchable_by=["Lairon", "Stage 1", "Lairon"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Rest",
            game_text="Remove all Special Conditions and 5 damage counters (all if there are less than 5) from Lairon. Lairon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=lambda ctx: _rest(ctx, 5),
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)