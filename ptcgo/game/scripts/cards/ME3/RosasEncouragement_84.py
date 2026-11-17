from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import behind_on_prizes, is_basic_energy_card

card = SupporterCardDef(
    guid="d999eb9a-921a-5d50-abc7-a907f4d7b9a8",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RosasEncouragement.Name",
    display_name="Rosa's Encouragement",
    searchable_by=["Rosa's Encouragement", "Supporter"],
    subtypes=["Supporter"],
    collector_number=84,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    effect=attach_from_discard(is_basic_energy_card, count=2, target="choice"), condition=behind_on_prizes()
)
