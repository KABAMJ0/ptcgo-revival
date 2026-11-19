from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.effects import is_trainer_card


async def acerolas_premonition(ctx):
    """Opponent reveals their hand; draw a card for each Trainer card found there."""
    cards = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    count = sum(1 for c in cards if is_trainer_card(c))
    if count:
        await ctx.draw_cards(count)


card = SupporterCardDef(
    guid="cf3faa0a-b061-5306-b231-e29e6acc3326",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcerolasPremonition.Name",
    display_name="Acerola's Premonition",
    searchable_by=["Acerola's Premonition", "Supporter"],
    subtypes=["Supporter"],
    collector_number=24,
    set_code="SWSH9TG",
    rarity=Rarities.RareUltra,
    effect=acerolas_premonition
)
