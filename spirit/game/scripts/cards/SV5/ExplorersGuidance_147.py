from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top

card = SupporterCardDef(
    guid="74b89390-d8d9-5a35-a024-bb8c0eb9b4d7",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ExplorersGuidance.Name",
    display_name="Explorer's Guidance",
    searchable_by=["Explorer's Guidance", "Supporter", "Ancient"],
    subtypes=["Supporter", "Ancient"],
    collector_number=147,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    effect=look_at_top(6, take=2)
)
