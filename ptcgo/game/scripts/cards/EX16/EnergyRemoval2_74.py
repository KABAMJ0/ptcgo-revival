from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_energy_opponent

card = ItemCardDef(
    guid="3afde8ac-a739-5561-9ec9-a302835b8e78",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval2.Name",
    display_name="Energy Removal 2",
    searchable_by=["Energy Removal 2", "Item"],
    subtypes=["Item"],
    collector_number=74,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    effect=discard_energy_opponent(flip=True)
)
