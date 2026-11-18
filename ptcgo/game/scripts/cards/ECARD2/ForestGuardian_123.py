from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top

card = SupporterCardDef(
    guid="7b04c584-4115-5f15-a26d-bca587ffea4e",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ForestGuardian.Name",
    display_name="Forest Guardian",
    searchable_by=["Forest Guardian", "Supporter"],
    subtypes=["Supporter"],
    collector_number=123,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1)
)
