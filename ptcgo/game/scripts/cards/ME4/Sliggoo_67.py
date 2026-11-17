from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b576e0ac-a831-5dc9-a0b3-78f5f9b71f1c",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name",
    display_name="Sliggoo",
    searchable_by=["Sliggoo", "Stage 1", "Sliggoo"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="ME4",
    rarity=Rarities.Common,
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