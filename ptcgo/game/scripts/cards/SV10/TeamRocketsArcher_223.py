from ptcgo.game.card_effects.support_common import shuffle_hand_into_deck_draw
from ptcgo.game.data_utils import SupporterCardDef, def_for
from ptcgo.game.attributes import Rarities


def _team_rocket_koed_last_turn(board, player_id):
    records = getattr(getattr(board, "turn_state", None),
                      "pokemon_left_play_last_turn", None) or []
    for record in records:
        if record.get("owner_id") != player_id or record.get("by_attack") is None:
            continue
        printed = getattr(def_for(record.get("archetype_id")), "display_name", "") or ""
        if printed.lower().startswith("team rocket"):
            return True
    return False


card = SupporterCardDef(
    guid="4598e795-0c7f-5273-99a7-6a8327fd48fd",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsArcher.Name",
    display_name="Team Rocket's Archer",
    searchable_by=["Team Rocket's Archer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=223,
    set_code="SV10",
    rarity=Rarities.Rare,
    effect=shuffle_hand_into_deck_draw(5, opponent_n=3),
    condition=_team_rocket_koed_last_turn
)
