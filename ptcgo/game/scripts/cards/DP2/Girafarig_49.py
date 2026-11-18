from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="09be04b2-57a8-53eb-96eb-9ee7334eeecf",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    display_name="Girafarig",
    searchable_by=["Girafarig", "Basic", "Girafarig"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=203,
    abilities=[
        Attack(
            title="Crane Neck",
            game_text="Search your deck for a Trainer card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Psybeam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=unimplemented,
        ),
    ],
)