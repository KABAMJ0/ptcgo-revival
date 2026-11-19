from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities

async def _rotate_prizes(ctx):
    area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    prizes = list(area.children) if area is not None else []
    count = len(prizes)
    if not count:
        return
    await ctx.shuffle_into_deck(prizes)
    fresh = ctx.deck_top(count)
    if fresh:
        await ctx.put_in_prizes(list(fresh))


card = ItemCardDef(
    guid="7ef29643-8712-5a65-91da-d74c087985c9",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedeemableTicket.Name",
    display_name="Redeemable Ticket",
    searchable_by=["Redeemable Ticket", "Item"],
    subtypes=["Item"],
    collector_number=156,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    effect=_rotate_prizes
)
