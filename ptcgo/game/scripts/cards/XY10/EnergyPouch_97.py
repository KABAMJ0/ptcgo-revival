from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card


async def energy_pouch_on_ko(ctx):
    """The holder is Knocked Out by an opponent's attack: put all Basic Energy
    attached to it into your hand."""
    pokemon = ctx.ko_pokemon
    if not ctx.ko_from_attack or pokemon is None:
        return
    energies = [e for e in ctx.attached_energies(pokemon) if is_basic_energy_card(e)]
    if energies:
        await ctx.put_in_hand(energies, reveal=False)


card = PokemonToolCardDef(
    guid="8067bf07-1cd5-588d-b3b2-dfd6ab99c2ff",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyPouch.Name",
    display_name="Energy Pouch",
    searchable_by=["Energy Pouch", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=97,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    on_carrier_knocked_out=energy_pouch_on_ko
)
