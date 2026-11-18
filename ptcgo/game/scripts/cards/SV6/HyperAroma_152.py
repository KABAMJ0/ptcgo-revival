from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_stage_one

card = ItemCardDef(
    guid="885ca228-2ea5-58f7-8ed2-c6be13fd8501",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HyperAroma.Name",
    display_name="Hyper Aroma",
    searchable_by=["Hyper Aroma", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=152,
    set_code="SV6",
    rarity=Rarities.Rare,
    effect=search_to_hand(is_stage_one, count=3)
)
