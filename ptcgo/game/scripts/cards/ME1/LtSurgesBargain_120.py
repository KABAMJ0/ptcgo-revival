from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import surges_bargain

card = SupporterCardDef(
    guid="884e5682-2c6d-5d70-b50a-b25185ee311b",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurgesBargain.Name",
    display_name="Lt. Surge's Bargain",
    searchable_by=["Lt. Surge's Bargain", "Supporter"],
    subtypes=["Supporter"],
    collector_number=120,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    effect=surges_bargain(4)
)
