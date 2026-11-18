from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.patterns import is_pokemon_of_type
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.trainers import all_of

card = PokemonCardDef(
    guid="d3e563a1-8499-5618-b91e-fa00ab40c5c7",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic", "Charmander"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="PL4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Call for Friends",
            game_text="Search your deck for a Fire Basic Pok\u00e9mon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(
                all_of(is_basic_pokemon, lambda card: is_pokemon_of_type(card, "fire")),
                count=1,
                reveal=True,
            ),
        ),
        Attack(
            title="Steady Firebreathing",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)