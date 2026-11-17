from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8c8089f0-336a-5d58-a198-d48285f41a9c",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name",
    display_name="Turtwig",
    searchable_by=["Turtwig", "Basic", "Turtwig"],
    subtypes=["Basic"],
    collector_number=131,
    set_code="PL3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=387,
    abilities=[
        Attack(
            title="Shell Attack",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Stomp",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)