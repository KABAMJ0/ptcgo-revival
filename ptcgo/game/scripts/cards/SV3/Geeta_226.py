from ptcgo.game.card_effects.support_common import search_attach_energy_then_lock_attacks
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="ac6d0f3a-9cea-5a09-a106-30a2ff7ac4e4",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Geeta.Name",
    display_name="Geeta",
    searchable_by=["Geeta", "Supporter"],
    subtypes=["Supporter"],
    collector_number=226,
    set_code="SV3",
    rarity=Rarities.Rare,
    effect=search_attach_energy_then_lock_attacks(2, "Choose up to 2 Basic Energy cards")
)
