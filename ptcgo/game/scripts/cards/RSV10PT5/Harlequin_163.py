from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities


async def harlequin(ctx):
    """Each player shuffles their hand into their deck, then one coin decides
    who draws 5 and who draws 3."""
    for player_id in (ctx.player_id, ctx.opponent_id):
        await ctx.shuffle_into_deck(ctx.hand(player_id), player_id)
    heads = (await ctx.flip_coins(1, title="Harlequin"))[0]
    await ctx.draw_cards(5 if heads else 3)
    await ctx.draw_cards(3 if heads else 5, ctx.opponent_id)


card = SupporterCardDef(
    guid="66ac9f3f-7428-5c87-a6e8-7ad826faf32a",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Harlequin.Name",
    display_name="Harlequin",
    searchable_by=["Harlequin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=163,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    effect=harlequin
)
