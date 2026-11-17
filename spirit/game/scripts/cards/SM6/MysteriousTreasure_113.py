from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import any_of, pokemon_of, with_discard_cost

card = ItemCardDef(
    guid="e4c0fe58-9836-570d-8aa9-22fd1452d245",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousTreasure.Name",
    display_name="Mysterious Treasure",
    searchable_by=["Mysterious Treasure", "Item"],
    subtypes=["Item"],
    collector_number=113,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, search_to_hand(any_of(pokemon_of("psychic"), pokemon_of("dragon")), count=1))
)
