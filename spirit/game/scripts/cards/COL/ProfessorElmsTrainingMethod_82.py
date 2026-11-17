from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_evolution_pokemon

card = SupporterCardDef(
    guid="0b098b47-301f-551b-921f-06fd337e836e",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElmsTrainingMethod.Name",
    display_name="Professor Elm's Training Method",
    searchable_by=["Professor Elm's Training Method", "Supporter"],
    subtypes=["Supporter"],
    collector_number=82,
    set_code="COL",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_evolution_pokemon, count=1)
)
