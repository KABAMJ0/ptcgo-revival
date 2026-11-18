from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9f1f824d-2088-5788-9452-1b98b2620a31",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic", "Jynx"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=124,
    abilities=[
        Attack(
            title="Intense Kiss",
            game_text="At the end of your opponent's next turn, discard the Defending Pok\u00e9mon and all attached cards.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Psy Bolt",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)