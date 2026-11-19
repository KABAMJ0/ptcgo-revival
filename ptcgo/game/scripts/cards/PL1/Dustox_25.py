from ptcgo.game.attributes import AbilityTypes
from ptcgo.game.data_utils import def_for


def _has_kind(pokemon, *kinds):
    """Whether this Pokemon carries a printed ability of one of `kinds`
    (POKE_POWER / POKE_BODY), read off the definition's restored kinds."""
    if pokemon is None:
        return False
    definition = def_for(pokemon.archetype_id)
    for ability in getattr(definition, "abilities", []) or []:
        if getattr(ability, "ability_type", None) in kinds:
            return True
    return False

from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)


async def chemical_scale(ctx):
    """After the damage: a defender holding a Poke-Power or Poke-Body is
    Burned and Confused."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    if not _has_kind(defender, AbilityTypes.POKE_POWER, AbilityTypes.POKE_BODY):
        return
    await ctx.apply_special_condition(defender, SpecialConditions.BURNED)
    await ctx.apply_special_condition(defender, SpecialConditions.CONFUSED)

card = PokemonCardDef(
    guid="3f9b560d-79e7-58eb-bad2-1a0cd213ca60",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dustox.Name",
    display_name="Dustox",
    searchable_by=["Dustox", "Stage 2", "Dustox"],
    subtypes=["Stage 2"],
    collector_number=25,
    set_code="PL1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name",
    family_id=265,
    abilities=[
        Ability(
            title="Camouflage Pattern",
            game_text="Prevent all effects of attacks, including damage, done to Dustox by your opponent's Pok\u00e9mon that is affected by 2 or more Special Conditions.",
            effect=unimplemented,
        ),
        Attack(
            title="Smogscreen",
            game_text="The Defending Pok\u00e9mon is now Poisoned. If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Chemical Scale",
            game_text="If the Defending Pok\u00e9mon has any Pok\u00e9-Powers or Pok\u00e9-Bodies, the Defending Pok\u00e9mon is now Burned and Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=chemical_scale,
        ),
    ],
)