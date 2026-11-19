from ptcgo.game.card_effects.support_common import baby_evolution, search_to_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import all_of, is_basic_pokemon, pokemon_of

_baby_effect, _baby_in_hand = baby_evolution("Mantine")

card = PokemonCardDef(
    guid="7f20dfdc-a87e-524c-a9c5-21cc03d3524c",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantyke.Name",
    display_name="Mantyke",
    searchable_by=["Mantyke", "Basic", "Mantyke"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=458,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Mantine from your hand onto Mantyke (this counts as evolving Mantyke) and remove all damage counters from Mantyke.",
            activation=Activations.ONCE_PER_TURN,
            condition=_baby_in_hand,
            effect=_baby_effect,
        ),
        Attack(
            title="Call for Friends",
            game_text="Search your deck for a Water Basic Pok\u00e9mon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={},
            effect=search_to_hand(
                all_of(pokemon_of("water"), is_basic_pokemon),
                count=1,
                minimum=1,
                reveal=True,
            ),
        ),
    ],
)