from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import all_of, is_basic_energy_card, is_pokemon_card

card = ItemCardDef(
    guid="dffbeedc-023d-5e43-ae2a-3db735d2e307",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperRod.Name",
    display_name="Super Rod",
    searchable_by=["Super Rod", "Item"],
    subtypes=["Item"],
    collector_number=149,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(all_of(is_pokemon_card, is_basic_energy_card), count=3, to="deck_shuffle")
)
