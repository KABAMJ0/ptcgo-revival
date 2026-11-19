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
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def power_wave(ctx):
    """30 to every Pokemon in play that has any Poke-Powers."""
    for pokemon in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
        if _has_kind(pokemon, AbilityTypes.POKE_POWER):
            await ctx.deal_damage(30, target=pokemon)

card = PokemonCardDef(
    guid="04fb52a9-67d3-56e6-8011-5c0e0628c567",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manectric.Name",
    display_name="Manectric",
    searchable_by=["Manectric", "Stage 1", "Manectric"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    family_id=309,
    abilities=[
        Ability(
            title="Electric Barrier",
            game_text="Prevent all damage done to your Benched Pok\u00e9mon (excluding any Manectric) by attacks.",
            effect=unimplemented,
        ),
        Attack(
            title="Power Wave",
            game_text="This attack does 30 damage to each Pok\u00e9mon that has any Pok\u00e9-Powers (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=power_wave,
        ),
        Attack(
            title="Attract Current",
            game_text="Search your deck for a Lightning Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)