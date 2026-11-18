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
    guid="7d9ddd5d-b625-5f1f-9442-92b0d67da15e",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Naveen.Name",
    display_name="Naveen",
    searchable_by=["Naveen", "Supporter"],
    subtypes=["Supporter"],
    collector_number=79,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    effect=_naveen
)
