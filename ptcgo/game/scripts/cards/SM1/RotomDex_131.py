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
    guid="5e94fa4a-54ad-5206-864e-f34de06f53a2",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RotomDex.Name",
    display_name="Rotom Dex",
    searchable_by=["Rotom Dex", "Item"],
    subtypes=["Item"],
    collector_number=131,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=_rotate_prizes
)
