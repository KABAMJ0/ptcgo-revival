from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a2351ba7-9b81-5df8-b914-1cf13ca894a2",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistea.Name",
    display_name="Sinistea",
    searchable_by=["Sinistea", "Basic", "Sinistea"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=854,
    abilities=[
        Attack(
            title="Furtive Drop",
            game_text="Put 2 damage counters on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)