from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    all_of, card_named_contains, is_pokemon_card, with_discard_cost,
)

_HOLON_POKEMON = all_of(is_pokemon_card, card_named_contains("Holon"))

async def _holon_adventurer(ctx, discarded):
    """Draw 3, or 4 when the card spent on the cost was a Pokemon with Holon in
    its name (the discard is the cost, the draw is the payoff)."""
    await ctx.draw_cards(4 if any(_HOLON_POKEMON(c) for c in discarded) else 3)


card = SupporterCardDef(
    guid="8312838c-e731-5380-b37e-b6dbadc725fc",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonAdventurer.Name",
    display_name="Holon Adventurer",
    searchable_by=["Holon Adventurer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=85,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, _holon_adventurer, pass_discarded=True)
)
