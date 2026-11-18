from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def licking_flames(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(3, "Licking Flames")
    tails = sum(1 for result in results if not result)
    if tails:
        await ctx.discard_energy_from(
            ctx.attacker, tails,
            prompt="Choose Energy to discard from this Pok\u00e9mon")


card = PokemonCardDef(
    guid="7da0946c-64bb-52fc-94ca-bc37cd49139e",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name",
    display_name="Heatmor",
    searchable_by=["Heatmor", "Basic", "Heatmor"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=631,
    abilities=[
        Attack(
            title="Live Coal",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Licking Flames",
            game_text="Flip 3 coins. For each tails, discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=licking_flames,
        ),
    ],
)