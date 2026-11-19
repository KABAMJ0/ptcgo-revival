from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    is_basic_pokemon, is_tool_card, stadium_ability,
)
from ptcgo.game.session.passives import tool_slots_free


async def _attach_tool(ctx, tool, target):
    """Attach a searched Tool under `target`: attach_energy is the session's
    generic effect-side attachment (move + intro), then the holder's granted
    abilities are re-synced."""
    if tool_slots_free(ctx.board, target) <= 0:
        return
    if await ctx.attach_energy(tool, target):
        await ctx.session.refresh_granted_abilities(target)


async def _contest_hall(ctx):
    """Once during each player's turn, if their Bench isn't full: flip a coin;
    on heads, bench a searched Basic, then optionally a searched Tool onto it."""
    if len(ctx.my_bench()) >= ctx.bench_limit():
        return
    if not await ctx.ask_yes_no("Use Pokémon Contest Hall to flip a coin?"):
        return
    if not (await ctx.flip_coins(1, title="Pokémon Contest Hall"))[0]:
        return
    basics = await ctx.search_deck(
        is_basic_pokemon, count=1, minimum=0,
        prompt="Choose a Basic Pokémon to put onto your Bench")
    benched = basics[0] if basics else None
    if benched is not None and not await ctx.bench_pokemon(benched):
        benched = None
    await ctx.shuffle_deck()
    if benched is None:
        return
    tools = await ctx.search_deck(
        is_tool_card, count=1, minimum=0,
        prompt="Choose a Pokémon Tool card to attach to that Pokémon")
    if tools:
        await _attach_tool(ctx, tools[0], benched)
        await ctx.shuffle_deck()


card = StadiumCardDef(
    guid="51a3be9d-f1de-54f2-a7d4-8134d48f475b",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonContestHall.Name",
    display_name="Pokémon Contest Hall",
    searchable_by=["Pok\u00e9mon Contest Hall", "Stadium"],
    subtypes=["Stadium"],
    collector_number=93,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    ability=stadium_ability("Pokémon Contest Hall", _contest_hall)
)
