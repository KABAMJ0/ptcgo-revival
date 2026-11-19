from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard


def _partner_on_stack(ctx):
    """The other Puzzle of Time already sitting on the trainer slot.

    The pair is played one card after the other, so the second card's effect
    sees its partner still on `activeTrainer` -- that is how it knows to skip
    the single-card branch.
    """
    area = ctx.board.find_global_area("activeTrainer")
    for card in (area.children if area else []):
        if card is not ctx.source and card.archetype_id == ctx.source.archetype_id:
            return card
    return None


async def _puzzle_of_time(ctx):
    """1 Puzzle of Time: reorder the top 3. 2 played at once: recover 2 cards."""
    if _partner_on_stack(ctx) is not None:
        await recover_from_discard(count=2, minimum=0)(ctx)
        return
    second = next((card for card in ctx.hand()
                   if card.archetype_id == ctx.source.archetype_id), None)
    if second is not None and await ctx.ask_yes_no(
            "Play a second Puzzle of Time at once?"):
        await ctx.session._execute_play_trainer(ctx.player_id, second)
        return
    await ctx.reorder_deck_top(3)


card = ItemCardDef(
    guid="28440831-0696-58c2-acd5-1ba1ea9f1721",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PuzzleofTime.Name",
    display_name="Puzzle of Time",
    searchable_by=["Puzzle of Time", "Item"],
    subtypes=["Item"],
    collector_number=109,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=_puzzle_of_time
)
