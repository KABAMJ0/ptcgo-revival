from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_tool_card

card = SupporterCardDef(
    guid="dc5fe907-5777-590e-82d0-17a2978aac22",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DepartmentStoreGirl.Name",
    display_name="Department Store Girl",
    searchable_by=["Department Store Girl", "Supporter"],
    subtypes=["Supporter"],
    collector_number=85,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_tool_card, count=3)
)
