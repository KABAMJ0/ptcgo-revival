from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities


async def rainbow_brush(ctx):
    """Choose an Energy attached to 1 of your Pokemon, swap it for a basic
    Energy card from the deck, and shuffle the first Energy into the deck."""
    holders = [p for p in ctx.my_pokemon_in_play() if ctx.attached_energies(p)]
    if not holders:
        return
    holder = await ctx.choose_pokemon(
        holders, "Choose the Pokémon holding the Energy to switch") \
        if len(holders) > 1 else holders[0]
    if holder is None:
        return
    picks = await ctx.choose_cards(
        ctx.attached_energies(holder), 1, minimum=1,
        prompt="Choose the Energy card to switch out")
    if not picks:
        return
    found = await ctx.search_deck(
        is_basic_energy_card, count=1, minimum=1,
        prompt="Choose a basic Energy card to switch in")
    if not found:
        await ctx.shuffle_deck()
        return
    await ctx.attach_energy(found[0], holder)
    await ctx.shuffle_into_deck(picks[:1])


card = ItemCardDef(
    guid="fa9c4885-6550-5be3-a9a4-fb34bdb48261",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RainbowBrush.Name",
    display_name="Rainbow Brush",
    searchable_by=["Rainbow Brush", "Item"],
    subtypes=["Item"],
    collector_number=182,
    set_code="SM7",
    rarity=Rarities.RareSecret,
    effect=rainbow_brush
)
