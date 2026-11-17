from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import trainer_card_other_than

card = ItemCardDef(
    guid="ab14acf2-41de-5fb0-b424-f7c10e446763",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrainersMail.Name",
    display_name="Trainers' Mail",
    searchable_by=["Trainers' Mail", "Item"],
    subtypes=["Item"],
    collector_number=100,
    set_code="XY7",
    rarity=Rarities.RareSecret,
    effect=look_at_top(4, take=1, predicate=trainer_card_other_than("trainers mail"), rest="shuffle", minimum=0)
)
