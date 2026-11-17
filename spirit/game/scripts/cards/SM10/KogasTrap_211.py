from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import SpecialConditions, condition_opponent_active

card = SupporterCardDef(
    guid="a5732e77-bc72-5c8e-bb32-6f9772081548",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.KogasTrap.Name",
    display_name="Koga's Trap",
    searchable_by=["Koga's Trap", "Supporter"],
    subtypes=["Supporter"],
    collector_number=211,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    effect=condition_opponent_active(SpecialConditions.CONFUSED, SpecialConditions.POISONED)
)
