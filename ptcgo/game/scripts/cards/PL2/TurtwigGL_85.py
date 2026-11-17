from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="796d9b73-e039-5edc-b44e-b5daaad6f76a",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TurtwigGL.Name",
    display_name="Turtwig GL",
    searchable_by=["Turtwig GL", "Basic", "SP", "TurtwigGL"],
    subtypes=["Basic", "SP"],
    collector_number=85,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=387,
    abilities=[
        Ability(
            title="Overgrow",
            game_text="As long as Turtwig GL's remaining HP is 60 or less, each of Turtwig GL's attacks does 30 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Giga Drain",
            game_text="After your attack, remove from Turtwig GL the number of damage counters equal to the damage you did to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)