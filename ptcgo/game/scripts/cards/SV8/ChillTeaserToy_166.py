from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_energy_to_hand


def going_second_first_turn(board, player_id):
    """Play condition: this is the player's first turn and they went second."""
    state = getattr(board, "turn_state", None)
    if state is None:
        return False
    return state.turn_number == 2 and state.active_player_id == player_id

card = ItemCardDef(
    guid="48c8af8d-88a8-5fe6-8301-fa6a17f91474",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChillTeaserToy.Name",
    display_name="Chill Teaser Toy",
    searchable_by=["Chill Teaser Toy", "Item"],
    subtypes=["Item"],
    collector_number=166,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    effect=opponent_energy_to_hand(1),
    condition=going_second_first_turn
)
