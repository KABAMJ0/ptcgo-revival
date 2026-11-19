from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    is_basic_energy_card,
    is_evolution_pokemon,
    stadium_ability,
)


async def _mystery_zone(ctx):
    if not any(is_evolution_pokemon(card) for card in ctx.hand()):
        return
    if not await ctx.ask_yes_no(
            "Search your deck for a basic Energy card?"):
        return
    found = await ctx.search_deck(
        is_basic_energy_card, count=1, minimum=0,
        prompt="Choose a basic Energy card to put into your hand")
    if found:
        await ctx.reveal_cards(found)
        await ctx.put_in_hand(found, reveal=True)
    evolution = [card for card in ctx.hand() if is_evolution_pokemon(card)]
    if evolution:
        picks = await ctx.choose_cards(
            evolution, 1,
            prompt="Choose an Evolution card to put into your deck")
        if picks:
            await ctx.reveal_cards(picks)
            await ctx.shuffle_into_deck(picks, ctx.player_id)
            return
    await ctx.shuffle_deck()


card = StadiumCardDef(
    guid="7547734d-3a2d-5dff-9ca6-be96b8ce13ad",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryZone.Name",
    display_name="Mystery Zone",
    searchable_by=["Mystery Zone", "Stadium"],
    subtypes=["Stadium"],
    collector_number=137,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    ability=stadium_ability("Mystery Zone", _mystery_zone)
)
