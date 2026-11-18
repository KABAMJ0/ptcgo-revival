from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="deeb803d-b5ae-5123-91af-6822691132dd",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tepig.Name",
    display_name="Tepig",
    searchable_by=["Tepig", "Basic", "Tepig"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=498,
    abilities=[
        Attack(
            title="Steady Firebreathing",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)