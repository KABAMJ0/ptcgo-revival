from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top

card = SupporterCardDef(
    guid="13382a32-89f2-5e13-9806-632e8f8689c6",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ExplorersGuidance.Name",
    display_name="Explorer's Guidance",
    searchable_by=["Explorer's Guidance", "Supporter", "Ancient"],
    subtypes=["Supporter", "Ancient"],
    collector_number=200,
    set_code="SV5",
    rarity=Rarities.Rare,
    effect=look_at_top(6, take=2)
)
