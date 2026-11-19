from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_opponent_special_energy_to_lost_zone

card = ItemCardDef(
    guid="1a0fdbbf-214e-501e-ba70-8d97fc3f623b",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LostRemover.Name",
    display_name="Lost Remover",
    searchable_by=["Lost Remover", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="COL",
    rarity=Rarities.Uncommon,
    effect=discard_opponent_special_energy_to_lost_zone(1)
)
