from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import (
    AttrID, CLIENT_POKEMON_TYPE_NAMES, PokemonTypes, PokemonStage, Rarities,
)


async def rainbow_wave(ctx):
    types = []
    for energy in ctx.attached_energies(ctx.attacker):
        for energy_type in PokemonTypes:
            if energy_type is PokemonTypes.COLORLESS:
                continue
            if energy_type.value in types:
                continue
            if energy_provides_type(energy, energy_type.value):
                types.append(energy_type.value)
    if not types:
        return 0
    labels = [CLIENT_POKEMON_TYPE_NAMES[PokemonTypes(t)] for t in types]
    pick = await ctx.choose(
        "Choose a type of Energy other than Colorless attached to Mew.", labels)
    if pick is None or not 0 <= pick < len(types):
        return 0
    chosen = types[pick]
    dealt = 0
    for pokemon in ctx.opponent_pokemon_in_play():
        if chosen in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or []):
            dealt += await ctx.deal_damage(
                20, target=pokemon, apply_modifiers=False)
    return dealt

card = PokemonCardDef(
    guid="87a2036c-4ee8-532d-b98e-a2e0a95df53e",
    key="SI1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="SI1",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Attack(
            title="Rainbow Wave",
            game_text="Choose a type of Energy other than Colorless attached to Mew. This attack does 20 damage to each of your opponent's Pok\u00e9mon of that type (including Benched Pok\u00e9mon). Don't apply Weakness and Resistance.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=rainbow_wave,
        ),
    ],
)