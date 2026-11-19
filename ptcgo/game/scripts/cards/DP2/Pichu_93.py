from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.card_effects.support_common import baby_evolution
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_baby_effect, _baby_in_hand = baby_evolution("Pikachu")

card = PokemonCardDef(
    guid="ba04e3e7-f900-5cf1-ab01-91f78e491c41",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pichu.Name",
    display_name="Pichu",
    searchable_by=["Pichu", "Basic", "Pichu"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="DP2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=172,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Pikachu from your hand onto Pichu (this counts as evolving Pichu) and remove all damage counters from Pichu.",
            activation=Activations.ONCE_PER_TURN,
            condition=_baby_in_hand,
            effect=_baby_effect,
        ),
        Attack(
            title="Chupi",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={},
            damage=20,
            effect=flip_or_nothing(),
        ),
    ],
)