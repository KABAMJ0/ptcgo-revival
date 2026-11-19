from ptcgo.game.data_utils import SupporterCardDef, def_for
from ptcgo.game.attributes import Rarities

async def _tate_lizas_training(ctx):
    if not await ctx.draw_cards(2):
        return
    stadium = ctx.stadium_in_play()
    if stadium is None:
        return
    name = (getattr(def_for(stadium.archetype_id), "display_name", "") or "").lower()
    if "legendary" in name:
        await ctx.put_in_hand([ctx.source], reveal=True)


card = SupporterCardDef(
    guid="66d794f6-bc70-51fe-9706-058254112e11",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TateLizasTraining.Name",
    display_name="Tate & Liza's Training",
    searchable_by=["Tate & Liza's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="ME6",
    rarity=Rarities.Rare,
    effect=_tate_lizas_training
)
