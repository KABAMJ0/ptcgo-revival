from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities


async def _daisys_help(ctx):
    await ctx.draw_cards(2)
    prizes = ctx.face_down_prize_cards()
    if prizes:
        await ctx.reveal_cards(prizes, to_player=ctx.player_id)


card = SupporterCardDef(
    guid="fe4b5be1-21cc-53e9-81e9-23e5dd461c6f",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DaisysHelp.Name",
    display_name="Daisy's Help",
    searchable_by=["Daisy's Help", "Supporter"],
    subtypes=["Supporter"],
    collector_number=195,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    effect=_daisys_help
)
