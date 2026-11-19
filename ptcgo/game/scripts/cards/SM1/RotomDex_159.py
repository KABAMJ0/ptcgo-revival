from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities


async def rotom_dex(ctx):
    """Count your Prize cards, shuffle them into your deck, then put that many
    cards from the top of your deck face down as your Prize cards."""
    prizes = ctx.face_down_prize_cards() + ctx.face_up_prize_cards()
    if not prizes:
        return
    count = len(prizes)
    await ctx.shuffle_into_deck(prizes)
    await ctx.put_in_prizes(ctx.deck_top(count))


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
    effect=rotom_dex
)
