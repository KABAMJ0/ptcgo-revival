from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _twister(ctx):
    """Twister: a coin per heads-off-Effect; both tails does nothing."""
    results = await ctx.flip_coins(2, "Twister")
    heads = sum(1 for r in results if r)
    if not heads:
        return
    await ctx.deal_damage()
    for _ in range(heads):
        defender = ctx.defender
        if defender is None:
            break
        await ctx.discard_energy_from(defender, 1)

card = PokemonCardDef(
    guid="8f34e21d-6ac2-5eb0-9dee-b81eeb53968b",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    display_name="Dragonair",
    searchable_by=["Dragonair", "Stage 1", "Dragonair"],
    subtypes=["Stage 1"],
    collector_number=149,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Twister",
            game_text="Flip 2 coins. For each heads, discard an Energy from your opponent's Active Pok\u00e9mon. If both of them are tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=_twister,
        ),
    ],
)