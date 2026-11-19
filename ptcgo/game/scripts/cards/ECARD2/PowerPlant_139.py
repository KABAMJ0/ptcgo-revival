from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, stadium_ability
from ptcgo.game.card_effects.support_common import recover_from_discard


async def _power_plant(ctx):
    """Once during each player's turn, that player may discard a basic Energy
    card from their hand to put a basic Energy card from their discard pile
    into their hand (shown to the opponent)."""
    if not any(is_basic_energy_card(card) for card in ctx.hand()):
        return
    if not any(is_basic_energy_card(card) for card in ctx.discard_pile()):
        return
    discarded = await ctx.discard_from_hand(
        1, minimum=1, predicate=is_basic_energy_card,
        prompt="Discard a basic Energy card from your hand",
    )
    if not discarded:
        return
    await recover_from_discard(
        is_basic_energy_card, 1, reveal=True,
        prompt="Choose a basic Energy card from your discard pile",
    )(ctx)


card = StadiumCardDef(
    guid="049dc55e-b4e4-58b7-a637-15f0c051114a",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerPlant.Name",
    display_name="Power Plant",
    searchable_by=["Power Plant", "Stadium"],
    subtypes=["Stadium"],
    collector_number=139,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    ability=stadium_ability("Power Plant", _power_plant),
)
