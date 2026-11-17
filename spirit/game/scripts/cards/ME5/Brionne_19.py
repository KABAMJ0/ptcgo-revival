from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fa895c57-e1b1-580b-b5ce-ae920fd18829",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Brionne.Name",
    display_name="Brionne",
    searchable_by=["Brionne", "Stage 1", "Brionne"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Popplio.Name",
    family_id=728,
    abilities=[
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.WATER: 1},
            damage=40,
        ),
    ],
)