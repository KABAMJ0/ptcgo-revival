from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_flip_draw

card = SupporterCardDef(
    guid="4340e509-27b6-5376-988b-6a73dac655a7",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Drasna.Name",
    display_name="Drasna",
    searchable_by=["Drasna", "Supporter"],
    subtypes=["Supporter"],
    collector_number=231,
    set_code="SV8",
    rarity=Rarities.Rare,
    effect=shuffle_hand_flip_draw(8, 3)
)
