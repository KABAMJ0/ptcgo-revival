from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import all_of, is_basic_pokemon, is_rule_box_free_pokemon, stadium_ability

card = StadiumCardDef(
    guid="605f1626-67da-5866-84b1-c38018c2df75",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Artazon.Name",
    display_name="Artazon",
    searchable_by=["Artazon", "Stadium"],
    subtypes=["Stadium"],
    collector_number=76,
    set_code="SV4PT5",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Artazon', search_to_bench(all_of(is_basic_pokemon, is_rule_box_free_pokemon), 1))
)
