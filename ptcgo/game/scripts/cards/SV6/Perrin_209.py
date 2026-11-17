from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import reveal_then_search_same

card = SupporterCardDef(
    guid="0c970ad8-4028-577a-9ff6-6109fc15ad27",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Perrin.Name",
    display_name="Perrin",
    searchable_by=["Perrin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=209,
    set_code="SV6",
    rarity=Rarities.Rare,
    effect=reveal_then_search_same()
)
