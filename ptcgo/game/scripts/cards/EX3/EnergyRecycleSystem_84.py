from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import energy_recycle_choice

card = ItemCardDef(
    guid="631c7a2e-67c5-5ee4-8340-d7d6ac73a8b5",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycleSystem.Name",
    display_name="Energy Recycle System",
    searchable_by=["Energy Recycle System", "Item"],
    subtypes=["Item"],
    collector_number=84,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    effect=energy_recycle_choice()
)
