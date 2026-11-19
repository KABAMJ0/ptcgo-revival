from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top

card = SupporterCardDef(
    guid="56ce7725-71e6-5cab-8db8-5ffff482b9b5",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SagesTraining.Name",
    display_name="Sage's Training",
    searchable_by=["Sage's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=85,
    set_code="COL",
    rarity=Rarities.Uncommon,
    effect=look_at_top(5, take=2, rest="discard")
)
