from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import flip_protection
from ptcgo.game.attributes import AttrID


async def _healing_light(ctx):
    """Healing Light: 1 counter off each of your damaged Pokemon."""
    for pokemon in ctx.my_pokemon_in_play():
        if pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon):
            await ctx.heal(10, target=pokemon)

card = PokemonCardDef(
    guid="13cf8ce0-7176-558d-8019-b03f1b926ce6",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightDragonair.Name",
    display_name="Light Dragonair",
    searchable_by=["Light Dragonair", "Stage 1", "LightDragonair"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Healing Light",
            game_text="Remove 1 damage counter from each of your Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_healing_light,
        ),
        Attack(
            title="Protective Wave",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Light Dragonair.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
    ],
)