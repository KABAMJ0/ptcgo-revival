from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_special_energy, is_stadium_card, is_tool_card


async def _search_into_hand(ctx, predicate):
    picks = await ctx.search_deck(
        predicate, count=1, minimum=0,
        prompt="Choose a card to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


async def _guzma_and_hala(ctx):
    """Search a Stadium into hand, shuffle, then optionally discard 2 other
    cards to also search a Pokemon Tool and a Special Energy."""
    await _search_into_hand(ctx, is_stadium_card)
    await ctx.shuffle_deck()
    if ctx.hand_size() < 2:
        return
    if not await ctx.ask_yes_no(
            "Discard 2 cards from your hand to also search for a Pokémon Tool "
            "card and a Special Energy card?"):
        return
    discarded = await ctx.discard_from_hand(
        2, minimum=2, prompt="Discard 2 cards from your hand")
    if len(discarded) < 2:
        return
    for predicate in (is_tool_card, is_special_energy):
        await _search_into_hand(ctx, predicate)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="0cc365dd-1358-59a7-9898-886d34efdcd8",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GuzmaHala.Name",
    display_name="Guzma & Hala",
    searchable_by=["Guzma & Hala", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=229,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=_guzma_and_hala
)
