from ptcgo.game.card_effects.trainers import is_special_energy, is_stadium_card, is_tool_card, search_one_of_each
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities


async def guzma_hala(ctx):
    """Search the deck for a Stadium card; you may discard 2 other cards to
    also search for a Pokemon Tool card and a Special Energy card."""
    kinds = [is_stadium_card]
    others = [c for c in ctx.hand() if c is not ctx.source]
    if len(others) >= 2 and await ctx.ask_yes_no(
        "Discard 2 other cards from your hand to also search for a "
        "Pokémon Tool card and a Special Energy card?"
    ):
        discarded = await ctx.discard_from_hand(
            2, minimum=2, prompt="Discard 2 other cards from your hand")
        if len(discarded) >= 2:
            kinds += [is_tool_card, is_special_energy]
    await search_one_of_each(kinds)(ctx)


card = SupporterCardDef(
    guid="fdd971e0-c437-596c-a49a-0a92d7b95d86",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GuzmaHala.Name",
    display_name="Guzma & Hala",
    searchable_by=["Guzma & Hala", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=193,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=guzma_hala
)
