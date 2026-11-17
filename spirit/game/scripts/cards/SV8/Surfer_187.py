from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import switch_then_draw_until

card = SupporterCardDef(
    guid="84949575-1331-5aeb-a7a0-eea43ad24c47",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Surfer.Name",
    display_name="Surfer",
    searchable_by=["Surfer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=187,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    effect=switch_then_draw_until(5)
)
