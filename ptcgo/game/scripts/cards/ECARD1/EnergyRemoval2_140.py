from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_energy_opponent

card = ItemCardDef(
    guid="d1e0df22-cbc3-593d-a852-55e0b47f0abf",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval2.Name",
    display_name="Energy Removal 2",
    searchable_by=["Energy Removal 2"],
    subtypes=[],
    collector_number=140,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=discard_energy_opponent(flip=True)
)
