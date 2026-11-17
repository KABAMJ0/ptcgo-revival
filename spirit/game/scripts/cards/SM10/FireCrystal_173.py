from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import basic_energy_of

card = ItemCardDef(
    guid="710d6432-b23e-5aa0-bfdf-56071c6bf6b3",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FireCrystal.Name",
    display_name="Fire Crystal",
    searchable_by=["Fire Crystal", "Item"],
    subtypes=["Item"],
    collector_number=173,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(basic_energy_of("fire"), count=3, to="hand")
)
