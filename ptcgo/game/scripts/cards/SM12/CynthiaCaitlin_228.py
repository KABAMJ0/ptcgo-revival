from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import named_exactly
from ptcgo.game.session.effects import is_supporter_card

async def _cynthia_caitlin(ctx):
    """A Supporter from the discard pile (not another copy of this card, not a
    card this effect discarded), then an optional discard for 3 cards."""
    pool = [c for c in ctx.discard_pile()
            if is_supporter_card(c)
            and not named_exactly("Cynthia & Caitlin")(c)]
    if pool:
        picks = await ctx.choose_cards(
            pool, 1, minimum=0,
            prompt="Choose a Supporter card from your discard pile")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    hand = ctx.hand()
    if not hand:
        return
    extra = await ctx.choose_cards(
        hand, 1, minimum=0,
        prompt="Discard another card from your hand to draw 3 cards?")
    if extra:
        await ctx.discard_cards(extra)
        await ctx.draw_cards(3)


card = SupporterCardDef(
    guid="b0972c70-b0bb-5a0f-b202-7c91a8bbdb5e",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CynthiaCaitlin.Name",
    display_name="Cynthia & Caitlin",
    searchable_by=["Cynthia & Caitlin", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=228,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=_cynthia_caitlin,
)
