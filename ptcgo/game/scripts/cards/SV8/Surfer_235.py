from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import switch_then_draw_until

card = SupporterCardDef(
    guid="30104b53-f211-5b53-85b3-286092e8c741",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Surfer.Name",
    display_name="Surfer",
    searchable_by=["Surfer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=235,
    set_code="SV8",
    rarity=Rarities.Rare,
    effect=switch_then_draw_until(5)
)
