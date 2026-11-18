from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d51baa49-0514-5459-b578-8920d259a6dc",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    display_name="Graveler",
    searchable_by=["Graveler", "Stage 1", "Graveler"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Double-edge",
            game_text="Graveler does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)