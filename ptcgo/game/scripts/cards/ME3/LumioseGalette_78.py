from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities, AttrID, SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES


async def _heal_and_cure_active(ctx):
    """Heal 20 from the Active, then remove ONE of its Special Conditions."""
    active = ctx.my_active()
    if active is None:
        return
    await ctx.heal(20, active)
    present = list((active.get_attribute(AttrID.SPECIAL_CONDITIONS) or []))
    known = [c for c in SpecialConditions
             if c is not SpecialConditions.UNSET
             and CLIENT_SPECIAL_CONDITION_NAMES[c] in present]
    if not known:
        return
    names = [CLIENT_SPECIAL_CONDITION_NAMES[c] for c in known]
    pick = 0 if len(names) == 1 else await ctx.choose(
        "Choose a Special Condition to remove", names)
    await ctx.cure_condition(active, known[pick])


card = ItemCardDef(
    guid="8d5e687d-fa0f-552f-95b8-387f3bdf819c",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LumioseGalette.Name",
    display_name="Lumiose Galette",
    searchable_by=["Lumiose Galette", "Item"],
    subtypes=["Item"],
    collector_number=78,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    effect=_heal_and_cure_active,
)
