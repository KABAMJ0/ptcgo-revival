from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_energy_opponent, is_special_energy

card = ItemCardDef(
    guid="2a1cae75-b493-50bf-bd67-ca99d579d4f7",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnhancedHammer.Name",
    display_name="Enhanced Hammer",
    searchable_by=["Enhanced Hammer", "Item"],
    subtypes=["Item"],
    collector_number=162,
    set_code="XY5",
    rarity=Rarities.RareSecret,
    effect=discard_energy_opponent(energy_pred=is_special_energy)
)
