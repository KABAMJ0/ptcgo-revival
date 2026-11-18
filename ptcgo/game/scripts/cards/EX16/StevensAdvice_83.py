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
    guid="74016157-7106-526d-aaef-a70b0f76b93d",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StevensAdvice.Name",
    display_name="Steven's Advice",
    searchable_by=["Steven's Advice", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    effect=_stevens_advice,
    condition=hand_at_most(5),
)
