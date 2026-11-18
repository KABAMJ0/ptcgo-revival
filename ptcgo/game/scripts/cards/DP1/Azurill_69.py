from ptcgo.game.card_effects.support_common import baby_evolution
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_baby_effect, _baby_in_hand = baby_evolution("Marill")

card = PokemonCardDef(
    guid="c479e7dd-8b80-5e69-ad9b-06bc5a213aef",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azurill.Name",
    display_name="Azurill",
    searchable_by=["Azurill", "Basic", "Azurill"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="DP1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=298,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Marill from your hand onto Azurill (this counts a evolving Azurill) and remove all damage counters from Azurill.",
            activation=Activations.ONCE_PER_TURN,
            condition=_baby_in_hand,
            effect=_baby_effect,
        ),
        Attack(
            title="Delivery",
            game_text="Put any 1 card from your discard pile into your hand.",
            cost={},
            effect=unimplemented,
        ),
    ],
)