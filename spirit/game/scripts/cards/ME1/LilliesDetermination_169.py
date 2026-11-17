from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import shuffle_hand_draw_exact_prizes

card = SupporterCardDef(
    guid="b0ba1112-85a9-553d-833e-dbf81e79cbeb",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LilliesDetermination.Name",
    display_name="Lillie's Determination",
    searchable_by=["Lillie's Determination", "Supporter"],
    subtypes=["Supporter"],
    collector_number=169,
    set_code="ME1",
    rarity=Rarities.Rare,
    effect=shuffle_hand_draw_exact_prizes(6, 6, 8)
)
