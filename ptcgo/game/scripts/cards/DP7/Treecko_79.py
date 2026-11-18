from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.session.effects import is_basic_pokemon

card = PokemonCardDef(
    guid="805748f7-1aba-5b46-ae93-fe677d5cf00e",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name",
    display_name="Treecko",
    searchable_by=["Treecko", "Basic", "Treecko"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="DP7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=252,
    abilities=[
        Attack(
            title="Call for Friends",
            game_text="Search your deck for a Basic Pok\u00e9mon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_basic_pokemon, count=1, reveal=True),
        ),
        Attack(
            title="Poison Breath",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
    ],
)