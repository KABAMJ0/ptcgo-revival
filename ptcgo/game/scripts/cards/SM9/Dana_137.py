from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_stage_two, opponent_active_is

card = SupporterCardDef(
    guid="f7b0941e-0a4d-5f1f-a46f-78a5f6b1467e",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dana.Name",
    display_name="Dana",
    searchable_by=["Dana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=137,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(None, count=2), condition=opponent_active_is(is_stage_two)
)
