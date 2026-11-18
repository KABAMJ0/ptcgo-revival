from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import reveal_then_search_same

card = SupporterCardDef(
    guid="2568e5ee-14ec-5968-b17c-7c1cf267f8de",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Perrin.Name",
    display_name="Perrin",
    searchable_by=["Perrin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=220,
    set_code="SV6",
    rarity=Rarities.Rare,
    effect=reveal_then_search_same()
)
