from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="722be1d1-9e9c-5eea-b617-91a0c8f48dc0",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Impidimp.Name",
    display_name="Impidimp",
    searchable_by=["Impidimp", "Basic", "Impidimp"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=859,
    abilities=[
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)