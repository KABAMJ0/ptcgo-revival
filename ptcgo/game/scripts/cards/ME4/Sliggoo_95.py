from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c89b6099-1e41-5cce-9a7e-b9df5df66021",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name",
    display_name="Sliggoo",
    searchable_by=["Sliggoo", "Stage 1", "Sliggoo"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name",
    family_id=704,
    abilities=[
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            damage=70,
        ),
    ],
)