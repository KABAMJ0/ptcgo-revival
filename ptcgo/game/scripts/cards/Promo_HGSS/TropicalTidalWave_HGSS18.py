from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities

async def _tidal_wave(ctx):
    coins = await ctx.flip_coins(1, "Tropical Tidal Wave")
    owner = ctx.opponent_id if coins and coins[0] else ctx.player_id
    pool = [card for card, _holder in ctx.tools_in_play()
            if card.owning_player_id == owner]
    stadium = ctx.stadium_in_play()
    if stadium is not None and stadium.owning_player_id == owner:
        pool.append(stadium)
    if pool:
        await ctx.discard_cards(pool)


card = ItemCardDef(
    guid="bea95630-268a-5101-bd9d-32d55a06f5ad",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalTidalWave.Name",
    display_name="Tropical Tidal Wave",
    searchable_by=["Tropical Tidal Wave", "Item"],
    subtypes=["Item"],
    collector_number=18,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    effect=_tidal_wave,
)
