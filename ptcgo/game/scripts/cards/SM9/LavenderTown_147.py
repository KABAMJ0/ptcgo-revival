from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_ability


async def reveal_opponent_hand(ctx):
    """That player may have their opponent reveal their hand."""
    await ctx.reveal_hand(ctx.opponent_id)


card = StadiumCardDef(
    guid="6a6dbfa1-4f6d-5511-82d2-6a709d43bb5d",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LavenderTown.Name",
    display_name="Lavender Town",
    searchable_by=["Lavender Town", "Stadium"],
    subtypes=["Stadium"],
    collector_number=147,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    ability=stadium_ability("Lavender Town", reveal_opponent_hand)
)
