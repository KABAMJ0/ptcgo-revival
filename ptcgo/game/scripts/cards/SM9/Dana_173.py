from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_stage_two, opponent_active_is

card = SupporterCardDef(
    guid="c30e707e-dfed-5d15-a697-d00df9cf6e0a",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dana.Name",
    display_name="Dana",
    searchable_by=["Dana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=173,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(None, count=2), condition=opponent_active_is(is_stage_two)
)
