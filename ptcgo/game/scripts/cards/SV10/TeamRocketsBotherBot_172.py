import random

from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities


async def _bother_bot(ctx):
    opponent = ctx.opponent_id
    revealed = await ctx.turn_prize_cards_face_up(count=1, player_id=opponent)
    hand = ctx.hand(opponent)
    if not hand:
        return
    card = random.choice(hand)
    await ctx.reveal_cards([card])
    if not revealed:
        return
    if not await ctx.ask_yes_no(
            "Switch that Prize card with the revealed card?"):
        return
    prize = revealed[0]
    await ctx.put_in_prizes([card], opponent, face_up=True)
    await ctx.put_in_hand([prize], reveal=False)


card = ItemCardDef(
    guid="760e883a-b915-5d40-b6d4-5782fae40b16",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsBotherBot.Name",
    display_name="Team Rocket's Bother-Bot",
    searchable_by=["Team Rocket's Bother-Bot", "Item"],
    subtypes=["Item"],
    collector_number=172,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=_bother_bot
)
