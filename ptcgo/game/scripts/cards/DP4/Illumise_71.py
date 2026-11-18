from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.patterns import is_pokemon_of_type
from ptcgo.game.card_effects.trainers import all_of

card = PokemonCardDef(
    guid="c35b5801-925b-5157-a5dd-6ff1e1894588",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Illumise.Name",
    display_name="Illumise",
    searchable_by=["Illumise", "Basic", "Illumise"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="DP4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=314,
    abilities=[
        Ability(
            title="Scent Conduct",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a Grass Basic Pok\u00e9mon and put it onto your Bench. Shuffle your deck afterward. This power can't be used if Illumise is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            effect=flip_or_nothing(then=search_to_bench(all_of(is_basic_pokemon, lambda card: is_pokemon_of_type(card, "grass")), count=1)),
        ),
        Attack(
            title="Firefly Scent",
            game_text="If the Defending Pok\u00e9mon has any Pok\u00e9-Bodies, that Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)