from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="a8435051-9202-5c3c-9a68-6e32b1d9303a",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorJuniper.Name",
    display_name="Professor Juniper",
    searchable_by=["Professor Juniper", "Supporter"],
    subtypes=["Supporter"],
    collector_number=116,
    set_code="BW9",
    rarity=Rarities.RareUltra,
    effect=discard_hand_draw(7)
)
