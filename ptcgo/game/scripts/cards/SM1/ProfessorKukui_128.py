from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_turn_boost

card = SupporterCardDef(
    guid="1a6ed5b9-7cf5-5a75-a2dd-8cce5b230615",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorKukui.Name",
    display_name="Professor Kukui",
    searchable_by=["Professor Kukui", "Supporter"],
    subtypes=["Supporter"],
    collector_number=128,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=draw_then_turn_boost(2, 20)
)
