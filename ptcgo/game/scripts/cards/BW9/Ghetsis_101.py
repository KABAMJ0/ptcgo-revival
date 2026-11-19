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
    guid="ba47b87e-6a16-59ac-8381-7dcd97bf7c94",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ghetsis.Name",
    display_name="Ghetsis",
    searchable_by=["Ghetsis", "Supporter", "Team Plasma"],
    subtypes=["Supporter", "Team Plasma"],
    collector_number=101,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    effect=_ghetsis
)
