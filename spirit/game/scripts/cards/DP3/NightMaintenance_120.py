from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import any_of, is_basic_energy_card, is_pokemon_card

card = ItemCardDef(
    guid="165c29f7-1263-5c87-a6d0-d3e2f40da45d",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightMaintenance.Name",
    display_name="Night Maintenance",
    searchable_by=["Night Maintenance", "Item"],
    subtypes=["Item"],
    collector_number=120,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(any_of(is_pokemon_card, is_basic_energy_card), count=3, to="deck_shuffle")
)
