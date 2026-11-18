from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import any_of, is_basic_energy_card, is_pokemon_card

card = ItemCardDef(
    guid="374c81d2-1510-53cc-9a38-c8e79ccb3896",
    key="POP8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightMaintenance.Name",
    display_name="Night Maintenance",
    searchable_by=["Night Maintenance", "Item"],
    subtypes=["Item"],
    collector_number=9,
    set_code="POP8",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(any_of(is_pokemon_card, is_basic_energy_card), count=3, to="deck_shuffle")
)
