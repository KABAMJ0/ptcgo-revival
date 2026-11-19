from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card


async def time_shard_on_ko(ctx):
    """Knocked out by damage from the Defending Pokemon's attack: return up to
    2 basic Energy cards attached to it to your hand, before the stack leaves
    play."""
    pokemon = ctx.ko_pokemon
    if not ctx.ko_from_attack or pokemon is None:
        return
    energies = [e for e in ctx.attached_energies(pokemon)
                if is_basic_energy_card(e)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=0,
        prompt="Choose up to 2 basic Energy cards to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = PokemonToolCardDef(
    guid="6afddc1d-2b79-5aba-96a9-3cb8d4cb33b5",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TimeShard.Name",
    display_name="Time Shard",
    searchable_by=["Time Shard", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=135,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    on_carrier_knocked_out=time_shard_on_ko
)
