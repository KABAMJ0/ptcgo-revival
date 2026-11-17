from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_draw

card = SupporterCardDef(
    guid="9d9df75a-5db1-525f-bccf-b33836e7de1e",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Shauna.Name",
    display_name="Shauna",
    searchable_by=["Shauna", "Supporter"],
    subtypes=["Supporter"],
    collector_number=127,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_draw(5)
)
