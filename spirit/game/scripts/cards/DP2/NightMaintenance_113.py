from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import any_of, is_basic_energy_card, is_pokemon_card

card = ItemCardDef(
    guid="352ceac9-0ecf-52dc-9703-0cb90904fa01",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightMaintenance.Name",
    display_name="Night Maintenance",
    searchable_by=["Night Maintenance", "Item"],
    subtypes=["Item"],
    collector_number=113,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(any_of(is_pokemon_card, is_basic_energy_card), count=3, to="deck_shuffle")
)
