from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import shuffle_hand_draw

card = SupporterCardDef(
    guid="179c31ec-0ced-5af4-9eba-1424132ea1e9",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Shauna.Name",
    display_name="Shauna",
    searchable_by=["Shauna", "Supporter"],
    subtypes=["Supporter"],
    collector_number=111,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    effect=shuffle_hand_draw(5)
)
