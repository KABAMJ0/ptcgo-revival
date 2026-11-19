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
    guid="412f9441-5fff-596e-9c6c-d4b1d8df02a7",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klawf.Name",
    display_name="Klawf",
    searchable_by=["Klawf", "Basic", "Klawf"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=950,
    abilities=[
        Attack(
            title="Snipping Pincers",
            game_text="Flip 2 coins. For each heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=burning_licks,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)