from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="d2619164-a038-5106-9538-099ae9ea958f",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorJuniper.Name",
    display_name="Professor Juniper",
    searchable_by=["Professor Juniper", "Supporter"],
    subtypes=["Supporter"],
    collector_number=101,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=discard_hand_draw(7)
)
