from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.attacks_common import damage_counters_on
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def outrage(ctx):
    """On heads 30 plus 10 per damage counter on Shining Gyarados."""
    heads = await ctx.flip_coins(1, "Outrage")
    if not (heads and heads[0]):
        return
    counters = damage_counters_on("self")(ctx)
    await ctx.deal_damage(30 + 10 * counters)


async def devastate(ctx):
    """Discard 2 Fire Energy or nothing; then 10 to each of their Benched
    Pokemon."""
    fire = [e for e in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(e, PokemonTypes.FIRE.value)]
    if len(fire) < 2:
        return
    for _ in range(2):
        gone = await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda card: energy_provides_type(card, PokemonTypes.FIRE.value),
            prompt="Discard a Fire Energy from Shining Gyarados")
        if not gone:
            return
    for pokemon in list(ctx.opponent_bench()):
        await ctx.deal_damage(10, target=pokemon, apply_modifiers=False)

card = PokemonCardDef(
    guid="a874f692-62c0-55d2-8862-c23d5efa7bba",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningGyarados.Name",
    display_name="Shining Gyarados",
    searchable_by=["Shining Gyarados", "Basic", "ShiningGyarados"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=130,
    abilities=[
        Attack(
            title="Outrage",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 10 more damage for each damage counter on Shining Gyarados. If tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 2},
            damage=30,
            damage_operator="+",
            effect=outrage,
        ),
        Attack(
            title="Devastate",
            game_text="Discard 2 Fire Energy cards attached to Shining Gyarados or this attack does nothing. This attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Then, flip a coin. If heads, choose 1 Energy card attached to each of your opponent's Pok\u00e9mon that has any Energy cards attached to it and discard those Energy cards.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.FIRE: 2},
            damage=50,
            effect=devastate,
        ),
    ],
)