from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import ends_turn_after

card = SupporterCardDef(
    guid="e274e0be-74d8-58c2-b796-9200f85d3341",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StevensResolve.Name",
    display_name="Steven's Resolve",
    searchable_by=["Steven's Resolve", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    effect=ends_turn_after(search_to_hand(None, count=3))
)
