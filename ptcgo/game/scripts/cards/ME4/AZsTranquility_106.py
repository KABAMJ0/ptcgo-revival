from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import switch_then_heal_ex

card = SupporterCardDef(
    guid="07742ad8-fee6-58c7-ae71-f86ce5d87b90",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AZsTranquility.Name",
    display_name="AZ's Tranquility",
    searchable_by=["AZ's Tranquility", "Supporter"],
    subtypes=["Supporter"],
    collector_number=106,
    set_code="ME4",
    rarity=Rarities.Rare,
    effect=switch_then_heal_ex(80)
)
