from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.effects import is_supporter_card


def call_bell_playable(board, player_id):
    state = getattr(board, "turn_state", None)
    return (state is not None and state.turn_number == 2
            and getattr(state, "active_player_id", None) == player_id)


async def call_bell(ctx):
    picks = await ctx.search_deck(
        is_supporter_card, count=1, minimum=0,
        prompt="Choose a Supporter card")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="8e5ffe8b-aca0-5e3a-948a-46e550b263ae",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CallBell.Name",
    display_name="Call Bell",
    searchable_by=["Call Bell", "Item"],
    subtypes=["Item"],
    collector_number=165,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    effect=call_bell,
    condition=call_bell_playable,
)
