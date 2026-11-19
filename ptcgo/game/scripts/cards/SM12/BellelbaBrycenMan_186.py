from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.models.board import PokemonEntity
from ptcgo.game.session.effects import full_stack


async def _trim_bench(ctx, player_id):
    """`player_id` discards their own Benched Pokemon, with everything attached,
    until they have 3."""
    bench = ctx.board.find_player_area(player_id, "bench")
    while bench is not None:
        pokemon = [c for c in bench.children if isinstance(c, PokemonEntity)]
        if len(pokemon) <= 3:
            return
        picks = await ctx.choose_cards(
            pokemon, 1, minimum=1, player_id=player_id,
            prompt="Choose a Benched Pokémon to discard")
        if not picks:
            return
        await ctx.discard_cards(full_stack(picks[0]))


async def _bellelba_and_brycen_man(ctx):
    """Discard the top 3 cards of each deck; then, optionally, discard 3 other
    cards to make each player bench-trim to 3, the opponent first."""
    for player_id in (ctx.player_id, ctx.opponent_id):
        top = ctx.deck_top(3, player_id)
        if top:
            await ctx.discard_cards(top)
    if ctx.hand_size() < 3:
        return
    if not await ctx.ask_yes_no(
            "Discard 3 cards from your hand to make each player discard "
            "Benched Pokémon until they have 3?"):
        return
    discarded = await ctx.discard_from_hand(
        3, minimum=3, prompt="Discard 3 cards from your hand")
    if len(discarded) < 3:
        return
    await _trim_bench(ctx, ctx.opponent_id)
    await _trim_bench(ctx, ctx.player_id)


card = SupporterCardDef(
    guid="138ffcaa-5146-5450-8849-d9e4afb25a84",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BellelbaBrycenMan.Name",
    display_name="Bellelba & Brycen-Man",
    searchable_by=["Bellelba & Brycen-Man", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=186,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=_bellelba_and_brycen_man
)
