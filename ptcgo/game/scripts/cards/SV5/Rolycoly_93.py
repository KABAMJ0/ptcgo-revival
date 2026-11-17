from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1252da13-08a8-5445-9a9d-93d43641d3d9",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rolycoly.Name",
    display_name="Rolycoly",
    searchable_by=["Rolycoly", "Basic", "Rolycoly"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=837,
    abilities=[
        Attack(
            title="Rolling Tackle",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)