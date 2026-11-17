from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import attach_darkness_to_each_poison

card = SupporterCardDef(
    guid="cec08525-6f8d-5c01-9bbf-c988a0fa91c9",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JaninesSecretArt.Name",
    display_name="Janine's Secret Art",
    searchable_by=["Janine's Secret Art", "Supporter"],
    subtypes=["Supporter"],
    collector_number=59,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    effect=attach_darkness_to_each_poison()
)
