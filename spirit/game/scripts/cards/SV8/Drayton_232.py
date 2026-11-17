from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import all_of, is_pokemon_card, is_trainer_card

card = SupporterCardDef(
    guid="030a53af-d430-5732-a34a-51b11b93ffff",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Drayton.Name",
    display_name="Drayton",
    searchable_by=["Drayton", "Supporter"],
    subtypes=["Supporter"],
    collector_number=232,
    set_code="SV8",
    rarity=Rarities.Rare,
    effect=look_at_top(7, take=1, predicate=all_of(is_pokemon_card, is_trainer_card))
)
