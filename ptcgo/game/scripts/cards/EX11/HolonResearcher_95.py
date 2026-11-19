from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import requires_hand, search_to_hand
from ptcgo.game.card_effects.trainers import (
    card_named_contains, is_metal_energy_card, is_pokemon_card,
    with_discard_cost,
)

_DELTA_MARKER = card_named_contains("\u03b4")


def _metal_or_delta(card):
    """A Metal Energy card, or a Pokemon whose printed name carries \u03b4."""
    return is_metal_energy_card(card) or (
        is_pokemon_card(card) and _DELTA_MARKER(card))


async def _holon_search(ctx):
    await search_to_hand(
        _metal_or_delta, 1, reveal=True,
        prompt="Choose a Metal Energy or a \u03b4 Pokemon card")(ctx)


card = SupporterCardDef(
    guid="735f78ef-f7c2-523e-a612-92b4ffe40595",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonResearcher.Name",
    display_name="Holon Researcher",
    searchable_by=["Holon Researcher", "Supporter"],
    subtypes=["Supporter"],
    collector_number=95,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    condition=requires_hand(n=1),
    effect=with_discard_cost(1, _holon_search),
)
