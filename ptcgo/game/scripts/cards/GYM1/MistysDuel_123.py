from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities

async def _mistys_duel(ctx):
    winner = ctx.player_id if (await ctx.flip_coins(1, title="Misty's Duel"))[0] \
        else ctx.opponent_id
    if ctx.hand(winner):
        await ctx.shuffle_into_deck(ctx.hand(winner), winner)
    await ctx.draw_cards(5, winner)


card = ItemCardDef(
    guid="f619ee51-f7cb-5140-aadc-aae64672190b",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysDuel.Name",
    display_name="Misty's Duel",
    searchable_by=["Misty's Duel"],
    subtypes=[],
    collector_number=123,
    set_code="GYM1",
    rarity=Rarities.Common,
    effect=_mistys_duel
)
