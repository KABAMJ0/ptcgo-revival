from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import retreat_cost_is

card = SupporterCardDef(
    guid="74871db2-cdb1-5dfe-b660-698657ac5808",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokManiac.Name",
    display_name="Poké Maniac",
    searchable_by=["Pok\u00e9 Maniac", "Supporter"],
    subtypes=["Supporter"],
    collector_number=236,
    set_code="SM11",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(retreat_cost_is(4), count=3)
)
