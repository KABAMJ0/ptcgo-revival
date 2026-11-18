from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, switch

async def _rainbow_brush(ctx):
    holders = [p for p in ctx.my_pokemon_in_play() if ctx.attached_energies(p)]
    if not holders:
        return
    target = await ctx.choose_pokemon(
        holders, "Choose a Pokémon with Energy attached") \
        if len(holders) > 1 else holders[0]
    if target is None:
        return
    energies = ctx.attached_energies(target)
    picked = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose an Energy card to switch") if len(energies) > 1 else energies[:1]
    if not picked:
        return
    found = await ctx.search_deck(
        is_basic_energy_card, count=1, minimum=0,
        prompt="Choose a basic Energy card to attach")
    if found:
        await ctx.attach_energy(found[0], target)
    await ctx.shuffle_into_deck(picked)


card = ItemCardDef(
    guid="e52193d6-c1c9-5bf1-910b-2786a41ef753",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RainbowBrush.Name",
    display_name="Rainbow Brush",
    searchable_by=["Rainbow Brush", "Item"],
    subtypes=["Item"],
    collector_number=141,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=_rainbow_brush
)
