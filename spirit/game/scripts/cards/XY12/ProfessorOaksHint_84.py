from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_until_effect
from spirit.game.card_effects.trainers import ends_turn_after

card = SupporterCardDef(
    guid="50303223-e9c7-5a18-bb74-27048380401a",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksHint.Name",
    display_name="Professor Oak's Hint",
    searchable_by=["Professor Oak's Hint", "Supporter"],
    subtypes=["Supporter"],
    collector_number=84,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    effect=ends_turn_after(draw_until_effect(7))
)
