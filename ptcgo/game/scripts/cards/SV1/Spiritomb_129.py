from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _timber_cleave(ctx):
    """Flip 2 coins. If both are heads, the opponent's Active is Knocked Out."""
    coins = await ctx.flip_coins(2, "Timber Cleave")
    if all(coins):
        await ctx.knock_out(ctx.defender)


card = PokemonCardDef(
    guid="5f4757da-5434-5647-bed8-8b489219074f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=129,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=442,
    abilities=[
        Attack(
            title="Taunt",
            game_text="Switch in 1 of your opponent's Benched Pok\u00e9mon to the Active Spot.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Doom Decree",
            game_text="Flip 2 coins. If both of them are heads, your opponent's Active Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.DARKNESS: 2},
            effect=_timber_cleave,
        ),
    ],
)