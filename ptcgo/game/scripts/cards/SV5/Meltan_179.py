from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="459cd83d-abea-5359-a79c-cfb91c68371a",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    display_name="Meltan",
    searchable_by=["Meltan", "Basic", "Meltan"],
    subtypes=["Basic"],
    collector_number=179,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=808,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.METAL: 2},
            damage=50,
        ),
    ],
)