from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_recover_basic_energy

card = ItemCardDef(
    guid="fb38792c-fec6-5aaf-b357-c22d7627de15",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRestore.Name",
    display_name="Energy Restore",
    searchable_by=["Energy Restore", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    effect=flip_recover_basic_energy(3)
)
