from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="96d0420c-0ce6-5c5b-8766-d0f0c81a1619",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    display_name="Noibat",
    searchable_by=["Noibat", "Basic", "Noibat"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=714,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Destructive Sound",
            game_text="Your opponent reveals their hand. Discard all Item cards you find there.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)