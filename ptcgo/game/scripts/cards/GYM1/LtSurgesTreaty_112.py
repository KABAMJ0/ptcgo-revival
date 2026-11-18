from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities


async def _surges_treaty(ctx):
    choice = await ctx.choose(
        "Choose one",
        ["Everyone takes 1 of their Prizes into their hand", "They draw a card"],
        player_id=ctx.opponent_id, use_panel=False)
    if choice == 1:
        await ctx.draw_cards(1)
        return
    for player in (ctx.player_id, ctx.opponent_id):
        await ctx.take_prizes(1, player, minimum=1, check_win=False)


card = ItemCardDef(
    guid="66d88f43-01aa-573a-88ae-9b7efbe4af1f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurgesTreaty.Name",
    display_name="Lt. Surge's Treaty",
    searchable_by=["Lt. Surge's Treaty"],
    subtypes=[],
    collector_number=112,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    effect=_surges_treaty
)
