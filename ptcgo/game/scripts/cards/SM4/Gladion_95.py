from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import take_face_down_prize_shuffle_self

card = SupporterCardDef(
    guid="b43d09c8-ab22-5d3b-af7f-6f3481608951",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gladion.Name",
    display_name="Gladion",
    searchable_by=["Gladion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=95,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    effect=take_face_down_prize_shuffle_self()
)
