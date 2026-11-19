from ptcgo.game.card_effects.trainers import gx_used_condition, shuffle_hand_draw_if
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities


card = SupporterCardDef(
    guid="f3084b97-94c7-581c-8d61-9cf6f4fca24a",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hala.Name",
    display_name="Hala",
    searchable_by=["Hala", "Supporter"],
    subtypes=["Supporter"],
    collector_number=143,
    set_code="SM2",
    rarity=Rarities.RareUltra,
    effect=shuffle_hand_draw_if(gx_used_condition(True), 7, 4)
)
