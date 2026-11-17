from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import attach_darkness_to_each_poison

card = SupporterCardDef(
    guid="a1873aac-c350-5be6-9adc-6d4c02841edd",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JaninesSecretArt.Name",
    display_name="Janine's Secret Art",
    searchable_by=["Janine's Secret Art", "Supporter"],
    subtypes=["Supporter"],
    collector_number=173,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=attach_darkness_to_each_poison()
)
