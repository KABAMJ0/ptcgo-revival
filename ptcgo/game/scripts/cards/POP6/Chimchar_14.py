from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import is_fire_energy

async def ember(ctx):
    """30; heads discards a Fire Energy attached to Chimchar."""
    await ctx.deal_damage(30)
    results = await ctx.flip_coins(1, "Ember")
    if results and results[0]:
        await ctx.discard_energy_from(ctx.attacker, 1, predicate=is_fire_energy)
card = PokemonCardDef(
    guid="4270540e-5827-5899-b2b7-b9ba37c32667",
    key="POP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimchar.Name",
    display_name="Chimchar",
    searchable_by=["Chimchar", "Basic", "Chimchar"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="POP6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=390,
    abilities=[
        Attack(
            title="Scratch",
            cost={},
            damage=10,
        ),
        Attack(
            title="Ember",
            game_text="Flip a coin. If heads discard a Fire Energy attached to Chimchar.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ember,
        ),
    ],
)