from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_opponent_energy

card = ItemCardDef(
    guid="ba29102d-bffa-50fc-9029-2423e5d1772b",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval.Name",
    display_name="Energy Removal",
    searchable_by=["Energy Removal"],
    subtypes=[],
    collector_number=92,
    set_code="BASE1",
    rarity=Rarities.Common,
    effect=discard_opponent_energy(1)
)
