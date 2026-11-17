from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_draw

card = SupporterCardDef(
    guid="44a9e31a-f5e8-58a2-b918-b7de65bb74e2",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Shauna.Name",
    display_name="Shauna",
    searchable_by=["Shauna", "Supporter"],
    subtypes=["Supporter"],
    collector_number=104,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_draw(5)
)
