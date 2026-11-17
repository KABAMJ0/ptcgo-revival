from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_per_typed, hand_is_last

card = SupporterCardDef(
    guid="2aa98f63-7db3-5bbc-ba5c-3c8b93c9da2a",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesLastStand.Name",
    display_name="Blaine's Last Stand",
    searchable_by=["Blaine's Last Stand", "Supporter"],
    subtypes=["Supporter"],
    collector_number=52,
    set_code="HF",
    rarity=Rarities.Rare,
    effect=draw_per_typed("fire", 2), condition=hand_is_last()
)
