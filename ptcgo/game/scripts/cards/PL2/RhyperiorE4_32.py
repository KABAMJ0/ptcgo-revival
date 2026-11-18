from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aa835b2c-b975-5b3e-b7fc-a8f3df6ddb2b",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RhyperiorE4.Name",
    display_name="Rhyperior E4",
    searchable_by=["Rhyperior E4", "Basic", "SP", "RhyperiorE4"],
    subtypes=["Basic", "SP"],
    collector_number=32,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=464,
    abilities=[
        Attack(
            title="Double Lariat",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)