from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top

card = SupporterCardDef(
    guid="25628850-e253-5e25-a7d8-9282c01c76af",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Janine.Name",
    display_name="Janine",
    searchable_by=["Janine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=176,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=look_at_top(4, take=2)
)
