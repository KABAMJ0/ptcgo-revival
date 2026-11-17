from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, card_named_contains, is_evolution_pokemon

card = ItemCardDef(
    guid="6025b89d-bb5e-58d0-8a0a-4db9c5a6a2ea",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TheBosssWay.Name",
    display_name="The Boss's Way",
    searchable_by=["The Boss's Way"],
    subtypes=[],
    collector_number=73,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_evolution_pokemon, card_named_contains("dark")), count=1)
)
