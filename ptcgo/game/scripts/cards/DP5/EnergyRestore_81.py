from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_recover_basic_energy

card = ItemCardDef(
    guid="71602ad8-0751-5c37-9e3a-2b65539a8964",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRestore.Name",
    display_name="Energy Restore",
    searchable_by=["Energy Restore", "Item"],
    subtypes=["Item"],
    collector_number=81,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    effect=flip_recover_basic_energy(3)
)
