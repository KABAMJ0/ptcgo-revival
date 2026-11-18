from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_pokemon


async def _target_whistle(ctx):
    opponent = ctx.opponent_id
    if len(ctx.opponent_bench()) >= ctx.bench_limit(opponent):
        return
    pool = [card for card in ctx.discard_pile(opponent)
            if is_basic_pokemon(card, ctx.board)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1,
        prompt="Choose a Basic Pok\u00e9mon from your opponent's discard pile")
    if picks:
        await ctx.bench_pokemon(picks[0])


card = ItemCardDef(
    guid="2ba5e8c2-2986-59c8-936b-af875bdf0431",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TargetWhistleTeamFlareGear.Name",
    display_name="Target Whistle Team Flare Gear",
    searchable_by=["Target Whistle Team Flare Gear", "Item"],
    subtypes=["Item"],
    collector_number=106,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    effect=_target_whistle
)
