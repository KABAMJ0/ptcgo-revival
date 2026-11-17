from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="525c6a15-67ad-57fc-b31b-4fc0c8652da7",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hatenna.Name",
    display_name="Hatenna",
    searchable_by=["Hatenna", "Basic", "Hatenna"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=856,
    abilities=[
        Attack(
            title="Find a Friend",
            game_text="Search your deck for a Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)