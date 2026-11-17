from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import turn_damage_boost

card = SupporterCardDef(
    guid="38ef7a38-41af-50b7-866d-86d3c6351fa9",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlackBeltsTraining.Name",
    display_name="Black Belt's Training",
    searchable_by=["Black Belt's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=98,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    effect=turn_damage_boost(40)
)
