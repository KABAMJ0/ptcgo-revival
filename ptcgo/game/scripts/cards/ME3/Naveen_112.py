from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

async def _naveen(ctx):
    hand = ctx.hand()
    if hand:
        picks = await ctx.choose_cards(
            hand, len(hand), minimum=0,
            prompt="Choose any number of cards to discard")
        if picks:
            await ctx.discard_cards(picks)
    await ctx.draw_until(5)


card = SupporterCardDef(
    guid="e35be0f5-68b6-5514-a4a3-b07de2cd0c06",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Naveen.Name",
    display_name="Naveen",
    searchable_by=["Naveen", "Supporter"],
    subtypes=["Supporter"],
    collector_number=112,
    set_code="ME3",
    rarity=Rarities.Rare,
    effect=_naveen
)
