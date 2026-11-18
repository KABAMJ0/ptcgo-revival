from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_flip_draw

card = SupporterCardDef(
    guid="83b7dccb-b2e3-54d9-9c03-d0ae542b3f5b",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Drasna.Name",
    display_name="Drasna",
    searchable_by=["Drasna", "Supporter"],
    subtypes=["Supporter"],
    collector_number=173,
    set_code="SV8",
    rarity=Rarities.Common,
    effect=shuffle_hand_flip_draw(8, 3)
)
