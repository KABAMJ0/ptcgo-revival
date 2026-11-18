from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_size_at_least, keep_one_shuffle_rest_draw

card = SupporterCardDef(
    guid="8f3a7c42-53df-530b-b29f-fd96705a4b07",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorRowan.Name",
    display_name="Professor Rowan",
    searchable_by=["Professor Rowan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=123,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    effect=keep_one_shuffle_rest_draw(4), condition=hand_size_at_least(2)
)
