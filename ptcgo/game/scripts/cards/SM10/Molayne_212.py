from ptcgo.game.card_effects.trainers import is_metal_energy_card, is_trainer_card
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities


async def molayne(ctx):
    """Discard 2 Metal Energy cards from your hand, then shuffle a Trainer card
    from your discard pile into your deck."""
    metal = [c for c in ctx.hand() if is_metal_energy_card(c)]
    if len(metal) < 2:
        return
    picks = await ctx.choose_cards(
        metal, 2, minimum=2, prompt="Discard 2 Metal Energy cards from your hand")
    if len(picks) < 2:
        return
    await ctx.discard_cards(picks)
    await recover_from_discard(
        is_trainer_card, count=1, minimum=1, reveal=True, to="deck_shuffle")(ctx)


card = SupporterCardDef(
    guid="4db8befe-b191-5726-a9b3-46d9ff359f7a",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Molayne.Name",
    display_name="Molayne",
    searchable_by=["Molayne", "Supporter"],
    subtypes=["Supporter"],
    collector_number=212,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    effect=molayne
)
