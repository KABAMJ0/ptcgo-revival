from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_draw

card = SupporterCardDef(
    guid="68a06f33-f721-5452-a4c5-0bb6e64f675e",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cynthia.Name",
    display_name="Cynthia",
    searchable_by=["Cynthia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=82,
    set_code="SVault",
    rarity=Rarities.RareUltra,
    effect=shuffle_hand_draw(6)
)
