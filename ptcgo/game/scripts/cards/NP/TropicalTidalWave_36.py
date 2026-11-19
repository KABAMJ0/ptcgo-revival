from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities


async def _tropical_tidal_wave(ctx):
    """Heads: every Trainer card the opponent has in play. Tails: yours,
    excluding Supporter cards -- Supporters are never in play, so the attached
    Tools plus the Stadium are the whole set either way."""
    heads = (await ctx.flip_coins(1, title="Tropical Tidal Wave"))[0]
    owner = ctx.opponent_id if heads else ctx.player_id
    tools = [card for card, _holder in ctx.tools_in_play()
             if card.owning_player_id == owner]
    if tools:
        await ctx.discard_cards(tools)
    stadium = ctx.stadium_in_play()
    if stadium is not None and stadium.owning_player_id == owner:
        await ctx.discard_stadium()


card = ItemCardDef(
    guid="9f983769-6f1d-59d6-ac67-646e7b6337db",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalTidalWave.Name",
    display_name="Tropical Tidal Wave",
    searchable_by=["Tropical Tidal Wave", "Item"],
    subtypes=["Item"],
    collector_number=36,
    set_code="NP",
    rarity=Rarities.RarePromo,
    effect=_tropical_tidal_wave
)
