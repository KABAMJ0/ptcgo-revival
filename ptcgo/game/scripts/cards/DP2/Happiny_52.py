from ptcgo.game.card_effects.support_common import baby_evolution
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_baby_effect, _baby_in_hand = baby_evolution("Chansey")

card = PokemonCardDef(
    guid="f94c9882-8123-5796-b350-5ce5f432c969",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Happiny.Name",
    display_name="Happiny",
    searchable_by=["Happiny", "Basic", "Happiny"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=440,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Chansey from your hand onto Happiny (this counts as evolving Happiny) and remove all damage counters from Happiny.",
            activation=Activations.ONCE_PER_TURN,
            condition=_baby_in_hand,
            effect=_baby_effect,
        ),
        Attack(
            title="Lively",
            game_text="Remove 2 damage counters from 1 of your Pok\u00e9mon.",
            cost={},
            effect=unimplemented,
        ),
    ],
)