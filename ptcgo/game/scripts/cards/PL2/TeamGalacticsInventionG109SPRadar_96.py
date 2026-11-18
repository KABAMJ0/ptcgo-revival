from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of_subtype, hand_size_at_least

async def _sp_radar(ctx):
    hand = ctx.hand()
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, 1, minimum=1,
        prompt="Choose a card from your hand to put on top of your deck")
    if not picks:
        return
    await ctx.put_on_top_of_deck(picks[0])
    found = await ctx.search_deck(
        pokemon_of_subtype("SP"), count=1, minimum=0,
        prompt="Choose a Pokémon SP to put into your hand")
    if found:
        await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="e51d11cc-9321-5711-bf6b-57a8752adea7",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamGalacticsInventionG109SPRadar.Name",
    display_name="Team Galactic's Invention G-109 SP Radar",
    searchable_by=["Team Galactic's Invention G-109 SP Radar", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    effect=_sp_radar, condition=hand_size_at_least(2)
)
