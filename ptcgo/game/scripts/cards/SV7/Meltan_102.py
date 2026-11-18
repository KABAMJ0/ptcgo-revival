from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0c17152c-532f-5b3b-954a-e333c421c453",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    display_name="Meltan",
    searchable_by=["Meltan", "Basic", "Meltan"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=808,
    abilities=[
        Attack(
            title="Stampede",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
        Attack(
            title="Beam",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)