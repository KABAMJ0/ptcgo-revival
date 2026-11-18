from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c4ebed62-d3bc-5f74-abcc-014fd302d898",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name",
    display_name="Geodude",
    searchable_by=["Geodude", "Basic", "Geodude"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="BASE3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=74,
    abilities=[
        Attack(
            title="Stone Barrage",
            game_text="Flip a coin until you get tails. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)