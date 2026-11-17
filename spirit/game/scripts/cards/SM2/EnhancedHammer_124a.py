from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_energy_opponent, is_special_energy

card = ItemCardDef(
    guid="b0b7d30b-c42c-5e55-8717-5f93c027287c",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnhancedHammer.Name",
    display_name="Enhanced Hammer",
    searchable_by=["Enhanced Hammer", "Item"],
    subtypes=["Item"],
    collector_number=124,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=discard_energy_opponent(energy_pred=is_special_energy)
)
