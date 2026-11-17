from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="78363cec-11a5-5055-8a4b-b8aae6be221b",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name",
    display_name="Flittle",
    searchable_by=["Flittle", "Basic", "Flittle"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=955,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)