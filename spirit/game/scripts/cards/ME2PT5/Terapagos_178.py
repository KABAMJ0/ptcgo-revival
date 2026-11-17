from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="efd3c5fe-8157-5ca9-a18e-ff53592d7004",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Terapagos.Name",
    display_name="Terapagos",
    searchable_by=["Terapagos", "Basic", "Terapagos"],
    subtypes=["Basic"],
    collector_number=178,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1024,
    abilities=[
        Attack(
            title="Prism Charge",
            game_text="Search your deck for up to 3 Basic Energy cards of different types and attach them to your Tera Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Hard Tackle",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)