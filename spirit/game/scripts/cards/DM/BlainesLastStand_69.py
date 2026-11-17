from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_per_typed, hand_is_last

card = SupporterCardDef(
    guid="361a53c3-36c7-58e9-a123-33be61c7368b",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesLastStand.Name",
    display_name="Blaine's Last Stand",
    searchable_by=["Blaine's Last Stand", "Supporter"],
    subtypes=["Supporter"],
    collector_number=69,
    set_code="DM",
    rarity=Rarities.RareUltra,
    effect=draw_per_typed("fire", 2), condition=hand_is_last()
)
