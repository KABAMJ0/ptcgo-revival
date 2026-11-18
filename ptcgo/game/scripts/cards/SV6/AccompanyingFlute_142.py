from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_pokemon


async def _accompanying_flute(ctx):
    opponent = ctx.opponent_id
    top = ctx.deck_top(5, opponent)
    if not top:
        return
    await ctx.reveal_cards(top)
    space = ctx.bench_limit(opponent) - len(ctx.opponent_bench())
    candidates = [card for card in top if is_basic_pokemon(card, ctx.board)]
    picks = []
    if candidates and space > 0:
        picks = await ctx.choose_cards(
            candidates, min(len(candidates), space), minimum=0,
            display_cards=top,
            prompt="Choose Basic Pok\u00e9mon to put onto your opponent's Bench")
    for card in picks:
        await ctx.bench_pokemon(card)
    rest = [card for card in top if card not in picks]
    if rest:
        await ctx.shuffle_into_deck(rest, opponent)


card = ItemCardDef(
    guid="6e44b374-a287-579d-b69c-4e98c4658a6b",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AccompanyingFlute.Name",
    display_name="Accompanying Flute",
    searchable_by=["Accompanying Flute", "Item"],
    subtypes=["Item"],
    collector_number=142,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    effect=_accompanying_flute
)
