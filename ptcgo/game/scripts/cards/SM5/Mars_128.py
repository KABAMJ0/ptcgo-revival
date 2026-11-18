from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_opponent_discard

card = SupporterCardDef(
    guid="995329f5-c227-5f4b-b551-b7e25bef0985",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mars.Name",
    display_name="Mars",
    searchable_by=["Mars", "Supporter"],
    subtypes=["Supporter"],
    collector_number=128,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=draw_then_opponent_discard(2, 1, random=True)
)
