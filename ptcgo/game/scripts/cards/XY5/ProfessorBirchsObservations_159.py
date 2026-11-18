from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_flip_draw

card = SupporterCardDef(
    guid="cc26edad-ecc7-55b9-b7c5-ff405493cea1",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorBirchsObservations.Name",
    display_name="Professor Birch's Observations",
    searchable_by=["Professor Birch's Observations", "Supporter"],
    subtypes=["Supporter"],
    collector_number=159,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    effect=shuffle_hand_flip_draw(7, 4)
)
