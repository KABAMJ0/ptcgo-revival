from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card


async def wishful_baton_on_ko(ctx):
    """Your Active was Knocked Out by an opponent's attack: move up to 3 Basic
    Energy cards from it to 1 of your Benched Pokemon."""
    pokemon = ctx.ko_pokemon
    if not ctx.ko_from_attack or pokemon is None or not ctx.was_active_at_ko:
        return
    energies = [e for e in ctx.attached_energies(pokemon) if is_basic_energy_card(e)]
    bench = ctx.my_bench()
    if not energies or not bench:
        return
    picks = await ctx.choose_cards(
        energies, 3, minimum=0,
        prompt="Choose up to 3 Basic Energy cards to move")
    if not picks:
        return
    target = (await ctx.choose_pokemon(bench, "Choose a Benched Pokemon to move them to")
              if len(bench) > 1 else bench[0])
    if target is None:
        return
    for card in picks:
        await ctx.move_energy(card, target)


card = PokemonToolCardDef(
    guid="a105c6b0-4c0c-5732-a910-1b96b0b78c39",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WishfulBaton.Name",
    display_name="Wishful Baton",
    searchable_by=["Wishful Baton", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=121,
    set_code="SM4",
    rarity=Rarities.RareSecret,
    on_carrier_knocked_out=wishful_baton_on_ko
)
