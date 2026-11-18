from ptcgo.game.data_utils import SupporterCardDef, def_for
from ptcgo.game.attributes import Rarities

async def _caretaker(ctx):
    if not await ctx.draw_cards(2):
        return
    stadium = ctx.stadium_in_play()
    if stadium is None:
        return
    name = (getattr(def_for(stadium.archetype_id), "display_name", "") or "").lower()
    if name == "community center":
        await ctx.shuffle_into_deck([ctx.source])


card = SupporterCardDef(
    guid="59e54be4-d150-5fcb-bfbd-5858379367f1",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Caretaker.Name",
    display_name="Caretaker",
    searchable_by=["Caretaker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=203,
    set_code="SV6",
    rarity=Rarities.Rare,
    effect=_caretaker
)
