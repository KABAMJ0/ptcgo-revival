from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aaee6235-d372-5ccc-ae0c-d774e7d07b6f",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name",
    display_name="Grotle",
    searchable_by=["Grotle", "Stage 1", "Grotle"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name",
    family_id=387,
    abilities=[
        Attack(
            title="Absorb",
            game_text="Remove 1 damage counter from Grotle.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)