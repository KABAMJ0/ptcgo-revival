from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import retreat_cost_is

card = SupporterCardDef(
    guid="34c81731-196f-51d0-b671-e79bf01a74b0",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokManiac.Name",
    display_name="Poké Maniac",
    searchable_by=["Pok\u00e9 Maniac", "Supporter"],
    subtypes=["Supporter"],
    collector_number=204,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(retreat_cost_is(4), count=3)
)
