from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities


async def _mistys_wish(ctx):
    prizes = ctx.face_down_prize_cards()
    if not prizes:
        return
    picks = await ctx.choose_cards(
        prizes, 1, minimum=1, prompt="Choose a Prize card to look at")
    if not picks:
        return
    prize = picks[0]
    await ctx.reveal_cards([prize], to_player=ctx.player_id)
    accepts = await ctx.ask_yes_no(
        "May this player switch that Prize card with a card from their hand?",
        player_id=ctx.opponent_id)
    if accepts and ctx.hand():
        hand_picks = await ctx.choose_cards(
            ctx.hand(), 1, minimum=1,
            prompt="Choose a card to put into your Prize cards")
        if hand_picks:
            await ctx.put_in_hand([prize], reveal=True)
            await ctx.put_in_prizes(list(hand_picks))
            return
    await ctx.draw_cards(1)


card = ItemCardDef(
    guid="8a3bf543-6627-5e5f-9529-cf757595acee",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysWish.Name",
    display_name="Misty's Wish",
    searchable_by=["Misty's Wish"],
    subtypes=[],
    collector_number=108,
    set_code="GYM2",
    rarity=Rarities.Rare,
    effect=_mistys_wish
)
