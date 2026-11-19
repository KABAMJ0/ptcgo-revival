from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import surges_bargain

card = SupporterCardDef(
    guid="d7cf4737-83c9-57b7-83e5-17d8cf3a4995",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurgesBargain.Name",
    display_name="Lt. Surge's Bargain",
    searchable_by=["Lt. Surge's Bargain", "Supporter"],
    subtypes=["Supporter"],
    collector_number=170,
    set_code="ME1",
    rarity=Rarities.Rare,
    effect=surges_bargain(4)
)
