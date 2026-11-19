from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def burning_licks(ctx):
    """70 damage; flip 2 coins, discard an Energy from the opponent's Active per heads."""
    await ctx.deal_damage()
    heads = await ctx.flip_coins(2, "Burning Licks")
    count = sum(heads)
    if count and not ctx.effects_blocked(ctx.defender):
        await ctx.discard_energy_from(ctx.defender, count)


card = PokemonCardDef(
    guid="6dbe83ad-73eb-5a2f-abce-d97a245bd002",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Centiskorch.Name",
    display_name="Centiskorch",
    searchable_by=["Centiskorch", "Stage 1", "Centiskorch"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    family_id=850,
    abilities=[
        Attack(
            title="Coiling Crush",
            game_text="Flip 2 coins. For each heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=burning_licks,
        ),
        Attack(
            title="Heat Crawler",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)