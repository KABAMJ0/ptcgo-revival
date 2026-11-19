from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def twister(ctx):
    """Printed 50; one Energy off the Defending Pokemon per heads, and two tails
    does nothing at all."""
    flips = await ctx.flip_coins(2, "Twister")
    heads = sum(1 for flip in flips if flip)
    if heads == 0:
        return
    await ctx.deal_damage()
    for _ in range(heads):
        if ctx.defender is None:
            break
        gone = await ctx.discard_energy_from(
            ctx.defender, 1, prompt="Discard an Energy from the Defending Pokemon")
        if not gone:
            break

card = PokemonCardDef(
    guid="7d4c02d0-6178-5a9e-a7cd-5f0ab4844ac3",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=19,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=230,
    abilities=[
        Attack(
            title="Genetic Memory",
            game_text="Use any attack from Kingdra's Basic Pok\u00e9mon card or Evolution card. (Kingdra doesn't have to pay for that attack's Energy cost.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Twister",
            game_text="Flip 2 coins. For each heads, choose 1 Energy card attached to the Defending Pok\u00e9mon, if any, and discard it. If both are tails, this attack does nothing (not even damage).",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=twister,
        ),
    ],
)