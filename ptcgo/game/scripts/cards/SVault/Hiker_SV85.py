from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities


async def _hiker(ctx):
    which = await ctx.choose(
        "Look at the top 5 cards of which deck?",
        ["Your deck", "Your opponent's deck"])
    if which not in (0, 1):
        return
    pid = ctx.player_id if which == 0 else ctx.opponent_id
    top = ctx.deck_top(5, pid)
    if not top:
        return
    picks = await ctx.choose_cards(
        top, 1, minimum=1,
        prompt="Choose the card to put on top of that deck")
    if not picks:
        return
    others = [card for card in top if card is not picks[0]]
    if others:
        await ctx.shuffle_into_deck(others, pid)
    await ctx.put_on_top_of_deck(picks[0])


card = SupporterCardDef(
    guid="6ec9927a-a69f-59e2-871a-6e7277eeb200",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hiker.Name",
    display_name="Hiker",
    searchable_by=["Hiker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=85,
    set_code="SVault",
    rarity=Rarities.RareUltra,
    effect=_hiker
)
