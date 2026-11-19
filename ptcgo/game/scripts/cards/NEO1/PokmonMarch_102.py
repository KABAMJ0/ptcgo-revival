from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.effects import is_basic_pokemon


async def _march_search(ctx, player_id, bench):
    if len(bench) >= ctx.bench_limit(player_id):
        return
    if not await ctx.ask_yes_no(
            "Search your deck for a Basic Pok\u00e9mon and put it onto your Bench?",
            player_id=player_id):
        return
    picks = await ctx.search_deck(
        is_basic_pokemon, count=1, minimum=0,
        prompt="Choose a Basic Pok\u00e9mon for your Bench",
        player_id=player_id)
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck(player_id)


async def pokemon_march(ctx):
    await _march_search(ctx, ctx.opponent_id, ctx.opponent_bench())
    await _march_search(ctx, ctx.player_id, ctx.my_bench())


card = ItemCardDef(
    guid="fa51c915-8eac-504b-86a9-c5f695a61cbe",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonMarch.Name",
    display_name="Pok\u00e9mon March",
    searchable_by=["Pok\u00e9mon March"],
    subtypes=[],
    collector_number=102,
    set_code="NEO1",
    rarity=Rarities.Common,
    effect=pokemon_march,
)
