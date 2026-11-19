from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def birthday_surprise(ctx):
    """Printed 30 damage: the engine has no birthday to read, so the printed
    branch is the one that always applies."""
    await ctx.deal_damage()

card = PokemonCardDef(
    guid="6f844409-f4d8-545e-88c2-77085f51b2ff",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.sPikachu.Name",
    display_name="_____'s Pikachu",
    searchable_by=["_____'s Pikachu", "Basic", "sPikachu"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Birthday Surprise",
            game_text="If it's not your birthday, this attack does 30 damage. If it is your birthday, flip a coin. If heads, this attack does 30 damage plus 50 more damage; if tails, this attack does 30 damage.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            damage_operator="+",
            effect=birthday_surprise,
        ),
    ],
)