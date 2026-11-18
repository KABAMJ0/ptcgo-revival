from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities


async def _evil_deeds(ctx):
    opponent = ctx.opponent_id
    hand = ctx.hand(opponent)
    if hand:
        await ctx.reveal_hand(of_player=opponent)
        picks = await ctx.choose_cards(
            hand, 1, prompt="Choose a card in your opponent's hand")
        if picks:
            await ctx.shuffle_into_deck(picks, opponent)
    options = ["2", "1", "0"]
    draw = int(options[await ctx.choose(
        "Draw up to 2 cards?", options, player_id=opponent, use_panel=False)])
    if draw:
        await ctx.draw_cards(draw, opponent)


card = ItemCardDef(
    guid="ff17bf31-7963-5204-9aeb-caae73a94664",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsEvilDeeds.Name",
    display_name="Team Rocket's Evil Deeds",
    searchable_by=["Team Rocket's Evil Deeds"],
    subtypes=[],
    collector_number=103,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    effect=_evil_deeds
)
