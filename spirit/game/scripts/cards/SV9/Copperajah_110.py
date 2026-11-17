from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cb675654-949c-54f1-8f4b-8404295dbbdc",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Copperajah.Name",
    display_name="Copperajah",
    searchable_by=["Copperajah", "Stage 1", "Copperajah"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    hp=190,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name",
    family_id=878,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
        Attack(
            title="Mega Impact",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)