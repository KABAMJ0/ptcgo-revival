from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities


async def opal_effect(ctx):
    """Flip 2 coins. Search your deck for a number of cards up to the
    number of heads, put them into your hand, and shuffle your deck."""
    heads = await ctx.flip_coins(2, "Opal")
    count = heads.count(True)
    if count > 0:
        picks = await ctx.search_deck(
            count=count, minimum=0, prompt=f"Choose up to {count} cards",
        )
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="adc7037a-463b-53bc-b0d3-ad11d3d1d067",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Opal.Name",
    display_name="Opal",
    searchable_by=["Opal", "Supporter"],
    subtypes=["Supporter"],
    collector_number=28,
    set_code="SWSH11TG",
    rarity=Rarities.RareUltra,
    effect=opal_effect
)
