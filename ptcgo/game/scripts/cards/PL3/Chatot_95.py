from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.session.effects import is_basic_pokemon

card = PokemonCardDef(
    guid="2c44d537-951f-52c8-a9da-767bc42631d1",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chatot.Name",
    display_name="Chatot",
    searchable_by=["Chatot", "Basic", "Chatot"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="PL3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=441,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(is_basic_pokemon, count=1),
        ),
        Attack(
            title="Nosedive",
            game_text="Flip a coin. If tails, Chatot does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)