from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)

_CONDITIONS = [
    ("Asleep", SpecialConditions.ASLEEP),
    ("Burned", SpecialConditions.BURNED),
    ("Confused", SpecialConditions.CONFUSED),
    ("Paralyzed", SpecialConditions.PARALYZED),
    ("Poisoned", SpecialConditions.POISONED),
]


async def _miracle_powder(ctx):
    """Flip a coin; on heads pick a Special Condition for the Defending Pokemon."""
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, "Miracle Powder")
    defender = ctx.defender
    if not heads or not heads[0] or defender is None:
        return
    pick = await ctx.choose("Choose a Special Condition",
                            [name for name, _ in _CONDITIONS])
    await ctx.apply_special_condition(defender, _CONDITIONS[pick][1])

card = PokemonCardDef(
    guid="745afa28-9a03-5265-bef3-af08d9730f63",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name",
    display_name="Vivillon",
    searchable_by=["Vivillon", "Stage 2", "Vivillon"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    family_id=664,
    abilities=[
        Attack(
            title="Miracle Powder",
            game_text="Flip a coin. If heads, choose a Special Condition. Your opponent's Active Pok\u00e9mon is now affected by that Special Condition.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=_miracle_powder,
        ),
        Attack(
            title="Bug Buzz",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)