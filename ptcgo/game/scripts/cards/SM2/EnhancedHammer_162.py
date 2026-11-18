from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_energy_opponent, is_special_energy

card = ItemCardDef(
    guid="170fe1d6-bba9-5ee6-93d8-f20687db8f5c",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnhancedHammer.Name",
    display_name="Enhanced Hammer",
    searchable_by=["Enhanced Hammer", "Item"],
    subtypes=["Item"],
    collector_number=162,
    set_code="SM2",
    rarity=Rarities.RareSecret,
    effect=discard_energy_opponent(energy_pred=is_special_energy)
)
