from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_tool_card

card = ItemCardDef(
    guid="81b11637-88ca-5d85-8101-26390a2fb766",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EcoArm.Name",
    display_name="Eco Arm",
    searchable_by=["Eco Arm", "Item"],
    subtypes=["Item"],
    collector_number=71,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_tool_card, count=3, to="deck_shuffle")
)
