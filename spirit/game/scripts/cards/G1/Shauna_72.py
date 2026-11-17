from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import shuffle_hand_draw

card = SupporterCardDef(
    guid="3aff0924-4513-57cc-8415-035f756bf56b",
    key="G1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Shauna.Name",
    display_name="Shauna",
    searchable_by=["Shauna", "Supporter"],
    subtypes=["Supporter"],
    collector_number=72,
    set_code="G1",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_draw(5)
)
