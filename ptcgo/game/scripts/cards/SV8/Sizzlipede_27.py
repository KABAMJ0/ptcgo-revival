from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e3338d22-e91f-5f65-a557-5acc4634c590",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    display_name="Sizzlipede",
    searchable_by=["Sizzlipede", "Basic", "Sizzlipede"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=850,
    abilities=[
        Attack(
            title="Live Coal",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Hook",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)