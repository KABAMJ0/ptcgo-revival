from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

async def _harlequin(ctx):
    if ctx.hand():
        await ctx.shuffle_into_deck(ctx.hand())
    if ctx.hand(ctx.opponent_id):
        await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
    if (await ctx.flip_coins(1, title="Harlequin"))[0]:
        await ctx.draw_cards(5)
        await ctx.draw_cards(3, ctx.opponent_id)
    else:
        await ctx.draw_cards(3)
        await ctx.draw_cards(5, ctx.opponent_id)


card = SupporterCardDef(
    guid="cfd6cc68-b88a-5c53-be51-296535cb92b7",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Harlequin.Name",
    display_name="Harlequin",
    searchable_by=["Harlequin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="RSV10PT5",
    rarity=Rarities.Uncommon,
    effect=_harlequin
)
