from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

async def _lillies_end_of_turn(ctx):
    excess = ctx.hand_size() - 2
    if ctx.hand_size() < 3 or excess <= 0:
        return
    picks = await ctx.choose_cards(
        ctx.hand(), excess, minimum=excess,
        prompt="Choose cards to shuffle into your deck")
    if picks:
        await ctx.shuffle_into_deck(picks)


async def _lillies_full_force(ctx):
    await ctx.draw_cards(4)
    ctx.schedule_turn_effect("end_of_this_turn", _lillies_end_of_turn)


card = SupporterCardDef(
    guid="ffa2f0e4-f690-5351-884d-4eeab6b5e2e2",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LilliesFullForce.Name",
    display_name="Lillie's Full Force",
    searchable_by=["Lillie's Full Force", "Supporter"],
    subtypes=["Supporter"],
    collector_number=230,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=_lillies_full_force
)
