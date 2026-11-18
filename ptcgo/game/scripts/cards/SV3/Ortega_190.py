from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_hand_to_bottom

card = SupporterCardDef(
    guid="54dd38fe-89c1-57a0-a37d-f46b92270c16",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ortega.Name",
    display_name="Ortega",
    searchable_by=["Ortega", "Supporter"],
    subtypes=["Supporter"],
    collector_number=190,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    effect=opponent_hand_to_bottom()
)
