from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="952ae9ea-85e3-5416-8c54-ffe0568cea65",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorSycamore.Name",
    display_name="Professor Sycamore",
    searchable_by=["Professor Sycamore", "Supporter"],
    subtypes=["Supporter"],
    collector_number=107,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=discard_hand_draw(7)
)
