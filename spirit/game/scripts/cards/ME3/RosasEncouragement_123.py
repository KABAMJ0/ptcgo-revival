from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import behind_on_prizes, is_basic_energy_card

card = SupporterCardDef(
    guid="6f47dfef-c845-579f-96b8-98f5f1a0da04",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RosasEncouragement.Name",
    display_name="Rosa's Encouragement",
    searchable_by=["Rosa's Encouragement", "Supporter"],
    subtypes=["Supporter"],
    collector_number=123,
    set_code="ME3",
    rarity=Rarities.Rare,
    effect=attach_from_discard(is_basic_energy_card, count=2, target="choice"), condition=behind_on_prizes()
)
