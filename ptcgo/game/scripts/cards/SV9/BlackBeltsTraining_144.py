from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import turn_damage_boost

card = SupporterCardDef(
    guid="12c16c08-3fe5-5874-8088-5186546709e7",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlackBeltsTraining.Name",
    display_name="Black Belt's Training",
    searchable_by=["Black Belt's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=144,
    set_code="SV9",
    rarity=Rarities.Common,
    effect=turn_damage_boost(40)
)
