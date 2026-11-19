from ptcgo.game.card_effects.trainers import gx_unlock_for_name
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities


def _stadium_in_play(board, player_id):
    area = board.find_global_area("activeStadium")
    return bool(area and area.children)


async def bonnie(ctx):
    """Discard the Stadium in play; this turn your Zygarde-GX may use its GX
    attack even if your GX attack is spent."""
    await ctx.discard_stadium()
    await gx_unlock_for_name("Zygarde-GX")(ctx)


card = SupporterCardDef(
    guid="6bdc2fce-76e7-5f93-b359-01371a8198be",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bonnie.Name",
    display_name="Bonnie",
    searchable_by=["Bonnie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=128,
    set_code="SM6",
    rarity=Rarities.RareUltra,
    effect=bonnie,
    condition=_stadium_in_play
)
