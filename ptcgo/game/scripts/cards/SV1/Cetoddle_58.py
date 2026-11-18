from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0774c54b-708f-5c44-942b-ab5cd0c93365",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name",
    display_name="Cetoddle",
    searchable_by=["Cetoddle", "Basic", "Cetoddle"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=974,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)