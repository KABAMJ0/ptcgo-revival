from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_pokemon_ex, turn_damage_boost_vs

card = SupporterCardDef(
    guid="7c2b2dc0-5f9a-5750-a24a-b426baf72f14",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlackBeltsTraining.Name",
    display_name="Black Belt's Training",
    searchable_by=["Black Belt's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=96,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    effect=turn_damage_boost_vs(40, is_pokemon_ex)
)
