from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.trainers import is_basic_pokemon_with_hp_at_most

card = ItemCardDef(
    guid="5d16c670-5da6-5e17-a994-0dd2b460e5f0",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BuddyBuddyPoffin.Name",
    display_name="Buddy-Buddy Poffin",
    searchable_by=["Buddy-Buddy Poffin", "Item"],
    subtypes=["Item"],
    collector_number=101,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(is_basic_pokemon_with_hp_at_most(70), 2)
)
