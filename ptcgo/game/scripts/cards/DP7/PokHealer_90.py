from ptcgo.game.data_utils import ItemCardDef, def_for
from ptcgo.game.attributes import AttrID, Rarities
from ptcgo.game.session.effects import CLIENT_SPECIAL_CONDITION_NAMES

_CONDITION_BY_NAME = {name: condition
                      for condition, name in CLIENT_SPECIAL_CONDITION_NAMES.items()}


def _named(card, name):
    definition = def_for(card.archetype_id)
    return bool(definition) and definition.display_name == name


def _second_copy(ctx):
    return next((c for c in ctx.hand()
                 if c.entity_id != ctx.source.entity_id
                 and _named(c, "Pok\u00e9 Healer +")), None)


async def _pok_healer(ctx):
    """2 copies at once: remove 8 damage counters and every Special Condition
    from your Active Pokemon. 1 copy: remove 1 damage counter and 1 Special
    Condition from it."""
    active = ctx.my_active()
    if active is None:
        return
    pair = _second_copy(ctx)
    if pair is not None and await ctx.ask_yes_no(
            "Play a second Pok\u00e9 Healer + to remove 8 damage counters and "
            "all Special Conditions instead?"):
        await ctx.discard_cards([pair])
        await ctx.heal(80, active)
        await ctx.cure_all_conditions(active)
        return
    await ctx.heal(10, active)
    present = [name for name
               in (active.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
               if name in _CONDITION_BY_NAME]
    if not present:
        return
    index = 0
    if len(present) > 1:
        index = await ctx.choose("Remove a Special Condition", present)
    await ctx.cure_condition(active, _CONDITION_BY_NAME[present[index]])


card = ItemCardDef(
    guid="8b781dff-5511-5088-8e93-eee4ccf49dd5",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokHealer.Name",
    display_name="Poké Healer +",
    searchable_by=["Pok\u00e9 Healer +", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    effect=_pok_healer,
)
