from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import all_of, is_pokemon_card, is_trainer_card

card = SupporterCardDef(
    guid="5e4269e3-c966-54b9-a467-42ee66e48bc6",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Drayton.Name",
    display_name="Drayton",
    searchable_by=["Drayton", "Supporter"],
    subtypes=["Supporter"],
    collector_number=244,
    set_code="SV8",
    rarity=Rarities.Rare,
    effect=look_at_top(7, take=1, predicate=all_of(is_pokemon_card, is_trainer_card))
)
