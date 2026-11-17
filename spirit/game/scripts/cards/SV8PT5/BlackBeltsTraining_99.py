from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import turn_damage_boost

card = SupporterCardDef(
    guid="e0b24553-f769-5af1-972a-c1efb21d9dcb",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlackBeltsTraining.Name",
    display_name="Black Belt's Training",
    searchable_by=["Black Belt's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=99,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    effect=turn_damage_boost(40)
)
