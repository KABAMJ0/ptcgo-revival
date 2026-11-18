from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_draw_going_second

card = SupporterCardDef(
    guid="2012bb05-1b6c-5c3b-aefd-3f055e3b3b49",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ParasolLady.Name",
    display_name="Parasol Lady",
    searchable_by=["Parasol Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=169,
    set_code="SV4",
    rarity=Rarities.Common,
    effect=shuffle_hand_draw_going_second(4, 8)
)
