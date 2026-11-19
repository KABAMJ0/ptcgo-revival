from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities


async def _cyruss_initiative(ctx):
    """Flip 2 coins; if either is heads, look at the opponent's hand and put one
    card there per heads on the bottom of their deck. The card's player chooses
    the cards (`player_id` stays this ctx's player), not the opponent."""
    heads = sum(await ctx.flip_coins(2, title="Cyrus's Initiative"))
    if heads == 0:
        return
    await ctx.reveal_hand(of_player=ctx.opponent_id)
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    count = min(heads, len(hand))
    picks = await ctx.choose_cards(
        hand, count, minimum=count,
        prompt="Choose cards to put on the bottom of their deck")
    for card in picks:
        await ctx.put_on_bottom_of_deck(card)


card = SupporterCardDef(
    guid="9a0fa344-2dc9-5429-8518-1bae6d651f94",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CyrussInitiative.Name",
    display_name="Cyrus's Initiative",
    searchable_by=["Cyrus's Initiative", "Supporter"],
    subtypes=["Supporter"],
    collector_number=137,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    effect=_cyruss_initiative
)
