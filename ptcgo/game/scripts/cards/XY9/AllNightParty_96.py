from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import Ability, Activations
from ptcgo.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES, SpecialConditions


def active_is_asleep(board, player_id, stadium) -> bool:
    active = board.active_pokemon(player_id)
    if active is None:
        return False
    asleep = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
    return asleep in (active.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])

async def all_night_party(ctx):
    """If your Active Pokemon is Asleep, remove that condition and heal 30."""
    active = ctx.my_active()
    if active is None:
        return
    await ctx.cure_all_conditions(active)
    await ctx.heal(30, active)


card = StadiumCardDef(
    guid="06cda8ff-46cf-5b60-8302-9eab2e539f61",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AllNightParty.Name",
    display_name="All-Night Party",
    searchable_by=["All-Night Party", "Stadium"],
    subtypes=["Stadium"],
    collector_number=96,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="All-Night Party",
        activation=Activations.ONCE_PER_TURN,
            condition=active_is_asleep,
        effect=all_night_party,
    )
)
