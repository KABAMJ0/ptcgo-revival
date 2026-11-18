from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.patterns import is_pokemon_of_type
from ptcgo.game.card_effects.trainers import all_of, any_of, named

card = PokemonCardDef(
    guid="feb32897-07ab-56ed-bc77-ccd747680635",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSeviper.Name",
    display_name="Team Aqua's Seviper",
    searchable_by=["Team Aqua's Seviper", "Basic", "TeamAquasSeviper"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="EX4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=336,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Grass Basic Pok\u00e9mon or Basic Pok\u00e9mon with Team Aqua in its name and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(any_of(all_of(is_basic_pokemon, lambda card: is_pokemon_of_type(card, "grass")), all_of(is_basic_pokemon, named("team aqua"))), count=1),
        ),
        Attack(
            title="Thick Poison",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused and Poisoned. If tails, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=unimplemented,
        ),
    ],
)