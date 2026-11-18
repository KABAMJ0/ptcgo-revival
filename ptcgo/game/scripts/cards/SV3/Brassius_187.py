from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import count_hand_shuffle_draw_plus

card = SupporterCardDef(
    guid="54a3ad83-cef1-5f70-a312-64d099e029f9",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brassius.Name",
    display_name="Brassius",
    searchable_by=["Brassius", "Supporter"],
    subtypes=["Supporter"],
    collector_number=187,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    effect=count_hand_shuffle_draw_plus(1)
)
