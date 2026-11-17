from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import choose_one, is_basic_energy_card

card = ItemCardDef(
    guid="5d36af85-9b3d-50d4-9078-07db64b03353",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycleSystem.Name",
    display_name="Energy Recycle System",
    searchable_by=["Energy Recycle System", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=choose_one([("Put a basic Energy card from your discard pile into your hand", recover_from_discard(is_basic_energy_card, count=1, to="hand")), ("Shuffle 3 basic Energy cards from your discard pile into your deck", recover_from_discard(is_basic_energy_card, count=3, to="deck_shuffle"))])
)
