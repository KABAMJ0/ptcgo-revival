from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import ends_turn_after


async def thought_wave_machine(ctx):
    """Flip a coin until you get tails: return 1 Energy from the opponent's
    Active to their hand for each heads (all of them if there are fewer).
    Your turn is over and you do not get to attack."""
    heads = await ctx.flip_until_tails("Thought Wave Machine")
    holder = ctx.opponent_active()
    if holder is not None and heads:
        energies = ctx.attached_energies(holder)[:heads]
        if energies:
            await ctx.put_in_hand(energies, reveal=False)


card = ItemCardDef(
    guid="98ec0812-e124-51e7-ad24-93e77612bb91",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ThoughtWaveMachine.Name",
    display_name="Thought Wave Machine",
    searchable_by=["Thought Wave Machine", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=96,
    set_code="NEO4",
    rarity=Rarities.Rare,
    effect=ends_turn_after(thought_wave_machine)
)
