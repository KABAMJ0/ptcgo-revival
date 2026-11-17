from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.trainers import is_basic_pokemon_with_hp_at_most

card = ItemCardDef(
    guid="0792eed9-8d70-5cb5-b94f-1fdfdc046cfe",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BuddyBuddyPoffin.Name",
    display_name="Buddy-Buddy Poffin",
    searchable_by=["Buddy-Buddy Poffin", "Item"],
    subtypes=["Item"],
    collector_number=184,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    effect=search_to_bench(is_basic_pokemon_with_hp_at_most(70), 2)
)
