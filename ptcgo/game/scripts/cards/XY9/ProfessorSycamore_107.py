from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_hand_draw

card = SupporterCardDef(
    guid="e3782a6d-4b9a-5ad2-835c-c0c187d6ac78",
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
