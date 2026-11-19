from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.support_common import remove_self_from_play
from ptcgo.game.data_utils import Activations
from ptcgo.game.attributes import AttrID
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _can_withdraw(board, player_id, pokemon):
    """Not the turn Tentacool came into play, and not while affected."""
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []:
        return False
    turn_state = getattr(board, "turn_state", None)
    if turn_state is None:
        return True
    return turn_state.entered_play_turn.get(pokemon.entity_id, 0) \
        < turn_state.turn_number


card = PokemonCardDef(
    guid="76ac62b3-6b94-5dbf-8bf0-f0083f55eb4a",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    display_name="Tentacool",
    searchable_by=["Tentacool", "Basic", "Tentacool"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="BASE6",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=72,
    abilities=[
        Ability(
            title="Cowardice",
            game_text="At any time during your turn (before your attack), you may return Tentacool to your hand. (Discard all cards attached to Tentacool.) This power can't be used the turn you put Tentacool into play or if Tentacool is affected by a Special Condition.",
            activation=Activations.UNLIMITED,
            condition=_can_withdraw,
            effect=remove_self_from_play(destination="hand", with_attachments="discard"),
        ),
        Attack(
            title="Acid",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)