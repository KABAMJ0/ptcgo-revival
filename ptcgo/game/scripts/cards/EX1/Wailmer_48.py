from ptcgo.game.card_effects.attacks_common import damage_per_extra_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _rest(ctx, counters):
    await ctx.deal_damage()
    target = ctx.attacker
    await ctx.cure_all_conditions(target)
    await ctx.heal(counters * 10, target)
    await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)

card = PokemonCardDef(
    guid="c76c129c-3f5f-5ec2-8457-8ec3a171809f",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    display_name="Wailmer",
    searchable_by=["Wailmer", "Basic", "Wailmer"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=320,
    abilities=[
        Attack(
            title="Rest",
            game_text="Remove all Special Conditions and 4 damage counters from Wailmer (all if there are less than 4). Wailmer is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=lambda ctx: _rest(ctx, 4),
        ),
        Attack(
            title="Water Gun",
            game_text="This attack does 20 damage plus 10 more damage for each Water Energy attached to Wailmer but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per_extra_energy(10, energy_type=PokemonTypes.WATER, cap=20, base=20),
        ),
    ],
)