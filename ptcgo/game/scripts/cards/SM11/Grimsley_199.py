from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import move_counters_between_opponents

card = SupporterCardDef(
    guid="5d564d00-7915-550f-870e-394143551841",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Grimsley.Name",
    display_name="Grimsley",
    searchable_by=["Grimsley", "Supporter"],
    subtypes=["Supporter"],
    collector_number=199,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    effect=move_counters_between_opponents(3)
)
