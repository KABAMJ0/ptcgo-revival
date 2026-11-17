from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import move_energy_to_active

card = SupporterCardDef(
    guid="e7a79eec-dc57-536d-8161-1b06dc3a4dcc",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NsPlan.Name",
    display_name="N's Plan",
    searchable_by=["N's Plan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="ZSV10PT5",
    rarity=Rarities.Uncommon,
    effect=move_energy_to_active(2)
)
