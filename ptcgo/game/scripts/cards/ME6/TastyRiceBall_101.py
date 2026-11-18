from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_any


async def _tasty_rice_ball(ctx):
    """30 damage off the Active, plus 30 for each other Rice Ball in the discard."""
    active = ctx.my_active()
    if active is None:
        return
    rice_ball = card_named_any(["Tasty Rice Ball"])
    in_discard = sum(1 for card in ctx.discard_pile() if rice_ball(card))
    await ctx.heal(30 * (in_discard + 1), active)


card = ItemCardDef(
    guid="ae2f9b43-d086-5997-b219-c3a73d037254",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TastyRiceBall.Name",
    display_name="Tasty Rice Ball",
    searchable_by=["Tasty Rice Ball", "Item"],
    subtypes=["Item"],
    collector_number=101,
    set_code="ME6",
    rarity=Rarities.Common,
    effect=_tasty_rice_ball,
)
