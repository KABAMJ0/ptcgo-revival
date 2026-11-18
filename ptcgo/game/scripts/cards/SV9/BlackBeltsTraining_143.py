from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_ex, turn_damage_boost_vs

card = SupporterCardDef(
    guid="815e0848-49ef-511b-b614-fceb0ae0a41b",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlackBeltsTraining.Name",
    display_name="Black Belt's Training",
    searchable_by=["Black Belt's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=143,
    set_code="SV9",
    rarity=Rarities.Common,
    effect=turn_damage_boost_vs(40, is_pokemon_ex)
)
