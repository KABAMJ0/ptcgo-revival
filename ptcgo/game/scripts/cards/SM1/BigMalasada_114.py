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
    guid="7a2c3aff-ac27-5a97-8ca0-7e239c97e5ee",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BigMalasada.Name",
    display_name="Big Malasada",
    searchable_by=["Big Malasada", "Item"],
    subtypes=["Item"],
    collector_number=114,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=_heal_and_cure_active,
)
