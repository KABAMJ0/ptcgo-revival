from ptcgo.game.card_effects.trainers import gx_used_condition, shuffle_hand_draw_if
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities


card = SupporterCardDef(
    guid="d32bcd94-b172-596f-af42-3a5df001fec5",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hala.Name",
    display_name="Hala",
    searchable_by=["Hala", "Supporter"],
    subtypes=["Supporter"],
    collector_number=126,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_draw_if(gx_used_condition(True), 7, 4)
)
