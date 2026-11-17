from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_tool_card, stadium_ability

card = StadiumCardDef(
    guid="72f9116a-7cc5-5e36-ab5e-bf1cc295dd8b",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TownStore.Name",
    display_name="Town Store",
    searchable_by=["Town Store", "Stadium"],
    subtypes=["Stadium"],
    collector_number=196,
    set_code="SV3",
    rarity=Rarities.Common,
    ability=stadium_ability('Town Store', search_to_hand(is_tool_card, count=1))
)
