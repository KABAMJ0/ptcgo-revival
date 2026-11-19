from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_item_card

async def _ghetsis(ctx):
    hand = ctx.hand(ctx.opponent_id)
    await ctx.reveal_hand(ctx.opponent_id)
    items = [card for card in hand if is_item_card(card)]
    if not items:
        return
    await ctx.shuffle_into_deck(items, ctx.opponent_id)
    await ctx.draw_cards(len(items))


card = SupporterCardDef(
    guid="e6192c06-9992-544d-b2a1-de32994d1037",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ghetsis.Name",
    display_name="Ghetsis",
    searchable_by=["Ghetsis", "Supporter", "Team Plasma"],
    subtypes=["Supporter", "Team Plasma"],
    collector_number=115,
    set_code="BW9",
    rarity=Rarities.RareUltra,
    effect=_ghetsis
)
