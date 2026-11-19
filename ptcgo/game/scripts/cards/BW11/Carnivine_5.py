from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def ambush_bite(ctx):
    """Flip a coin: heads pays the printed 20 plus 20 more and strips an Energy
    from the Defending Pokemon; tails pays the printed 20 alone."""
    heads = await ctx.flip_coins(1, "Ambush Bite")
    if not (heads and heads[0]):
        await ctx.deal_damage()
        return
    await ctx.deal_damage(40)
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        await ctx.discard_energy_from(
            defender, 1,
            prompt="Choose an Energy to discard from the Defending Pokémon")


card = PokemonCardDef(
    guid="66c3933a-3ebc-5448-996a-ddd1718a1a51",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name",
    display_name="Carnivine",
    searchable_by=["Carnivine", "Basic", "Carnivine"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=455,
    abilities=[
        Attack(
            title="Ambush Bite",
            game_text="Flip a coin. If heads, this attack does 20 more damage and discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=ambush_bite,
        ),
    ],
)