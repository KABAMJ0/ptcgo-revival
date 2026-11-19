import inspect

from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_supporter_card
from ptcgo.game.session.effects import TRAINER_EFFECTS_BY_GUID


async def _sabrinas_suggestion(ctx):
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    supporters = [card for card in hand if is_supporter_card(card)]
    if not supporters:
        return
    picks = await ctx.choose_cards(
        supporters, 1, minimum=0,
        prompt="Choose a Supporter card to use the effect of")
    if not picks:
        return
    copied = picks[0]
    effect = TRAINER_EFFECTS_BY_GUID.get((copied.archetype_id or "").lower())
    if not inspect.iscoroutinefunction(effect):
        return
    # Run the copied Supporter's script with the copied card as the effect's
    # source, so a body that refers to "this card" acts on the card taken from
    # the opponent's hand rather than on this card.
    original = ctx.source
    ctx.source = copied
    try:
        await effect(ctx)
    finally:
        ctx.source = original


card = SupporterCardDef(
    guid="ea70ea85-89a6-5b5b-87c8-55c229b32ed7",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinasSuggestion.Name",
    display_name="Sabrina's Suggestion",
    searchable_by=["Sabrina's Suggestion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=154,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=_sabrinas_suggestion
)
