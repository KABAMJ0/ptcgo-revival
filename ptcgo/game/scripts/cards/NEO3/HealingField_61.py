from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities, AttrID
from ptcgo.game.card_effects.trainers import stadium_ability


async def _healing_field(ctx):
    """Once each turn: flip a coin; heads removes 2 damage counters from the
    acting player's Active (1 if it only has 1)."""
    active = ctx.my_active()
    if active is None:
        return
    damage = ctx.max_hp(active) - active.get_attribute(AttrID.HP, 0)
    if damage <= 0:
        return
    if not (await ctx.flip_coins(1, title="Healing Field"))[0]:
        return
    await ctx.heal(min(2, damage // 10) * 10, active)


card = StadiumCardDef(
    guid="88ffd2cc-7c5b-5ddd-80f7-0edc1d5b9370",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HealingField.Name",
    display_name="Healing Field",
    searchable_by=["Healing Field", "Stadium"],
    subtypes=["Stadium"],
    collector_number=61,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    ability=stadium_ability("Healing Field", _healing_field),
)
