from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import switch_then_heal_ex

card = SupporterCardDef(
    guid="66e46e42-a454-51e0-8f5b-1399c6985bd7",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AZsTranquility.Name",
    display_name="AZ's Tranquility",
    searchable_by=["AZ's Tranquility", "Supporter"],
    subtypes=["Supporter"],
    collector_number=120,
    set_code="ME4",
    rarity=Rarities.Rare,
    effect=switch_then_heal_ex(80)
)
