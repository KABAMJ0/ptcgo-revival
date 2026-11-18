from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities

async def _discard_any_draw_same(ctx):
    await ctx.reveal_hand(ctx.opponent_id)
    hand = ctx.hand()
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, len(hand), minimum=0,
        prompt="Choose any number of cards to discard")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.draw_cards(len(picks))


card = ItemCardDef(
    guid="2052ce18-9aff-51a7-aeb8-a36dd65d6d56",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SecretMission.Name",
    display_name="Secret Mission",
    searchable_by=["Secret Mission"],
    subtypes=[],
    collector_number=118,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    effect=_discard_any_draw_same
)
