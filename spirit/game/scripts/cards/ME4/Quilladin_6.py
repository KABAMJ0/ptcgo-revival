from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a0b96a33-bedb-5114-a384-583a7419f4b4",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quilladin.Name",
    display_name="Quilladin",
    searchable_by=["Quilladin", "Stage 1", "Quilladin"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="ME4",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chespin.Name",
    family_id=650,
    abilities=[
        Attack(
            title="Leafy Charge",
            game_text="Search your deck for a Basic Grass Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)