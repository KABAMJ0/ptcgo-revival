from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="52460ca2-75b2-5e70-9187-80175b21e4cc",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    display_name="Varoom",
    searchable_by=["Varoom", "Basic", "Varoom"],
    subtypes=["Basic"],
    collector_number=155,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=965,
    abilities=[
        Attack(
            title="Suffocating Gas",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)