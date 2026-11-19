from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    any_of, named_exactly, stadium_ability,
)

_OMANYTE_OR_KABUTO = any_of(named_exactly("Omanyte"), named_exactly("Kabuto"))


async def _lake_bench(ctx):
    """Put an Omanyte or Kabuto from the discard pile onto the Bench."""
    if len(ctx.my_bench()) >= ctx.bench_limit(ctx.player_id):
        return
    pool = [c for c in ctx.discard_pile() if _OMANYTE_OR_KABUTO(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1, minimum=0,
        prompt="Choose an Omanyte or Kabuto to put onto your Bench")
    if picks:
        await ctx.bench_pokemon(picks[0])


card = StadiumCardDef(
    guid="cef622e7-dd42-5c7c-9221-1a22335e1ec0",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UndergroundLake.Name",
    display_name="Underground Lake",
    searchable_by=["Underground Lake", "Stadium"],
    subtypes=["Stadium"],
    collector_number=141,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    ability=stadium_ability("Underground Lake", _lake_bench),
)
