from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import all_of, is_basic_pokemon, is_rule_box_free_pokemon, stadium_ability

card = StadiumCardDef(
    guid="f600a9cc-25cd-50b3-8c91-a0dd1bc6f80d",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Artazon.Name",
    display_name="Artazon",
    searchable_by=["Artazon", "Stadium"],
    subtypes=["Stadium"],
    collector_number=229,
    set_code="SV3",
    rarity=Rarities.Rare,
    ability=stadium_ability('Artazon', search_to_bench(all_of(is_basic_pokemon, is_rule_box_free_pokemon), 1))
)
