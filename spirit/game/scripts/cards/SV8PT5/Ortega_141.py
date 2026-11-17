from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_hand_to_bottom

card = SupporterCardDef(
    guid="147df5d2-cde1-5924-9a09-e2bf34834437",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ortega.Name",
    display_name="Ortega",
    searchable_by=["Ortega", "Supporter"],
    subtypes=["Supporter"],
    collector_number=141,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=opponent_hand_to_bottom()
)
