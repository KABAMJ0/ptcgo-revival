from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_hand_to_bottom

card = SupporterCardDef(
    guid="545f93e4-94ea-5a4b-b885-af78de418a55",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ortega.Name",
    display_name="Ortega",
    searchable_by=["Ortega", "Supporter"],
    subtypes=["Supporter"],
    collector_number=219,
    set_code="SV3",
    rarity=Rarities.Rare,
    effect=opponent_hand_to_bottom()
)
