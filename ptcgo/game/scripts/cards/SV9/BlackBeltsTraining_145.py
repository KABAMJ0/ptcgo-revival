from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import turn_damage_boost

card = SupporterCardDef(
    guid="307de55f-7321-553c-80b0-79b5edf12f2f",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlackBeltsTraining.Name",
    display_name="Black Belt's Training",
    searchable_by=["Black Belt's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SV9",
    rarity=Rarities.Common,
    effect=turn_damage_boost(40)
)
