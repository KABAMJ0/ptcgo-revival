from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="64e2636a-69db-5bc8-986c-81503ee88e7c",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stunfiskex.Name",
    display_name="Stunfisk ex",
    searchable_by=["Stunfisk ex", "Basic", "ex", "Stunfiskex"],
    subtypes=["Basic", "ex"],
    collector_number=114,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=618,
    abilities=[
        Attack(
            title="Big Bite",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Flopping Trap",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)