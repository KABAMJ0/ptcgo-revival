from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="58f3b074-bcae-5b89-8971-53b3255842ec",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name",
    display_name="Swinub",
    searchable_by=["Swinub", "Basic", "Swinub"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="HGSS4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=220,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Ice Ball",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)