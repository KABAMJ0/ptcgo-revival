from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import shuffle_hand_draw_exact_prizes

card = SupporterCardDef(
    guid="6a881d47-b002-58c2-8a3b-d9011d762db0",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LilliesDetermination.Name",
    display_name="Lillie's Determination",
    searchable_by=["Lillie's Determination", "Supporter"],
    subtypes=["Supporter"],
    collector_number=184,
    set_code="ME1",
    rarity=Rarities.Rare,
    effect=shuffle_hand_draw_exact_prizes(6, 6, 8)
)
