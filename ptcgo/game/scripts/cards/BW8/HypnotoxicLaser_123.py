from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities, SpecialConditions


async def _hypnotoxic_laser(ctx):
    """Their Active is Poisoned; heads also puts it Asleep."""
    target = ctx.opponent_active()
    if target is None:
        return
    await ctx.apply_special_condition(target, SpecialConditions.POISONED)
    if not (await ctx.flip_coins(1, title="Hypnotoxic Laser"))[0]:
        return
    target = ctx.opponent_active()
    if target is not None:
        await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)


card = ItemCardDef(
    guid="56651494-fb94-5b38-9de7-64e8845b5336",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HypnotoxicLaser.Name",
    display_name="Hypnotoxic Laser",
    searchable_by=["Hypnotoxic Laser", "Item", "Team Plasma"],
    subtypes=["Item", "Team Plasma"],
    collector_number=123,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=_hypnotoxic_laser,
)
