from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import SpecialConditions, condition_opponent_active

card = SupporterCardDef(
    guid="e9112bd6-8e01-5f66-b1c7-caed7b635293",
    key="SM115",
    name="com.direwolfdigital.cake.data.archetypes.trainer.KogasTrap.Name",
    display_name="Koga's Trap",
    searchable_by=["Koga's Trap", "Supporter"],
    subtypes=["Supporter"],
    collector_number=59,
    set_code="SM115",
    rarity=Rarities.Uncommon,
    effect=condition_opponent_active(SpecialConditions.CONFUSED, SpecialConditions.POISONED)
)
