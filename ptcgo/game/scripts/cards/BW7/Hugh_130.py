from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

async def _hugh(ctx):
    for player_id in (ctx.opponent_id, ctx.player_id):
        size = ctx.hand_size(player_id)
        if size > 5:
            await ctx.discard_from_hand(
                size - 5, minimum=size - 5, player_id=player_id,
                prompt="Discard cards until you have 5 in your hand")
        elif size < 5:
            await ctx.draw_until(5, player_id)


card = SupporterCardDef(
    guid="e65008f5-1b43-5b61-b244-d159baf7db68",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hugh.Name",
    display_name="Hugh",
    searchable_by=["Hugh", "Supporter"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    effect=_hugh
)
