from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1da827d9-2878-5500-864b-eccb392c3975",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hippowdon.Name",
    display_name="Hippowdon",
    searchable_by=["Hippowdon", "Stage 1", "Hippowdon"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name",
    family_id=449,
    abilities=[
        Attack(
            title="Sand Spray",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
        Attack(
            title="Land Crush",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=140,
        ),
    ],
)