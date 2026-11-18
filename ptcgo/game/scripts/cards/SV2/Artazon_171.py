from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import all_of, is_basic_pokemon, is_rule_box_free_pokemon, stadium_ability

card = StadiumCardDef(
    guid="b13a955f-3726-5ead-ba03-d8e08fe80bfd",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Artazon.Name",
    display_name="Artazon",
    searchable_by=["Artazon", "Stadium"],
    subtypes=["Stadium"],
    collector_number=171,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Artazon', search_to_bench(all_of(is_basic_pokemon, is_rule_box_free_pokemon), 1))
)
