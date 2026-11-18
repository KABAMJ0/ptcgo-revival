from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import AttrID, Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card


async def _heavy_baton(ctx):
    holder = ctx.ko_pokemon
    if holder is None or not ctx.ko_from_attack or not ctx.was_active_at_ko:
        return
    if (holder.get_attribute(AttrID.RETREAT_COST) or 0) != 4:
        return
    pool = [card for card in ctx.attached_energies(holder)
            if is_basic_energy_card(card)]
    bench = ctx.my_bench()
    if not pool or not bench:
        return
    await ctx.move_energy_freely(
        [holder], bench, predicate=is_basic_energy_card, max_count=3,
        prompt="Choose a Basic Energy to move to your Bench")


card = PokemonToolCardDef(
    guid="fd4607ce-096d-5688-85b9-c8ffeae83472",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeavyBaton.Name",
    display_name="Heavy Baton",
    searchable_by=["Heavy Baton", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=151,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    on_carrier_knocked_out=_heavy_baton,
)
