from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import shuffle_hand_draw_lock_trainers

card = ItemCardDef(
    guid="706feb4c-fadd-509d-9b08-72219cc312ed",
    key="BP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElm.Name",
    display_name="Professor Elm",
    searchable_by=["Professor Elm"],
    subtypes=[],
    collector_number=3,
    set_code="BP",
    rarity=Rarities.RarePromo,
    effect=shuffle_hand_draw_lock_trainers(7)
)
