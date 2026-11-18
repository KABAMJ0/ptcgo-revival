from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_opponent_discard

card = SupporterCardDef(
    guid="2b5f706d-5c17-508e-b7c9-48a40b8f2162",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mars.Name",
    display_name="Mars",
    searchable_by=["Mars", "Supporter"],
    subtypes=["Supporter"],
    collector_number=154,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    effect=draw_then_opponent_discard(2, 1, random=True)
)
