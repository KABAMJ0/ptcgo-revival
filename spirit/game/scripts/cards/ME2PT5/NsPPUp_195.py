from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="68190365-7b3c-53e5-9b74-24d5fba43061",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NsPPUp.Name",
    display_name="N's PP Up",
    searchable_by=["N's PP Up", "Item"],
    subtypes=["Item"],
    collector_number=195,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=attach_from_discard(is_basic_energy_card, count=1, target="choice")
)
