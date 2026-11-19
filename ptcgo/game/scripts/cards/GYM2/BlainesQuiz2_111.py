from ptcgo.game.card_effects.trainers import blaines_quiz
from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="35a87a27-b12a-5237-bcda-db283205e1a5",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesQuiz2.Name",
    display_name="Blaine's Quiz #2",
    searchable_by=["Blaine's Quiz #2"],
    subtypes=[],
    collector_number=111,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    effect=blaines_quiz("category", draw=2)
)
