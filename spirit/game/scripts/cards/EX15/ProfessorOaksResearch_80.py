from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import shuffle_hand_draw

card = SupporterCardDef(
    guid="d5d9ad67-c5e3-5947-81af-2dadf8e1c5ac",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksResearch.Name",
    display_name="Professor Oak's Research",
    searchable_by=["Professor Oak's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=80,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_draw(5)
)
