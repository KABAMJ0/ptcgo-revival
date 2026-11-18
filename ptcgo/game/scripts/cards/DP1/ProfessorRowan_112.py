from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_size_at_least, keep_one_shuffle_rest_draw

card = SupporterCardDef(
    guid="4cf3e77b-6467-5346-9ec7-9ba7aae897be",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorRowan.Name",
    display_name="Professor Rowan",
    searchable_by=["Professor Rowan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=112,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    effect=keep_one_shuffle_rest_draw(4), condition=hand_size_at_least(2)
)
