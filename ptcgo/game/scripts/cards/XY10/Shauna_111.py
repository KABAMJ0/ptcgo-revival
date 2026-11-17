from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_draw

card = SupporterCardDef(
    guid="45af2673-7da9-5e60-a2a3-6d6ea7fdc535",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Shauna.Name",
    display_name="Shauna",
    searchable_by=["Shauna", "Supporter"],
    subtypes=["Supporter"],
    collector_number=111,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_draw(5)
)
