from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def blustery_wind(ctx):
    """120 damage; you may discard the Stadium in play."""
    await ctx.deal_damage()
    if ctx.stadium_in_play() and await ctx.ask_yes_no("Discard the Stadium in play?"):
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="d7d8d6c2-e266-5a08-a6e0-ab3f7d989dbe",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wooloo.Name",
    display_name="Wooloo",
    searchable_by=["Wooloo", "Basic", "Wooloo"],
    subtypes=["Basic"],
    collector_number=124,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=831,
    abilities=[
        Attack(
            title="Knock Over",
            game_text="You may discard a Stadium in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=blustery_wind,
        ),
    ],
)