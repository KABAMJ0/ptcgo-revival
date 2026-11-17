from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d4372f8f-c9a9-57d2-9627-098781d65165",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    display_name="Minccino",
    searchable_by=["Minccino", "Basic", "Minccino"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="ME4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=572,
    abilities=[
        Attack(
            title="Take Down",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)