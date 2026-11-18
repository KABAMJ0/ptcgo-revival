from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top

card = SupporterCardDef(
    guid="329e5a8b-f55f-5909-849e-f4d057bc3b85",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rika.Name",
    display_name="Rika",
    searchable_by=["Rika", "Supporter"],
    subtypes=["Supporter"],
    collector_number=258,
    set_code="SV4",
    rarity=Rarities.Rare,
    effect=look_at_top(4, take=2, rest="bottom")
)
