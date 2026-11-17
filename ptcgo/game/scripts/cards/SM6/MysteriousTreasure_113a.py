from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import any_of, pokemon_of, with_discard_cost

card = ItemCardDef(
    guid="2761d4f0-f0a0-56fc-8aed-90ffc37a4d80",
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
