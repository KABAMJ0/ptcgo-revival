from ptcgo.game.card_effects.trainers import choose_one, discard_hand_draw, discard_hand_then, look_top_peek
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities


async def _draw_bottom(ctx):
    """The five cards at the BOTTOM of the deck (children[-1] is the top)."""
    bottom = ctx.deck()[:5]
    if bottom:
        await ctx.put_in_hand(bottom, reveal=False)


async def _bottom_five(ctx):
    await discard_hand_then(_draw_bottom, ctx)


async def ingo_emmet(ctx):
    """Look at the top card, then discard your hand and draw 5 from the top or
    from the bottom of your deck."""
    await look_top_peek(1)(ctx)
    await choose_one([
        ("Discard your hand and draw 5 cards", discard_hand_draw(5)),
        ("Discard your hand and draw 5 cards from the bottom of your deck",
         _bottom_five),
    ])(ctx)


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
    effect=ingo_emmet
)
