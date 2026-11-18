from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import all_of, is_pokemon_card, is_trainer_card

card = SupporterCardDef(
    guid="d94af90f-8b18-53ac-80cb-929b06354ea5",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Drayton.Name",
    display_name="Drayton",
    searchable_by=["Drayton", "Supporter"],
    subtypes=["Supporter"],
    collector_number=174,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, predicate=all_of(is_pokemon_card, is_trainer_card))
)
