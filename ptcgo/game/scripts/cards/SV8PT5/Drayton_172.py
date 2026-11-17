from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import all_of, is_pokemon_card, is_trainer_card

card = SupporterCardDef(
    guid="6af875d3-ddf0-5383-92f0-ea7c9e2a7fdd",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Drayton.Name",
    display_name="Drayton",
    searchable_by=["Drayton", "Supporter"],
    subtypes=["Supporter"],
    collector_number=172,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=look_at_top(7, take=1, predicate=all_of(is_pokemon_card, is_trainer_card))
)
