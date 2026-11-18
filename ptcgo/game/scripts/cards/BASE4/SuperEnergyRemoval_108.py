from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_own_energy_opponent_two

card = ItemCardDef(
    guid="d432f18b-0bce-5d88-bdff-fc4838071e09",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperEnergyRemoval.Name",
    display_name="Super Energy Removal",
    searchable_by=["Super Energy Removal"],
    subtypes=[],
    collector_number=108,
    set_code="BASE4",
    rarity=Rarities.Rare,
    effect=discard_own_energy_opponent_two()
)
