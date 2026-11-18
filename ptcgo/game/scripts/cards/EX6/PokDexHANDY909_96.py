from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities

async def _handy909(ctx):
    await ctx.shuffle_deck()
    await ctx.reorder_deck_top(6)


card = ItemCardDef(
    guid="f7a7239d-41b0-513e-9374-b71d9d71612e",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokDexHANDY909.Name",
    display_name="PokéDex HANDY909",
    searchable_by=["Pok\u00e9Dex HANDY909", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    effect=_handy909
)
