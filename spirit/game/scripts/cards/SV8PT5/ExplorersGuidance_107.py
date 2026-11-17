from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top

card = SupporterCardDef(
    guid="ca8e74f6-9d35-5df8-9854-834e100c0c74",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ExplorersGuidance.Name",
    display_name="Explorer's Guidance",
    searchable_by=["Explorer's Guidance", "Supporter", "Ancient"],
    subtypes=["Supporter", "Ancient"],
    collector_number=107,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    effect=look_at_top(6, take=2)
)
