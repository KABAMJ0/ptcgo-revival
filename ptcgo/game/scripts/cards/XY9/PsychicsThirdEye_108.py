from ptcgo.game.data_utils import SupporterCardDef
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


card = SupporterCardDef(
    guid="c0c48f4f-0d69-5b91-af3f-1f25caf3e771",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PsychicsThirdEye.Name",
    display_name="Psychic's Third Eye",
    searchable_by=["Psychic's Third Eye", "Supporter"],
    subtypes=["Supporter"],
    collector_number=108,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=_discard_any_draw_same
)
