from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _absorb(ctx):
    """Printed damage, then remove counters equal to half of it, rounded up to
    the nearest 10 ("If <name> has fewer damage counters than that, remove all
    of them" is what ctx.heal already clamps to)."""
    dealt = await ctx.deal_damage()
    if dealt <= 0 or ctx.attacker is None:
        return
    await ctx.heal(((dealt // 2 + 9) // 10) * 10, ctx.attacker)

card = PokemonCardDef(
    guid="e5247889-ab4e-580a-be50-03e90f82bdf7",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabutops.Name",
    display_name="Kabutops",
    searchable_by=["Kabutops", "Stage 2", "Kabutops"],
    subtypes=["Stage 2"],
    collector_number=24,
    set_code="BASE3",
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
            effect=_absorb,
        ),
    ],
)