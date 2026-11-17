from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import any_of, is_basic_energy_card, is_pokemon_card

card = ItemCardDef(
    guid="b0e13d69-77c9-5a16-bbf7-50f0b9ffa14a",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightStretcher.Name",
    display_name="Night Stretcher",
    searchable_by=["Night Stretcher", "Item"],
    subtypes=["Item"],
    collector_number=61,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(any_of(is_pokemon_card, is_basic_energy_card), count=1, to="hand")
)
