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
    guid="a8dd560b-233c-5e23-84af-52f218ed0804",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RotomDex.Name",
    display_name="Rotom Dex",
    searchable_by=["Rotom Dex", "Item"],
    subtypes=["Item"],
    collector_number=159,
    set_code="SM1",
    rarity=Rarities.RareSecret,
    effect=_rotate_prizes
)
