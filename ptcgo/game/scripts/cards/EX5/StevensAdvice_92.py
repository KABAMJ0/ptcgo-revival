from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_at_most

async def _stevens_advice(ctx):
    available = min(len(ctx.opponent_pokemon_in_play()), len(ctx.deck()))
    if available <= 0:
        return
    picks = await ctx.choose_cards(
        ctx.deck_top(available), available, minimum=0,
        prompt="Choose up to %d card(s) to draw" % available)
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = SupporterCardDef(
    guid="25e2b4fb-8b58-5b04-a194-09894b6545c3",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StevensAdvice.Name",
    display_name="Steven's Advice",
    searchable_by=["Steven's Advice", "Supporter"],
    subtypes=["Supporter"],
    collector_number=92,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    effect=_stevens_advice,
    condition=hand_at_most(6),
)
