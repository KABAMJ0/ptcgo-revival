from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, pokemon_of_subtype

_IS_FUTURE = pokemon_of_subtype("Future")


async def _reboot_pod(ctx):
    """Attach a basic Energy card from the discard pile to each of your Future
    Pokemon (mandatory, one per Pokemon, as far as the discard pile allows)."""
    for pokemon in [p for p in ctx.my_pokemon_in_play() if _IS_FUTURE(p)]:
        available = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not available:
            return
        picks = await ctx.choose_cards(
            available, 1, minimum=1,
            prompt="Choose a basic Energy card from your discard pile to attach")
        if picks:
            await ctx.attach_energy(picks[0], pokemon)


card = ItemCardDef(
    guid="e74b1a10-66f3-56ec-9833-3992e2bb1c15",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RebootPod.Name",
    display_name="Reboot Pod",
    searchable_by=["Reboot Pod", "Item", "Future", "ACE SPEC"],
    subtypes=["Item", "Future", "ACE SPEC"],
    collector_number=158,
    set_code="SV5",
    rarity=Rarities.Rare,
    effect=_reboot_pod,
)
