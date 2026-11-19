from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_fossil_or_fossil_evolution

card = SupporterCardDef(
    guid="a19dcdd8-24df-5c3f-81dd-dbf181ec5c37",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilExcavator.Name",
    display_name="Fossil Excavator",
    searchable_by=["Fossil Excavator", "Supporter"],
    subtypes=["Supporter"],
    collector_number=82,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    effect=search_fossil_or_fossil_evolution()
)
