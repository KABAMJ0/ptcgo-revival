from ptcgo.game.card_effects.support_common import baby_evolution
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_baby_effect, _baby_in_hand = baby_evolution("Jynx")

card = PokemonCardDef(
    guid="ff106a12-09ea-5b3d-8706-ccf36c1c8056",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoochum.Name",
    display_name="Smoochum",
    searchable_by=["Smoochum", "Basic", "Smoochum"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=238,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Jynx from your hand onto Smoochum (this counts as evolving Smoochum) and remove all damage counters from Smoochum.",
            activation=Activations.ONCE_PER_TURN,
            condition=_baby_in_hand,
            effect=_baby_effect,
        ),
        Attack(
            title="Psykiss",
            game_text="Flip a coin. If heads, choose a Special Energy card attached to 1 of your opponent's Pok\u00e9mon and have your opponent shuffle that card into his or her deck.",
            cost={},
            effect=unimplemented,
        ),
    ],
)