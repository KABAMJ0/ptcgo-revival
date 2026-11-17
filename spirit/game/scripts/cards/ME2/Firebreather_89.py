from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import basic_energy_of

card = SupporterCardDef(
    guid="60a6fc1b-cc14-5a61-956c-aa1044535416",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Firebreather.Name",
    display_name="Firebreather",
    searchable_by=["Firebreather", "Supporter"],
    subtypes=["Supporter"],
    collector_number=89,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(basic_energy_of("fire"), count=7)
)
