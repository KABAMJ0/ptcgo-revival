from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import is_basic_pokemon_with_hp_at_most

card = ItemCardDef(
    guid="bfe214ab-67a3-5631-a281-25fee7141538",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BuddyBuddyPoffin.Name",
    display_name="Buddy-Buddy Poffin",
    searchable_by=["Buddy-Buddy Poffin", "Item"],
    subtypes=["Item"],
    collector_number=223,
    set_code="SV6",
    rarity=Rarities.Rare,
    effect=search_to_bench(is_basic_pokemon_with_hp_at_most(70), 2)
)
