from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities


async def _daisys_help(ctx):
    await ctx.draw_cards(2)
    prizes = ctx.face_down_prize_cards()
    if prizes:
        await ctx.reveal_cards(prizes, to_player=ctx.player_id)


card = SupporterCardDef(
    guid="886ab84e-6600-575e-bf9e-5cd670cba2c4",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DaisysHelp.Name",
    display_name="Daisy's Help",
    searchable_by=["Daisy's Help", "Supporter"],
    subtypes=["Supporter"],
    collector_number=158,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    effect=_daisys_help
)
