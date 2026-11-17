from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import pokemon_of_subtype, with_discard_cost

card = ItemCardDef(
    guid="1945e426-d6f3-596e-a039-7ea84f40831d",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnoRadar.Name",
    display_name="Techno Radar",
    searchable_by=["Techno Radar", "Item", "Future"],
    subtypes=["Item", "Future"],
    collector_number=180,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, search_to_hand(pokemon_of_subtype("Future"), count=2))
)
