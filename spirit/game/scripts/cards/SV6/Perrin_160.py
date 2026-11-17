from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import reveal_then_search_same

card = SupporterCardDef(
    guid="7cc10ee0-6a32-5930-845a-114b5e224f7c",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Perrin.Name",
    display_name="Perrin",
    searchable_by=["Perrin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=160,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    effect=reveal_then_search_same()
)
