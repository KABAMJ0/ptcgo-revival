from ptcgo.game.card_effects.support_common import baby_evolution, search_to_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_card

_baby_effect, _baby_in_hand = baby_evolution("Roselia")

card = PokemonCardDef(
    guid="8148d161-27a5-5fad-b5c1-181d59e77a39",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Budew.Name",
    display_name="Budew",
    searchable_by=["Budew", "Basic", "Budew"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=406,
    abilities=[
        Ability(
            title="Poison Enzyme",
            game_text="Prevent all effects of attacks, including damage, done to Budew by your opponent's Poisoned Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Roselia from your hand onto Budew (this counts as evolving Budew) and remove all damage counters from Budew.",
            activation=Activations.ONCE_PER_TURN,
            condition=_baby_in_hand,
            effect=_baby_effect,
        ),
        Attack(
            title="Buddy-buddy",
            game_text="Search your deck for a Pok\u00e9mon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={},
            effect=search_to_hand(is_pokemon_card, count=1, minimum=1, reveal=True),
        ),
    ],
)