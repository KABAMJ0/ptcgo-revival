from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import shuffle_hand_draw_exact_prizes

card = SupporterCardDef(
    guid="c1f56a82-b7fa-5619-a09c-b04fc0536f0c",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LilliesDetermination.Name",
    display_name="Lillie's Determination",
    searchable_by=["Lillie's Determination", "Supporter"],
    subtypes=["Supporter"],
    collector_number=192,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_draw_exact_prizes(6, 6, 8)
)
