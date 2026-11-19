from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _half_drain(ctx, heal_target):
    """Printed damage, then remove half of it (rounded up to the nearest 10)
    worth of damage counters from `heal_target`; a heal clamps to the damage
    actually on it ("if it has fewer, remove all of them")."""
    dealt = await ctx.deal_damage()
    if heal_target is None or dealt <= 0:
        return
    half = (dealt + 1) // 2
    await ctx.heal(((half + 9) // 10) * 10, heal_target)


async def absorb(ctx):
    await _half_drain(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="e837ad16-bdad-5138-9540-f0511e98182c",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabutops.Name",
    display_name="Kabutops",
    searchable_by=["Kabutops", "Stage 2", "Kabutops"],
    subtypes=["Stage 2"],
    collector_number=27,
    set_code="BASE6",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    family_id=140,
    abilities=[
        Attack(
            title="Sharp Sickle",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
        Attack(
            title="Absorb",
            game_text="Remove a number of damage counters from Kabutops equal to half the damage done to the Defending Pok\u00e9mon (after applying Weakness and Resistance) (rounded up to the nearest 10). If Kabutops has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.FIGHTING: 4},
            damage=40,
            effect=absorb,
        ),
    ],
)