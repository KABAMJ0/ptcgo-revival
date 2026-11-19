import random

from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_darkness_pokemon


def _not_first_turn(board, player_id):
    state = getattr(board, "turn_state", None)
    return state is None or state.turn_number > 2


async def _grimsleys_move(ctx):
    top = ctx.deck_top(7)
    if not top:
        return
    benched = []
    candidates = [card for card in top if is_darkness_pokemon(card)]
    if candidates and len(ctx.my_bench()) < ctx.bench_limit():
        picks = await ctx.choose_cards(
            candidates, 1, minimum=0, display_cards=top,
            prompt="Choose a Darkness Pok\u00e9mon to put onto your Bench")
        if picks and await ctx.bench_pokemon(picks[0]):
            benched = picks
    rest = [card for card in top if card not in benched]
    random.shuffle(rest)
    for card in rest:
        await ctx.put_on_bottom_of_deck(card)


card = SupporterCardDef(
    guid="b0d5b3d7-aecd-5795-97e6-c98c1eb54432",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GrimsleysMove.Name",
    display_name="Grimsley's Move",
    searchable_by=["Grimsley's Move", "Supporter"],
    subtypes=["Supporter"],
    collector_number=90,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    condition=_not_first_turn,
    effect=_grimsleys_move
)
