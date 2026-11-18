from ptcgo.game.data_utils import SupporterCardDef, subtypes_for
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card


async def flints_willpower(ctx):
    """Attach 1 basic Energy card from your hand to 1 of your Pokemon SP."""
    energies = [c for c in ctx.hand() if is_basic_energy_card(c)]
    targets = [p for p in ctx.my_pokemon_in_play() if "SP" in subtypes_for(p.archetype_id)]
    if not energies or not targets:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a basic Energy card to attach")
    if not picks:
        return
    target = (await ctx.choose_pokemon(targets, "Choose a Pokemon SP to attach it to")
              if len(targets) > 1 else targets[0])
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)


card = SupporterCardDef(
    guid="421f8f5c-33d0-54a9-8a4e-066234cb82c1",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FlintsWillpower.Name",
    display_name="Flint's Willpower",
    searchable_by=["Flint's Willpower", "Supporter"],
    subtypes=["Supporter"],
    collector_number=91,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    effect=flints_willpower
)
