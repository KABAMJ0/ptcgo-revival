from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

import math


async def nap(ctx):
    """Remove 3 damage counters from Piloswine."""
    await ctx.heal(30, ctx.attacker)


async def high_speed_charge(ctx):
    """Printed 80, 30 to Piloswine itself, and no attack from it next turn."""
    await ctx.deal_damage()
    await ctx.deal_damage(30, target=ctx.attacker, apply_modifiers=False)

card = PokemonCardDef(
    guid="873706d0-4ec7-5f20-9dca-cd37b8871e16",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    display_name="Piloswine",
    searchable_by=["Piloswine", "Stage 1", "Piloswine"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name",
    family_id=220,
    abilities=[
        Attack(
            title="Nap",
            game_text="Remove 3 damage counters from Piloswine. If it has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=nap,
        ),
        Attack(
            title="High-Speed Charge",
            game_text="Piloswine does 30 damage to itself. Piloswine can't use this attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            locks_next_turn=True,
            effect=high_speed_charge,
        ),
    ],
)