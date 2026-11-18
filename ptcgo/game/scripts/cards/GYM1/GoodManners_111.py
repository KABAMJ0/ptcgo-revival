from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_pokemon


def _no_basic_pokemon_in_hand(board, player_id):
    hand = board.find_player_area(player_id, "hand")
    return not any(is_basic_pokemon(card) for card in (hand.children if hand else []))


async def _good_manners(ctx):
    hand = ctx.hand()
    if hand:
        await ctx.reveal_cards(list(hand))
    picks = await ctx.search_deck(
        is_basic_pokemon, count=1, minimum=0,
        prompt="Choose a Basic Pokémon to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="ebb39525-5bf3-5a07-a618-0b40b165e1ad",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GoodManners.Name",
    display_name="Good Manners",
    searchable_by=["Good Manners"],
    subtypes=[],
    collector_number=111,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    condition=_no_basic_pokemon_in_hand,
    effect=_good_manners
)
