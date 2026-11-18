from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities


async def _impostors_invention(ctx):
    opponent = ctx.opponent_id
    area = ctx.board.find_player_area(opponent, "prizePile")
    prizes = list(area.children) if area is not None else []
    if not prizes:
        return
    await ctx.session.prompt_view_cards(
        ctx.player_id, ctx.source.entity_id, prizes,
        prompt="Your opponent's Prize cards")
    if not await ctx.ask_yes_no(
            "Have your opponent shuffle their Prize cards into their deck?"):
        return
    await ctx.shuffle_into_deck(prizes, opponent)
    await ctx.put_in_prizes(ctx.deck_top(len(prizes), opponent), opponent)


card = ItemCardDef(
    guid="ebfbca4d-594e-54a6-a20b-6a47a335c9e9",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ImpostorProfessorOaksInvention.Name",
    display_name="Impostor Professor Oak's Invention",
    searchable_by=["Impostor Professor Oak's Invention"],
    subtypes=[],
    collector_number=94,
    set_code="NEO4",
    rarity=Rarities.Rare,
    effect=_impostors_invention
)
