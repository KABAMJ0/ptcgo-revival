from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_opponent_energy

card = ItemCardDef(
    guid="445c272e-28dd-5f7a-aaeb-ac6bd41aa74d",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval.Name",
    display_name="Energy Removal",
    searchable_by=["Energy Removal"],
    subtypes=[],
    collector_number=119,
    set_code="BASE4",
    rarity=Rarities.Common,
    effect=discard_opponent_energy(1)
)
