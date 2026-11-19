from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import (
    AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)
from ptcgo.game.card_effects.attacks_common import condition_attack


async def synchronoise(ctx):
    """Printed 60; 20 to each Benched Pokemon sharing a type with the
    opponent's Active, with no Weakness or Resistance on the Bench."""
    active = ctx.opponent_active()
    shared = set(active.get_attribute(AttrID.POKEMON_TYPES) or []) if active else set()
    await ctx.deal_damage()
    if not shared:
        return
    for pokemon in ctx.opponent_bench():
        if shared & set(pokemon.get_attribute(AttrID.POKEMON_TYPES) or []):
            await ctx.deal_damage(20, target=pokemon, apply_modifiers=False)


card = PokemonCardDef(
    guid="01cff739-aee1-5c8e-8ac3-afdd146a1091",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bruxish.Name",
    display_name="Bruxish",
    searchable_by=["Bruxish", "Basic", "Bruxish"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=779,
    abilities=[
        Attack(
            title="Gnash Teeth",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Synchronoise",
            game_text="This attack does 20 damage to each of your opponent's Benched Pok\u00e9mon that shares a type with your opponent's Active Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=synchronoise,
        ),
    ],
)