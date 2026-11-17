from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_active_has, shuffle_hand_draw

card = SupporterCardDef(
    guid="217238b1-90bf-50f1-b99e-c76b098ad6d9",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Atticus.Name",
    display_name="Atticus",
    searchable_by=["Atticus", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="SV4PT5",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_draw(7), condition=opponent_active_has("POISONED")
)
