from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_evolution_pokemon

card = SupporterCardDef(
    guid="af50690d-42dc-5b00-b59c-d33aad08c347",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElmsTrainingMethod.Name",
    display_name="Professor Elm's Training Method",
    searchable_by=["Professor Elm's Training Method", "Supporter"],
    subtypes=["Supporter"],
    collector_number=100,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_evolution_pokemon, count=1)
)
