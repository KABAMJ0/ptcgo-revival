from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities


async def night_teleporter(ctx):
    """Flip a coin: heads, put your hand on top of your deck and search any 1 card."""
    if not (await ctx.flip_coins(1, "Night Teleporter"))[0]:
        return
    for card in list(ctx.hand()):
        await ctx.put_on_top_of_deck(card)
    found = await ctx.search_deck(
        lambda card: True, count=1, minimum=0,
        prompt="Choose any 1 card to put into your hand")
    if found:
        await ctx.put_in_hand(found)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="aa9bd243-2fb7-5e6c-9eca-be3ff1c35ba3",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightTeleporter.Name",
    display_name="Night Teleporter",
    searchable_by=["Night Teleporter", "Item"],
    subtypes=["Item"],
    collector_number=138,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    effect=night_teleporter,
)
