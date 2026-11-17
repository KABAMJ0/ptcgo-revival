from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import all_of, is_basic_energy_card, is_pokemon_card

card = ItemCardDef(
    guid="39bcdaef-c761-5dba-8ce7-609588b850b8",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperRod.Name",
    display_name="Super Rod",
    searchable_by=["Super Rod", "Item"],
    subtypes=["Item"],
    collector_number=188,
    set_code="SV2",
    rarity=Rarities.Common,
    effect=recover_from_discard(all_of(is_pokemon_card, is_basic_energy_card), count=3, to="deck_shuffle")
)
