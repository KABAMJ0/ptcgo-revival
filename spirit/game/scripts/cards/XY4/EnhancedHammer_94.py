from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_energy_opponent, is_special_energy

card = ItemCardDef(
    guid="d3ea5356-fc9d-585a-8286-584fe869b7f3",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnhancedHammer.Name",
    display_name="Enhanced Hammer",
    searchable_by=["Enhanced Hammer", "Item"],
    subtypes=["Item"],
    collector_number=94,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    effect=discard_energy_opponent(energy_pred=is_special_energy)
)
