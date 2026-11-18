from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_tool_and_special_energy_from_opponent

card = SupporterCardDef(
    guid="cd7a3c9b-c3d3-5383-9a11-381909c30235",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ruffian.Name",
    display_name="Ruffian",
    searchable_by=["Ruffian", "Supporter"],
    subtypes=["Supporter"],
    collector_number=157,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    effect=discard_tool_and_special_energy_from_opponent()
)
