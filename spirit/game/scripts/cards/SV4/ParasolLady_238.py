from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import shuffle_hand_draw_going_second

card = SupporterCardDef(
    guid="5f66f3c9-6071-57fc-887f-b36aba673aa2",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ParasolLady.Name",
    display_name="Parasol Lady",
    searchable_by=["Parasol Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=238,
    set_code="SV4",
    rarity=Rarities.Rare,
    effect=shuffle_hand_draw_going_second(4, 8)
)
