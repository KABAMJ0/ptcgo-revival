from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import energy_recycle_choice

card = ItemCardDef(
    guid="a98b1351-fabe-5eb2-a15b-0d05ef0a0156",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycleSystem.Name",
    display_name="Energy Recycle System",
    searchable_by=["Energy Recycle System", "Item"],
    subtypes=["Item"],
    collector_number=73,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    effect=energy_recycle_choice()
)
