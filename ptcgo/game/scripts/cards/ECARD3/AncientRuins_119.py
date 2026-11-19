from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_supporter_card, stadium_ability


async def _ancient_ruins(ctx):
    if ctx.supporters_played_this_turn():
        return
    if not await ctx.ask_yes_no("Reveal your hand to your opponent?"):
        return
    revealed = await ctx.reveal_hand()
    if any(is_supporter_card(card) for card in revealed):
        return
    await ctx.draw_cards(1)


card = StadiumCardDef(
    guid="ab4d0d31-b831-544a-a999-cc68262693ca",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientRuins.Name",
    display_name="Ancient Ruins",
    searchable_by=["Ancient Ruins", "Stadium"],
    subtypes=["Stadium"],
    collector_number=119,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    ability=stadium_ability("Ancient Ruins", _ancient_ruins)
)
