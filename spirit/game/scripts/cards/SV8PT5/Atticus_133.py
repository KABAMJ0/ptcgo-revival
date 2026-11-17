from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_active_has, shuffle_hand_draw

card = SupporterCardDef(
    guid="5cdc599f-bcff-5ef8-aae7-6df9f1ea70a4",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Atticus.Name",
    display_name="Atticus",
    searchable_by=["Atticus", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=shuffle_hand_draw(7), condition=opponent_active_has("POISONED")
)
