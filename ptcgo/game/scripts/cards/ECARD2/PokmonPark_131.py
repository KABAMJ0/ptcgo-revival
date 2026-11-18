from ptcgo.game.data_utils import Ability, StadiumCardDef, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot


async def pokemon_park_heal(ctx):
    """A manual Energy attachment from hand to the attaching player's own
    Benched Pokemon removes 1 damage counter from it."""
    receiver = ctx.energy_receiver
    if receiver is None or ctx.attaching_player_id is None:
        return
    if receiver.owning_player_id != ctx.attaching_player_id:
        return
    if is_in_active_spot(receiver):
        return
    await ctx.heal(10, receiver)


card = StadiumCardDef(
    guid="d83ca121-f6ae-5e3e-8ea4-401c5ad0228e",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonPark.Name",
    display_name="Pok\u00e9mon Park",
    searchable_by=["Pok\u00e9mon Park", "Stadium"],
    subtypes=["Stadium"],
    collector_number=131,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    abilities=[Ability(
        title="Pok\u00e9mon Park",
        trigger=Triggers.ON_ENERGY_ATTACHED,
        effect=pokemon_park_heal,
        shared_once_per_turn="pokemon-park",
    )]
)
