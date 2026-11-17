from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_per_typed, hand_is_last

card = SupporterCardDef(
    guid="87ce236a-7ef6-5bef-b96f-309a975d7373",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesLastStand.Name",
    display_name="Blaine's Last Stand",
    searchable_by=["Blaine's Last Stand", "Supporter"],
    subtypes=["Supporter"],
    collector_number=58,
    set_code="DM",
    rarity=Rarities.RareHolo,
    effect=draw_per_typed("fire", 2), condition=hand_is_last()
)
