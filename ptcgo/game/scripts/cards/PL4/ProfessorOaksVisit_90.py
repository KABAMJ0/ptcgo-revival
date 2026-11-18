from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_bottom

card = SupporterCardDef(
    guid="59b4d717-a86e-5964-8499-461bf0b206f4",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksVisit.Name",
    display_name="Professor Oak's Visit",
    searchable_by=["Professor Oak's Visit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=90,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    effect=draw_then_bottom(3, 1)
)
