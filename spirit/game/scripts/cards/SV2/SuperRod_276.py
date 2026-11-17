from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import all_of, is_basic_energy_card, is_pokemon_card

card = ItemCardDef(
    guid="bdac5530-1a31-5738-92ba-07ef1d24a01a",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperRod.Name",
    display_name="Super Rod",
    searchable_by=["Super Rod", "Item"],
    subtypes=["Item"],
    collector_number=276,
    set_code="SV2",
    rarity=Rarities.Rare,
    effect=recover_from_discard(all_of(is_pokemon_card, is_basic_energy_card), count=3, to="deck_shuffle")
)
