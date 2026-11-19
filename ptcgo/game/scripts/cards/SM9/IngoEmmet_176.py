from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

async def _ingo_emmet(ctx):
    """Look at the top card, then discard the hand and draw 5 from the top or
    the bottom of the deck."""
    top = ctx.deck_top(1)
    if top:
        await ctx.reveal_cards(top, ctx.player_id)
    choice = await ctx.choose(
        "Choose 1",
        ["Discard your hand and draw 5 cards",
         "Discard your hand and draw 5 cards from the bottom of your deck"])
    hand = ctx.hand()
    if hand:
        await ctx.discard_cards(list(hand))
    if choice == 1:
        # Deck children are stored bottom-first (put_on_bottom_of_deck uses 0).
        await ctx.put_in_hand(ctx.deck()[:5], reveal=False)
    else:
        await ctx.draw_cards(5)


card = SupporterCardDef(
    guid="a8d45f54-163a-5ded-a20f-a0ab79d1b2f8",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IngoEmmet.Name",
    display_name="Ingo & Emmet",
    searchable_by=["Ingo & Emmet", "Supporter"],
    subtypes=["Supporter"],
    collector_number=176,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=_ingo_emmet,
)
