from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_each_typed

card = SupporterCardDef(
    guid="7fa050f1-4ae2-54a5-ba34-66989c387ef8",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ClemontsQuickWit.Name",
    display_name="Clemont's Quick Wit",
    searchable_by=["Clemont's Quick Wit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=167,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    effect=heal_each_typed(60, "lightning")
)
