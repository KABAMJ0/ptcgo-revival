from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import switch_then_heal_ex

card = SupporterCardDef(
    guid="c4b06e35-21cf-5405-90fd-f87b4dd1a80b",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AZsTranquility.Name",
    display_name="AZ's Tranquility",
    searchable_by=["AZ's Tranquility", "Supporter"],
    subtypes=["Supporter"],
    collector_number=76,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    effect=switch_then_heal_ex(80)
)
