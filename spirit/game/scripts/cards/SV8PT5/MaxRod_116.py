from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import any_of, is_basic_energy_card, is_pokemon_card

card = ItemCardDef(
    guid="610a3643-f358-507c-bc80-602a47c27fc2",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxRod.Name",
    display_name="Max Rod",
    searchable_by=["Max Rod", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=116,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=recover_from_discard(any_of(is_pokemon_card, is_basic_energy_card), count=5, to="hand")
)
