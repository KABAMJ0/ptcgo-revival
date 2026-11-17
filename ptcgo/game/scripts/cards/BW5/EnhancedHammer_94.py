from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_energy_opponent, is_special_energy

card = ItemCardDef(
    guid="221ddf2d-7c58-5ae3-a40d-95c5965608ca",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnhancedHammer.Name",
    display_name="Enhanced Hammer",
    searchable_by=["Enhanced Hammer", "Item"],
    subtypes=["Item"],
    collector_number=94,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    effect=discard_energy_opponent(energy_pred=is_special_energy)
)
