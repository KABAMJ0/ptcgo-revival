from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import switch_then_draw_until

card = SupporterCardDef(
    guid="35537d0d-bea6-50a6-8f37-4f9730ee6a96",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Surfer.Name",
    display_name="Surfer",
    searchable_by=["Surfer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=200,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    effect=switch_then_draw_until(5)
)
