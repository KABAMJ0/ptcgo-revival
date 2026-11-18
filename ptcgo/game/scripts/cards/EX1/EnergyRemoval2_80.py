from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_energy_opponent

card = ItemCardDef(
    guid="1e441269-b8be-54c4-8d06-1123d4c5722b",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval2.Name",
    display_name="Energy Removal 2",
    searchable_by=["Energy Removal 2", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    effect=discard_energy_opponent(flip=True)
)
