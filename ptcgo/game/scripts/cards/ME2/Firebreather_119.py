from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import basic_energy_of

card = SupporterCardDef(
    guid="7105c378-fce9-558b-9627-e5d4df898c49",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Firebreather.Name",
    display_name="Firebreather",
    searchable_by=["Firebreather", "Supporter"],
    subtypes=["Supporter"],
    collector_number=119,
    set_code="ME2",
    rarity=Rarities.Rare,
    effect=search_to_hand(basic_energy_of("fire"), count=7)
)
