from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_draw_going_second

card = SupporterCardDef(
    guid="5ffe3b73-78a8-595c-9bbc-6e3b9f7192c2",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ParasolLady.Name",
    display_name="Parasol Lady",
    searchable_by=["Parasol Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=255,
    set_code="SV4",
    rarity=Rarities.Rare,
    effect=shuffle_hand_draw_going_second(4, 8)
)
