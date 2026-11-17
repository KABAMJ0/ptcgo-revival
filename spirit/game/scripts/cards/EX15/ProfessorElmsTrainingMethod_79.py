from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_evolution_pokemon

card = SupporterCardDef(
    guid="66aafb48-0f1b-5a93-94ed-dabde6734c7c",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElmsTrainingMethod.Name",
    display_name="Professor Elm's Training Method",
    searchable_by=["Professor Elm's Training Method", "Supporter"],
    subtypes=["Supporter"],
    collector_number=79,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_evolution_pokemon, count=1)
)
