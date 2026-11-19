from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_and_discard

card = SupporterCardDef(
    guid="55dd9ea6-f7ae-5705-9063-e5db2acc1ae6",
    key="SWSH12TG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorBurnet.Name",
    display_name="Professor Burnet",
    searchable_by=["Professor Burnet", "Supporter"],
    subtypes=["Supporter"],
    collector_number=26,
    set_code="SWSH12TG",
    rarity=Rarities.RareUltra,
    effect=search_and_discard(2)
)
