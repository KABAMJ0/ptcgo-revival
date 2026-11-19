from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities


async def cynthias_ambition(ctx):
    """Draw to 5, or to 8 if any of your Pokemon were KO'd last turn."""
    target = 8 if ctx.kos_suffered_last_turn() > 0 else 5
    await ctx.draw_until(target)


card = SupporterCardDef(
    guid="4ce75eab-b578-578b-b13c-26721eb57e56",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CynthiasAmbition.Name",
    display_name="Cynthia's Ambition",
    searchable_by=["Cynthia's Ambition", "Supporter"],
    subtypes=["Supporter"],
    collector_number=60,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareUltra,
    effect=cynthias_ambition
)
