from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5df4e149-7efb-51fc-b638-01ad3f968bce",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    display_name="Litwick",
    searchable_by=["Litwick", "Basic", "Litwick"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=607,
    abilities=[
        Attack(
            title="Will-O-Wisp",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)