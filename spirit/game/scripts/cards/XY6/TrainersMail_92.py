from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import trainer_card_other_than

card = ItemCardDef(
    guid="221140c0-b4a0-53e0-bf40-1ec7ae9aff90",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrainersMail.Name",
    display_name="Trainers' Mail",
    searchable_by=["Trainers' Mail", "Item"],
    subtypes=["Item"],
    collector_number=92,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    effect=look_at_top(4, take=1, predicate=trainer_card_other_than("trainers mail"), rest="shuffle", minimum=0)
)
