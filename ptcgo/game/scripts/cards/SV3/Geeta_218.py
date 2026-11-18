from ptcgo.game.card_effects.support_common import search_attach_energy_then_lock_attacks
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="fb68926f-99a3-5ca8-ae9a-b7d80dc2eaa3",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Geeta.Name",
    display_name="Geeta",
    searchable_by=["Geeta", "Supporter"],
    subtypes=["Supporter"],
    collector_number=218,
    set_code="SV3",
    rarity=Rarities.Rare,
    effect=search_attach_energy_then_lock_attacks(2, "Choose up to 2 Basic Energy cards")
)
