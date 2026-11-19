from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def blazing_destruction(ctx):
    """Discard a Stadium in play."""
    if ctx.stadium_in_play():
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="8a9e0f41-57ac-5418-a7d8-088293a77e56",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic", "Charmander"],
    subtypes=["Basic"],
    collector_number=168,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Blazing Destruction",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.FIRE: 1},
            effect=blazing_destruction,
        ),
        Attack(
            title="Steady Firebreathing",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
        ),
    ],
)