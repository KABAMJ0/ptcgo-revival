from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_energy_opponent, is_special_energy

card = ItemCardDef(
    guid="074bf196-9dd8-535f-9e27-1db505665b8d",
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
