from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

async def _draw_to_eight(ctx):
    await ctx.draw_until(8)


async def _blues_tactics(ctx):
    ctx.schedule_turn_effect("end_of_this_turn", _draw_to_eight)


card = SupporterCardDef(
    guid="84ae1c5d-7eb9-5642-9099-a96ca3cddb7c",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BluesTactics.Name",
    display_name="Blue's Tactics",
    searchable_by=["Blue's Tactics", "Supporter"],
    subtypes=["Supporter"],
    collector_number=231,
    set_code="SM11",
    rarity=Rarities.RareUltra,
    effect=_blues_tactics
)
