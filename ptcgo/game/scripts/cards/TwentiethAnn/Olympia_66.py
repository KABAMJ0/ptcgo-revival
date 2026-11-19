from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import switch_then_heal

card = SupporterCardDef(
    guid="06a476f5-5dbe-54e5-9687-eeaf9c1f71c5",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Olympia.Name",
    display_name="Olympia",
    searchable_by=["Olympia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=66,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=switch_then_heal(30)
)
