from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import shuffle_hand_draw

card = SupporterCardDef(
    guid="8ea804bd-9540-5de4-940d-39094d485f4b",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cynthia.Name",
    display_name="Cynthia",
    searchable_by=["Cynthia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=148,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    effect=shuffle_hand_draw(6)
)
