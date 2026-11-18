from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import ends_turn_after

card = SupporterCardDef(
    guid="4fd6fca6-1def-5d7a-9eb1-45de50325b0b",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StevensResolve.Name",
    display_name="Steven's Resolve",
    searchable_by=["Steven's Resolve", "Supporter"],
    subtypes=["Supporter"],
    collector_number=165,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    effect=ends_turn_after(search_to_hand(None, count=3))
)
