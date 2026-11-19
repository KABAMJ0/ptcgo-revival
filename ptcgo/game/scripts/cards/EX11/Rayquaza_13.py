from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, def_for, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per


def _missing_holon_guard(ctx) -> bool:
    """Delta Guard: with a Holon Energy card attached, Lightning Storm's effect
    (the 7 damage counters on Rayquaza) is ignored."""
    for energy in ctx.attached_energies(ctx.attacker):
        definition = def_for(getattr(energy, "archetype_id", "") or "")
        if (getattr(definition, "display_name", "") or "").startswith("Holon Energy"):
            return False
    return True


async def _lightning_storm(ctx):
    """Printed damage, then 7 damage counters on Rayquaza -- unless Delta Guard
    ignores that effect."""
    await ctx.deal_damage()
    if _missing_holon_guard(ctx):
        await ctx.deal_damage(70, target=ctx.attacker, as_counters=True)


card = PokemonCardDef(
    guid="6b3e443d-fc6a-57b0-8b8f-2eaa44240e96",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza δ",
    searchable_by=["Rayquaza \u03b4", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.WATER,
    family_id=384,
    abilities=[
        Ability(
            title="Delta Guard",
            game_text="As long as Rayquaza has any Holon Energy cards attached to it, ignore the effect of Rayquaza's Lightning Storm attack.",
            effect=unimplemented,
        ),
        Attack(
            title="Power Blow",
            game_text="Does 10 damage times the amount of Energy attached to Rayquaza.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(count_energy("self"), 10, base=0),
        ),
        Attack(
            title="Lightning Storm",
            game_text="Put 7 damage counters on Rayquaza.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_lightning_storm,
        ),
    ],
)