from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities, AttrID, SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES
from ptcgo.game.card_effects.trainers import stadium_ability


async def _all_night_party(ctx):
    """Once each turn: if the acting player's Active is Asleep, they may wake
    it and heal 30 from it."""
    active = ctx.my_active()
    if active is None:
        return
    asleep = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
    if asleep not in (active.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
        return
    await ctx.cure_condition(active, SpecialConditions.ASLEEP)
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
    ability=stadium_ability("All-Night Party", _all_night_party),
)
