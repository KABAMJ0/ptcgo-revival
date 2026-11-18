from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities


async def _lookers_investigation(ctx):
    await ctx.reveal_hand(of_player=ctx.opponent_id)
    side = await ctx.choose("Choose a player", ["You", "Your opponent"])
    player = ctx.player_id if side == 0 else ctx.opponent_id
    hand = ctx.hand(player)
    if hand:
        await ctx.shuffle_into_deck(hand, player)
    options = ["5", "4", "3", "2", "1", "0"]
    draw = int(options[await ctx.choose(
        "Draw up to 5 cards", options, player_id=player, use_panel=False)])
    if draw:
        await ctx.draw_cards(draw, player)


card = SupporterCardDef(
    guid="8e02099c-35e4-547c-9e47-5c79697ff14b",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LookersInvestigation.Name",
    display_name="Looker's Investigation",
    searchable_by=["Looker's Investigation", "Supporter"],
    subtypes=["Supporter"],
    collector_number=109,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    effect=_lookers_investigation
)
