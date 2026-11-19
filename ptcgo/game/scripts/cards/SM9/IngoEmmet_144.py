from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import choose_one, discard_hand_draw


async def _discard_hand_draw_bottom(ctx, draw=5):
    hand = ctx.hand()
    if hand:
        await ctx.discard_cards(list(hand))
    deck = ctx.deck()
    for card in deck[-draw:]:
        await ctx.put_in_hand([card], reveal=False)


_DRAW_OPTIONS = choose_one([
    ("Discard your hand and draw 5 cards", discard_hand_draw(5)),
    ("Discard your hand and draw 5 cards from the bottom of your deck",
     _discard_hand_draw_bottom),
])


async def _ingo_and_emmet(ctx):
    top = ctx.deck_top(1)
    if top:
        await ctx.reveal_cards(top, to_player=ctx.player_id)
    await _DRAW_OPTIONS(ctx)


card = SupporterCardDef(
    guid="0f5a1f20-cd44-578b-9b9d-a1c8481903b5",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IngoEmmet.Name",
    display_name="Ingo & Emmet",
    searchable_by=["Ingo & Emmet", "Supporter"],
    subtypes=["Supporter"],
    collector_number=144,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=_ingo_and_emmet
)
