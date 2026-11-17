from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import any_of, pokemon_of, with_discard_cost

card = ItemCardDef(
    guid="b598c5db-dd31-562b-a498-4d88c5a2aed3",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousTreasure.Name",
    display_name="Mysterious Treasure",
    searchable_by=["Mysterious Treasure", "Item"],
    subtypes=["Item"],
    collector_number=145,
    set_code="SM6",
    rarity=Rarities.RareSecret,
    effect=with_discard_cost(1, search_to_hand(any_of(pokemon_of("psychic"), pokemon_of("dragon")), count=1))
)
