from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top

card = SupporterCardDef(
    guid="ee3235b0-c395-5758-8120-17fb8babec2e",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rika.Name",
    display_name="Rika",
    searchable_by=["Rika", "Supporter"],
    subtypes=["Supporter"],
    collector_number=172,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    effect=look_at_top(4, take=2, rest="bottom")
)
