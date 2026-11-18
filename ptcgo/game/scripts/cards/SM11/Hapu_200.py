from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top

card = SupporterCardDef(
    guid="b4863af3-49c5-51d7-af22-66305e1bba37",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hapu.Name",
    display_name="Hapu",
    searchable_by=["Hapu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=200,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    effect=look_at_top(6, take=2)
)
