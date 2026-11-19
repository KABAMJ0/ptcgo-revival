from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

async def _amarys_end_of_turn(ctx):
    if ctx.hand_size() >= 5:
        await ctx.discard_cards(ctx.hand())


async def _amarys(ctx):
    await ctx.draw_cards(4)
    ctx.schedule_turn_effect("end_of_this_turn", _amarys_end_of_turn)


card = SupporterCardDef(
    guid="14eb2aaa-274c-5352-8f82-e70bdec9ec28",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Amarys.Name",
    display_name="Amarys",
    searchable_by=["Amarys", "Supporter"],
    subtypes=["Supporter"],
    collector_number=132,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=_amarys
)
