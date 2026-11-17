from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_draw_exact_prizes

card = SupporterCardDef(
    guid="52b10a5e-fc89-52fe-9ba8-57f2c1800380",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LilliesDetermination.Name",
    display_name="Lillie's Determination",
    searchable_by=["Lillie's Determination", "Supporter"],
    subtypes=["Supporter"],
    collector_number=119,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_draw_exact_prizes(6, 6, 8)
)
