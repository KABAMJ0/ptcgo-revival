from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top

card = SupporterCardDef(
    guid="af452ef5-816d-5fb1-b824-375a7e1ddbd1",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SagesTraining.Name",
    display_name="Sage's Training",
    searchable_by=["Sage's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="HGSS3",
    rarity=Rarities.Uncommon,
    effect=look_at_top(5, take=2, rest="discard")
)
