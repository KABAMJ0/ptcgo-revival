from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.attacks_common import search_bench_as_basic
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _has_react_energy(ctx):
    from ptcgo.game.content.definitions import def_for
    for energy in ctx.attached_energies(ctx.attacker):
        definition = def_for(energy.archetype_id)
        if definition is not None and "react" in (definition.display_name or "").lower():
            return True
    return False


async def stretch_claws(ctx):
    """Printed 20, plus 20 to 1 of the opponent's Benched Pokemon when a React
    Energy is attached."""
    if _has_react_energy(ctx):
        await snipe_attack(20, pool="bench", count=1, also_base=True,
                           apply_modifiers=False)(ctx)
    else:
        await ctx.deal_damage()

card = PokemonCardDef(
    guid="e496735b-4e1e-51c7-8a36-9d1d2b728fb1",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name",
    display_name="Anorith",
    searchable_by=["Anorith", "Stage 1", "Anorith"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ClawFossil.Name",
    family_id=347,
    abilities=[
        Attack(
            title="Influence",
            game_text="Search your deck for Omanyte, Kabuto, Aerodactyl, Lileep, or Anorith and put up to 2 of them onto your Bench. Shuffle your deck afterward. Treat the new Benched Pok\u00e9mon as Basic Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_bench_as_basic(["Omanyte", "Kabuto", "Aerodactyl", "Lileep", "Anorith"], 2, "Choose up to 2 Fossils to Bench"),
        ),
        Attack(
            title="Stretch Claws",
            game_text="If Anorith has any React Energy cards attached to it, this attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=stretch_claws,
        ),
    ],
)