from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.effects import is_basic_pokemon


async def erikas_perfume(ctx):
    """Look at your opponent's hand, then put any number of Basic Pokemon from
    it onto their Bench as long as there is room."""
    await ctx.reveal_hand(ctx.opponent_id)
    basics = [c for c in ctx.hand(ctx.opponent_id) if is_basic_pokemon(c)]
    if not basics:
        return
    picks = await ctx.choose_cards(
        basics, len(basics), minimum=0,
        prompt="Choose any number of Basic Pokemon to put onto their Bench")
    for card in picks:
        if not await ctx.bench_pokemon(card):
            break


card = ItemCardDef(
    guid="c4c84d52-9fdd-59ae-bfc5-f6d4dce6972e",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasPerfume.Name",
    display_name="Erika's Perfume",
    searchable_by=["Erika's Perfume"],
    subtypes=[],
    collector_number=110,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    effect=erikas_perfume
)
