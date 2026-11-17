from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.trainers import is_basic_pokemon_with_hp_at_most

card = ItemCardDef(
    guid="225e8657-34dd-59ae-a2eb-4c8a4a764235",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BuddyBuddyPoffin.Name",
    display_name="Buddy-Buddy Poffin",
    searchable_by=["Buddy-Buddy Poffin", "Item"],
    subtypes=["Item"],
    collector_number=144,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(is_basic_pokemon_with_hp_at_most(70), 2)
)
