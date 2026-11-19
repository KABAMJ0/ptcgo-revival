from ptcgo.game.card_effects.support_common import baby_evolution
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_baby_effect, _baby_in_hand = baby_evolution("Mr. Mime")

card = PokemonCardDef(
    guid="93adbcfc-a344-5195-a247-6695a7c3a815",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MimeJr.Name",
    display_name="Mime Jr.",
    searchable_by=["Mime Jr.", "Basic", "MimeJr"],
    subtypes=["Basic"],
    collector_number=115,
    set_code="PL3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=439,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Mr. Mime from your hand onto Mime Jr. (this counts as evolving Mime Jr.) and remove all damage counters from Mime Jr.",
            activation=Activations.ONCE_PER_TURN,
            condition=_baby_in_hand,
            effect=_baby_effect,
        ),
        Attack(
            title="Encore",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. That Pok\u00e9mon can use only that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)