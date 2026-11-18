from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_turn_boost

card = SupporterCardDef(
    guid="30a2b596-dc83-5a33-b1cf-40ba5f7d9405",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorKukui.Name",
    display_name="Professor Kukui",
    searchable_by=["Professor Kukui", "Supporter"],
    subtypes=["Supporter"],
    collector_number=148,
    set_code="SM1",
    rarity=Rarities.RareUltra,
    effect=draw_then_turn_boost(2, 20)
)
