from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import any_of, is_basic_energy_card, is_pokemon_card

card = ItemCardDef(
    guid="b2e43c24-7f49-5932-8270-97194f11bed1",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightStretcher.Name",
    display_name="Night Stretcher",
    searchable_by=["Night Stretcher", "Item"],
    subtypes=["Item"],
    collector_number=173,
    set_code="ME1",
    rarity=Rarities.Rare,
    effect=recover_from_discard(any_of(is_pokemon_card, is_basic_energy_card), count=1, to="hand")
)
